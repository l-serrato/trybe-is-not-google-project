from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queues = PriorityQueue()

    priority1 = {"nome_do_arquivo": "qualquercoisa.txt", "qtd_linhas": 5}
    priority2 = {"nome_do_arquivo": "qualquercoisa.txt", "qtd_linhas": 2}

    queues.enqueue(priority1)

    assert len(queues) == 1

    queues.dequeue()
    assert len(queues) == 0

    queues.enqueue(priority1)
    queues.enqueue(priority2)

    assert queues.search(0) == priority2
    assert queues.search(1) == priority1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queues.search(15)
