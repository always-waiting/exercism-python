def verse(i):
    if i == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\n" \
                "Go to the store and buy some more, " \
                "99 bottles of beer on the wall.\n"
    if i == 1:
        return "1 bottle of beer on the wall, 1 bottle of beer.\n" \
                "Take it down and pass it around, " \
                "no more bottles of beer on the wall.\n"

    plural = {1: ''}
    return  f"{i} bottles of beer on the wall, {i} bottles of beer.\n" \
            f"Take one down and pass it around, " \
            f"{i-1} bottle{plural.get(i-1,'s')} of beer on the wall.\n"

def song(start, stop=0):
    return ''.join(verse(i)+'\n' for i in range(start, stop-1, -1))
