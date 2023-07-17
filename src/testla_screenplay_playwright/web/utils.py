from typing import Pattern
from playwright.sync_api import Locator, Page
from .types import Selector, SelectorOptionsState, SubSelector, SelectorOptions, SubSelectorOptions

def get_sublocator(locator: Locator, sub_locator: Locator, text: str | Pattern | None = None) -> Locator:
    """Dealing with selector == Playwright Locator and options.hasText"""
    return locator.filter(has=sub_locator, has_text=text)

def sub_locator_lookup(page: Page, locator: Locator, timeout: float | None = None, sub_selector: SubSelector | None = None, state: SelectorOptionsState | None = 'visible') -> Locator:
    resolved_locator = locator
    # wait for selector to become visible based on timeout options
    resolved_locator.wait_for(timeout=timeout, state=state)
    # subSelector: if selector is a string, need to find it using page.locator(), if it is already a Playwright Locator use it directly.
    # PROBLEM: if we use the Playwright locator directly, it does not consider the parent selector anymore -> can lead to problems regarding resolving to multiple elements   
    if sub_selector is not None:
        # instantiate a Dummy options object to pass recursively instead of None
        if sub_selector.options is None:
            sub_selector.options = SubSelectorOptions()

        if type(sub_selector.selector) is str:
            resolved_locator = resolved_locator.locator(selector_or_locator=sub_selector.selector, has_text=sub_selector.options.has_text) 
        else:
            resolved_locator = get_sublocator(resolved_locator, sub_locator=sub_selector.selector, text=sub_selector.options.has_text)
        # wait for sub selector to become visible based on timeout options
        resolved_locator.wait_for(timeout=timeout)

        if sub_selector.options.sub_selector is None:
            resolved_locator = sub_locator_lookup(
                page=page, 
                locator=resolved_locator, 
                timeout=sub_selector.options.timeout, 
                sub_selector=sub_selector.options.sub_selector,
                state=sub_selector.options.state
            )
    return resolved_locator


def recursive_locator_lookup(page: Page, selector: Selector, options: SelectorOptions | None = None) -> Locator:
    """Find the given locator with the given SelectorOptions."""
    # check if this method was called with options == None.
    # if this is really the case, just resolve the locator, wait for it to be visible and return it.
    if options is None:
        locator = page.locator(selector, has_text=None) if type(selector) is str else get_sublocator(selector, sub_locator=None, text=None)
        locator.wait_for()
        return locator

    # find first level locator: if selector is a string, need to find it using page.locator(), if it is already a Playwright Locator use it directly.
    locator = page.locator(selector, has_text=options.has_text) if type(selector) is str else get_sublocator(selector, sub_locator=None, text=options.has_text)
    # pass the first level locator into sub locator lookup
    return sub_locator_lookup(page=page, locator=locator, timeout=options.timeout, sub_selector=options.sub_selector, state=options.state) 
