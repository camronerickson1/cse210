"""
Assignment: W02 Prove: Developer - Solo Code Submission
Tic-Tac-Toe
Author: Camron Erickson
"""

"""This function will create a list that we can display in a grid later"""
def create_grid():
    grid=[1,2,3,4,5,6,7,8,9]
    return grid
    #we will use this return in the other functions

"""This function will allow us to make an initial display of the grid.  Subsequent displays are automatic, being found in the update_grid function"""
def display_grid(grid):
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print("--+---+--")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print("--+---+--")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")

"""This will check to see if either player has 3 in a row"""
def check_winner(grid):
    if grid[0] == grid[1] == grid[2] or grid[3] == grid[4] == grid[5] or grid[6] == grid[7] == grid[8] or grid[0] == grid[3] == grid[6] or grid[1] == grid[4] == grid[7] or grid[2] == grid[5] == grid[8] or grid[0] == grid[4] == grid[8] or grid[2] == grid[4] == grid[6]:
        return True

"""This is where most of the work will be done and where the gameplay is found"""
def update_grid(grid):
    winner = check_winner(grid)
    turn = "x" #this makes the player with 'x' the one that goes first
    while turn =="x":
        selection = int(input("X's turn to choose a square (1-9): ")) - 1
        if grid[selection] != "X" and grid[selection] != "O":
            grid[selection] = "X"
            display_grid(grid)
            winner = check_winner(grid)
            draw = is_draw(grid)

            if winner == True:
                print("X Wins!")
                turn = "end"
                return False
                
            elif draw == True:
                print("It's a draw!")
                return False

            else:
                turn = "o"
        else:
            print("This spot is already taken. Please try again.")
        
    while turn =="o":
        selection = int(input("O's turn to choose a square (1-9): ")) - 1
        if grid[selection] != "X" and grid[selection] != "O":
            grid[selection] = "O"
            display_grid(grid)
            winner = check_winner(grid)
            draw = is_draw(grid)

            if winner == True:
                print("O Wins!")
                turn = "end"
                return False
                
            elif draw == True:
                print("It's a draw!")
                return False

            else:
                turn = "x"
        else:
            print("This spot is already taken. Please try again.")
        
"""Here we will check to see if there are any spaces left to play in.  If not, it is a draw."""       
def is_draw(grid):
    count = 0
    for i in grid:
        if i == "X" or i == "O":
            count += 0
        else:
            count += 1
    #all empty spaces will result in count being greater than 0
    if count == 0:
        return True

"""This is our main function where we will tie everything toegether"""
def main():
    grid =create_grid()
    display_grid(grid)
    test = True
    while test == True:
        i = update_grid(grid)
        if i == False:
            test = False
        
"""Here is where we will run everything"""      
if __name__=="__main__":
    main()