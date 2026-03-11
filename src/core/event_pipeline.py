from events.event_bus import EventBus
from events.event_types import EventType


class EventPipeline:

    def __init__(self):

        self.bus = EventBus()

    def publish(self, event_type: EventType, payload: dict):

        self.bus.publish(event_type, payload)

    def subscribe(self, event_type: EventType, handler):

        self.bus.subscribe(event_type, handler)