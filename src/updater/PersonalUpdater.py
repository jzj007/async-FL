import time

import wandb

from updater.SyncUpdater import SyncUpdater


class PersonalUpdater(SyncUpdater):
    def __init__(self, server_thread_lock, stop_event, config, mutex_sem, empty_sem, full_sem):
        SyncUpdater.__init__(self, server_thread_lock, stop_event, config, mutex_sem, empty_sem, full_sem)

    def run(self):
        for epoch in range(self.T):
            self.full_sem.acquire()
            self.mutex_sem.acquire()
            update_list = []
            # 接收所有的更新
            while not self.queue_manager.empty():
                update_list.append(self.queue_manager.get())
            self.server_thread_lock.acquire()
            self.update_server_weights(epoch, update_list)
            self.run_personalization_test(epoch, update_list)
            self.server_thread_lock.release()
            self.current_time.time_add()
            # 本轮结束
            self.mutex_sem.release()
            self.empty_sem.release()
            time.sleep(0.01)

        # 终止所有client线程
        self.client_manager.stop_all_clients()

    def run_personalization_test(self, epoch, update_list):
        accuracy = 0
        loss = 0
        for i in range(len(update_list)):
            accuracy += update_list[i]["accuracy"]
            loss += update_list[i]["loss"]
        accuracy = accuracy / len(update_list)
        loss = loss / len(update_list)
        self.loss_list.append(loss)
        self.accuracy_list.append(accuracy)
        self.print_lock.acquire()
        print('Epoch(t):', epoch, 'avg-accuracy:', accuracy, 'loss', loss)
        if self.config['enabled']:
            wandb.log({'accuracy': accuracy, 'loss': loss})
        self.print_lock.release()

        return accuracy, loss

