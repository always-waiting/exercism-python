def flatten(array):
    ret = []
    for item in array:
        if isinstance(item,list) or isinstance(item, tuple):
            ret.extend(flatten(item))
        else:
            if item != None:
                ret.append(item)
    return ret

