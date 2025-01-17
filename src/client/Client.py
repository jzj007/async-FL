import collections
from abc import abstractmethod
from multiprocessing import Process
from threading import Thread

from utils.GlobalVarGetter import GlobalVarGetter
from utils.ProcessManager import MessageQueueFactory


class Client(Process if len(GlobalVarGetter().get()) == 0 else Thread):
    def __init__(self, c_id, stop_event, selected_event, delay, train_ds, index_list, dev):
        if Client.__bases__ == (Process,):
            Process.__init__(self)
        else:
            Thread.__init__(self)
        self.model = None
        self.client_id = c_id
        self.event = selected_event
        self.event.clear()
        self.stop_event = stop_event
        self.delay = delay
        self.train_ds = train_ds
        self.dev = dev

        self.weights_buffer = collections.OrderedDict()
        self.time_stamp = 0
        self.time_stamp_buffer = 0
        self.received_weights = False
        self.received_time_stamp = False
        self.params = {}
        self.event_is_set = False
        self.schedule_t = None
        self.index_list = index_list
        self.message_queue = MessageQueueFactory.create_message_queue()
        self.training_params = self.message_queue.get_training_params()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def train_one_epoch(self):
        pass

    @abstractmethod
    def wait_notify(self):
        pass