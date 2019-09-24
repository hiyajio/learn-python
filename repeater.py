many_times = int(input("How many times do I have to tell you? "))

for times in range(many_times):
    print(f"Time/s {times+1}: CLEAN UP YOUR ROOM!")
    if times >= 4:
        print("I don't think you're listening anymore. I'm done")
        break