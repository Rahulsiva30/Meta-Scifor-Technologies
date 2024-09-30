"""In a school, a football competition is going to be held. The sports captain needs to create a list of the
players with their heights. According to the rule, only those students can participate in the competition
who have a height greater than 167cm. To make things easier write a python program. Create a list of
tuples with the name of the player and their height in cm. Note: while taking the input from the users,
dont include the players whose height is less than 167cm. ( Use continue statement )
● Sample list: [ (“Chris” , 170) , (“Aditya” , 182) , (“Chirag” , 176 ) ]

players_name_list=[]
players_height_list=[]
Total_players_list=()
players_name_total=int(input("Enter the total players: "))

for players in range(players_name_total):
    players_name = input(f"Enter the name of player {players+1}: ")
    players_height = int(input(f"Enter the height of player {players+1}: "))
    players_name_list.append(players_name)
    players_height_list.append(players_height)
    try:
          if players_height > 167:
              Total_players_list=tuple(zip(players_name_list,players_height_list)) 
          elif players_height < 167:   
               print()       
    except ValueError:
         print("Please enter a valid number for height.")

print(Total_players_list)"""

name="In a school, a football competition is going to be held. The sports captain needs to create a list of the players with their heights. \
According to the rule, only those students can participate in the competition\
who have a height greater than 167cm. To make things easier write a python program. Create a list of\
tuples with the name of the player and their height in cm. Note: while taking the input from the users,\
dont include the players whose height is less than 167cm. ( Use continue statement )\
● Sample list: [ (“Chris” , 170) , (“Aditya” , 182) , (“Chirag” , 176 ) ]"




