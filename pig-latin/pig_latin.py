def translate(strs):
    if strs[0] in ['a','e','i','o','u']:
        return strs + "ay"
    if strs[0:3] in ["thr", "squ", "sch"]:
        return strs[3:]+strs[0:3]+"ay"
    if strs[0:2] in ["th", "ch", "qu"]:
        return strs[2:]+strs[0:2]+"ay"
    if strs[0:2] in ["yt","xr"]:
        return strs + "ay"
    return strs[1:] + strs[0:1] + "ay"
