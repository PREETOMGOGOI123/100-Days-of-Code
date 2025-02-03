print("""            ....
                      .: :..:::::'
                   ..:.::''''  '''     .. . .
                 .':: ::''  .. ..   .::'' '''
                  ':::' .::.'::  .'..::::::.
               ..:.::::: '.. :.'.:'''
         ...:'''  '':'::':'   ''
        :^ ^  'o>   .:'''
        :..'        '.
         '''''::    ':             .........
              :     :.       ...::''' ' ' '''::.
            .::     ':::.:':'''''            :::':.
           .::'                             :::
           ::'                              ::. ...::.
          .::'                        .      '''.' . :.
          '::.                       ::... .  .'.''':::.
           ':.                   ....:::::':::::.    ':::..
           .:'         .:'.:.'::::::' '        ':::..  ':::::.
      ....:::::..     .:::::::'' '                 '':.    '':'
    .':.:.:::::::'. ...:: ''
  .'.''          .':'::'  
.::'          .''::
              ' ':':'.. .
                     '''.'""")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("left or right?\n")
if direction != "left":
    print("Fall into a hole.\nGame Over.")
else:
    motion = input("swim or wait?\n")
    if motion != "wait":
        print("Attacked by trout.\nGame Over.")
    else:
        door = input("Which door? blue/red/yellow\n")
        if door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")