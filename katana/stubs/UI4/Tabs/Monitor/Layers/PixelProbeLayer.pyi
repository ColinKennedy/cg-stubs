# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
from typing import ClassVar, Set, Tuple

class PixelProbeLayer(QT4GLLayerStack.LayerStack.Layer):
    _SelectBufferSize: ClassVar[int] = ...
    def __init__(self, valuePolicy, *args, **kwargs) -> None: ...
    def defaultProcessEvent(self, event): ...
    def drawGeometry(self): ...
    def getPickedObjects(self, mousePos): ...
    def paintGL(self): ...
    def processDragEvent(self, event): ...