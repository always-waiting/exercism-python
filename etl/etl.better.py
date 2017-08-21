def transform(d):
    '''Just reverse the dictionary'''
    return {l.lower(): p for p, letters in d.items() for l in letters}

def transform(strs):
    result = {}
    for k,v in strs.items():
        for i in v:
            result.update({i.lower():k})
    return dict(result.items())
