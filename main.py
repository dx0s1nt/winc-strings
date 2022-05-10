# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from urllib.request import CacheFTPHandler


eerste_scoorder="Ruud Gullit"
tweede_scoorder="Marco van Basten"
goal_0=32
goal_1=54
scorers=eerste_scoorder+' '+str(goal_0)+', '+tweede_scoorder+' '+str(goal_1)
report=f"{eerste_scoorder} scored in the {goal_0}nd minute\n{tweede_scoorder} scored in the {goal_1}th minute"
player="Jan Wouters"
first_name=player[0:player.find(' ')]
last_name_len=len(player[player.find(' ')+1:])
name_short=player[0]+'. '+player[len(player)-last_name_len:]
#voornaam moet minimaal 1 letter bevatten
chant=f"{first_name}!"+ f" {first_name}!" * (len(first_name)-1)
good_chant=(chant[-1]!=' ')