import Boost.Python
import types
from typing import Any, Callable, ClassVar, overload

Fatal: Callable
GetCodeLocation: Callable
PrepareModule: Callable
PreparePythonModule: Callable
RaiseCodingError: Callable
RaiseRuntimeError: Callable
Status: Callable
TF_APPLICATION_EXIT_TYPE: DiagnosticType
TF_DIAGNOSTIC_CODING_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_FATAL_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_STATUS_TYPE: DiagnosticType
TF_DIAGNOSTIC_WARNING_TYPE: DiagnosticType
Warn: Callable
_Alpha: _TestEnum
_Bravo: _TestEnum
_Charlie: _TestEnum
_Delta: _TestEnum

class CallContext(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def file(self) -> type: ...
    @property
    def function(self) -> type: ...
    @property
    def line(self) -> type: ...
    @property
    def prettyFunction(self) -> type: ...

class CppException(Exception): ...

class Debug(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetDebugSymbolDescription(cls, arg1: str) -> str: ...
    @classmethod
    def GetDebugSymbolDescriptions(cls) -> str: ...
    @classmethod
    def GetDebugSymbolNames(cls) -> list[str]: ...
    @classmethod
    def IsDebugSymbolNameEnabled(cls, arg1: str) -> bool: ...
    @classmethod
    def SetDebugSymbolsByName(cls, pattern: str, value: bool) -> list[str]: ...
    @classmethod
    def SetOutputFile(cls, arg1: FILE) -> None: ...
    def __reduce__(self) -> Any: ...

class DiagnosticType(Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: str) -> Any: ...
    def __reduce__(self) -> Any: ...

class Enum(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetValueFromFullName(cls, arg1: str) -> Enum: ...
    def __reduce__(self) -> Any: ...

class Error(_DiagnosticBase):
    class Mark(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None: ...
        def Clear(self) -> bool: ...
        def GetErrors(self, *args, **kwargs) -> Any: ...
        def IsClean(self) -> bool: ...
        def SetMark(self) -> None: ...
        def __reduce__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def errorCode(self) -> Any: ...
    @property
    def errorCodeString(self) -> Any: ...

class ErrorException(RuntimeError):
    __init__: ClassVar[Callable] = ...

class MallocTag(Boost.Python.instance):
    class CallTree(Boost.Python.instance):
        class CallSite(Boost.Python.instance):
            def __init__(self, *args, **kwargs) -> None: ...
            def __reduce__(self) -> Any: ...
            @property
            def nBytes(self) -> Any: ...
            @property
            def name(self) -> Any: ...
        class PathNode(Boost.Python.instance):
            def __init__(self, *args, **kwargs) -> None: ...
            def GetChildren(self) -> list: ...
            def __reduce__(self) -> Any: ...
            @property
            def nAllocations(self) -> Any: ...
            @property
            def nBytes(self) -> Any: ...
            @property
            def nBytesDirect(self) -> Any: ...
            @property
            def siteName(self) -> Any: ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetCallSites(self) -> list: ...
        def GetPrettyPrintString(self) -> str: ...
        def GetRoot(self) -> MallocTag.CallTree.PathNode: ...
        def LogReport(self, rootName: str = ...) -> str: ...
        @overload
        def Report(self, rootName: str = ...) -> None: ...
        @overload
        def Report(self, fileName: str, rootName: str = ...) -> None: ...
        def __reduce__(self) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetCallStacks(self) -> list: ...
    @classmethod
    def GetCallTree(cls) -> MallocTag.CallTree: ...
    @classmethod
    def GetMaxTotalBytes(cls) -> int: ...
    @classmethod
    def GetTotalBytes(cls) -> int: ...
    @classmethod
    def Initialize(cls, arg1: str) -> bool: ...
    @classmethod
    def IsInitialized(cls) -> bool: ...
    @classmethod
    def SetCapturedMallocStacksMatchList(cls, arg1: str) -> None: ...
    @classmethod
    def SetDebugMatchList(cls, arg1: str) -> None: ...
    def __reduce__(self) -> Any: ...

class NamedTemporaryFile:
    __init__: ClassVar[Callable] = ...
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...
    @property
    def name(self) -> Any: ...

class Notice(Boost.Python.instance):
    class Listener(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None: ...
        def Revoke(self) -> Any: ...
        def __reduce__(self) -> Any: ...
    def __init__(self) -> None: ...
    @overload
    @classmethod
    def Register(cls, noticeType, callback, sender) -> Listener: ...
    @overload
    @classmethod
    def Register(cls, arg1: Type, arg2: object, arg3: object) -> Listener: ...
    def RegisterGlobally(self, noticeType, callback) -> Listener: ...
    @overload
    def Send(self, arg2: object) -> int: ...
    @overload
    def Send(self, sender) -> Any: ...
    def SendGlobally(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class PyModuleWasLoaded(Notice):
    def __init__(self, *args, **kwargs) -> None: ...
    def name(self) -> str: ...
    def __reduce__(self) -> Any: ...

class RefPtrTracker(Boost.Python.instance):
    def __init__(self, tupleargs, dictkwds) -> None: ...
    def GetAllTracesReport(self) -> str: ...
    def GetAllWatchedCountsReport(self) -> str: ...
    def GetTracesReportForWatched(self, arg2: int) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class ScopeDescription(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: str) -> None: ...
    def SetDescription(self, arg2: str) -> None: ...
    def __enter__(self) -> ScopeDescription: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType) -> None: ...
    def __reduce__(self) -> Any: ...

class ScriptModuleLoader(Boost.Python.instance):
    def __init__(self, tupleargs, dictkwds) -> None: ...
    def GetModuleNames(self) -> list[str]: ...
    def GetModulesDict(self) -> dict: ...
    def WriteDotFile(self, arg2: str) -> None: ...
    def _LoadModulesForLibrary(self, arg2: object) -> None: ...
    def _RegisterLibrary(self, arg2: object, arg3: object, arg4: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class Singleton(Boost.Python.instance):
    def __init__(self, tupleargs, dictkwds) -> None: ...
    def __reduce__(self) -> Any: ...

class StatusObject(_DiagnosticBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class Stopwatch(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def AddFrom(self, arg2: Stopwatch) -> None: ...
    def Reset(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def microseconds(self) -> type: ...
    @property
    def milliseconds(self) -> type: ...
    @property
    def nanoseconds(self) -> type: ...
    @property
    def sampleCount(self) -> type: ...
    @property
    def seconds(self) -> type: ...

class TemplateString(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: str) -> None: ...
    def GetEmptyMapping(self) -> dict: ...
    def GetParseErrors(self) -> list[str]: ...
    def SafeSubstitute(self, arg2: dict) -> str: ...
    def Substitute(self, arg2: dict) -> str: ...
    def __reduce__(self) -> Any: ...
    @property
    def template(self) -> type: ...
    @property
    def valid(self) -> type: ...

class Tf_PyEnumWrapper(Enum):
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def __and__(self, arg2: int) -> Any: ...
    @overload
    def __and__(self, arg2: Tf_PyEnumWrapper) -> Any: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    @overload
    def __or__(self, arg2: int) -> Any: ...
    @overload
    def __or__(self, arg2: Tf_PyEnumWrapper) -> Any: ...
    def __rand__(self, arg2: int) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __ror__(self, arg2: int) -> Any: ...
    def __rxor__(self, arg2: int) -> Any: ...
    @overload
    def __xor__(self, arg2: int) -> Any: ...
    @overload
    def __xor__(self, arg2: Tf_PyEnumWrapper) -> Any: ...
    @property
    def displayName(self) -> Any: ...
    @property
    def fullName(self) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def value(self) -> Any: ...

class Tf_TestAnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: str) -> None: ...
    def __bool__(self) -> bool: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    @overload
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    @overload
    def __ne__(self, other: object) -> bool: ...
    @overload
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def annotation(self) -> Any: ...

class Tf_TestPyContainerConversions(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetPairTimesTwo(self) -> Any: ...
    def GetTokens(self) -> Any: ...
    def GetVectorTimesTwo(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class Tf_TestPyOptional(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def TakesOptional(self, optString: object = ..., optStrvec: object = ...) -> tuple: ...
    def TestOptionalChar(self) -> Any: ...
    def TestOptionalDouble(self) -> Any: ...
    def TestOptionalFloat(self) -> Any: ...
    def TestOptionalInt(self) -> Any: ...
    def TestOptionalLong(self) -> Any: ...
    def TestOptionalShort(self) -> Any: ...
    def TestOptionalString(self) -> Any: ...
    def TestOptionalStringVector(self) -> Any: ...
    def TestOptionalUChar(self) -> Any: ...
    def TestOptionalUInt(self) -> Any: ...
    def TestOptionalULong(self) -> Any: ...
    def TestOptionalUShort(self) -> Any: ...
    def __reduce__(self) -> Any: ...

class Type(Boost.Python.instance):
    Unknown: ClassVar[Type] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg2: Type) -> None: ...
    @classmethod
    def AddAlias(cls, arg2: Type, arg3: str) -> None: ...
    @classmethod
    def Define(cls) -> Type: ...
    @classmethod
    def Find(cls) -> Type: ...
    @classmethod
    def FindByName(cls, arg1: str) -> Type: ...
    @classmethod
    def FindDerivedByName(cls, arg2: str) -> Type: ...
    def GetAliases(self, arg2: Type) -> tuple: ...
    def GetAllAncestorTypes(self) -> tuple: ...
    def GetAllDerivedTypes(self) -> tuple: ...
    @classmethod
    def GetRoot(cls) -> Type: ...
    def IsA(self, arg2: Type) -> bool: ...
    def _DumpTypeHierarchy(self, TfType) -> Any: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def baseTypes(self) -> type: ...
    @property
    def derivedTypes(self) -> Any: ...
    @property
    def isEnumType(self) -> type: ...
    @property
    def isPlainOldDataType(self) -> type: ...
    @property
    def isUnknown(self) -> type: ...
    @property
    def pythonClass(self) -> type: ...
    @property
    def sizeof(self) -> Any: ...
    @property
    def typeName(self) -> type: ...

class Warning(_DiagnosticBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class WindowsImportWrapper:
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...

class _ClassWithClassMethod(Boost.Python.instance):
    Test: ClassVar[method] = ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def __reduce__(self) -> Any: ...

class _ClassWithVarArgInit(Boost.Python.instance):
    def __init__(self, tupleargs, dictkwds) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def allowExtraArgs(self) -> Any: ...
    @property
    def args(self) -> Any: ...
    @property
    def expired(self) -> Any: ...
    @property
    def kwargs(self) -> Any: ...

class _DiagnosticBase(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def commentary(self) -> Any: ...
    @property
    def diagnosticCode(self) -> Any: ...
    @property
    def diagnosticCodeString(self) -> Any: ...
    @property
    def sourceFileName(self) -> Any: ...
    @property
    def sourceFunction(self) -> Any: ...
    @property
    def sourceLineNumber(self) -> Any: ...

class _Enum(Boost.Python.instance):
    class TestEnum2(Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: str) -> Any: ...
        def __reduce__(self) -> Any: ...
    class TestKeywords(Tf_PyEnumWrapper):
        False_: ClassVar[TestKeywords] = ...
        None_: ClassVar[TestKeywords] = ...
        True_: ClassVar[TestKeywords] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        global_: ClassVar[TestKeywords] = ...
        import_: ClassVar[TestKeywords] = ...
        print_: ClassVar[TestKeywords] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: str) -> Any: ...
        def __reduce__(self) -> Any: ...
    class TestScopedEnum(Tf_PyEnumWrapper):
        Alef: ClassVar[TestScopedEnum] = ...
        Bet: ClassVar[TestScopedEnum] = ...
        Gimel: ClassVar[TestScopedEnum] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: str) -> Any: ...
        def __reduce__(self) -> Any: ...
    One: ClassVar[TestEnum2] = ...
    Three: ClassVar[TestEnum2] = ...
    Two: ClassVar[TestEnum2] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class _TestBase(Boost.Python.instance):
    def __init__(self) -> None: ...
    def TestCallVirtual(self) -> str: ...
    @overload
    def Virtual(self) -> str: ...
    @overload
    def Virtual(self) -> None: ...
    @overload
    def Virtual2(self) -> None: ...
    @overload
    def Virtual2(self) -> None: ...
    @overload
    def Virtual3(self, arg2: str) -> None: ...
    @overload
    def Virtual3(self, arg2: str) -> None: ...
    @overload
    def Virtual4(self) -> str: ...
    @overload
    def Virtual4(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestDerived(_TestBase):
    def __init__(self) -> None: ...
    @overload
    def Virtual(self) -> str: ...
    @overload
    def Virtual(self) -> str: ...
    @overload
    def Virtual2(self) -> None: ...
    @overload
    def Virtual2(self) -> None: ...
    @overload
    def Virtual3(self, arg2: str) -> None: ...
    @overload
    def Virtual3(self, arg2: str) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __reduce__(self) -> Any: ...
    @property
    def expired(self) -> Any: ...

class _TestEnum(Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: str) -> Any: ...
    def __reduce__(self) -> Any: ...

class _TestScopedEnum(Tf_PyEnumWrapper):
    Beryllium: ClassVar[_TestScopedEnum] = ...
    Boron: ClassVar[_TestScopedEnum] = ...
    Hydrogen: ClassVar[_TestScopedEnum] = ...
    Lithium: ClassVar[_TestScopedEnum] = ...
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: str) -> Any: ...
    def __reduce__(self) -> Any: ...

class _TestStaticMethodError(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def Error(self) -> None: ...
    def __reduce__(self) -> Any: ...

class _TestStaticTokens(Boost.Python.instance):
    Fuji: ClassVar[str] = ...
    McIntosh: ClassVar[str] = ...
    Pippin: ClassVar[str] = ...
    orange: ClassVar[str] = ...
    pear: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...

class _testStaticTokens(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self) -> Any: ...
    @property
    def Fuji(self) -> Any: ...
    @property
    def McIntosh(self) -> Any: ...
    @property
    def Pippin(self) -> Any: ...
    @property
    def orange(self) -> Any: ...
    @property
    def pear(self) -> Any: ...

def DictionaryStrcmp(arg1: str, arg2: str) -> int: ...
def DumpTokenStats() -> None: ...
def FindLongestAccessiblePrefix(arg1: str) -> int: ...
def GetAppLaunchTime() -> int: ...
def GetCurrentScopeDescriptionStack() -> list[str]: ...
def GetEnvSetting(arg1: str) -> T: ...
def GetStackTrace() -> Any: ...
def InstallTerminateAndCrashHandlers() -> None: ...
def InvokeWithErrorHandling(tupleargs, dictkwds) -> Any: ...
def IsValidIdentifier(arg1: str) -> bool: ...
def LogStackTrace(reason: str, logToDb: bool = ...) -> None: ...
def MakeValidIdentifier(arg1: str) -> str: ...
def PrintStackTrace(file, str) -> Any: ...
def RealPath(path: str, allowInaccessibleSuffix: bool = ..., raiseOnError: bool = ...) -> str: ...
def ReportActiveErrorMarks() -> None: ...
def RepostErrors(exception: object) -> bool: ...
def SetPythonExceptionDebugTracingEnabled(enabled: bool) -> None: ...
def StringSplit(arg1: str, arg2: str) -> list[str]: ...
def StringToDouble(arg1: str) -> float: ...
def StringToLong(arg1: str) -> int: ...
def StringToULong(arg1: str) -> int: ...
def TouchFile(fileName: str, create: bool = ...) -> bool: ...
def _CallThrowTest(arg1: object) -> None: ...
def _ConvertByteListToByteArray(arg1: list) -> Any: ...
def _DerivedFactory() -> _TestDerived: ...
def _DerivedNullFactory() -> _TestDerived: ...
def _Fatal(arg1: str, arg2: str, arg3: str, arg4: str, arg5: int) -> None: ...
def _GetLongMax() -> int: ...
def _GetLongMin() -> int: ...
def _GetULongMax() -> int: ...
def _RaiseCodingError(arg1: str, arg2: str, arg3: str, arg4: str, arg5: int) -> None: ...
def _RaiseRuntimeError(arg1: str, arg2: str, arg3: str, arg4: str, arg5: int) -> None: ...
def _ReturnsBase(arg1: object) -> Any: ...
def _ReturnsBaseRefPtr(arg1: object) -> Any: ...
def _ReturnsConstBase(arg1: object) -> Any: ...
def _RoundTripWrapperCallTest(arg1: object) -> Any: ...
def _RoundTripWrapperIndexTest(arg1: object, arg2: int) -> Any: ...
def _RoundTripWrapperTest(arg1: object) -> Any: ...
def _Status(arg1: str, arg2: str, arg3: str, arg4: str, arg5: int) -> None: ...
def _TakesBase(arg1: object) -> tuple: ...
def _TakesConstBase(arg1: object) -> str: ...
def _TakesDerived(arg1: object) -> str: ...
def _TakesReference(arg1: object) -> None: ...
def _TakesVecVecString(arg1: object) -> int: ...
def _TestAnnotatedBoolResult(arg1: bool, arg2: str) -> Tf_TestAnnotatedBoolResult: ...
def _ThrowCppException() -> str: ...
def _ThrowTest(arg1: str) -> None: ...
def _Warn(arg1: str, arg2: str, arg3: str, arg4: str, arg5: int) -> None: ...
def __SetErrorExceptionClass(arg1: object) -> None: ...
def _callUnboundInstance(arg1: object, arg2: str) -> str: ...
def _callback(arg1: object) -> None: ...
def _doErrors() -> None: ...
def _invokeTestCallback() -> str: ...
def _mightRaise(arg1: bool) -> None: ...
def _registerInvalidEnum(arg1: object) -> None: ...
def _returnsTfEnum(arg1: object) -> Any: ...
def _sendTfNoticeWithSender(arg1: object) -> None: ...
def _setTestCallback(arg1: object) -> None: ...
def _stringCallback(arg1: object) -> str: ...
def _stringStringCallback(arg1: object) -> str: ...
def _takesTestEnum(arg1: object) -> None: ...
def _takesTestEnum2(arg1: object) -> None: ...
def _takesTfEnum(arg1: object) -> None: ...