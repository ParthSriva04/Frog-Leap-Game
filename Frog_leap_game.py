def display_game(positions):
    print("[0,1,2,3,4,5,6]")
    print(positions)
def main():
    print("\nAIM : To move all 'G'(Green) frogs to right and 'B'(Brown) frogs to left ")
    print("1. A frog can only jump in a given direction")
    print("2. A frog can jump over only 1 frog at a time")
    print("3. A frog can also jump to nearby vacant rock in given direction")
    positions=['G','G','G','-','B','B','B'] 
    #'G' represents green frogs
    # 'B' represents Brown Frogs
    # '-' represents Blank Space
    
    while True:
        display_game(positions)
        move=input("Press q to quit \nEnter the position of piece:")
        if move=='q':
            print("YOU LOSE")
            break
            continue

        try:
            move=int(move)
        except ValueError:
            print("Invalid Move")
            continue
        if move<0 or move>6 or positions[move]=='-':
            print("Invalid Move")
            continue 
            

        pos2=0
        if positions[move]=='G':
            if move+1<=6 and positions[move+1]=='-':
                pos2=move+1
            elif move+2<=6 and positions[move+2]=='-' and positions[move+1]=='B':
                pos2=move+2
            else:
                print("Invalid Move")
                continue
        elif positions[move]=='B':
            if move-1>=0 and positions[move-1]=='-':
                pos2=move-1
            elif move-2>=0 and positions[move-2]=='-' and positions[move-1]=='G':
                pos2=move-2

            else:
                print("Invalid Move")
                continue
        positions[move],positions[pos2]=positions[pos2],positions[move]

        if positions ==  ['B', 'B', 'B', '-', 'G', 'G', 'G']:
            display_game(positions)
            print("You Win!")
            break            
if __name__ == "__main__":
    main()        