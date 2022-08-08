class SubSelector:
    selector: str
    options = {
        "has_text": str | None,
        "timeout": float | None,
        "sub_selector": object | None,
    }

class SelectorOptions:
    has_text: str | None
    sub_selector: SubSelector | None
    timeout: float | None