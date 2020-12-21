board = [' ' for x in range(10)]


def insertletter(letter,pos):
    board[pos]=letter
    
def spaceisfree(pos):
    return board[pos]==' '
    
def printboard(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |   ")
    

def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
    
def iswinner(b,l):
    return(b[1]==l and b[2]==l and b[3]==l or
    b[4]==l and b[5]==l and b[6]==l or
    b[7]==l and b[8]==l and b[9]==l or 
    b[1]==l and b[4]==l and b[7]==l or
    b[2]==l and b[5]==l and b[8]==l or
    b[3]==l and b[6]==l and b[9]==l or
    b[1]==l and b[5]==l and b[9]==l or
    b[3]==l and b[5]==l and b[7]==l) 


def playermove():
    run = True
    while run:
        move=int(input("Please select a position to enter the X between 1 to 9: "))
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceisfree(move):
                    run=False
                    insertletter("X",move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type a number between 1 to 9 ")
        except:
            print("Please type a number! ")
            
        
def computermove():
    posiblemoves=[x for x ,letter in enumerate(board) if letter==' ' and x!=0]
    move=0
    for let in ('O','X'):
        for i in posiblemoves:
            boardcopy = board[:]
            boardcopy[i]=let
            if iswinner(boardcopy,let):
                move = i 
                return move
    cornersopen=[]
    for i in posiblemoves:
        if i in[1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move =selectRandom(cornersopen)
        return move 
    if 5 in posiblemoves:
        move = 5
        return move
    
    edgesopen=[]
    for i in posiblemoves:
        if i in[2,4,6,8]:
            edegesopen.append(i)
    if len(edgesopen)>0:
        move=selectRandom(edgesopen)
        return move
    
def selectRandom(li):
    import random 
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game! ")
    printboard(board)
    while not(isboardfull(board)):
        if not(iswinner(board,'O')):
            playermove()
            printboard(board)
        else:
            print("Sorry you loose!")
            break
        
        if not(iswinner(board,'X')):
            move=computermove()
            if move==0:
                print("Tie game!")
            else:
                insertletter('O',move)
                print("Computer placed an O on position "+str(move)+":")
                printboard(board)
        else:
            print("You win!")
            break
    
    if isboardfull(board):
        print("Tie game!")
        
        
while True:
    x=input("Do you want to play again? (y/n)")
    if x.lower()=="y":
        board=[' ' for x in range(10)]
        print("---------------------------------")
        main()
    else:
        break
