# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import PyFnAttribute as FnAttribute
import UI4.Widgets.MonitorLayer.Utils as MonitorLayerUtils
import Nodes2DAPI as Nodes2DAPI
import PyFnAttribute
import Utils as Utils
from PyUtilModule.VirtualKatana import RenderGlobals as RenderGlobals, RenderManager as RenderManager
from _typeshed import Incomplete
from typing import Set, Tuple

DISPLAY_WHILE_MANIPULATING: bool
IGNORE_ALPHA: bool
MONITOR_LAYER_DEFAULT: bool

class MonitorLayer:
    viewportFollowedByLiveRender: Incomplete
    def __init__(self, tab) -> None: ...
    def _MonitorLayer__cameraMatchesRenderCamera(self, viewport): ...
    def _MonitorLayer__getCatalogItemRenderCamera(self) -> tuple[int, str]: ...
    def _MonitorLayer__manipulationStarts(self): ...
    def _MonitorLayer__manipulationStops(self): ...
    def _MonitorLayer__on_catalog_clientSlotUpdate(self, eventType: str | None, eventID: object): ...
    def _MonitorLayer__on_catalog_itemDelete(self, eventType: str | None, eventID: object, item: CatalogAPI.CatalogItem): ...
    def _MonitorLayer__on_catalog_itemImageRegionUpdate(self, eventType: str | None, eventID: object, item: CatalogAPI.CatalogItem, layerview: Incomplete | None = ..., updateRects: Incomplete | None = ...): ...
    def _MonitorLayer__on_catalog_itemRenderCameraUpdate(self, eventType: str | None, eventID: object, item: CatalogAPI.CatalogItem): ...
    def _MonitorLayer__on_catalog_rebuild(self, eventType, eventID): ...
    def _MonitorLayer__registerMonitorLayerEventHandlers(self): ...
    def _MonitorLayer__resetMonitorLayer(self): ...
    def _MonitorLayer__setMonitorLayerOption(self, viewport, name, value: PyFnAttribute.IntAttribute = ...): ...
    def _MonitorLayer__setMonitorLayerOptionForAllViewports(self, name: str, value: PyFnAttribute.IntAttribute = ...): ...
    def _MonitorLayer__setUp(self): ...
    def _MonitorLayer__tearDown(self): ...
    def _MonitorLayer__unregisterLayerEventHandlers(self): ...
    def matchFirstViewportCameraWithCatalogItemRenderCamera(self): ...
    def setDisplayWhileManipulating(self, displayWhileManipulating: bool): ...
    def setEnabled(self, enabled: bool): ...
    def setIgnoresAlpha(self, value): ...
    def setMonitorLayerVisible(self, visible: bool): ...
    def setupCatalogItem(self): ...
    def toggleEnabled(self): ...
    def toggleIgnoresAlpha(self): ...
    def toggledisplayWhileManipulating(self): ...
    def update(self): ...
    def updateImageVisibilityForViewport(self, viewport, visible: bool = ...): ...
    def updateMonitorLayerIgnoresAlpha(self): ...
    def updateSelection(self): ...
    @property
    def displayWhileManipulating(self): ...
    @property
    def enabled(self): ...
    @property
    def monitorLayerIgnoresAlpha(self): ...