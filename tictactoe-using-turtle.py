import sys
import turtle as t

#creating box
t.setup(250,250)
#right first kodu position
t.penup()
t.goto(25,0)
t.pendown()
t.left(90)
#right first kodu
t.forward(75)
t.penup()
t.goto(25,0)
t.pendown()
t.back(75)

#left kodu seting position
t.penup()
t.goto(25,0)
t.left(90)
t.goto(-25,0)
t.right(90)

#left kodu drawing
t.pendown()
t.forward(75)
t.penup()
t.goto(-25,0)
t.pendown()
t.back(75)
t.penup()

#upper line
t.penup()
t.goto(0,25)
t.pendown()
t.left(90)

#drawing upper line
t.forward(75)
t.penup()
t.goto(0,25)
t.pendown()
t.back(75)
t.penup()
t.goto(0,50)

#lower line
t.goto(0,0)
t.goto(0,-25)
t.pendown()
t.right(180)

#lower line drawing
t.forward(75)
t.penup()
t.goto(0,-25)
t.pendown()
t.back(75)
t.position()
t.penup()

#defining user
print('Player1 choose x or o')
player1 = input()

if player1 == 'x':
    print('player1 chose x')
    print('player2 chose o')
    player2 = 'o'
elif player1 =='o':
    print('player1 chosed o')
    print('player2 chose x')
    player1 = 'o'
    player2 = 'x'
else:
    print ("Choose right option!")
    exit
player1_win_list = []
player2_win_list = []

check_duplicates = []


##### If user pressed 1 #####
def if_user_pressed_1(player_name):
    if player_name == 'x':
        t.goto(-75,70)
        t.right(45)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(45)# returning to original position
        t.goto(-30,70)
        t.pendown()
        t.left(225)
        t.forward(60)
        t.penup()
        t.right(225)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(-50,70)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 2 #####
def if_user_pressed_2(player_name):
    if player_name == 'x':
        t.goto(20,75)
        t.right(130)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(130)# returing to original position
        t.goto(-20,75)
        t.pendown()
        t.right(45)
        t.forward(60)
        t.penup()
        t.left(45)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(0,75)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)
###############################

##### If user pressed 3 #####
def if_user_pressed_3(player_name):
    if player_name == 'x':
        t.goto(30,75)
        t.right(40)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(40)# returing to original position
        t.goto(75,75)
        t.pendown()
        t.right(135)
        t.forward(60)
        t.penup()
        t.left(135)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(60,75)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 4 #####
def if_user_pressed_4(player_name):
    if player_name == 'x':
        t.goto(-75,20)
        t.right(45)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(45)# returning to original position
        t.goto(-30,20)
        t.pendown()
        t.left(225)
        t.forward(60)
        t.penup()
        t.right(225)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(-50,20)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 5 #####
def if_user_pressed_5(player_name):
    if player_name == 'x':
        t.goto(-20,20)
        t.right(45)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(45)# returning to original position
        t.goto(20,20)
        t.pendown()
        t.right(135)
        t.forward(60)
        t.penup()
        t.left(135)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(0,17)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 6 #####
def if_user_pressed_6(player_name):
    if player_name == 'x':
        t.goto(30,20)
        t.right(40)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(40)# returing to original position
        t.goto(75,20)
        t.pendown()
        t.right(135)
        t.forward(60)
        t.penup()
        t.left(135)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(60,20)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 7 #####
def if_user_pressed_7(player_name):
    if player_name == 'x':
        t.goto(-75,-30)
        t.right(45)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(45)# returning to original position
        t.goto(-30,-30)
        t.pendown()
        t.left(225)
        t.forward(60)
        t.penup()
        t.right(225)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(-50,-30)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 8 #####
def if_user_pressed_8(player_name):
    if player_name == 'x':
        t.goto(20,-30)
        t.right(130)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(130)# returing to original position
        t.goto(-20,-30)
        t.pendown()
        t.right(45)
        t.forward(60)
        t.penup()
        t.left(45)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(0,-30)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

