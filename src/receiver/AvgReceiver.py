import time


class AvgReceiver:
    def __init__(self, queue, config):
        self.queue = queue
        self.config = config

    def receive(self, nums):
        while self.queue.qsize() < nums:
            time.sleep(0.01)
