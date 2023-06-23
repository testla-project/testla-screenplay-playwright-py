import pytest
from typing import List
from playwright.sync_api import Page, BrowserContext, Cookie, expect
from testla_screenplay import Actor
from src.shared.actions.sleep import Sleep
from src.web.abilities.browse_the_web import BrowseTheWeb
from src.web.actions.navigate import Navigate
from src.web.actions.drag_and_drop import DragAndDrop
from src.web.actions.check import Check
from src.web.actions.click import Click
from src.web.actions.fill import Fill
from src.web.actions.type import Type
from src.web.actions.hover import Hover
from src.web.actions.press import Press
from src.web.actions.add import Add
from src.web.actions.get import Get
from src.web.actions.clear import Clear
from src.web.actions.set import Set
from src.web.actions.remove import Remove


# execute test with: pytest --headed
# -s only if you need stdout output (print) 
# -k "test case" for only 1 specific test case

actor: Actor = Actor.named("Test Actor")

@pytest.fixture(scope="function", autouse=True)
def test_setup_tests(page: Page):
    # set up the test actor
    actor.can(BrowseTheWeb.using(page=page)).With("page", page)


def test_navigate():
    url = "https://www.google.de/"
    actor.attempts_to(
        Navigate.to(url)
    )
    expect(actor.states("page")).to_have_url(url)


def test_drag_and_drop():
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/drag_and_drop")
    )

    # before drag: Box A is on the Left
    expect(actor.states("page").locator('[id="column-a"] header')).to_have_text('A')

    # execute the drag
    actor.attempts_to(
        DragAndDrop.execute('[id="column-a"]', '[id="column-b"]'),
    )

    # after Drag: Box B is on the Left
    expect(actor.states("page").locator('[id="column-a"] header')).to_have_text('B')


def test_check():
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/checkboxes"),
        Check.element('//input[1]'),
        Check.element('//input[2]'),
    )
    expect(actor.states('page').locator('//input[1]')).to_be_checked()
    expect(actor.states('page').locator('//input[2]')).to_be_checked()


def test_click():
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/add_remove_elements/")
    )
    # assert that there is no button before we add it with our Click
    expect(actor.states('page').locator('[class="added-manually"]')).to_have_count(0)

    actor.attempts_to(
        Click.on('button[onclick="addElement()"]'),
        Sleep(5)
    )
    # assert that the button is here after our Click
    expect(actor.states('page').locator('[class="added-manually"]')).to_have_count(1)


def test_fill_and_type():
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/login"),
        Fill.In('[id="username"]', 'tomsmith'),
        Type.In('[id="password"]', 'SuperSecretPassword!'),
        Click.on('[class="radius"]'),
    )
    # assert that the login worked
    expect(actor.states('page')).to_have_url("https://the-internet.herokuapp.com/secure")


def test_hover():
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/hovers")
    )
    # assert that there is no info before the hover
    expect(actor.states('page').locator('[href="/users/1"]')).not_to_be_visible()

    actor.attempts_to(
        Hover.over('div.figure:nth-child(3) > img:nth-child(1)'),
    )
    # assert that the info is now visible after hover
    expect(actor.states('page').locator('[href="/users/1"]')).to_be_visible()


def test_press():
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/key_presses")
    )
    # assert that there is nothing in the result box
    expect(actor.states('page').locator('[id="result"]')).to_have_text('')

    actor.attempts_to(
        Click.on('[id="target"]'),
        Press.key('a'),
    )
    # assert that the pressed button was recognized
    expect(actor.states('page').locator('[id="result"]')).to_have_text('You entered: A')

    
# TODO: recursive locators!
# test_wait_and_recursive locators

def test_cookies():
    context: BrowserContext = actor.states("page").context

    actor.attempts_to(
        Navigate.to("https://google.com")
    )
    # assert that there are cookies to clear
    assert len(context.cookies()) != 0

    # Clear any cookies not added by us
    actor.attempts_to(
        Clear.cookies(),
    )
    # assert that that cookies are successfully cleared
    assert len(context.cookies()) == 0

    # Add some cookies
    cookies_to_add: List[Cookie] = [{
        "name": 'cookie1', "value": 'someValue', "domain": '.google.com', "path": '/', "expires": 1700269944, "httpOnly": True, "secure": True, "sameSite": 'Lax',
    }, {
        "name": 'cookie2', "value": 'val', "domain": '.google.com', "path": '/', "expires": 1700269944, "httpOnly": True, "secure": True, "sameSite": 'Lax',
    }]
    actor.attempts_to(
        Add.cookies(cookies_to_add)
    )
    # assert that cookies are successfully added
    assert context.cookies() == cookies_to_add

    # Get the cookies we just added
    get_cookies: List[Cookie] = actor.attempts_to(
        Get.cookies('https://google.com'),
    )
    # assert that cookies are retrieved successfully
    assert get_cookies == cookies_to_add

def test_session_and_local_storage():
    actor.attempts_to(
        Navigate.to('https://google.com'),

        Set.local_storage_item('localKey', 'localValue'),
        Set.session_storage_item('sessionKey', 'sessionValue'),
    )

    # check local storage item
    local = actor.attempts_to(
        Get.local_storage_item('localKey'),
    )
    assert local == 'localValue'

    # check session storage item
    session = actor.attempts_to(
        Get.session_storage_item('sessionKey'),
    )
    assert session == 'sessionValue'

    # check for values that are not there
    local_undefined = actor.attempts_to(
        Get.local_storage_item('???'),
    )
    assert local_undefined == None

    # check for values that are not there
    session_undefined = actor.attempts_to(
        Get.session_storage_item('???'),
    )
    assert session_undefined == None

    # remove local storage item and verify that it was deleted
    local_deleted = actor.attempts_to(
        Remove.local_storage_item('localKey'),
        Get.local_storage_item('localKey'),
    )
    assert local_deleted == None

    # remove session storage item and verify that it was deleted
    session_deleted = actor.attempts_to(
        Remove.session_storage_item('localKey'),
        Get.session_storage_item('localKey'),
    )
    assert session_deleted == None