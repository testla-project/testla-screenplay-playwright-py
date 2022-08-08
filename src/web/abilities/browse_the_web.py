from typing import List, Literal, Optional
from playwright.sync_api import Cookie, Page, Response, expect
# from @testla/screenplay import Ability, Actor


class BrowseTheWeb(Ability):
    """This class represents the actor's ability to use a Browser."""

    def __init__(self, page: Page):
        super.__init__()
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

    def hover(self, selector: str, modifiers: List[Literal['Alt', 'Control', 'Meta', 'Shift']] | None = None) -> None:
        """Use the page mouse to hover over the specified element.

        :param selector: the selector of the element to hover over.
        :param modifiers: (optional) the keys that should be pressed while hovering. Supported: 'Alt', 'Control', 'Meta', 'Shift'.
        """
        return self.page.hover(selector, modifiers)

    def press(self, keys: str) -> None:
        """Press the specified key(s) on the keyboard.

        :param keys: the key(s). multiple keys can be pressed by concatenating with '+'.
        """
        return self.page.keyboard.press(keys)

    def check_box(self, selector: str) -> None:
        """Check the specified checkbox.

        :param selector: the selector of the checkbox.
        """
        return self.page.check(selector)

    def wait_for_selector(self, selector: str):
        """Wait until the element of the specified selector exists.
        
        :param selector: the selector of the element.
        """
        return self.page.locator(selector)

    def drag_and_drop(self, source_selector: str, target_selector: str) -> None:
        """Drag the specified source element to the specified target element and drop it.

        :param source_selector: the selector of the source element.
        :param target_selector: the selector of the target element.
        """
        return self.page.drag_and_drop(source_selector, target_selector)

    def fill(self, selector: str, input: str) -> None:
        """Fill the element specified by the selector with the given input.
        
        :param selector: the selector of the element.
        :param input: the input to fill the element with.
        """
        return self.page.fill(selector, input)

    def type(self, selector: str, input: str) -> None:
        """Type the given input into the element specified by the selector.
        
        :param selector: the selector of the element.
        :param input: the input to fill the element with.
        """
        return self.page.type(selector, input)

    def click(self, selector: str) -> None:
        """Click the element specified by the selector.

        :param selector: the selector of the element to click.
        """
        return self.page.click(selector)

    def dblclick(self, selector: str) -> None:
        """Double click the element specified by the selector.

        :param selector: the selector of the element to double click.
        """
        return self.page.dblclick(selector)

    def check_visibility_state(self, selector: str, mode: Literal['visible', 'hidden'], timeout: Optional[float] = None) -> bool:
        """Validate if a locator on the page is visible or hidden.
        
        :param mode: the expected property of the selector that needs to be checked. either 'visible' or 'hidden'.
        :param selector: the locator to check for.
        :param timeout: (optional) maximum timeout to wait for.
        :returns: true if the element is visible/hidden as expected. Throws an error if the timeout was reached.
        """
        if mode is 'visible':
            expect(self.page.locator(selector)).to_be_visible(timeout)
        else:
            expect(self.page.locator(selector)).to_be_hidden(timeout)
        return true

    def check_enabled_state(self, selector: str, mode: Literal['enabled', 'disabled'], timeout: Optional[float] = None) -> bool:
        """Validate if a locator on the page is enabled or disabled.
        
        :param mode: the expected property of the selector that needs to be checked. Either 'enabled' or 'disabled'.
        :param selector: the locator to check for.
        :param timeout: (optional) maximum timeout to wait for.
        :returns: true if the element is enabled/disabled as expected. Throws an error if the timeout was reached.
        """
        if mode is 'enabled':
            expect(self.page.locator(selector)).to_be_enabled(timeout)
        else:
            expect(self.page.locator(selector)).to_be_disabled(timeout)
        return true

    def get_cookies(self, urls: str | List[str] = None) -> List[Cookie]:
        """Get the cookies of the current browser context. If no URLs are specified, this method returns all cookies.
        If URLs are specified, only cookies that affect those URLs are returned."""
        return self.page.context.cookies(urls)

    def add_cookies(self, cookies: List[Cookie]) -> None:
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
            return Promise.reject();
        }""", { 'key': key })

    def set_local_storage_item(self, key: str, value: object) -> object:
        """Set a local storage item identified by the given key + value, creating a new key/value pair if none existed for key previously.
        
        :param key: the key that specifies the item.
        :param value: the value to set.
        """
        return self.page.evaluate("""({ key, value }) => {
            localStorage.setItem(key, JSON.stringify(value));
            return Promise.resolve();
        }""", { 'key': key, 'value': value })

    def remove_local_storage_item(self, key: str) -> None:
        """Delete a local storage item, if a key/value pair with the given key exists.
        
        :param key: the key that specifies the item.
        """
        return self.page.evaluate("""(key) => {
            localStorage.removeItem(key);
            return Promise.resolve();
        }""", { 'key': key })

    def get_session_storage_item(self, key: str) -> object:
        """Get a session storage item.
        
        :param key: the key that specifies the item.
        """
        return self.page.evaluate("""(key) => {
            const value = sessionStorage.getItem(key);
            if (value) {
                return Promise.resolve(JSON.parse(value));
            }
            return Promise.reject();
        }""", { 'key': key })

    def set_session_storage_item(self, key: str, value: object) -> object:
        """Set a session storage item identified by the given key + value, creating a new key/value pair if none existed for key previously.
        
        :param key: the key that specifies the item.
        :param value: the value to set.
        """
        return self.page.evaluate("""({ key, value }) => {
            sessionStorage.setItem(key, JSON.stringify(value));
            return Promise.resolve();
        }""", { 'key': key, 'value': value })

    def remove_session_storage_item(self, key: str) -> None:
        """Delete a session storage item, if a key/value pair with the given key exists.
        
        :param key: the key that specifies the item.
        """
        return self.page.evaluate("""(key) => {
            sessionStorage.removeItem(key);
            return Promise.resolve();
        }""", { 'key': key })