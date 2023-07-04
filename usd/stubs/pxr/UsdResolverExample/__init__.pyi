# mypy: disable_error_code = misc
import Boost.Python
from typing import Any, ClassVar, overload

class ResolverContext(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, mappingFile: object) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetMappingFile(self) -> str: ...
    def __hash__(self) -> int: ...
    def __reduce__(self) -> Any: ...