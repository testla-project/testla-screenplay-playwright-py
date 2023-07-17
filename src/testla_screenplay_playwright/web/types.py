from re import Pattern
from typing import Literal, Union
from playwright.sync_api import Locator

class Selector: Union[str, Locator]

class SelectorOptionsState: Literal['visible', 'hidden', 'attached', 'detached']

class SubSelectorOptions:
    def __init__(self, has_text: str | Pattern | None = None, timeout: float | None = None, sub_selector: object | None = None, state: SelectorOptionsState | None = None):
        self.has_text = has_text
        self.timeout = timeout
        self.sub_selector = sub_selector
        self.state = state


class SubSelector:
    # selector: Selector
    # options: dict | None = {
    #     "has_text": str | None, 
    #     "timeout": float | None,
    #     "sub_selector": object | None,
    #     "state": SelectorOptionsState | None,
    # }

    def __init__(self, selector: Selector | None = None, options: SubSelectorOptions | None = None):
        self.selector = selector
        self.options = options

class SelectorOptions:
    """Useful options to specify further characteristics of the selector."""

    def __init__(self, has_text: str | Pattern | None = None, sub_selector: SubSelector | None = None, timeout: float | None = None, state: SelectorOptionsState | None = None):
        self.has_text = has_text
        self.sub_selector = sub_selector
        self.timeout = timeout
        self.state = state
