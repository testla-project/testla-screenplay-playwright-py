# from @testla/screenplay import Action, Actor
from time import sleep


class Sleep(Action):
    """Action Class. Pauses further test execution for a while. Does not require a particular Ability."""

    def __init__(self, secs: float):
        super.__init__()
        self.secs = secs

    def perform_as(self) -> None:
        return sleep(self.secs)

    @staticmethod
    def For(secs: float) -> "Sleep":
        """Pause the execution of further test steps for a given interval in seconds.

        :param secs: interval in seconds.
        """
        return Sleep(secs)

