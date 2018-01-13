""" 
Name : Prateek Vachher
Email ID : vachh007@umn.edu
Class : CSCI 1133
Lecturer : Dr. Amy Larson

"""

################################ Initial Definitions

import turtle, copy, random
flag = 1

turt = turtle.Turtle()
turt1 = turtle.Turtle()
turt2 = turtle.Turtle()

turt.speed(0)
turt1.speed(0)
turt2.speed(0)

################################# Function Definitions

def make_bigsquare(turtle1): ## Makes Big Square for Sudoku
    turtle1.goto(0,0)
    turtle1.penup()
    turtle1.forward(200)
    turtle1.right(90)
    turtle1.pendown()
    turtle1.pensize(10)
    for x in range(4):
        turtle1.forward(200)
        turtle1.right(90)
        turtle1.forward(200)
    turtle1.pensize(3)    

def make_smallsquare(turtle1): ## Makes Grids inside Sudoku
    ###
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(400)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    ###
    turtle1.pensize(10)
    turtle1.forward(400)
    turtle1.pensize(3)
    ###
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    turtle1.forward(400)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(400)
    turtle1.left(90)
    turtle1.forward(100)
    turtle1.left(90)
    ###
    turtle1.pensize(10)
    turtle1.forward(400)
    turtle1.pensize(3)
    ###
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(400)
    turtle1.penup()

def convert_position(position):  ## Converts Position to Coordinates (A1 = 1,1)
    row = str(int(position[-1])-1)
    if position[0] == 'A':
        column = 0
    elif position[0] == 'B':
        column = 1
    elif position[0] == 'C':
        column = 2
    elif position[0] == 'D':
        column = 3
    return str(row)+str(column)

