def exists_word(word, instance):
    result = list()

    for i in range(0, len(instance)):
        file = instance.search(i)
        insts = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list(),
        }

        for line, text in enumerate(file["linhas_do_arquivo"]):
            if word.casefold() in text.casefold():
                insts["ocorrencias"].append({"linha": line + 1})

        if len(insts["ocorrencias"]) > 0:
            result.append(insts)

    return result


def search_by_word(word, instance):
    result = []
    for file in instance.queue:
        insts = []
        for index, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                insts.append({
                    'linha': index + 1,
                    'conteudo': line
                })
        if insts:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': insts
            })
    return result
