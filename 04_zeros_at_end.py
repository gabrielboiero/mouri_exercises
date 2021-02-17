def zeros_at_end(values):
    return list(filter(lambda x: x != 0, values)) + [0] * values.count(0)
