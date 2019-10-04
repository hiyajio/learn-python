from keyword import iskeyword as iskey

def contains_keyword(*words):
    for word in words:
        if iskey(word): return True
    return False