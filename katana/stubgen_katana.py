from __future__ import absolute_import, annotations, division, print_function

import re
from typing import Any

import mypy.stubgen
import mypy.stubgenc
from mypy.fastparse import parse_type_comment
from mypy.stubgen import main
from mypy.stubgenc import ArgSig
from mypy.stubgenc import DocstringSignatureGenerator as CDocstringSignatureGenerator
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

import Callbacks.Callbacks
from Callbacks.Callbacks import _TypeEnum
from stubgenlib import DocstringSignatureGenerator

EPY_REG = re.compile(r"([LC]\{([^}]+)\})")
LIST_OF_REG = re.compile(r"\b(list|Sequence|Iterable|Iterator) of (.*)")
TUPLE_OF_REG = re.compile(r"\btuple of ([a-zA-Z0-9_.,() ]*)")
SET_OF_REG = re.compile(r"\bset of ([a-zA-Z0-9_.]*)")
NUMERIC_TUPLE_REG = re.compile(r"\b(int|float)\[(\d+)\]")

# Remove these to troubleshoot errors:
DISABLED_CODES = '# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"\n\n'


def cleanup_type(type_name: str) -> str:
    type_name = type_name.replace('\n', ' ')
    type_name = type_name.rstrip('.')
    type_name = EPY_REG.sub(lambda m: m.group(2), type_name).strip()

    type_name = re.sub(r'\bNoneType\b', 'None', type_name)

    # special case
    optional = False
    if type_name.endswith(', or None'):
        optional = True
        type_name = type_name[: len(', or None')]

    replacements = [
        ('FnGeolib', 'PyFnGeolib'),
        ('FnAttribute', 'PyFnAttribute'),
        ('FnGeolibServices', 'PyFnGeolibServices'),
        ('FnGeolibProducers', 'PyFnGeolibProducers'),
        (
            r'PyFnGeolib.GeolibRuntime\.Transaction',
            'PyFnGeolib.GeolibRuntimeTransaction',
        ),
        (r'PyFnGeolib.GeolibRuntime\.Op', 'PyFnGeolib.GeolibRuntimeOp'),
        (r'NodegraphAPI\.LiveGroupMixin', 'NodegraphAPI.LiveGroup.LiveGroupMixin'),
        ('number', 'float'),
        ('module', 'types.ModuleType'),
        ('function', 'Callable'),
        ('callable', 'Callable'),
        ('hashable', 'Hashable'),
        ('iterable', 'Iterable'),
        ('class', 'type'),
        ('object', 'Any'),
        ('sequence', 'Sequence'),
        ('generator', 'Iterator'),
        ('long', 'int'),
        ('strings?', 'str'),
        ('Str', 'str'),
        ('int_', 'int'),
        ('none', 'None'),
    ]
    for find, replace in replacements:
        type_name = re.sub(r'\b{}\b'.format(find), replace, type_name)

    type_name = type_name.replace(' or ', ' | ')

    # FIXME: would be nice to have something that can do a search through known objects
    absolute_names = (
        (
            'TerminalOpDelegate',
            'Nodes3DAPI.TerminalOpDelegates.TerminalOpDelegate.TerminalOpDelegate',
        ),
        ('Nodes?', 'NodegraphAPI.Node'),
        ('GroupNode', 'NodegraphAPI.GroupNode'),
        ('Port', 'NodegraphAPI.Port'),
        ('GraphState', 'NodegraphAPI.GraphState'),
        ('Op', 'PyFnGeolib.GeolibRuntimeOp'),
        ('WorkingSet', 'PyUtilModule.WorkingSet.WorkingSet'),
        ('PortOpClient', 'Nodes3DAPI.PortOpClient.PortOpClient'),
        ('GroupAttribute', 'PyFnAttribute.GroupAttribute'),
    )
    for short_name, full_name in absolute_names:
        type_name = re.sub(
            r'(?<![A-Za-z0-9._]){}\b'.format(short_name), full_name, type_name
        )

    type_name = type_name.replace(
        'object convertible to a float', 'typing.SupportsFloat'
    )

    def list_sub(m):
        return "{}[{}]".format(m.group(1), m.group(2))

    type_name = LIST_OF_REG.sub(list_sub, type_name, count=1)

    def tuple_sub(m):
        members = [s.strip() for s in m.group(1).replace(" and ", " , ").split(",")]
        if len(members) == 1:
            members.append('...')
        return "tuple[{}]".format(", ".join(members))

    type_name = TUPLE_OF_REG.sub(tuple_sub, type_name, count=1)

    def set_sub(m):
        return "set[{}]".format(m.group(1))

    type_name = SET_OF_REG.sub(set_sub, type_name, count=1)

    def numeric_tuple_sub(m):
        count = int(m.group(2))
        return "tuple[{}]".format(', '.join([m.group(1)] * count))

    type_name = NUMERIC_TUPLE_REG.sub(numeric_tuple_sub, type_name, count=1)

    if optional:
        type_name = 'typing.Optional[{}]'.format(type_name)
    return type_name


class KatanaDocstringSignatureGenerator(DocstringSignatureGenerator):
    def cleanup_type(self, type_name: str) -> str:
        return cleanup_type(type_name)


class KatanaCSignatureGenerator(CDocstringSignatureGenerator):
    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        sigs = super().get_function_sig(default_sig, ctx)
        if sigs:
            sigs = [cleanup_sig(sig)[0] for sig in sigs]
        if ctx.fullname == "NodegraphAPI_cmodule.Parameter.getValue":
            return [sig._replace(ret_type="Any") for sig in sigs]
        elif ctx.fullname == "NodegraphAPI_cmodule.GroupNode.getChild":
            return [sig._replace(ret_type="Node") for sig in sigs]
        elif ctx.fullname == "NodegraphAPI_cmodule.Port.getNode":
            return [sig._replace(ret_type="Node") for sig in sigs]
        return sigs


