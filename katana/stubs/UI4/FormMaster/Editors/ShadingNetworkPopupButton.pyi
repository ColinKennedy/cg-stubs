# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
import UI4.Widgets as Widgets
from UI4.Widgets.BaseNodeGraphLayerStack import BaseNodeGraphLayerStack
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ErrorMessageWarningLabel(PyQt5.QtWidgets.QFrame):
    def __init__(self, parent, errorText) -> None: ...

class NodegraphWidgetLite(BaseNodeGraphLayerStack):
    _NodegraphWidgetLite__pixmaps: ClassVar[dict] = ...
    nodePortChosen: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    pressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, node: NodegraphAPI.Node, restrictPortType: Incomplete | None = ..., additionalLayers: Incomplete | None = ...) -> None: ...
    def _NodegraphWidgetLite__getMenuPopup(self): ...
    def _NodegraphWidgetLite__nodeLinkClick(self, node: NodegraphAPI.Node, portA, portB, x, y): ...
    def _NodegraphWidgetLite__nodePortClick(self, node: NodegraphAPI.Node, which, x, y): ...
    def _NodegraphWidgetLite__portMenuItemChosen(self, item, meta): ...
    def _NodegraphWidgetLite__showMenuPopup(self, x, y): ...
    def event(self, e): ...
    def fillPortMenu(self, menu, node: NodegraphAPI.Node, isInput, onlyConnectedToNode: Incomplete | None = ...): ...
    def frameAll(self): ...
    def getCurrentNodeView(self): ...
    def getNode(self) -> NodegraphAPI.Node: ...
    def getNodeDisplayName(self, node: NodegraphAPI.Node): ...
    def getWorldBounds(self): ...
    def hideEvent(self, event): ...
    def hitTestForTypeWithOptions(self, p, hitType, *args): ...
    def hitTestPoint(self, p): ...
    def idleUpdate(self): ...
    def removeLayers(self): ...
    def resizeEvent(self, evt): ...

class ShadingNetworkPopupButton(PyQt5.QtWidgets.QPushButton):
    _ShadingNetworkPopupButton__pixmaps: ClassVar[dict] = ...
    nodePortChosen: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    popupClosed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, restrictPortType: Incomplete | None = ..., networkAttrMethod: Incomplete | None = ..., additionalLayers: Incomplete | None = ...) -> None: ...
    def _ShadingNetworkPopupButton__buildPopup(self): ...
    def _ShadingNetworkPopupButton__getNetworkHash(self): ...
    def _ShadingNetworkPopupButton__nodePortChosen(self, nodeName, portType, portName): ...
    def _ShadingNetworkPopupButton__popClicked(self): ...
    def _ShadingNetworkPopupButton__popupClosed(self): ...
    def _ShadingNetworkPopupButton__popupShow(self): ...
    def hidePopup(self): ...

class _HidingVBox(PyQt5.QtWidgets.QFrame):
    closeSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    hideSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    networkHash: ClassVar[None] = ...
    showSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self) -> None: ...
    def closeEvent(self, e): ...
    def hideEvent(self, e): ...
    def showEvent(self, e): ...

class _NodeDrawingLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def paintGL(self): ...

class _PortInteractionLayer(QT4GLLayerStack.LayerStack.Layer):
    nodeLinkClick: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    nodePortClick: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _PortInteractionLayer__getNodeAndArrowShapeAt(self, position: None): ...
    def _PortInteractionLayer__processKeyPress(self, event: PyQt5.QtGui.QKeyEvent): ...
    def _PortInteractionLayer__processMouseMove(self, event: PyQt5.QtGui.QMouseEvent) -> bool: ...
    def _PortInteractionLayer__processMousePress(self, event: PyQt5.QtGui.QMouseEvent) -> bool: ...
    def paintGL(self): ...
    def processEvent(self, event: PyQt5.QtGui.QEvent): ...