##### If user pressed 9 #####
def if_user_pressed_9(player_name):
    if player_name == 'x':
        t.goto(30,-30)
        t.right(40)
        t.pendown()
        t.forward(60)
        t.penup()
        t.left(40)# returing to original position
        t.goto(75,-30)
        t.pendown()
        t.right(135)
        t.forward(60)
        t.penup()
        t.left(135)# returning to original position
        t.goto(0,0)
    elif player_name == 'o':
        t.penup()
        t.goto(60,-30)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(0,0)

###############################

######## main program ###########
while (1):
    player_input = input("Player "+str((len(check_duplicates) % 2)+1)+" : Enter 1 to 9. 0 to Quit     = ")
    player_input = int(player_input)
    if player_input in check_duplicates:
        print ("Duplicate number found! Try again\n\n")
    elif player_input not in range(1,10):
        print ("Player input is not in range of 1 to 9. Quitting program")
        break

    elif player_input in range(1,10):
        print ("Player input = "+str(player_input)+" is in range of 1 to 9")

        check_duplicates.append(player_input)
        if player_input == 1:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_1(player1)
                player1_win_list.append(1)
            else:
                if_user_pressed_1(player2)
                player2_win_list.append(1)
        if player_input == 2:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_2(player1)
                player1_win_list.append(2)
            else:
                if_user_pressed_2(player2)
                player2_win_list.append(2)
        if player_input == 3:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_3(player1)
                player1_win_list.append(3)
            else:
                if_user_pressed_3(player2)
                player2_win_list.append(3)
        if player_input == 4:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_4(player1)
                player1_win_list.append(4)
            else:
                if_user_pressed_4(player2)
                player2_win_list.append(4)
        if player_input == 5:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_5(player1)
                player1_win_list.append(5)
            else:
                if_user_pressed_5(player2)
                player2_win_list.append(5)
        if player_input == 6:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_6(player1)
                player1_win_list.append(6)
            else:
                if_user_pressed_6(player2)
                player2_win_list.append(6)
        if player_input == 7:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_7(player1)
                player1_win_list.append(7)
            else:
                if_user_pressed_7(player2)
                player1_win_list.append(7)
        if player_input == 8:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_8(player1)
                player1_win_list.append(8)
            else:
                if_user_pressed_8(player2)
                player2_win_list.append(8)
        if player_input == 9:
            if len(check_duplicates) % 2 !=0:
                if_user_pressed_9(player1)
                player1_win_list.append(9)
            else:
                if_user_pressed_9(player2)
                player2_win_list.append(9)

        if (1 in player1_win_list) and (2 in player1_win_list) and (3 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (4 in player1_win_list) and (5 in player1_win_list) and (6 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (7 in player1_win_list) and (8 in player1_win_list) and (9 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (1 in player1_win_list) and (5 in player1_win_list) and (9 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (3 in player1_win_list) and (5 in player1_win_list) and (7 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (1 in player1_win_list) and (4 in player1_win_list) and (7 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (2 in player1_win_list) and (5 in player1_win_list) and (8 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (3 in player1_win_list) and (6 in player1_win_list) and (9 in player1_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 1 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        ####################################################################################

        if (1 in player2_win_list) and (2 in player2_win_list) and (3 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (4 in player2_win_list) and (5 in player2_win_list) and (6 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (7 in player2_win_list) and (8 in player2_win_list) and (9 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (1 in player2_win_list) and (5 in player2_win_list) and (9 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (3 in player2_win_list) and (5 in player2_win_list) and (7 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (1 in player2_win_list) and (4 in player2_win_list) and (7 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (2 in player2_win_list) and (5 in player2_win_list) and (8 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        elif (3 in player2_win_list) and (6 in player2_win_list) and (9 in player2_win_list):
            print ("\n\n\n\n\n\n\n PLAYER 2 WON THE MATCH!\n\n\n\n\n\n\n\n")
            break
        if len(check_duplicates) == 9:
            print('\n\n\n\n\n\nDraw\n\n\n\n\n\n\n\n')
            break
    else:
        print ("Wrong option!")
        exit
