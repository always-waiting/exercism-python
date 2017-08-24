def handshake(x):
    if type(x) == str:
        try:
            x = int(x, 2)
        except ValueError:
            return []
    if x < 0:
        return []
    secret = []
    if x & 1:
        secret.append('wink')
    if x & 2:
        secret.append('double blink')
    if x & 4:
        secret.append('close your eyes')
    if x & 8:
        secret.append('jump')
    if x & 16:
        secret.reverse()
    return secret

def code(l):
    d = {'wink': 1, 'double blink': 2, 'close your eyes': 4, 'jump': 8}
    try:
        n = sum(d[x] for x in l)
    except KeyError:
        return '0'
    if l == l[::-1]:
        pass
    elif l[::-1] == handshake(n):
        n += 16
    return format(n, 'b')

