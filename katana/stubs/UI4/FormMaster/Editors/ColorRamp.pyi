# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyOpenColorIO as OCIO
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4Color as QT4Color
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.FormMaster.Editors.BaseRamp
import Utils as Utils
import collections
from UI4.FormMaster.Editors.BaseRamp import BaseRampFormWidget as BaseRampFormWidget
from UI4.FormMaster.Editors.SortableAttributeDropEditor import RegisterCoPolicyWidgetHintKey as RegisterCoPolicyWidgetHintKey
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ColorRampFormWidget(UI4.FormMaster.Editors.BaseRamp.BaseRampFormWidget):
    Presets: ClassVar[collections.OrderedDict] = ...
    ValuesTypeString: ClassVar[str] = ...
    def __init__(self, parent, policy, factory) -> None: ...
    def _ColorRampFormWidget__on_gradientWidget_rampChanged(self): ...
    def _ColorRampFormWidget__on_menu_aboutToShow(self): ...
    def _ColorRampFormWidget__on_presetAction_triggered(self): ...
    def _ColorRampFormWidget__sensitivityMenuCallback(self, action): ...
    def _ColorRampFormWidget__updateFilmlookActionText(self): ...
    def _addControlWidgets(self, knots: list[tuple], interpolator: str, interpolatorOptions: list[str], layout: PyQt5.QtWidgets.QHBoxLayout): ...
    def _lockChanged(self, state: bool): ...
    def _updateControlWidgets(self, knots: list[tuple], interpolator: str): ...

class GradientRender(PyQt5.QtWidgets.QWidget):
    def __init__(self, filmlook, width: int = ..., height: int = ..., parent: Incomplete | None = ...) -> None: ...
    def getColorAt(self, pos: PyQt5.QtGui.QPoint) -> PyQt5.QtGui.QColor: ...
    def paintEvent(self, e): ...
    def setFilmlookEnabled(self, value): ...
    def setKnots(self, knots: list[Knot], interp: str = ...): ...

class GradientWidget(PyQt5.QtWidgets.QWidget):
    rampChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, knots, interp, height: int = ..., useFilmlook: bool = ..., restrictComponents: bool = ..., parent: Incomplete | None = ...) -> None: ...
    def _GradientWidget__drawPositionLabel(self, knot): ...
    def _GradientWidget__hidePositionLabel(self): ...
    def _GradientWidget__knot_point(self, gpos): ...
    def _GradientWidget__on_xLabelVisibilityTimer_timeout(self): ...
    def addKnot(self, pos, color, render: bool = ...): ...
    def getInterp(self): ...
    def getKnotSensitivity(self): ...
    def hideEvent(self, event: PyQt5.QtGui.QHideEvent): ...
    def knotChanged(self, final: bool = ...): ...
    def knotClicked(self, knot): ...
    def knotDragged(self, knot, xmove, x): ...
    def knots(self): ...
    def mouseMoveEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
    def mousePressEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
    def mouseReleaseEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
    def removeKnot(self, knot): ...
    def render(self): ...
    def replaceKnots(self, knots, emit: bool = ...): ...
    def resizeEvent(self, event): ...
    def setFilmlookEnabled(self, value): ...
    def setInterp(self, interp): ...
    def setKnotSensitivity(self, sensitivity): ...

class Knot(PyQt5.QtWidgets.QWidget):
    clicked: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    knotChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    knotRemoved: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    positionChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, position, color, useFilmLook: bool = ..., restrictComponents: bool = ..., parent: Incomplete | None = ...) -> None: ...
    def _Knot__remove(self): ...
    def _Knot__updateBrush(self): ...
    def color(self): ...
    def colorChange(self, color): ...
    def contextMenuEvent(self, event): ...
    def isDown(self): ...
    def keyPressEvent(self, event): ...
    def mouseDoubleClickEvent(self, event): ...
    def mouseMoveEvent(self, event): ...
    def mousePressEvent(self, event): ...
    def mouseReleaseEvent(self, event): ...
    def paintEvent(self, ev): ...
    def position(self): ...
    def setColor(self, color): ...
    def setDown(self, value): ...
    def setFilmlookEnabled(self, value): ...
    def setPosition(self, position): ...
    def sizeHint(self): ...

class KnotToolTip(PyQt5.QtWidgets.QLabel):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...

def EvalSpline(u, knots): ...
def clamp(minvalue, maxvalue, value): ...
def createQColor(c, filmLook: bool = ...): ...
def fit(val, inmin, inmax, outmin, outmax): ...
def lerp(mix, a, b): ...