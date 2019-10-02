'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(listed, command, locate, value=0):
    if command == "remove":
        if locate == "end":
            return listed.pop()
        return listed.pop(0)
    elif command == "add":
        if locate == "end":
            listed.append(value)
        else: 
            listed.insert(0, value)
        return listed