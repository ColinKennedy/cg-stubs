import PySide6.QtWidgets
import pxr.Sdf as Sdf
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq import Utils as Utils
from pxr.Usdviewq.common import UIFonts as UIFonts, UIPrimTypeColors as UIPrimTypeColors
from typing import Callable, ClassVar

_GetPrimInfo: Callable

class PrimViewColumnIndex(ConstantsGroup):
    DRAWMODE: ClassVar[int] = ...
    GUIDES: ClassVar[int] = ...
    NAME: ClassVar[int] = ...
    TYPE: ClassVar[int] = ...
    VIS: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class PrimViewItem(PySide6.QtWidgets.QTreeWidgetItem):
    __init__: ClassVar[Callable] = ...
    _GetForegroundColor: ClassVar[Callable] = ...
    _HasAuthoredDrawMode: ClassVar[Callable] = ...
    _drawModeData: ClassVar[Callable] = ...
    _extractInfo: ClassVar[Callable] = ...
    _guideData: ClassVar[Callable] = ...
    _isComputedDrawModeInherited: ClassVar[Callable] = ...
    _isVisInherited: ClassVar[Callable] = ...
    _nameData: ClassVar[Callable] = ...
    _pull: ClassVar[Callable] = ...
    _pushVisRecursive: ClassVar[Callable] = ...
    _resetAncestorsRecursive: ClassVar[Callable] = ...
    _typeData: ClassVar[Callable] = ...
    _visData: ClassVar[Callable] = ...
    addChildren: ClassVar[Callable] = ...
    canChangeVis: ClassVar[Callable] = ...
    data: ClassVar[Callable] = ...
    loadVis: ClassVar[Callable] = ...
    makeVisible: ClassVar[Callable] = ...
    needsChildrenPopulated: ClassVar[Callable] = ...
    propagateDrawMode: ClassVar[Callable] = ...
    propagateVis: ClassVar[Callable] = ...
    push: ClassVar[Callable] = ...
    setLoaded: ClassVar[Callable] = ...
    setVisible: ClassVar[Callable] = ...
    toggleGuides: ClassVar[Callable] = ...
    toggleVis: ClassVar[Callable] = ...
    visChanged: ClassVar[Callable] = ...