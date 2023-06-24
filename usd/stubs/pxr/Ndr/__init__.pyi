import Boost.Python
import pxr.Tf
import typing
from typing import Any, ClassVar, overload

VersionFilterAllVersions: VersionFilter
VersionFilterDefaultOnly: VersionFilter

class DiscoveryPlugin(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def DiscoverNodes(self, arg2: DiscoveryPluginContext) -> Any: ...
    @overload
    def DiscoverNodes(self, arg2: DiscoveryPluginContext) -> None: ...
    @overload
    def GetSearchURIs(self) -> Any: ...
    @overload
    def GetSearchURIs(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class DiscoveryPluginContext(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def GetSourceType(self, arg2: object) -> Any: ...
    @overload
    def GetSourceType(self, arg2: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class DiscoveryPluginList(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def append(self, arg2: object) -> None: ...
    def extend(self, arg2: object) -> None: ...
    def __contains__(self, arg2: object) -> bool: ...
    def __delitem__(self, arg2: object) -> None: ...
    def __getitem__(self, arg2: object) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, arg2: object, arg3: object) -> None: ...

class DiscoveryUri(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    resolvedUri: Any
    uri: Any
    @overload
    def __init__(self, arg2: DiscoveryUri) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __reduce__(self) -> Any: ...

class Node(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def GetContext(self) -> str: ...
    def GetFamily(self) -> str: ...
    def GetIdentifier(self) -> Identifier: ...
    def GetInfoString(self) -> str: ...
    def GetInput(self, arg2: str | pxr.Ar.ResolvedPath) -> Property: ...
    def GetInputNames(self) -> TokenVec: ...
    def GetMetadata(self) -> dict: ...
    def GetName(self) -> str: ...
    def GetOutput(self, arg2: str | pxr.Ar.ResolvedPath) -> Property: ...
    def GetOutputNames(self) -> TokenVec: ...
    def GetResolvedDefinitionURI(self) -> str: ...
    def GetResolvedImplementationURI(self) -> str: ...
    def GetSourceCode(self) -> str: ...
    def GetSourceType(self) -> str: ...
    def GetVersion(self) -> Version: ...
    def IsValid(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class NodeDiscoveryResult(Boost.Python.instance):
    def __init__(self, identifier: object, version: Version, name: object, family: object, discoveryType: object, sourceType: object, uri: object, resolvedUri: object, sourceCode: object = ..., metadata: object = ..., blindData: object = ..., subIdentifier: object = ...) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def blindData(self) -> Any: ...
    @property
    def discoveryType(self) -> Any: ...
    @property
    def family(self) -> Any: ...
    @property
    def identifier(self) -> Any: ...
    @property
    def metadata(self) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def resolvedUri(self) -> Any: ...
    @property
    def sourceCode(self) -> Any: ...
    @property
    def sourceType(self) -> Any: ...
    @property
    def subIdentifier(self) -> Any: ...
    @property
    def uri(self) -> Any: ...
    @property
    def version(self) -> Any: ...

class NodeList(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def append(self, arg2: object) -> None: ...
    def extend(self, arg2: object) -> None: ...
    def __contains__(self, arg2: object) -> bool: ...
    def __delitem__(self, arg2: object) -> None: ...
    def __getitem__(self, arg2: object) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __reduce__(self) -> Any: ...
    def __setitem__(self, arg2: object, arg3: object) -> None: ...

class Property(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def CanConnectTo(self, arg2: Property) -> bool: ...
    def GetArraySize(self) -> int: ...
    def GetDefaultValue(self) -> Any: ...
    def GetInfoString(self) -> str: ...
    def GetMetadata(self) -> dict: ...
    def GetName(self) -> str: ...
    def GetType(self) -> str: ...
    def GetTypeAsSdfType(self) -> tuple: ...
    def IsArray(self) -> bool: ...
    def IsConnectable(self) -> bool: ...
    def IsDynamicArray(self) -> bool: ...
    def IsOutput(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Registry(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def GetAllNodeSourceTypes(self) -> TokenVec: ...
    def GetNodeByIdentifier(self, identifier: Identifier, typePriority: TokenVec = ...) -> Node: ...
    def GetNodeByIdentifierAndType(self, identifier: Identifier, nodeType: str | pxr.Ar.ResolvedPath) -> Node: ...
    def GetNodeByName(self, name: str | pxr.Ar.ResolvedPath, typePriority: TokenVec = ..., filter: VersionFilter = ...) -> Node: ...
    def GetNodeByNameAndType(self, name: str | pxr.Ar.ResolvedPath, nodeType: str | pxr.Ar.ResolvedPath, filter: VersionFilter = ...) -> Node: ...
    def GetNodeFromAsset(self, asset: pxr.Sdf.AssetPath | str, metadata: TokenMap = ..., subIdentifier: str | pxr.Ar.ResolvedPath = ..., sourceType: str | pxr.Ar.ResolvedPath = ...) -> Node: ...
    def GetNodeFromSourceCode(self, sourceCode: str | pxr.Ar.ResolvedPath, sourceType: str | pxr.Ar.ResolvedPath, metadata: TokenMap = ...) -> Node: ...
    def GetNodeIdentifiers(self, family: str | pxr.Ar.ResolvedPath = ..., filter: VersionFilter = ...) -> IdentifierVec: ...
    def GetNodeNames(self, family: str | pxr.Ar.ResolvedPath = ...) -> StringVec: ...
    def GetNodesByFamily(self, family: str | pxr.Ar.ResolvedPath = ..., filter: VersionFilter = ...) -> NodeList: ...
    def GetNodesByIdentifier(self, identifier: Identifier) -> NodeList: ...
    def GetNodesByName(self, name: str | pxr.Ar.ResolvedPath, filter: VersionFilter = ...) -> NodeList: ...
    def GetSearchURIs(self) -> StringVec: ...
    def SetExtraDiscoveryPlugins(self, arg2: list) -> None: ...
    def SetExtraParserPlugins(self, arg2: list[pxr.Tf.Type]) -> None: ...
    def __reduce__(self) -> Any: ...

class Version(Boost.Python.instance):
    @overload
    def __init__(self, arg2: int, arg3: int) -> None: ...
    @overload
    def __init__(self, arg2: int) -> None: ...
    @overload
    def __init__(self, arg2: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetAsDefault(self) -> Version: ...
    def GetMajor(self) -> int: ...
    def GetMinor(self) -> int: ...
    def GetStringSuffix(self) -> str: ...
    def IsDefault(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class VersionFilter(pxr.Tf.Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: object) -> Any: ...
    def __reduce__(self) -> Any: ...

class _AnnotatedBool(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def message(self) -> Any: ...

class _FilesystemDiscoveryPlugin(DiscoveryPlugin):
    class Context(DiscoveryPluginContext):
        def __init__(self) -> None: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __reduce__(self) -> Any: ...
        @property
        def expired(self) -> Any: ...
    @overload
    def __init__(self, arg2: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def DiscoverNodes(self, arg2: DiscoveryPluginContext) -> list: ...
    def GetSearchURIs(self) -> Any: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

def FsHelpersDiscoverFiles(searchPaths: StringVec, allowedExtensions: StringVec, followSymlinks: bool = ...) -> list: ...
def FsHelpersDiscoverNodes(searchPaths: StringVec, allowedExtensions: StringVec, followSymlinks: bool = ..., context: DiscoveryPluginContext = ...) -> tuple[NodeDiscoveryResultVec, DiscoveryPluginContext]: ...
def FsHelpersSplitShaderIdentifier(identifier: str | pxr.Ar.ResolvedPath) -> tuple[str, str, Version]: ...
def _ValidateProperty(arg1: Node, arg2: Property) -> _AnnotatedBool: ...