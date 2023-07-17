import os
import sys


def txt_importer(path_file):
    file_type = ".txt"
    if file_type not in path_file:
        sys.stderr.write("Formato inválido")

    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return None

    with open(path_file, "r") as content:
        return content.read().split("\n")
