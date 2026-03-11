from typing import List

from .event_models import Event


class EventStore:

    def __init__(self):

        self.events: List[Event] = []

    def save(self, event: Event):

        self.events.append(event)

    def get_all(self):

        return self.events