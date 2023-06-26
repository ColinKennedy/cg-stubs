import Boost.Python
import pxr.Ar
import typing
from typing import Any, ClassVar, overload

class MeshTopology(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: pxr.Vt.IntArray | typing.Iterable[int], arg5: pxr.Vt.IntArray | typing.Iterable[int], arg6: pxr.Vt.IntArray | typing.Iterable[int], arg7: SubdivTags) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: pxr.Vt.IntArray | typing.Iterable[int], arg5: pxr.Vt.IntArray | typing.Iterable[int], arg6: pxr.Vt.IntArray | typing.Iterable[int]) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: pxr.Vt.IntArray | typing.Iterable[int], arg5: pxr.Vt.IntArray | typing.Iterable[int], arg6: SubdivTags) -> None: ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: pxr.Vt.IntArray | typing.Iterable[int], arg5: pxr.Vt.IntArray | typing.Iterable[int]) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ComputeHash(self) -> int: ...
    def GetFaceVertexCounts(self) -> pxr.Vt.IntArray: ...
    def GetFaceVertexIndices(self) -> pxr.Vt.IntArray: ...
    def GetHoleIndices(self) -> pxr.Vt.IntArray: ...
    def GetOrientation(self) -> str: ...
    def GetScheme(self) -> str: ...
    def GetSubdivTags(self) -> SubdivTags: ...
    def Validate(self) -> MeshTopologyValidation: ...
    def WithHoleIndices(self, arg2: pxr.Vt.IntArray | typing.Iterable[int]) -> MeshTopology: ...
    def WithScheme(self, arg2: str | pxr.Ar.ResolvedPath) -> MeshTopology: ...
    def WithSubdivTags(self, arg2: SubdivTags) -> MeshTopology: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...

class MeshTopologyValidation(Boost.Python.instance):
    class Code(pxr.Tf.Tf_PyEnumWrapper):
        InvalidCornerIndicesElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCornerWeightsSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseIndicesElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseIndicesSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseLengthElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseMethod: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidCreaseWeightsSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVaryingInterpolationRule: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVertexCountsElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVertexIndicesElement: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidFaceVertexIndicesSize: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidOrientation: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidScheme: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidTriangleSubdivision: ClassVar[MeshTopologyValidation.Code] = ...
        InvalidVertexInterpolationRule: ClassVar[MeshTopologyValidation.Code] = ...
        NegativeCornerWeights: ClassVar[MeshTopologyValidation.Code] = ...
        NegativeCreaseWeights: ClassVar[MeshTopologyValidation.Code] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: object) -> Any: ...
        def __reduce__(self) -> Any: ...
    class Invalidation(Boost.Python.instance):
        code: Any
        message: Any
        def __init__(self, arg2: object) -> None: ...
        def __reduce__(self) -> Any: ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __iter__(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class OpenSubdivTokens(Boost.Python.instance):
    all: ClassVar[Any] = ...  # read-only
    bilinear: ClassVar[Any] = ...  # read-only
    boundaries: ClassVar[Any] = ...  # read-only
    catmullClark: ClassVar[Any] = ...  # read-only
    chaikin: ClassVar[Any] = ...  # read-only
    cornersOnly: ClassVar[Any] = ...  # read-only
    cornersPlus1: ClassVar[Any] = ...  # read-only
    cornersPlus2: ClassVar[Any] = ...  # read-only
    edgeAndCorner: ClassVar[Any] = ...  # read-only
    edgeOnly: ClassVar[Any] = ...  # read-only
    leftHanded: ClassVar[Any] = ...  # read-only
    loop: ClassVar[Any] = ...  # read-only
    none: ClassVar[Any] = ...  # read-only
    rightHanded: ClassVar[Any] = ...  # read-only
    smooth: ClassVar[Any] = ...  # read-only
    uniform: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class SubdivTags(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: object, arg3: object, arg4: object, arg5: object, arg6: pxr.Vt.IntArray | typing.Iterable[int], arg7: pxr.Vt.IntArray | typing.Iterable[int], arg8: pxr.Vt.FloatArray | typing.Iterable[float], arg9: pxr.Vt.IntArray | typing.Iterable[int], arg10: pxr.Vt.FloatArray | typing.Iterable[float]) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def ComputeHash(self) -> int: ...
    def GetCornerIndices(self) -> pxr.Vt.IntArray: ...
    def GetCornerWeights(self) -> pxr.Vt.FloatArray: ...
    def GetCreaseIndices(self) -> pxr.Vt.IntArray: ...
    def GetCreaseLengths(self) -> pxr.Vt.IntArray: ...
    def GetCreaseMethod(self) -> str: ...
    def GetCreaseWeights(self) -> pxr.Vt.FloatArray: ...
    def GetFaceVaryingInterpolationRule(self) -> str: ...
    def GetTriangleSubdivision(self) -> str: ...
    def GetVertexInterpolationRule(self) -> str: ...
    def SetCornerIndices(self, arg2: pxr.Vt.IntArray | typing.Iterable[int]) -> None: ...
    def SetCornerWeights(self, arg2: pxr.Vt.FloatArray | typing.Iterable[float]) -> None: ...
    def SetCreaseIndices(self, arg2: pxr.Vt.IntArray | typing.Iterable[int]) -> None: ...
    def SetCreaseLengths(self, arg2: pxr.Vt.IntArray | typing.Iterable[int]) -> None: ...
    def SetCreaseMethod(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetCreaseWeights(self, arg2: pxr.Vt.FloatArray | typing.Iterable[float]) -> None: ...
    def SetFaceVaryingInterpolationRule(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetTriangleSubdivision(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetVertexInterpolationRule(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...