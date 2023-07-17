from re import Pattern
from testla_screenplay import Actor, Question
from ..abilities.browse_the_web import BrowseTheWeb
from ..types import Selector, SelectorOptions
from typing import Literal


class Element(Question):
    """Question Class. Get a specified state for a selector like visible or enabled."""

    def __init__(self, selector: Selector, check_mode: Literal['to_be', 'not_to_be'], mode: Literal['visible', 'enabled', 'text', 'value'], *, payload: str | Pattern | None = None, options: SelectorOptions | None = None):
        self.check_mode = check_mode
        self.mode = mode
        self.selector = selector
        self.payload = payload
        self.options = options

    def answered_by(self, actor: Actor) -> bool:
        if self.mode == 'visible':
            # if the ability method is not the expected result there will be an exception
            if self.check_mode == 'to_be':
                return BrowseTheWeb.As(actor).check_visibility_state(selector=self.selector, mode='visible', options=self.options)
            else:
                return BrowseTheWeb.As(actor).check_visibility_state(selector=self.selector, mode='hidden', options=self.options)
        if self.mode == 'enabled':
            # if the ability method is not the expected result there will be an exception
            if self.check_mode == 'to_be':
                return BrowseTheWeb.As(actor).check_enabled_state(selector=self.selector, mode='enabled', options=self.options)
            else:
                return BrowseTheWeb.As(actor).check_enabled_state(selector=self.selector, mode='disabled', options=self.options)
        if self.mode == 'text':
            if self.check_mode == 'to_be':
                return BrowseTheWeb.As(actor).check_selector_text(selector=self.selector, text=self.payload, mode='has', options=self.options)
            else:
                return BrowseTheWeb.As(actor).check_selector_text(selector=self.selector, text=self.payload, mode='has_not', options=self.options)
        if self.mode == 'value':
            if self.check_mode == 'to_be':
                return BrowseTheWeb.As(actor).check_selector_value(selector=self.selector, value=self.payload, mode='has', options=self.options)
            else:
                return BrowseTheWeb.As(actor).check_selector_value(selector=self.selector, value=self.payload, mode='has_not', options=self.options)
        raise RuntimeError('Unknown mode: Element.answered_by')

    @staticmethod
    def to_be_visible(selector: Selector, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is visible.
        
        :param selector: the selector
        """
        return Element(selector, 'to_be', 'visible', options=options)

    @staticmethod
    def not_to_be_visible(selector: Selector, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is not visible. Opposite of Element.to_be_visible().
        
        :param selector: the selector
        """
        return Element(selector, 'not_to_be', 'visible', options=options)

    @staticmethod
    def to_be_enabled(selector: Selector, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is enabled.
        
        :param selector: the selector
        """
        return Element(selector, 'to_be', 'enabled', options=options)

    @staticmethod
    def not_to_be_enabled(selector: Selector, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is not enabled. Opposite of Element.to_be_enabled().
        
        :param selector: the selector
        """
        return Element(selector, 'not_to_be', 'enabled', options=options)
    
    @staticmethod
    def to_have_text(selector: Selector, text: str | Pattern, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is enabled.
        
        :param selector: the selector
        """
        return Element(selector, 'to_be', 'text', payload=text, options=options)
    
    @staticmethod
    def not_to_have_text(selector: Selector, text: str | Pattern, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is enabled.
        
        :param selector: the selector
        """
        return Element(selector, 'not_to_be', 'text', payload=text, options=options)

    @staticmethod
    def to_have_value(selector: Selector, value: str | Pattern, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is enabled.
        
        :param selector: the selector
        """
        return Element(selector, 'to_be', 'value', payload=value, options=options)
    
    @staticmethod
    def not_to_have_value(selector: Selector, value: str | Pattern, options: SelectorOptions | None = None) -> "Element":
        """Verifies if an element is enabled.
        
        :param selector: the selector
        """
        return Element(selector, 'not_to_be', 'value', payload=value, options=options)
