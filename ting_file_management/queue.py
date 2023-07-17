from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.queue):
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self.queue[index]
