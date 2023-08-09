# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class FastLabel(PyQt5.QtWidgets.QWidget):
    def __init__(self, text, parent) -> None: ...
    def _FastLabel__growWidth(self): ...
    def alignment(self): ...
    def minimumSizeHint(self): ...
    def paintEvent(self, event): ...
    def setAlignment(self, alignment): ...
    def setText(self, text): ...