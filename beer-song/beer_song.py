def verse(number):
    if number > 2:
        template = "%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottles of beer on the wall.\n"
        return template%(number, number, number-1)
    elif number == 2:
        template = "%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottle of beer on the wall.\n"
        return template%(number, number, number-1)
    elif number == 1:
        template = "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n"
        return template
    else:
        template = "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
        return template
def song(end,start):
    ret = []
    for i in range(end, start-1,-1):
        ret.append(verse(i))
    return "\n".join(ret)+"\n"
