def translate(strs):
    Y=['a','e','i','o','u']
    list_strs = list(strs)
    if strs[-2:]=="ay" or (strs[-1]+strs[0])=="ay" or strs[0] in Y:
        return strs+"ay"
    if strs[0] not in Y:
        for i,v in enumerate(list_strs):
            if v in Y:
                result = []
                for s in strs.split():
                    if s[i] =='u' and s[i-1]=='q':
                        result.append(s[i+1:]+s[:i+1]+"ay")
                    else:
                        result.append(s[i:]+s[:i]+"ay")
                return " ".join(result)
        return strs[1:]+strs[0]+"ay"
    return strs+"ay"
