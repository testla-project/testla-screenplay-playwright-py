from re import Pattern
from typing import Literal, NewType, Union
from playwright.sync_api import Locator

class Selector: Union[str, Locator]

class SelectorOptionsState: Literal['visible', 'hidden', 'attached', 'detached']

class SubSelector:
    selector: Selector
    options: dict | None = {
        "has_text": str | None, 
        "timeout": float | None,
        "sub_selector": object | None,
        "state": SelectorOptionsState | None,
    }

class SelectorOptions:
    has_text: str | Pattern | None
    sub_selector: SubSelector | None
    timeout: float | None
    state: SelectorOptionsState | None
