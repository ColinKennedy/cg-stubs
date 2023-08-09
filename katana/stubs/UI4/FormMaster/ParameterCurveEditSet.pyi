# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Utils as Utils
from typing import Set, Tuple

class ParameterCurveEditWatcher:
    def __init__(self) -> None: ...
    def _ParameterCurveEditWatcher__node_setEdited_callback(self, args): ...
    def _ParameterCurveEditWatcher__node_setName_callback(self, args): ...
    def _ParameterCurveEditWatcher__parameter_finalizeValue_callback(self, args): ...
    def _ParameterCurveEditWatcher__parameter_setName_callback(self, args): ...
    def _ParameterCurveEditWatcher__parameter_showKeys_callback(self, args): ...
    def _initializeSet(self, curveEditSetCopy): ...
    def _isActive(self, paramFullName): ...
    def _keysActiveChanged(self, paramFullName, active): ...
    def _keysChanged(self, paramFullName): ...
    def _nameChanged(self, oldParamFullName, newParamFullName, newParamLocalName): ...
    def _nodeNameChanged(self, oldNodeName, newNodeName): ...
    def _showKeys(self, paramFullName, show): ...

def ClearParameterCurveEditSet(): ...
def GetParameterCurveEdited(fullParamName): ...
def SetParameterCurveEdited(fullParamName, setEdit): ...