def mark_rows_columns(turt):  ##  Writes Column and Row Titles
    turt.goto(-150,200)
    turt.write('A',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(-50,200)
    turt.write('B',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(50,200)
    turt.write('C',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(150,200)
    turt.write('D',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(-240,120)
    turt.write('1',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(-240,20)
    turt.write('2',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(-240,-80)
    turt.write('3',move=False, align="center", font=("Arial", 50, "bold"))
    turt.goto(-240,-180)
    turt.write('4',move=False, align="center", font=("Arial", 50, "bold"))


def find_solution(grid):  ## Master Function to find solution

    def brute_force(grid): ## Function takes grid as input, identifies 0 elements and brute forces a solution
        list1 = []
        list2 = []
        db = []
        elements = [[1],[2],[3],[4]]

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    list1.append([x,y])
                    list2.append(0)

        def perm(elements):  ## Generates Permutations 
            list3 = []
            for x in elements:
                for x1 in elements:
                    list3.append(x+x1)
            return list3


        for counter in range(3):
            elements = perm(elements)

        for element in elements:
            new_grid = copy.deepcopy(grid)

            for a in range(len(list1)):
                new_grid[list1[a][0]][list1[a][1]] = element[a]

            db.append(new_grid)

        return db

    def check_row(elements):  ## Checks the grid for rows with same elements
        new_db = []
        for element in elements:
            flag = 1
            for sub_element in element:
                for counter in range(len(sub_element)):
                    if sub_element[counter] in sub_element[counter+1:]:
                        flag = 0
                        break
                if flag == 0:
                    break
            if flag == 1:
                new_db.append(element)
        return new_db

    def check_allcolumns(db):  ## Checks the grid for columns with same elements
        new = []
        for l in db:
            flag = 1
            for m in range(len(l)):
                if l[m] in l[m+1:]:
                    flag = 0
                    break
            if flag == 1:
                new.append(l)
        return new

    def swap_columns(db):  ## Swaps columns with rows
        new_db = []
        for l in db:
            wow1 = []
            for m in range(len(l)):
                wow = []
                for t in range(len(l)):
                    wow.append(l[t][m])
                wow1.append(wow)
            new_db.append(wow1)
        return new_db

    def check_block(db):   ### Checks sub-squares inside the sudoku grid
        new_db = []
        for l in db:
            flag = 1
            for m in range(0,len(l),2):
                for k in range(0,len(l),2):
                    if l[m][k] == l[m][k+1] or l[m][k] == l[m+1][k] or l[m][k] == l[m+1][k+1] or l[m+1][k] == l[m][k+1]:
                        flag = 0
                        break
            if flag == 1:
                new_db.append(l)
        return new_db
        
    return (check_block(swap_columns(check_row(swap_columns(check_allcolumns(check_row(brute_force(grid))))))))[0]  ### Returns one of the multiple possible sudoku solutions


def printer(original_grid,new_grid,answer_grid,assistance):  ## Prints the grid with several function based factors, such as assistance answer_grid, etc
    grid = new_grid
    points = [[[-150,120],[-50,120],[50,120],[150,120]],[[-150,20],[-50,20],[50,20],[150,20]],[[-150,-80],[-50,-80],[50,-80],[150,-80]],[[-150,-180],[-50,-180],[50,-180],[150,-180]]]
    for m in range(len(points)):
        for m1 in range(len(points[m])):
            turt.goto(points[m][m1][0],points[m][m1][1])
            if grid[m][m1] == 0:
                pass
            else:
                if grid[m][m1] != original_grid[m][m1] and assistance==1:
                    if grid[m][m1] == answer_grid[m][m1]:
                        turt2.clear()
                        turt.color ('green')
                        turt.write(str(grid[m][m1]), move=False, align="center", font=("Arial", 50, "normal"))
                        turt.color ('black')
                    else:
                        turt2.goto(0,-300)
                        turt2.color ('red')
                        turt2.write("Incorrect Attempt", move=False, align="center", font=("Arial", 55, "bold"))
                        turt.color ('black')

                elif grid[m][m1] != original_grid[m][m1] and assistance==0:
                    turt.color ('purple')
                    turt.write(str(grid[m][m1]), move=False, align="center", font=("Arial", 50, "normal"))
                    turt.color ('black')
                else: 
                    turt.write(str(grid[m][m1]), move=False, align="center", font=("Arial", 50, "normal"))

def printer_original(original_grid,new_grid):  ## Prints the grid structure with known numbers
    grid = new_grid
    points = [[[-150,120],[-50,120],[50,120],[150,120]],[[-150,20],[-50,20],[50,20],[150,20]],[[-150,-80],[-50,-80],[50,-80],[150,-80]],[[-150,-180],[-50,-180],[50,-180],[150,-180]]]
    for m in range(len(points)):
        for m1 in range(len(points[m])):
            turt1.goto(points[m][m1][0],points[m][m1][1])
            if grid[m][m1] == 0:
                pass
            else:                    
                turt1.write(str(grid[m][m1]), move=False, align="center", font=("Arial", 50, "normal"))


############################## WORKSPACE



while flag == 1:

    turt.clear()
    turt1.clear() 
    turt2.clear()

    ## Generates a database of questions of Sudoku
    questions = []
    questions.append([[4,0,0,1],[0,1,3,0],[0,4,1,0],[1,0,0,3]])
    questions.append([[0,4,0,1],[3,0,4,0],[1,0,0,4],[0,2,1,0]])
    questions.append([[0,4,3,2],[3,0,0,0],[4,1,0,0],[0,0,4,1]])
    questions.append([[3,4,1,2],[0,0,0,0],[0,0,0,0],[4,2,3,1]])
    questions.append([[0,0,0,0],[2,3,4,1],[3,4,1,2],[0,0,0,0]])
    questions.append([[0,2,4,0],[1,0,0,3],[4,0,0,2],[0,1,3,0]])

    grid_num = random.randint(0,len(questions)-1)  ## Randomly selects any sudoku question from the database
    grid = questions[grid_num]


    make_bigsquare(turt1)       ## Making Outer Square of Sudoku
    make_smallsquare(turt1)     ## Making Inner Grid of Sudoku
    mark_rows_columns(turt1)    ## Marking Rows and Columns


    turt.penup()
    turt1.penup()
    turt2.penup()

    turt.hideturtle()
    turt1.hideturtle()
    turt2.hideturtle()


    answer_grid = find_solution(grid)      ## Finds solution of the provided sudoku question
    grid1 = copy.deepcopy(grid)

    printer_original(grid,grid1)        ## Prints out the generated grid

    flag = 1
    while flag == 1:  ## While loop for game playtime

        a = turtle.textinput('Real-Time Correction','With Real-Time Correction? (Y/N)')  ## Real-Time correction

        if a.upper() == 'Y':

            flag = 1
            while flag == 1:
                b = turtle.textinput('Attempt', 'Enter Position and Number: (A3 2) ')  ## Input for position of input
                position = convert_position(b.split()[0])
                turt2.clear()
                number = b.split()[1]
                if grid1[int(position[0])][int(position[1])] == 0:
                    grid1[int(position[0])][int(position[1])] = int(number)
                elif grid1[int(position[0])][int(position[1])] == grid[int(position[0])][int(position[1])]:
                    turt2.goto(0,-300)
                    turt2.write("Invalid Move!", move=False, align="center", font=("Arial", 55, "bold"))
                else:
                    turt.clear()
                    grid1[int(position[0])][int(position[1])] = int(number)
                printer(grid,grid1,answer_grid,1)
                if grid1 == answer_grid:
                    turt2.goto(0,-300)
                    turt2.write("Game Over! You Win!", move=False, align="center", font=("Arial", 55, "bold"))
                    flag = 0
                    break

        elif a.upper() == 'N':
            flag = 1
            while flag == 1:
                b = turtle.textinput('Attempt', 'Enter Position and Number: (A3 2) ')
                turt2.clear()
                position = convert_position(b.split()[0])
                number = b.split()[1]
                if grid1[int(position[0])][int(position[1])] == 0:
                    grid1[int(position[0])][int(position[1])] = int(number)
                elif grid1[int(position[0])][int(position[1])] == grid[int(position[0])][int(position[1])]:
                    turt2.goto(0,-300)
                    turt2.write("Invalid Move!", move=False, align="center", font=("Arial", 55, "bold"))
                else:
                    turt.clear()
                    grid1[int(position[0])][int(position[1])] = int(number)
                printer(grid,grid1,answer_grid,0)
                if grid1 == answer_grid:
                    turt2.goto(0,-300)
                    turt2.write("Game Over! You Win!", move=False, align="center", font=("Arial", 55, "bold"))
                    flag = 0
                    break

    a = turtle.textinput('Play Again','Play Again? (Y/N) ') ## Play Again

    if a.upper() == 'Y':
        flag = 1
    else:
        flag = 0

##############################