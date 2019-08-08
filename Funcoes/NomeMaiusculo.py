name = 'minicurso de python para mulheres'


def cap_name(name):
    items = []
    p = ['da', 'de', 'di', 'do', 'du', 'para']
    for item in name.split():
        if not item in p:
            item = item.capitalize()
        items.append(item)
    return ' '.join(items)

print(cap_name(name))