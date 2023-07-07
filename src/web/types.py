from typing import Literal, Optional
import typing
from playwright.sync_api import Locator

from typing import Union

class Selector: Union[str, Locator]

class SelectorOptionsState: Literal['visible', 'hidden', 'attached', 'detached']

class SubSelector:
    selector: Selector
    options = {
        "has_text": str | None, 
        "timeout": float | None,
        #"sub_selector": "SubSelector" | None,
        "sub_selector": typing.NewType("SubSelector") | None,
        "state": SelectorOptionsState | None,
    } | None

class SelectorOptions:
    has_text: str | None
    sub_selector: SubSelector | None
    timeout: float | None
    state: SelectorOptionsState | None