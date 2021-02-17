def common(first, second):
    return list(set(first.split(' ')) & set(second.split(' ')))

def not_repeated(first, second):
    return list(set(first.split(' ')) ^ set(second.split(' ')))
