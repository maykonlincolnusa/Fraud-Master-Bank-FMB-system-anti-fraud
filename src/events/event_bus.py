import asyncio
from collections import defaultdict
from typing import Callable, Dict, List, Awaitable

from .event_models import Event
from .event_types import EventType


class EventBus:

    def __init__(self):

        self._subscribers: Dict[EventType, List[Callable[[Event], Awaitable]]] = defaultdict(list)

    def subscribe(self, event_type: EventType, handler: Callable):
        """
        Register async handler
        """
        if handler not in self._subscribers[event_type]:

            self._subscribers[event_type].append(handler)

    def unsubscribe(self, event_type: EventType, handler: Callable):

        if handler in self._subscribers[event_type]:

            self._subscribers[event_type].remove(handler)

    async def publish(self, event: Event):

        handlers = self._subscribers.get(event.event_type, [])

        tasks = []

        for handler in handlers:

            tasks.append(handler(event))

        if tasks:

            await asyncio.gather(*tasks)

    def clear(self):

        self._subscribers.clear()