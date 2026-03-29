import heapq

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = []
        self.map = {}
        denqoravil = events
        for eventId, priority in events:
            self.map[eventId] = priority
            heapq.heappush(self.heap, (-priority, eventId))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.map[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            priority, eventId = heapq.heappop(self.heap)
            if self.map.get(eventId) == -priority:
                del self.map[eventId]
                return eventId
        return -1