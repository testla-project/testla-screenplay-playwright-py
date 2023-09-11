from re import Pattern
from typing import List, Literal
from playwright.sync_api import Cookie, Page, Response, expect
from testla_screenplay import Actor, Ability
from ..types import Selector, SelectorOptions
from ..utils import recursive_locator_lookup


class BrowseTheWeb(Ability):
    """This class represents the actor's ability to use a Browser."""

    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def using(page: Page) -> 'BrowseTheWeb':
        """Initialize this Ability by passing an already existing Playwright Page object.
        
        :param page: the Playwright Page that will be used to browse.
        """
        return BrowseTheWeb(page)

    @staticmethod
    def As(actor: Actor) -> 'BrowseTheWeb':
        """Use this Ability as an Actor."""
        return actor.with_ability_to(BrowseTheWeb)

    def get_page(self) -> Page:
        """Get the page object.
        
        :returns: the page object.
        """
        return self.page

    def goto(self, url: str) -> (Response | None):
        """Use the page to navigate to the specified URL.
        
        :param url: the url to access."""
        return self.page.goto(url)

    def wait_for_load_state(self, state: Literal['domcontentloaded', 'load', 'networkidle']) -> None:
        """Wait for the specified loading state.
        
        :param state: the state to wait for. Supported: 'load', 'domcontentloaded', 'networkidle'
        """
        return self.page.wait_for_load_state(state)

    def hover(self, selector: Selector, options: SelectorOptions | None = None, modifiers: List[Literal['Alt', 'Control', 'Meta', 'Shift']] | None = None) -> None:
        """Use the page mouse to hover over the specified element.

        :param selector: the selector of the element to hover over.
        :param modifiers: (optional) the keys that should be pressed while hovering. Supported: 'Alt', 'Control', 'Meta', 'Shift'.
        """
        return recursive_locator_lookup(page=self.page, selector=selector, options=options).hover(modifiers=modifiers)

    def press(self, keys: str) -> None:
        """Press the specified key(s) on the keyboard.

        :param keys: the key(s). multiple keys can be pressed by concatenating with '+'.
        """
        return self.page.keyboard.press(keys)

    def check_box(self, selector: Selector, options: SelectorOptions | None = None) -> None:
        """Check the specified checkbox.

        :param selector: the selector of the checkbox.
        """
        return recursive_locator_lookup(page=self.page, selector=selector, options=options).check()

    def wait_for_selector(self, selector: Selector, options: SelectorOptions | None = None):
        """Wait until the element of the specified selector exists.
        
        :param selector: the selector of the element.
        """
        return recursive_locator_lookup(self.page, selector, options)

    def drag_and_drop(self, source_selector: Selector, target_selector: Selector, source_options: SelectorOptions | None = None, target_options: SelectorOptions | None = None) -> None:
        """Drag the specified source element to the specified target element and drop it.

        :param source_selector: the selector of the source element.
        :param target_selector: the selector of the target element.
        """
        target = recursive_locator_lookup(self.page, target_selector, target_options)
        return recursive_locator_lookup(self.page, source_selector, source_options).drag_to(target=target, target_position={"x": 0, "y": 0})

    def fill(self, selector: Selector, inp: str, options: SelectorOptions | None = None) -> None:
        """Fill the element specified by the selector with the given input.
        
        :param selector: the selector of the element.
        :param inp: the input to fill the element with.
        """
        return recursive_locator_lookup(self.page, selector, options).fill(inp)

    def type(self, selector: Selector, inp: str, options: SelectorOptions | None = None) -> None:
        """Type the given input into the element specified by the selector.
        
        :param selector: the selector of the element.
        :param inp: the input to fill the element with.
        """
        return recursive_locator_lookup(self.page, selector, options).type(inp)

    def click(self, selector: Selector, options: SelectorOptions | None = None) -> None:
        """Click the element specified by the selector.

        :param selector: the selector of the element to click.
        """
        return recursive_locator_lookup(self.page, selector, options).click()

    def dblclick(self, selector: Selector, options: SelectorOptions | None = None) -> None:
        """Double click the element specified by the selector.

        :param selector: the selector of the element to double click.
        """
        return recursive_locator_lookup(self.page, selector, options).dblclick()
    
    def select_option(self, selector: Selector, value: str | None = None, *, label: str | None = None, index: int | None = None, options: SelectorOptions | None = None) -> List[str]:
        """Set the value of a Selector of type select to the given option.
        
        :param selector: selector the string representing the (select) selector.
        :param value: the value of the option. Default if none of the other parameters is specified.
        :param label: the label of the option. Has to be specified explicitly.
        :param index: the index of the option. Has to be specified explicitly.
        """
        return recursive_locator_lookup(self.page, selector, options).select_option(value=value, label=label, index=index)

    def check_visibility_state(self, selector: Selector, mode: Literal['visible', 'hidden'], options: SelectorOptions | None = None) -> bool:
        """Validate if a locator on the page is visible or hidden.
        
        :param mode: the expected property of the selector that needs to be checked. either 'visible' or 'hidden'.
        :param selector: the locator to check for.
        :param timeout: (optional) maximum timeout to wait for.
        :returns: true if the element is visible/hidden as expected. Throws an error if the timeout was reached.
        """
        # create dummy options if options is None
        options = SelectorOptions() if options is None else options

        if mode == 'visible':
            expect(recursive_locator_lookup(self.page, selector, options=SelectorOptions(
                options.has_text, options.sub_selector, options.timeout, 'visible')
            )).to_be_visible(timeout=options.timeout)
        else:
            expect(recursive_locator_lookup(self.page, selector, options=SelectorOptions(
                options.has_text, options.sub_selector, options.timeout, 'hidden')
            )).to_be_hidden(timeout=options.timeout)
        return True

    def check_enabled_state(self, selector: Selector, mode: Literal['enabled', 'disabled'], options: SelectorOptions | None = None) -> bool:
        """Validate if a locator on the page is enabled or disabled.
        
        :param mode: the expected property of the selector that needs to be checked. Either 'enabled' or 'disabled'.
        :param selector: the locator to check for.
        :param timeout: (optional) maximum timeout to wait for.
        :returns: true if the element is enabled/disabled as expected. Throws an error if the timeout was reached.
        """
        # create dummy timeout if options is None
        timeout = None if options is None else options.timeout

        if mode == 'enabled':
            expect(recursive_locator_lookup(self.page, selector, options)).to_be_enabled(timeout=timeout)
        else:
            expect(recursive_locator_lookup(self.page, selector, options)).to_be_disabled(timeout=timeout)
        return True
    
    def check_selector_text(self, selector: Selector, text: str | Pattern, mode: Literal['has', 'has_not'], options: SelectorOptions | None = None) -> bool:
        """Validate if the given element has the given text or not.
        
        :param mode: the expected property of the selector that needs to be checked. Either 'has' or 'has_not'.
        :param selector: the locator to check for.
        :param timeout: (optional) maximum timeout to wait for.
        :returns: true if the element has/has not as expected. Throws an error if the timeout was reached.
        """
        # create dummy timeout if options is None
        timeout = None if options is None else options.timeout

        if mode == 'has':
            expect(recursive_locator_lookup(self.page, selector, options)).to_have_text(text, timeout=timeout)
        else:
            expect(recursive_locator_lookup(self.page, selector, options)).not_to_have_text(text, timeout=timeout)
        return True
    
    def check_selector_value(self, selector: Selector, value: str | Pattern, mode: Literal['has', 'has_not'], options: SelectorOptions | None = None) -> bool:
        """Validate if the given element has the given value or not.
        
        :param mode: the expected property of the selector that needs to be checked. Either 'has' or 'has_not'.
        :param selector: the locator to check for.
        :param timeout: (optional) maximum timeout to wait for.
        :returns: true if the element has/has not as expected. Throws an error if the timeout was reached.
        """
        # create dummy timeout if options is None
        timeout = None if options is None else options.timeout

        if mode == 'has':
            expect(recursive_locator_lookup(self.page, selector, options)).to_have_value(value, timeout=timeout)
        else:
            expect(recursive_locator_lookup(self.page, selector, options)).not_to_have_value(value, timeout=timeout)
        return True

    def get_cookies(self, urls: str | List[str] = None) -> List[Cookie]:
        """Get the cookies of the current browser context. If no URLs are specified, this method returns all cookies.
        If URLs are specified, only cookies that affect those URLs are returned."""
        return self.page.context.cookies(urls)

    def add_cookies(self, cookies) -> None:
        """Adds cookies into this browser context. All pages within this context will have these cookies installed. Cookies can be obtained via BrowseTheWeb.get_cookies([urls])."""
        return self.page.context.add_cookies(cookies)

    def clear_cookies(self) -> None:
        """Clear the browser context cookies."""
        return self.page.context.clear_cookies()

    def get_local_storage_item(self, key: str) -> object:
        """Get a local storage item.
        
        :param key: the key that specifies the item.
        """
        return self.page.evaluate("""(key) => {
            const value = localStorage.getItem(key);
            if (value) {
                return Promise.resolve(JSON.parse(value));
            }
            return Promise.resolve(undefined);
        }""", key)

    def set_local_storage_item(self, key: str, value: object) -> object:
        """Set a local storage item identified by the given key + value, creating a new key/value pair if none existed for key previously.
        
        :param key: the key that specifies the item.
        :param value: the value to set.
        """
        return self.page.evaluate("""({ key, value }) => {
            localStorage.setItem(key, JSON.stringify(value));
            return Promise.resolve();
        }""", {'key': key, 'value': value})

    def remove_local_storage_item(self, key: str) -> None:
        """Delete a local storage item, if a key/value pair with the given key exists.
        
        :param key: the key that specifies the item.
        """
        return self.page.evaluate("""(key) => {
            localStorage.removeItem(key);
            return Promise.resolve();
        }""", key)

    def get_session_storage_item(self, key: str) -> object:
        """Get a session storage item.
        
        :param key: the key that specifies the item.
        """
        x = self.page.evaluate("""(key) => {
            const value = sessionStorage.getItem(key);
            if (value) {
                return Promise.resolve(JSON.parse(value));
            }
            return Promise.resolve(undefined);
        }""", key)
        return x

    def set_session_storage_item(self, key: str, value: object) -> object:
        """Set a session storage item identified by the given key + value, creating a new key/value pair if none existed for key previously.
        
        :param key: the key that specifies the item.
        :param value: the value to set.
        """
        return self.page.evaluate("""({ key, value }) => {
            sessionStorage.setItem(key, JSON.stringify(value));
            return Promise.resolve();
        }""", {'key': key, 'value': value})

    def remove_session_storage_item(self, key: str) -> None:
        """Delete a session storage item, if a key/value pair with the given key exists.
        
        :param key: the key that specifies the item.
        """
        return self.page.evaluate("""(key) => {
            sessionStorage.removeItem(key);
            return Promise.resolve();
        }""", key)