class NoParseStubGenerator(mypy.stubgenc.NoParseStubGenerator):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.known_modules.extend(['PyQt5.QtCore', 'PyQt5.QtWidgets'])

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [KatanaDocstringSignatureGenerator()]

    def is_defined_in_module(self, obj: object) -> bool:
        # _TypeEnum is a type, but it's created dynamically.  This change ensures
        # that we don't assume things of type _TypeEnum are external to their
        # current module and should thus be imported.
        return super().is_defined_in_module(obj) or type(obj).__name__ == '_TypeEnum'

    def strip_or_import(self, type_name: str) -> str:
        if re.match('^[A-Za-z0-9_.]+$', type_name):
            parts = type_name.split('.')
            # It's impossible to get access to members of certain modules without
            # changing the import style, because the modules are replaced with
            # objects of the same name
            if (len(parts) >= 2 and parts[-2] == parts[-1]) or (
                len(parts) >= 3 and parts[-3] == parts[-2]
            ):
                self.import_tracker.add_import_from(
                    '.'.join(parts[:-1]), [(parts[-1], None)]
                )
                self.import_tracker.require_name(parts[-1])
                return parts[-1]
        return super().strip_or_import(type_name)

    def get_imports(self) -> str:
        imports = super().get_imports()
        return DISABLED_CODES + imports

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        # Note that there is a mix of fixes here for C and non-C modules, but
        # I'm not separating them because it's easy to get mixed uppp
        members = dict(super().get_members(obj))

        if isinstance(obj, type) and obj.__name__ == 'CallbacksManager':
            enums = {
                x: _TypeEnum(x)
                for x in dir(Callbacks.Callbacks.Type)
                if not x.startswith('_')
            }
            enumType = type('_TypeEnumList', (), enums)
            enumType.__module__ = 'Callbacks.Callbacks'
            members['Type'] = enumType

        return list(members.items())


class CFunctionStub:
    """
    Class that mimics a C function in order to provide parseable docstrings.
    """

    def __init__(self, name, doc, is_abstract=False):
        self.__name__ = name
        self.__doc__ = doc
        self.__abstractmethod__ = is_abstract

    def __get__(self):
        """
        This exists to make this object look like a method descriptor and thus
        return true for CStubGenerator.ismethod()
        """
        pass


class CStubGenerator(mypy.stubgenc.CStubGenerator):
    DATA_ATTRS = {
        'DataAttribute': 'T',
        'DoubleAttribute': 'float',
        'FloatAttribute': 'float',
        'IntAttribute': 'int',
        'StringAttribute': 'str',
    }

    def get_sig_generators(self) -> list[SignatureGenerator]:
        # sig_gens = super().get_sig_generators()
        return [KatanaCSignatureGenerator()]

    def get_imports(self) -> str:
        if self.module_name == 'PyFnAttribute':
            self.add_typing_import('TypeVar')
            type_vars = 'T = TypeVar("T")\n'
        else:
            type_vars = ''
        imports = super().get_imports()
        return DISABLED_CODES + imports + type_vars

    def get_base_types(self, obj: type) -> list[str]:
        bases = super().get_base_types(obj)
        if obj.__name__ in self.DATA_ATTRS or obj.__name__ == 'ConstVector':
            sub_type = self.DATA_ATTRS.get(obj.__name__, 'T')
            if obj.__name__ in ['DataAttribute', 'ConstVector']:
                self.add_typing_import('Generic')
                return bases + [f'Generic[{sub_type}]']
            else:
                base = bases[0]
                return [f'{base}[{sub_type}]']
        else:
            return bases

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        members = dict(super().get_members(obj))

        def add(x):
            members[x.__name__] = x

        if isinstance(obj, type) and obj.__name__ in self.DATA_ATTRS:
            sub_type = self.DATA_ATTRS[obj.__name__]
            is_abstract = obj.__name__ == 'DataAttribute'
            # Add abstract methods that are shared by all sub-classes
            add(
                CFunctionStub(
                    "getValue",
                    f"getValue(self, defaultValue: {sub_type} = ..., throwOnError: bool = ...) -> {sub_type}",
                    is_abstract=is_abstract,
                )
            )
            add(
                CFunctionStub(
                    "getData",
                    f"getData(self) -> ConstVector[{sub_type}]",
                    is_abstract=is_abstract,
                )
            )
            add(
                CFunctionStub(
                    "getNearestSample",
                    f"getNearestSample(self, sampleTime: float) -> ConstVector[{sub_type}]",
                    is_abstract=is_abstract,
                )
            )
            add(
                CFunctionStub(
                    "getSamples",
                    f"getSamples(self) -> Dict[float, ConstVector[{sub_type}]]",
                    is_abstract=is_abstract,
                )
            )
        elif isinstance(obj, type) and obj.__name__ == 'ConstVector':
            add(CFunctionStub("__iter__", "__iter__(self) -> Iterator[T]"))
            add(
                CFunctionStub(
                    "__getitem__",
                    "__getitem__(self, arg0: int) -> T\n"
                    "__getitem__(self, arg0: slice) -> ConstVector[T]",
                )
            )

        return list(members.items())


mypy.stubgen.NoParseStubGenerator = NoParseStubGenerator
mypy.stubgenc.NoParseStubGenerator = NoParseStubGenerator

mypy.stubgen.CStubGenerator = CStubGenerator
mypy.stubgenc.CStubGenerator = CStubGenerator
