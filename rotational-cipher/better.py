def rotate(story, shift):
    return ''.join([ # concentrate list to string
            (lambda c, is_upper: c.upper() if is_upper else c) # if original char is upper case than convert result to upper case too
                (
                  ("abcdefghijklmnopqrstuvwxyz"*2)[ord(char.lower()) - ord('a') + shift % 26], # rotate char, this is extra easy since Python accepts list indexs below 0
                  char.isupper()
                )
            if char.isalpha() else char # if not in alphabet then don't change it
            for char in story
        ])
