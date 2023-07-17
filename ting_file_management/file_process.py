import os
from ting_file_management.file_management import txt_importer


def process(queue, file_path):
    file_name = os.path.basename(file_path)

    if queue.contains(file_name):
        return

    data = txt_importer(file_path)
    if not data:
        return

    processed_data = {
        'nome_do_arquivo': file_name,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data
    }

    queue.enqueue(file_name)

    print(processed_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
