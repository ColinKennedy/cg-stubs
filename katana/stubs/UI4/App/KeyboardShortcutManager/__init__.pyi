# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import KeyboardShortcutItem as KeyboardShortcutItem, KeyboardShortcutManager as KeyboardShortcutManager, KeyboardShortcutManagerMixin as KeyboardShortcutManagerMixin, KeyboardShortcutModel as KeyboardShortcutModel, ManagedAction as ManagedAction
from UI4.App.KeyboardShortcutManager.KeyboardShortcutManager import BindActions as BindActions, BuildShortcutModel as BuildShortcutModel, CreateAction as CreateAction, GenerateActionID as GenerateActionID, GetActionID as GetActionID, GetFullActionName as GetFullActionName, GetFullKeyEventName as GetFullKeyEventName, GetKeyEventID as GetKeyEventID, GetKeyEventNameForShortcut as GetKeyEventNameForShortcut, GetShortcutForAction as GetShortcutForAction, GetShortcutForKeyEvent as GetShortcutForKeyEvent, HandleKeyEvent as HandleKeyEvent, IsShortcutRegisteredForAction as IsShortcutRegisteredForAction, IsShortcutRegisteredForClass as IsShortcutRegisteredForClass, LoadShortcuts as LoadShortcuts, RegisterAction as RegisterAction, RegisterActions as RegisterActions, RegisterKeyEvent as RegisterKeyEvent, UnregisterAction as UnregisterAction, UnregisterKeyEvent as UnregisterKeyEvent, UpdateAction as UpdateAction
from typing import Set, Tuple