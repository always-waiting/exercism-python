lyrics = {
    1: ["first", "a Partridge in a Pear Tree.\n"],
    2: ["second", "two Turtle Doves, "],
    3: ["third", "three French Hens, "],
    4: ["fourth", "four Calling Birds, "],
    5: ["fifth", "five Gold Rings, "],
    6: ["sixth", "six Geese-a-Laying, "],
    7: ["seventh", "seven Swans-a-Swimming, "],
    8: ["eighth", "eight Maids-a-Milking, "],
    9: ["ninth", "nine Ladies Dancing, "],
    10: ["tenth", "ten Lords-a-Leaping, "],
    11: ["eleventh", "eleven Pipers Piping, "],
    12: ["twelfth", "twelve Drummers Drumming, "]
}
base = "On the %s day of Christmas my true love gave to me, "
def verse(number):
    ret = [base%lyrics[number][0]]
    if number == 1:
        ret.append(lyrics[number][1])
    else:
        for i in range(number,0,-1):
            if i != 1:
                ret.append(lyrics[i][1])
            else:
                ret.append("and %s"%lyrics[i][1])
    return "".join(ret)


def verses(start, end):
    ret = []
    for i in range(start,end+1):
        ret.append(verse(i))
    return "\n".join(ret)+"\n"


def sing():
    return verses(1,12)
