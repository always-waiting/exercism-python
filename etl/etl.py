def transform(legacy_data):
    data = {}
    for k,v in legacy_data.items():
        for item in v:
            data[item.lower()] = k
    return data
