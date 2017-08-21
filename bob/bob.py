import re
def hey(question):
    if is_yell(question):
        return "Whoa, chill out!"
    elif is_question(question):
        return "Sure."
    elif is_silence(question):
        return "Fine. Be that way!"
    else:
        return "Whatever."

def is_yell(question):
    return question.isupper()

def is_question(question):
    return question.rstrip().endswith("?")

def is_silence(question):
    ques = re.sub("[^a-z0-9A-Z]","",question)
    return False if len(ques) else True

