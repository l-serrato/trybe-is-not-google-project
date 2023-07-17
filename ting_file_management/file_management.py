import os
import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)

    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return None

    with open(path_file, "r") as file:
        content = file.read()
        return content.split("\n")
