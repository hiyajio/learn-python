for numb in range(1,21):
    if numb == 4 or numb == 13:
        state = "UNLUCKY"
    elif numb % 2 == 1:
        state = "odd"
    else:
        state = "even"
    print(f"{numb} is {state}!")