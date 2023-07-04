# mypy: disable_error_code = misc
import Boost.Python
import pxr.UsdGeom
from typing import Any, ClassVar, overload

class Field3DAsset(FieldAsset):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateFieldDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFieldPurposeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Field3DAsset: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Field3DAsset: ...
    def GetFieldDataTypeAttr(self) -> pxr.Usd.Attribute: ...
    def GetFieldPurposeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class FieldAsset(FieldBase):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateFieldDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFieldIndexAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFieldNameAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFilePathAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateVectorDataRoleHintAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FieldAsset: ...
    def GetFieldDataTypeAttr(self) -> pxr.Usd.Attribute: ...
    def GetFieldIndexAttr(self) -> pxr.Usd.Attribute: ...
    def GetFieldNameAttr(self) -> pxr.Usd.Attribute: ...
    def GetFilePathAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def GetVectorDataRoleHintAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class FieldBase(pxr.UsdGeom.Xformable):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> FieldBase: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class OpenVDBAsset(FieldAsset):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def CreateFieldClassAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    def CreateFieldDataTypeAttr(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> OpenVDBAsset: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> OpenVDBAsset: ...
    def GetFieldClassAttr(self) -> pxr.Usd.Attribute: ...
    def GetFieldDataTypeAttr(self) -> pxr.Usd.Attribute: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...

class Tokens(Boost.Python.instance):
    Color: ClassVar[Any] = ...  # read-only
    Field3DAsset: ClassVar[Any] = ...  # read-only
    FieldAsset: ClassVar[Any] = ...  # read-only
    FieldBase: ClassVar[Any] = ...  # read-only
    None_: ClassVar[Any] = ...  # read-only
    Normal: ClassVar[Any] = ...  # read-only
    OpenVDBAsset: ClassVar[Any] = ...  # read-only
    Point: ClassVar[Any] = ...  # read-only
    Vector: ClassVar[Any] = ...  # read-only
    Volume: ClassVar[Any] = ...  # read-only
    bool_: ClassVar[Any] = ...  # read-only
    double2: ClassVar[Any] = ...  # read-only
    double3: ClassVar[Any] = ...  # read-only
    double_: ClassVar[Any] = ...  # read-only
    field: ClassVar[Any] = ...  # read-only
    fieldClass: ClassVar[Any] = ...  # read-only
    fieldDataType: ClassVar[Any] = ...  # read-only
    fieldIndex: ClassVar[Any] = ...  # read-only
    fieldName: ClassVar[Any] = ...  # read-only
    fieldPurpose: ClassVar[Any] = ...  # read-only
    filePath: ClassVar[Any] = ...  # read-only
    float2: ClassVar[Any] = ...  # read-only
    float3: ClassVar[Any] = ...  # read-only
    float_: ClassVar[Any] = ...  # read-only
    fogVolume: ClassVar[Any] = ...  # read-only
    half: ClassVar[Any] = ...  # read-only
    half2: ClassVar[Any] = ...  # read-only
    half3: ClassVar[Any] = ...  # read-only
    int2: ClassVar[Any] = ...  # read-only
    int3: ClassVar[Any] = ...  # read-only
    int64: ClassVar[Any] = ...  # read-only
    int_: ClassVar[Any] = ...  # read-only
    levelSet: ClassVar[Any] = ...  # read-only
    mask: ClassVar[Any] = ...  # read-only
    matrix3d: ClassVar[Any] = ...  # read-only
    matrix4d: ClassVar[Any] = ...  # read-only
    quatd: ClassVar[Any] = ...  # read-only
    staggered: ClassVar[Any] = ...  # read-only
    string: ClassVar[Any] = ...  # read-only
    uint: ClassVar[Any] = ...  # read-only
    unknown: ClassVar[Any] = ...  # read-only
    vectorDataRoleHint: ClassVar[Any] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class Volume(pxr.UsdGeom.Gprim):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, prim: pxr.Usd.Prim) -> None: ...
    @overload
    def __init__(self, schemaObj: pxr.Usd.SchemaBase) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def BlockFieldRelationship(self, name: str | pxr.Ar.ResolvedPath) -> bool: ...
    def CreateFieldRelationship(self, name: str | pxr.Ar.ResolvedPath, fieldPath: pxr.Sdf.Path | str) -> bool: ...
    @classmethod
    def Define(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Volume: ...
    @classmethod
    def Get(cls, stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> Volume: ...
    def GetFieldPath(self, name: str | pxr.Ar.ResolvedPath) -> pxr.Sdf.Path: ...
    def GetFieldPaths(self) -> dict: ...
    @classmethod
    def GetSchemaAttributeNames(cls, includeInherited: bool = ...) -> list[str]: ...
    def HasFieldRelationship(self, name: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def _GetStaticTfType(cls) -> pxr.Tf.Type: ...
    def __bool__(self) -> bool: ...
    def __reduce__(self) -> Any: ...