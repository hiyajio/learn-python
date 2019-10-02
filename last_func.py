'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(lis):
    if not lis:
        return None
    return lis.pop()