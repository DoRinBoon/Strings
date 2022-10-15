# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Assignment: Strings

#Part1
from unicodedata import name

player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = (f"{player_0} {goal_0}, {player_1} {goal_1}")
report = (f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute")
print (report)

#Part2
player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name = player[player.find(' '):]
first_name_len = len(first_name)
 
last_name_len = len(last_name)

name_short = (player[0] + '.' + last_name)
print (name_short)

yell = first_name + '! '
chant = yell *(first_name_len)
chant = chant.rstrip(chant[-1])
print (chant)

good_chant = (chant[-1] != ' ')
print (good_chant)
