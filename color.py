from termcolor import colored

text = colored("HI THERE!", color="red", on_color="on_white", attrs=["blink"])
print(text)