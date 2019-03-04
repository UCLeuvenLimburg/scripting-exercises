def frequencies(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result

def mode(ns):
    fs = frequencies(ns)
    return max(fs.items(), key=lambda el: el[1])[0]
