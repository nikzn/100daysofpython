print('''''               ***********************
               *********************************
           *******   *     *       *    *    *******
        *******   ***      **     **     ***   *******
      ******   *****       *********      *****    *****
    ******  ********       *********       ******    *****
   ****   **********       *********       *********   *****
  ****  **************    ***********     ************   ****
 ****  *************************************************  ****
****  ***************************************************  ****
****  ****************************************************  ****
****  ****************************************************  ****
 ****  ***************************************************  ****
  ****  *******     ****  ***********  ****     *********  ****
   ****   *****      *      *******      *      ********  ****
    *****   ****             *****             ******   *****
      *****   **              ***              **    ******
       ******   *              *              *   *******
         *******                                *******
            ********                         *******
               *********************************
                    ***********************
''')

print("WELCOME TO BATCAVE")
print("Your Mission is to find the BAT MOBILE")

direction = input("Where do you want to go type 'Left' to go to LEFT and 'Right' to go to RIGHT ")

if direction.lower() == 'right':
    action = input("You Reached at Sea. if you want to wait type 'Wait' or you want to swim Type 'swim'")
    if action.lower() == 'wait':
        door = input("Select a door? 'GREEN','YELLOW','BLUE' ")
        if door.lower() == 'green':
            print("You Win!!")
        else:
            print("GAME OVER !")
    else:
        print('GAME OVER !')
else:
    print('GAME OVER !!!')
