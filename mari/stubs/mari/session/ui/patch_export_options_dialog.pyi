from PySide2 import QtWidgets

class PatchExportOptionsDialog(QtWidgets.QDialog):
    def __init__(self, geoEntity, parent) -> None: ...
    @property
    def selectedPatches(self): ...
    @selectedPatches.setter
    def selectedPatches(self, selectedPatches) -> None: ...
    @property
    def selectedPatchesText(self): ...