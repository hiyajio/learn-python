def interleave(str1, str2):
    return "".join("".join(lett) for lett in zip(str1, str2))