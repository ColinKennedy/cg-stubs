# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import Utils.EventModule as EventModule
import UI4.Tabs.NodeGraphTab.Layers as Layers
import NodeGraphView as NodeGraphView
import NodegraphAPI as NodegraphAPI
import UI4.FormMaster.ParameterPolicy as ParameterPolicy
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4GLLayerStack as QT4GLLayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import RenderingAPI as RenderingAPI
import UI4 as UI4
import Utils as Utils
import typing
import weakref
from Callbacks.Callbacks import Callbacks as Callbacks
from UI4.KatanaPrefs.KatanaPrefsObject import KatanaPrefs as KatanaPrefs
from UI4.Widgets.BaseNodeGraphLayerStack import BaseNodeGraphLayerStack
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

_NUM_VIEW_STATES: int

class NodegraphWidget(BaseNodeGraphLayerStack):
    _NodegraphWidget__connectPort: ClassVar[int] = ...
    _NodegraphWidget__connectReturn: ClassVar[int] = ...
    _NodegraphWidget__connectSend: ClassVar[int] = ...
    _NodegraphWidget__maxNGVViewScale: ClassVar[float] = ...
    _NodegraphWidget__minNGVViewScale: ClassVar[float] = ...
    _NodegraphWidget__networkMaterialAutoConnectableNodeTypeNames: ClassVar[list] = ...
    _NodegraphWidget__nodegraphWidgetList: ClassVar[weakref.WeakKeyDictionary] = ...
    inputSidebar: ClassVar[int] = ...
    outputSidebar: ClassVar[int] = ...
    def __init__(self, parent: PyQt5.QtWidgets.QWidget) -> None: ...
    def _NodegraphWidget__addInputPortWithParams(self, node: NodegraphAPI.Node, params): ...
    def _NodegraphWidget__addOutputPortWithParams(self, node: NodegraphAPI.Node, params): ...
    def _NodegraphWidget__autoConnectToTerminalNode(self, terminalNode, newNode): ...
    def _NodegraphWidget__buildLayers(self): ...
    def _NodegraphWidget__capNodeGraphViewScale(self, viewScale): ...
    def _NodegraphWidget__currentNodeViewChanged(self, _previousViewNode, currentViewNode): ...
    def _NodegraphWidget__editBackdropInNgvCallback(self, node: NodegraphAPI.Node, _mouseButton): ...
    def _NodegraphWidget__explodeSelectionReal(self): ...
    def _NodegraphWidget__gatherCurrentlySelectedBackdropsByZDepth(self): ...
    @staticmethod
    def _NodegraphWidget__getHitKey(a: tuple[str, dict]) -> int: ...
    def _NodegraphWidget__getTerminalFloatingNode(self): ...
    def _NodegraphWidget__idle_callback(self, *args, **kwargs): ...
    def _NodegraphWidget__isNodeAutoConnectable(self, terminalNode, newNode): ...
    def _NodegraphWidget__loadbegin_callback(self, *args, **kwargs): ...
    def _NodegraphWidget__loadend_callback(self, *args, **kwargs): ...
    def _NodegraphWidget__mergeSelectedNodesReal(self): ...
    def _NodegraphWidget__nodeDeleteHandler(self, eventType, eventID, node: NodegraphAPI.Node, *args, **kwargs): ...
    def _NodegraphWidget__nodeDeselectAllInNgvCallback(self): ...
    def _NodegraphWidget__nodeGroupEnteredInNgvCallback(self, node: NodegraphAPI.Node, _mouseButton): ...
    def _NodegraphWidget__nodeRenamedInNgvCallback(self, node: NodegraphAPI.Node, name): ...
    def _NodegraphWidget__nodeSelectedInNgvCallback(self, nodes: NodegraphAPI.Node | list[NodegraphAPI.Node], selected): ...
    def _NodegraphWidget__nodeSetBypassedInNgvCallback(self, node: NodegraphAPI.Node, bypassed): ...
    def _NodegraphWidget__nodeSetEditedInNgvCallback(self, node: NodegraphAPI.Node, edited): ...
    def _NodegraphWidget__nodeSetViewedInNgvCallback(self, node: NodegraphAPI.Node, viewed): ...
    def _NodegraphWidget__nodeStateRefreshRequestedCallback(self, node: NodegraphAPI.Node): ...
    def _NodegraphWidget__nodeToolTipRequestedInNgvCallback(self, node: NodegraphAPI.Node, coords): ...
    def _NodegraphWidget__nodeUpdatedInNgvCallback(self, node: NodegraphAPI.Node, noop): ...
    def _NodegraphWidget__nodeViewStateNextCallback(self, node: NodegraphAPI.Node): ...
    def _NodegraphWidget__offsetFloatingNodePositions(self, terminalNode, newNodes): ...
    def _NodegraphWidget__popupContextMenuInNgvCallback(self, node: NodegraphAPI.Node, _mouseButton): ...
    def _NodegraphWidget__popupPortMenuInNgvCallback(self, port: NodegraphAPI.Port, portCoords): ...
    def _NodegraphWidget__portConnectedInNgvCallback(self, portA, portB): ...
    def _NodegraphWidget__portDisconnectedInNgvCallback(self, portA, portB): ...
    def _NodegraphWidget__portRenamedInNgvCallback(self, port: NodegraphAPI.Port, newPortName): ...
    def _NodegraphWidget__prefChanged_CB(self, eventType, eventID, *args, **kwargs): ...
    def _NodegraphWidget__reconnectAfterCollapse(self, nodes): ...
    def _NodegraphWidget__sidebarUpdatedInNgvCallback(self, groupNode, sidebar): ...
    def _NodegraphWidget__smoothstep(self, a, b, x): ...
    def _NodegraphWidget__startDragInNgvCallback(self, obj, _mouseButton): ...
    def _NodegraphWidget__toggleNodesInputConnectionsVisibilityHandler(self, *_, **kwargs): ...
    def _NodegraphWidget__toggleSelectedNodesInputConnectionsVisibilityHandler(self, *_): ...
    def _NodegraphWidget__toolTipRequestedInNgvCallback(self, port: NodegraphAPI.Port, portCoords): ...
    def _NodegraphWidget__updateDimmingMode(self, mode): ...
    def alignSelection(self): ...
    def autoPlace(self, nodes: Sequence[NodegraphAPI.Node]) -> bool: ...
    def canCollapseSelectionToStack(self): ...
    def cleanup(self): ...
    def clearTransientLayers(self): ...
    def collapseSelectedToStack(self): ...
    def collapseSelection(self): ...
    def createNodeType(self, nodeType, shouldFloat: bool = ..., maskInputPreferred: bool = ..., autoPlaceAllowed: bool = ...): ...
    def createStandardOrRendererSpecificNodes(self, value): ...
    def enableFloatingLayer(self): ...
    def event(self, e): ...
    def explodeSelection(self): ...
    def extractNodes(self, nodes): ...
    def fitBackdropNode(self): ...
    def fitSticky(self): ...
    def floatNodes(self, nodes: Sequence[NodegraphAPI.Node]): ...
    def focusInEvent(self, event: QFocusEvent): ...
    def focusOutEvent(self, event: QFocusEvent): ...
    def frameNodes(self, nodes, zoom: bool = ...): ...
    @staticmethod
    def getAllNodeGraphWidgets(): ...
    def getCurrentNodeView(self): ...
    def getGraphInteraction(self): ...
    def getGroupNodeUnderMouse(self): ...
    def getNetworkMaterialContextNodeNames(self) -> list[str]: ...
    def getNetworkMaterialNodeTypeNames(self) -> list[str]: ...
    def getNodeGraphContext(self) -> str: ...
    def getPointAdjustedToGroupNodeSpace(self, groupNode, point): ...
    def getPopupMenuClickLocation(self): ...
    def getPseudoTopLevelWidget(self): ...
    def getRecentNode(self): ...
    def getRendererContext(self, node: NodegraphAPI.Node) -> str: ...
    def getValidNodeTypesForCurrentContext(self): ...
    def getValidNodeTypesForCurrentRenderer(self): ...
    def getWorldBounds(self): ...
    def hasGroupNodeFocusChanged(self): ...
    def hitTestBox(self, p0, p1, viewNode: Incomplete | None = ...): ...
    def hitTestFirstHitForType(self, p, type): ...
    def hitTestFirstHitForTypeWithOptions(self, p, hitType, *args): ...
    def hitTestForType(self, p, type, excludeNodes: Incomplete | None = ...): ...
    def hitTestForTypeStartsWith(self, p, type): ...
    def hitTestForTypeWithOptions(self, p, hitType, *args): ...
    def hitTestNodeButtons(self, p): ...
    def hitTestPoint(self, p): ...
    def idleUpdate(self): ...
    def isolateNode(self, node: NodegraphAPI.Node): ...
    def mergeSelectedNodes(self): ...
    def nodeMenu(self): ...
    def paintGL(self): ...
    def placeNode(self, node: NodegraphAPI.Node, shouldFloat: bool = ..., maskInputPreferred: bool = ..., autoPlaceAllowed: bool = ...): ...
    def placeNodes(self, nodes: Sequence[NodegraphAPI.Node], shouldFloat: bool = ..., autoPlaceAllowed: bool = ...): ...
    def removeFloatingNode(self): ...
    def removeFloatingNodes(self): ...
    def resizeEvent(self, event: PyQt5.QtGui.QResizeEvent): ...
    def sendSelectedBackdropNodesToBack(self): ...
    def sendSelectedBackdropNodesToFront(self): ...
    def setCurrentNodeView(self, node: NodegraphAPI.Node): ...
    def setEyePoint(self, x): ...
    def setFloatingLayerBasePosition(self, pos): ...
    def setGraphInteraction(self, flag): ...
    def setGroupNodeAsRoot(self, groupNode): ...
    def setNGVShapeAttrs(self, node: NodegraphAPI.Node, attrDict): ...
    def setNodeGraphContext(self, context): ...
    def setPopupMenuClickLocation(self, x, y): ...
    def setViewScale(self, x, final: bool = ...): ...
    def shouldAutoScroll(self): ...
    def showEvent(self, event: PyQt5.QtGui.QShowEvent): ...
    def showLayeredMenu(self, menu): ...
    def toggleTeleports(self): ...
    @classmethod
    def updateAllNodegraphWidgets(cls): ...
    def updateOtherNodegraphsInSameNode(self): ...

def _OnNodeCreatedCallback(node: typing.Optional[NodegraphAPI.Node] = ..., nodeType: Incomplete | None = ..., **_kwargs): ...
def _SendBackdropNodesToBack(nodes: list) -> bool: ...
def _SendBackdropNodesToFront(nodes: list, undo: bool = ...) -> bool: ...
def __nodegraphPrefsCallback(*args, **kwargs): ...
def __nodegraphRedrawCallback(args): ...
def _getZDepthAttr(node: NodegraphAPI.Node): ...