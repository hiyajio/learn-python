'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(listed):
    listed = [num for num in listed if num % 2 == 0]
    product = 1
    for num in listed:
        product = product * num
    return product