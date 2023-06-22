from typing import Callable, ClassVar

CheckUsdzCompliance: Callable
CreateUsdzPackage: Callable
ExtractUsdzPackage: Callable
_AllowedUsdExtensions: Callable
_AllowedUsdzExtensions: Callable
_Err: Callable
_Print: Callable

class UsdzAssetIterator:
    __init__: ClassVar[Callable] = ...
    AllAssets: ClassVar[Callable] = ...
    UsdAssets: ClassVar[Callable] = ...
    _ExtractedFiles: ClassVar[Callable] = ...
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...