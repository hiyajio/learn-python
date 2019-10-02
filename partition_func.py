'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(listed, fn):
    return [[lis for lis in listed if fn(lis)], [lis for lis in listed if not fn(lis)]]