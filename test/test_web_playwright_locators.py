import pytest
from typing import List
from playwright.sync_api import Page, BrowserContext, Cookie, expect
from testla_screenplay import Actor
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
from src.web.actions.wait import Wait
from src.web.questions.element import Element
from src.web.types import SelectorOptions, SubSelector, SubSelectorOptions


# execute tests with: pytest <file> --headed
# <file> not needed. if there os no <file>, all test files will be executed.
# -s if you need stdout output (print) 
# -k "test case" for only 1 specific test case

actor: Actor = Actor.named("Test Actor")

@pytest.fixture(scope="function", autouse=True)
def test_setup_tests(page: Page):
    # set up the test actor
    actor.can(BrowseTheWeb.using(page=page))


def test_drag_and_drop():
    page = BrowseTheWeb.As(actor).get_page()
        
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/drag_and_drop")
    )

    # before drag: Box A is on the Left
    expect(page.locator('[id="column-a"] header')).to_have_text('A')

    # execute the drag
    actor.attempts_to(
        DragAndDrop.execute(page.locator('[id="column-a"]'), page.locator('[id="column-b"]')),
    )

    # after Drag: Box B is on the Left
    expect(page.locator('[id="column-a"] header')).to_have_text('B')


def test_check():
    page = BrowseTheWeb.As(actor).get_page()

    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/checkboxes"),
        Check.element(page.locator('//input[1]')),
        Check.element(page.locator('//input[2]')),
    )
    expect(page.locator('//input[1]')).to_be_checked()
    expect(page.locator('//input[2]')).to_be_checked()


def test_click():
    page = BrowseTheWeb.As(actor).get_page()

    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/add_remove_elements/")
    )
    # assert that there is no button before we add it with our Click
    expect(page.locator('[class="added-manually"]')).to_have_count(0)

    actor.attempts_to(
        Click.on("button", options=SelectorOptions(has_text="Add Element"))
    )
    # assert that the button is here after our Click
    expect(page.locator('[class="added-manually"]')).to_have_count(1)


def test_fill_and_type():
    page = BrowseTheWeb.As(actor).get_page()

    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/login"),
        Fill.In(page.locator('[id="username"]'), 'tomsmith'),
        Type.In(page.locator('[id="password"]'), 'SuperSecretPassword!'),
        Click.on(page.locator('[class="radius"]')),
    )
    # assert that the login worked
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")


def test_hover():
    page = BrowseTheWeb.As(actor).get_page()
        
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/hovers")
    )
    # assert that there is no info before the hover
    expect(page.locator('[href="/users/1"]')).not_to_be_visible()

    actor.attempts_to(
        Hover.over(page.locator('div.figure:nth-child(3) > img:nth-child(1)')),
    )
    # assert that the info is now visible after hover
    expect(page.locator('[href="/users/1"]')).to_be_visible()

    
def test_wait_and_recursive_locators():
    page = BrowseTheWeb.As(actor).get_page()
    
    actor.attempts_to(
        Navigate.to("https://the-internet.herokuapp.com/tables"),
        Wait.for_selector(
            page.locator('[id="table1"]'), 
            SelectorOptions(
                sub_selector=SubSelector(
                    selector='tbody tr',
                    options=SubSelectorOptions(
                        has_text='Conway', 
                        sub_selector=SubSelector(
                            page.locator('td:has-text("$50.00")')
                        )
                    )
                )
            )
        )
    )

def test_element_visible():
    page = BrowseTheWeb.As(actor).get_page()
    
    actor.attempts_to(
        Navigate.to('https://the-internet.herokuapp.com/tables'),
    )

    assert actor.asks(Element.to_be_visible(page.locator("h3"), SelectorOptions(has_text="Data Tables")))

    visible_res = False
    try:
        actor.asks(Element.to_be_visible(page.locator("h3"), SelectorOptions(has_text="this does not exist", timeout=1000.0)))
    except:
        visible_res = True
    assert visible_res

    assert actor.asks(Element.not_to_be_visible(page.locator("h3"), SelectorOptions(has_text="this does not exist")))

    not_visible_res = False
    try:
        actor.asks(Element.not_to_be_visible(page.locator("h3"), SelectorOptions(has_text="Data Tables", timeout=1000.0)))
    except:
        not_visible_res = True
    assert not_visible_res

def test_element_enabled():
    page = BrowseTheWeb.As(actor).get_page()
    
    actor.attempts_to(
        Navigate.to('https://the-internet.herokuapp.com/tinymce'),
        Click.on(page.locator('[aria-label="Bold"]')),
    )

    assert actor.asks(Element.to_be_enabled(page.locator('[aria-label="Undo"]')))

    enabled_res = False
    try:
        actor.asks(Element.to_be_enabled(page.locator('[aria-label="Redo"]'), SelectorOptions(timeout=1000.0)))
    except:
        enabled_res = True
    assert enabled_res

    assert actor.asks(Element.not_to_be_enabled(page.locator('[aria-label="Redo"]')))

    not_enabled_res = False
    try:
        actor.asks(Element.not_to_be_enabled(page.locator('[aria-label="Undo"]'), SelectorOptions(timeout=1000.0)))
    except:
        not_enabled_res = True
    assert not_enabled_res

def test_element_text():
    page = BrowseTheWeb.As(actor).get_page()
    
    actor.attempts_to(
        Navigate.to('https://the-internet.herokuapp.com/tables'),
    )

    assert actor.asks(Element.to_have_text(page.locator("h3"), "Data Tables"))

    text_res = False
    try:
        actor.asks(Element.to_have_text(page.locator("h3"), "this text does not exist", SelectorOptions(timeout=1000.0)))
    except:
        text_res = True
    assert text_res

    assert actor.asks(Element.not_to_have_text(page.locator("h3"), r"/[0-9]/")) # Regex pattern that does not exist

    not_text_res = False
    try:
        actor.asks(Element.not_to_have_text(page.locator("h3"), "Data Tables", SelectorOptions(timeout=1000.0)))
    except:
        not_text_res = True
    assert not_text_res

def test_element_value():
    page = BrowseTheWeb.As(actor).get_page()
    
    actor.attempts_to(
        Navigate.to('https://the-internet.herokuapp.com/login'),
        Fill.In(page.locator('[id="username"]'), 'test'),
    )

    assert actor.asks(Element.to_have_value(page.locator('[id="username"]'), 'test'))

    value_res = False
    try:
        actor.asks(Element.to_have_value(page.locator('[id="username"]'), 'this value is wrong', SelectorOptions(timeout=1000.0)))
    except:
        value_res = True
    assert value_res

    assert actor.asks(Element.not_to_have_value(page.locator('[id="username"]'), 'this value is wrong'))

    not_value_res = False
    try:
        actor.asks(Element.not_to_have_value(page.locator('[id="username"]'), 'test'))
    except:
        not_value_res = True
    assert not_value_res