import random
# ASCII Art for "Rock, Paper, Scissors"


rock_paper_scissors_art = r'''
U _____ u  _        ____   U  ___ u  __  __  U _____ u                  _   _           ____      _      __  __  U _____ u 
 __        __\| ___"|/ |"|    U /"___|   \/"_ \/U|' \/ '|u\| ___"|/         ___     | \ |"|       U /"___|uU  /"\  uU|' \/ '|u\| ___"|/ 
 \"\      /"/ |  _|" U | | u  \| | u     | | | |\| |\/| |/ |  _|"          |_"_|   <|  \| |>      \| |  _ / \/ _ \/ \| |\/| |/ |  _|"   
 /\ \ /\ / /\ | |___  \| |/__  | |/__.-,_| |_| | | |  | |  | |___           | |    U| |\  |u       | |_| |  / ___ \  | |  | |  | |___   
U  \ V  V /  U|_____|  |_____|  \____|\_)-\___/  |_|  |_|  |_____|        U/| |\u   |_| \_|         \____| /_/   \_\ |_|  |_|  |_____|  
.-,_\ /\ /_,-.<<   >>  //  \\  _// \\      \\   <<,-,,-.   <<   >>     .-,_|___|_,-.||   \\,-.      _)(|_   \\    >><<,-,,-.   <<   >>  
 \_)-'  '-(_/(__) (__)(_")("_)(__)(__)    (__)   (./  \.) (__) (__)     \_)-' '-(_/ (_")  (_/      (__)__) (__)  (__)(./  \.) (__) (__)
'''
print(rock_paper_scissors_art)


















rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]









# user_choice=input("choose 1 for rock 0 for paper and 2 for sciessor?")
# computer_choice=random.randint(0,2)
# if user_choice==computer_choice:
#     print("the match is draw")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer choose:")
print(game_images[computer_choice])

if user_choice==computer_choice:
     print("the match is draw")

elif user_choice==0 and computer_choice==1:
     print("you loose the computer choosen paper and you choosen rock")
elif user_choice==1 and computer_choice==0:
     print("you won the computer choosen rock and you choosen paper")
elif user_choice==2 and computer_choice==0:
     print("you loose the computer choosen rock and you choosen scissor")
elif user_choice==0 and computer_choice==2:
     print("you won the computer choosen scissor and you choosen rock")
elif user_choice==1 and computer_choice==2:
     print("you loose the computer choosen scissor and you choosen paper")
elif user_choice==2 and computer_choice==1:
     print("you won the computer choosen paper and you choosen scissor")
     
     


