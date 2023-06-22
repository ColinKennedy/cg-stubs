import Boost.Python
import pxr.Usd
from typing import Any, ClassVar, overload

class CullStyle(Boost.Python.enum):
    CULL_STYLE_BACK: ClassVar[CullStyle] = ...
    CULL_STYLE_BACK_UNLESS_DOUBLE_SIDED: ClassVar[CullStyle] = ...
    CULL_STYLE_FRONT: ClassVar[CullStyle] = ...
    CULL_STYLE_NOTHING: ClassVar[CullStyle] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class DrawMode(Boost.Python.enum):
    DRAW_GEOM_FLAT: ClassVar[DrawMode] = ...
    DRAW_GEOM_ONLY: ClassVar[DrawMode] = ...
    DRAW_GEOM_SMOOTH: ClassVar[DrawMode] = ...
    DRAW_POINTS: ClassVar[DrawMode] = ...
    DRAW_SHADED_FLAT: ClassVar[DrawMode] = ...
    DRAW_SHADED_SMOOTH: ClassVar[DrawMode] = ...
    DRAW_WIREFRAME: ClassVar[DrawMode] = ...
    DRAW_WIREFRAME_ON_SURFACE: ClassVar[DrawMode] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class Engine(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: pxr.Sdf.Path, arg3: object, arg4: object) -> None: ...
    def AddSelected(self, arg2: pxr.Sdf.Path, arg3: int) -> None: ...
    def ClearSelected(self) -> None: ...
    def GetCurrentRendererId(self) -> str: ...
    def GetRenderStats(self) -> dict: ...
    def GetRendererAovs(self) -> list[str]: ...
    def GetRendererCommandDescriptors(self) -> list: ...
    @classmethod
    def GetRendererDisplayName(cls, arg1: str) -> str: ...
    @classmethod
    def GetRendererPlugins(cls) -> list[str]: ...
    def GetRendererSetting(self, arg2: str) -> Any: ...
    def GetRendererSettingsList(self) -> list: ...
    def InvokeRendererCommand(self, command: str, args: HdCommandArgs = ...) -> bool: ...
    @classmethod
    def IsColorCorrectionCapable(cls) -> bool: ...
    def IsConverged(self) -> bool: ...
    def IsPauseRendererSupported(self) -> bool: ...
    def IsStopRendererSupported(self) -> bool: ...
    def PauseRenderer(self) -> bool: ...
    def Render(self, arg2: pxr.Usd.Prim, arg3: RenderParams) -> None: ...
    def RestartRenderer(self) -> bool: ...
    def ResumeRenderer(self) -> bool: ...
    def SetCameraPath(self, arg2: pxr.Sdf.Path) -> None: ...
    def SetCameraState(self, arg2: pxr.Gf.Matrix4d, arg3: pxr.Gf.Matrix4d) -> None: ...
    def SetColorCorrectionSettings(self, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str) -> None: ...
    def SetFraming(self, arg2: pxr.CameraUtil.Framing) -> None: ...
    def SetLightingState(self, arg2: object, arg3: pxr.Glf.SimpleMaterial, arg4: pxr.Gf.Vec4f) -> None: ...
    def SetOverrideWindowPolicy(self, arg2: tuple[bool, pxr.CameraUtil.ConformWindowPolicy]) -> None: ...
    def SetRenderBufferSize(self, arg2: pxr.Gf.Vec2i) -> None: ...
    def SetRenderViewport(self, arg2: pxr.Gf.Vec4d) -> None: ...
    def SetRendererAov(self, arg2: str) -> bool: ...
    def SetRendererPlugin(self, arg2: str) -> bool: ...
    def SetRendererSetting(self, arg2: str, arg3: Any) -> None: ...
    def SetSelected(self, arg2: list[pxr.Sdf.Path]) -> None: ...
    def SetSelectionColor(self, arg2: pxr.Gf.Vec4f) -> None: ...
    def SetWindowPolicy(self, arg2: pxr.CameraUtil.ConformWindowPolicy) -> None: ...
    def StopRenderer(self) -> bool: ...
    def TestIntersection(self, arg2: pxr.Gf.Matrix4d, arg3: pxr.Gf.Matrix4d, arg4: pxr.Usd.Prim, arg5: RenderParams) -> tuple: ...
    def __reduce__(self) -> Any: ...

class RenderParams(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    applyRenderState: Any
    bboxLineColor: Any
    bboxLineDashSize: Any
    bboxes: Any
    clearColor: Any
    clipPlanes: Any
    colorCorrectionMode: Any
    complexity: Any
    cullStyle: Any
    drawMode: Any
    enableIdRender: Any
    enableLighting: Any
    enableSampleAlphaToCoverage: Any
    enableSceneLights: Any
    enableSceneMaterials: Any
    enableUsdDrawModes: Any
    forceRefresh: Any
    frame: Any
    gammaCorrectColors: Any
    highlight: Any
    ocioColorSpace: Any
    ocioDisplay: Any
    ocioLook: Any
    ocioView: Any
    overrideColor: Any
    showGuides: Any
    showProxy: Any
    showRender: Any
    wireframeColor: Any
    def __init__(self) -> None: ...
    def __reduce__(self) -> Any: ...

class RendererCommandArgDescriptor(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def argName(self) -> Any: ...
    @property
    def defaultValue(self) -> Any: ...

class RendererCommandDescriptor(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def commandArgs(self) -> Any: ...
    @property
    def commandDescription(self) -> Any: ...
    @property
    def commandName(self) -> Any: ...

class RendererSetting(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def defValue(self) -> Any: ...
    @property
    def key(self) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def type(self) -> Any: ...

class RendererSettingType(Boost.Python.enum):
    FLAG: ClassVar[RendererSettingType] = ...
    FLOAT: ClassVar[RendererSettingType] = ...
    INT: ClassVar[RendererSettingType] = ...
    STRING: ClassVar[RendererSettingType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...