import pxr.Gf as Gf
from typing import Any, Callable, ClassVar

class UsdviewApi:
    __init__: ClassVar[Callable] = ...
    AddPrimToSelection: ClassVar[Callable] = ...
    ClearPrimSelection: ClassVar[Callable] = ...
    ComputeModelsFromSelection: ClassVar[Callable] = ...
    ComputeSelectedPrimsOfType: ClassVar[Callable] = ...
    GetSettings: ClassVar[Callable] = ...
    GetViewportCurrentRendererId: ClassVar[Callable] = ...
    GetViewportRendererNames: ClassVar[Callable] = ...
    GrabViewportShot: ClassVar[Callable] = ...
    GrabWindowShot: ClassVar[Callable] = ...
    PrintStatus: ClassVar[Callable] = ...
    SetViewportRenderer: ClassVar[Callable] = ...
    UpdateGUI: ClassVar[Callable] = ...
    UpdateViewport: ClassVar[Callable] = ...
    _ExportSession: ClassVar[Callable] = ...
    viewerMode: Any
    @property
    def cameraPrim(self) -> Any: ...
    @property
    def configDir(self) -> Any: ...
    @property
    def currentGfCamera(self) -> Any: ...
    @property
    def dataModel(self) -> Any: ...
    @property
    def frame(self) -> Any: ...
    @property
    def layer(self) -> Any: ...
    @property
    def prim(self) -> Any: ...
    @property
    def property(self) -> Any: ...
    @property
    def qMainWindow(self) -> Any: ...
    @property
    def selectedInstances(self) -> Any: ...
    @property
    def selectedPaths(self) -> Any: ...
    @property
    def selectedPoint(self) -> Any: ...
    @property
    def selectedPrims(self) -> Any: ...
    @property
    def spec(self) -> Any: ...
    @property
    def stage(self) -> Any: ...
    @property
    def stageIdentifier(self) -> Any: ...
    @property
    def viewportSize(self) -> Any: ...