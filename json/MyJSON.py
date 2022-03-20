
def serializable(data):
    pass

def deser(data: dict):
    cls = data['class']
    inti_attr = {'w': 10, 'h': 10}
    return type('type', (cls,), inti_attr)

def ser(obj, cls=None):
    if cls is None:
        if obj is not None:
            cls = type(obj)
    if obj is None:
        if cls is None:
            return None
        else:
            return {'class': cls, 'value': None}
    elif isinstance(obj, list):
        res = [ser(i) for i in obj]
        return {'class': type(obj), 'value': res}
    elif not hasattr(obj, '__dict__'):
        return obj
    elif len(vars(obj).keys()) == 0:
        return obj
    else:
        res = {}
        for i in vars(obj).items():
            res[i[0]] = ser(i[1])
        return {'class': type(obj), 'value': res}
