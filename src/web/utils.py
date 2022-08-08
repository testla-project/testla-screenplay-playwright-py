from playwright.sync_api import Locator, Page
from web.types import SubSelector, SelectorOptions
# import { SelectorOptions, SubSelector } from './types';


def sub_locator_lookup(page: Page, locator: Locator, timeout: float | None = None, sub_selector: SubSelector | None = None) -> Locator:
    resolved_locator: Locator = locator
    # wait for selector to become visible based on timeout options
    resolved_locator.wait_for(timeout=timeout)
    # check if we have subselectors
    if sub_selector:
        resolved_locator = resolved_locator.locator(selector=sub_selector.selector, has_text=sub_selector.options["has_text"])
        resolved_locator.wait_for(timeout=timeout)

        if sub_selector.options["sub_selector"]:
            resolved_locator = sub_locator_lookup(page=page, locator=resolved_locator, timeout=sub_selector.options["timeout"], sub_selector=sub_selector.options["sub_selector"])

    return resolved_locator


def recursive_locator_lookup(page: Page, selector: str, options: SelectorOptions | None = None) -> Locator:
    # find first level locator
    locator = page.locator(selector=selector, has_text=options.has_text)
    # pass the first level locator into sub locator lookup
    return sub_locator_lookup(page=page, locator=locator, timeout=options.timeout, sub_selector=options.sub_selector)
