def load(fn, mode = None):
    if mode:
        fh = open(fn, mode)
    else:
        fh = open(fn)
    data = fh.read()
    fh.close()
    return data