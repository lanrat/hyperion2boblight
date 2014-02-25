import threading

class PriorityList(object):
    """docstring for PriorityList"""
    def __init__(self):
        super(PriorityList, self).__init__()
        self.lock = threading.RLock()
        self.datas = {}
        self.event = threading.Event()

    def getPriorities(self):
        with self.lock:
            result = self.datas.keys()
        result.sort()
        return result

    def set(self, priority, data):
        with self.lock:
            self.datas[priority] = data
        self.event.set()

    def remove(self, priority):
        with self.lock:
            if priority in self.datas:
                del self.datas[priority]
        self.event.set()

    def clear(self):
        with self.lock:
            self.datas.clear()
        self.event.set()

    def getFirst(self):
        with self.lock:
            priorities = self.getPriorities()
            if len(priorities) > 0:
                result = (priorities[0], self.datas[priorities[0]])
            else:
                result = (None, None)
        return result