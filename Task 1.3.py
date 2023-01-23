# Task 1.3

# The Main Fucntion
def main():
    
    man = input("Please enter the position of the Man. Use 'e' for East and 'w' for West?").lower()
    cabbage = input("Please enter the position of the Cabbage. Use 'e' for East and 'w' for West?").lower()
    goat = input("Please enter the position of the Goat. Use 'e' for East and 'w' for West?").lower()
    wolf = input("Please enter the position of the Wolf. Use 'e' for East and 'w' for West?").lower()
    
    if moves(man,cabbage,goat,wolf) == False:
        print("You Are Unable To Make This Move")
    elif moves(man,cabbage,goat,wolf) == True:
        print("Well Done")

# Processing Moves
def moves(man,cabbage,goat,wolf):
    
    if goat == wolf and goat != man and man != wolf:
        return False
    elif cabbage == goat and man != goat and cabbage != man:
        return False
    else:
        return True
    
main()
