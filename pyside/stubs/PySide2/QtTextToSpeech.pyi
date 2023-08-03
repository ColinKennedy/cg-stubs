import PySide2.QtCore
import _typeshed
import collections.abc
import shiboken2
import typing
T = typing.TypeVar('T')
import typing_extensions

class QTextToSpeech(PySide2.QtCore.QObject):
    class State:
        BackendError: typing.ClassVar[QTextToSpeech.State] = ...
        Paused: typing.ClassVar[QTextToSpeech.State] = ...
        Ready: typing.ClassVar[QTextToSpeech.State] = ...
        Speaking: typing.ClassVar[QTextToSpeech.State] = ...
        values: typing.ClassVar[dict] = ...
        name: _typeshed.Incomplete
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __and__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __pos__(self): ...
        def __radd__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __rand__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __rmul__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __ror__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __rsub__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __rxor__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __sub__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
        def __xor__(self, other: typing.SupportsInt) -> QTextToSpeech.State: ...
    BackendError: typing.ClassVar[QTextToSpeech.State] = ...
    Paused: typing.ClassVar[QTextToSpeech.State] = ...
    Ready: typing.ClassVar[QTextToSpeech.State] = ...
    Speaking: typing.ClassVar[QTextToSpeech.State] = ...
    localeChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    pitchChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    rateChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    stateChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    voiceChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    volumeChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    @typing.overload
    def __init__(self, engine: str, parent: typing.Union[PySide2.QtCore.QObject, None] = ..., destroyed: typing.Callable = ..., locale: PySide2.QtCore.QLocale = ..., localeChanged: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., pitch: float = ..., pitchChanged: typing.Callable = ..., rate: float = ..., rateChanged: typing.Callable = ..., state: typing.Any = ..., stateChanged: typing.Callable = ..., voice: QVoice = ..., voiceChanged: typing.Callable = ..., volume: float = ..., volumeChanged: typing.Callable = ...) -> None: ...
    @typing.overload
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject, None] = ..., destroyed: typing.Callable = ..., locale: PySide2.QtCore.QLocale = ..., localeChanged: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., pitch: float = ..., pitchChanged: typing.Callable = ..., rate: float = ..., rateChanged: typing.Callable = ..., state: typing.Any = ..., stateChanged: typing.Callable = ..., voice: QVoice = ..., voiceChanged: typing.Callable = ..., volume: float = ..., volumeChanged: typing.Callable = ...) -> None: ...
    @classmethod
    def availableEngines(cls) -> typing.List[str]: ...
    def availableLocales(self) -> typing.List[PySide2.QtCore.QLocale]: ...
    def availableVoices(self) -> typing.List[QVoice]: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def pause(self) -> None: ...
    def pitch(self) -> float: ...
    def rate(self) -> float: ...
    def resume(self) -> None: ...
    def say(self, text: str) -> None: ...
    def setLocale(self, locale: PySide2.QtCore.QLocale) -> None: ...
    def setPitch(self, pitch: float) -> None: ...
    def setRate(self, rate: float) -> None: ...
    def setVoice(self, voice: QVoice) -> None: ...
    def setVolume(self, volume: float) -> None: ...
    def state(self) -> QTextToSpeech.State: ...
    def stop(self) -> None: ...
    def voice(self) -> QVoice: ...
    def volume(self) -> float: ...

class QTextToSpeechEngine(PySide2.QtCore.QObject):
    stateChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: typing.Union[PySide2.QtCore.QObject, None] = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    def availableLocales(self) -> typing.List[PySide2.QtCore.QLocale]: ...
    def availableVoices(self) -> typing.List[QVoice]: ...
    @classmethod
    def createVoice(cls, name: str, gender: QVoice.Gender, age: QVoice.Age, data: typing.Any) -> QVoice: ...
    def locale(self) -> PySide2.QtCore.QLocale: ...
    def pause(self) -> None: ...
    def pitch(self) -> float: ...
    def rate(self) -> float: ...
    def resume(self) -> None: ...
    def say(self, text: str) -> None: ...
    def setLocale(self, locale: PySide2.QtCore.QLocale) -> bool: ...
    def setPitch(self, pitch: float) -> bool: ...
    def setRate(self, rate: float) -> bool: ...
    def setVoice(self, voice: QVoice) -> bool: ...
    def setVolume(self, volume: float) -> bool: ...
    def state(self) -> QTextToSpeech.State: ...
    def stop(self) -> None: ...
    def voice(self) -> QVoice: ...
    @classmethod
    def voiceData(cls, voice: QVoice) -> typing.Any: ...
    def volume(self) -> float: ...

class QVoice(shiboken2.Object):
    class Age:
        Adult: typing.ClassVar[QVoice.Age] = ...
        Child: typing.ClassVar[QVoice.Age] = ...
        Other: typing.ClassVar[QVoice.Age] = ...
        Senior: typing.ClassVar[QVoice.Age] = ...
        Teenager: typing.ClassVar[QVoice.Age] = ...
        values: typing.ClassVar[dict] = ...
        name: _typeshed.Incomplete
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __and__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __pos__(self): ...
        def __radd__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __rand__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __rmul__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __ror__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __rsub__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __rxor__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __sub__(self, other: typing.SupportsInt) -> QVoice.Age: ...
        def __xor__(self, other: typing.SupportsInt) -> QVoice.Age: ...

    class Gender:
        Female: typing.ClassVar[QVoice.Gender] = ...
        Male: typing.ClassVar[QVoice.Gender] = ...
        Unknown: typing.ClassVar[QVoice.Gender] = ...
        values: typing.ClassVar[dict] = ...
        name: _typeshed.Incomplete
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __and__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __pos__(self): ...
        def __radd__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __rand__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __rmul__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __ror__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __rsub__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __rxor__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __sub__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
        def __xor__(self, other: typing.SupportsInt) -> QVoice.Gender: ...
    Adult: typing.ClassVar[QVoice.Age] = ...
    Child: typing.ClassVar[QVoice.Age] = ...
    Female: typing.ClassVar[QVoice.Gender] = ...
    Male: typing.ClassVar[QVoice.Gender] = ...
    Other: typing.ClassVar[QVoice.Age] = ...
    Senior: typing.ClassVar[QVoice.Age] = ...
    Teenager: typing.ClassVar[QVoice.Age] = ...
    Unknown: typing.ClassVar[QVoice.Gender] = ...
    @typing.overload
    def __init__(self, other: QVoice) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def age(self) -> QVoice.Age: ...
    @classmethod
    def ageName(cls, age: QVoice.Age) -> str: ...
    def gender(self) -> QVoice.Gender: ...
    @classmethod
    def genderName(cls, gender: QVoice.Gender) -> str: ...
    def name(self) -> str: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
