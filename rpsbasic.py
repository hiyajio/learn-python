print("...Rock...")
print("...Paper...")
print("...Scissors...\n\n")

p1_choice = input("(Enter Player 1's choice): ")
while p1_choice != "paper" and p1_choice != "rock" and p1_choice != "scissors":
    print("\nCan only choose between rock, paper, and scissors\n")
    p1_choice = input("(Enter Player 1's choice): ")

print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")
print("\n\n*** NO CHEATING ***\n\n")

p2_choice = input("(Enter Player 2's choice): ")
while p2_choice != "paper" and p2_choice != "rock" and p2_choice != "scissors":
    print("\nCan only choose between rock, paper, and scissors\n")
    p2_choice = input("(Enter Player 2's choice): ")
print("\n\nSHOOT!\n")

if (p1_choice == "rock"):
    if (p2_choice == "rock"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! It's a tie!\n")
    if (p2_choice == "paper"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! Player 2 wins!\n")
    if (p2_choice == "scissors"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! Player 1 wins!\n")
if (p1_choice == "paper"):
    if (p2_choice == "rock"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! Player 1 wins!\n")
    if (p2_choice == "paper"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! It's a tie!\n")
    if (p2_choice == "scissors"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! Player 2 wins!\n")
if (p1_choice == "scissors"):
    if (p2_choice == "rock"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! Player 2 wins!\n")
    if (p2_choice == "paper"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! Player 1 wins!\n")
    if (p2_choice == "scissors"):
        print("Player 1 chose " + p1_choice + " and Player 2 chose " + p2_choice + "! It's a tie!\n")

