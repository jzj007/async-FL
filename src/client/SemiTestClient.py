from client.SemiClient import SemiClient
from client.TestClient import TestClient


class SemiTestClient(TestClient, SemiClient):
    def __init__(self, c_id, stop_event, selected_event, delay, train_ds, index_list, config, dev):
        TestClient.__init__(self, c_id, stop_event, selected_event, delay, train_ds, index_list, config, dev)
        SemiClient.__init__(self, c_id, stop_event, selected_event, delay, train_ds, index_list, config, dev)

