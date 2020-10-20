import random 
import numpy

positions = ["X","X","X","X","X","X","X","X","X"]

def display(positions): 
    print(f" {positions[0]} | {positions[1]}  | {positions[2]}")
    print("-- + -- + --")
    print(f" {positions[3]} | {positions[4]}  | {positions[5]}")
    print("-- + -- + --")
    print(f" {positions[6]} | {positions[7]}  | {positions[8]}")


def pos_left(positions):
    for position in positions:
        if position == "X":
            return True
    return False 
        

def win(positions):
    i = 0
    #flatten_postions = numpy.array(positions).flatten()
    if positions[i] == positions[i+1] == positions[i+2] or positions[i] == positions[i+3] == positions[i+6] or positions[i] == positions[i+4] == positions[i+8]:
        if positions[i] == "0":
            print("You win")
            return True
        if positions[i] == "1":
            print("Computer wins")
            return True 
    
    if positions[i+3] == positions[i+4] == positions[i+5]: 
        if positions[i+3] == "0":
            print("You win")
            return True
        if positions[i+3] == "1":
            print("Computer wins")
            return True
            
    if positions[i+1] == positions[i+4] == positions[i+7]:
        if positions[i+1] == "0":
            print("You win")
            return True
        if positions[i+1] == "1":
            print("Computer wins")
            return True
            
    if positions[i+2] == positions[i+4] == positions[i+6] or positions[i+2] == positions[i+5] == positions[i+8]:
        if positions[i+2] == "0":
            print("You win")
            return True
        if positions[i+2] == "1":
            print("Computer wins")
            return True
            
    if positions[i+6] == positions[i+7] == positions[i+8]:
        if positions[i+6] == "0":
            print("You win")
            return True
        if positions[i+6] == "1":
            print("Computer wins")
            return True
    
    if(pos_left(positions) == False):
        print("It a tie")
        return True
    
    return False 

        
#computer input is 1 
def computer_turn(): 
    n = random.randint(1,9)
    
    if positions[n-1] != 0:
        print("Computers turn")
        positions[n-1] = 1
        display(positions)
        win(positions)
    if positions[n-1] == 0:
        computer_turn()
    
    
def user_turn():
    display(positions)
    while (win(positions) != True) or (pos_left(positions)):
    #user input is 0
        user_choice = int(input("Select a position: "))

        positions[user_choice - 1] = 0
        
        display(positions)
        win(positions)
        computer_turn()

user_turn()