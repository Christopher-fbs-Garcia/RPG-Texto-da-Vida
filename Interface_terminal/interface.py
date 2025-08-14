import os
from ..PlayerFile.player_setting import my_player

class Interface:
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def logo():
        print("o============================================================o")
        print("|                         LIFE GAME                          |")
        print("o============================================================o")




    def memento_mori():
        print("o============================================================o")
        print("| Nesta vida, há coisas que não escolhemos e outras que sim. |")
        print("| Mas podemos definar que seremos.                           |")
        print("o============================================================o")

    
    def screen_skills():
        print("o============================================================o")
        print("|                   ESCOLHA 3 HABILIDADES                    |")
        print("o============================================================o")
        print("| [1] Exatas        | [2] Linguagem       |  [3] Luta        |")
        print("o===================+=====================+==================o")
        print("| [4] Cozinhar      | [5] Ser Maromba     |  [6] Ser social  |")
        print("o===================+=====================+==================o")
        print("| [7] Tecnologia    | [8] Religiosa       |  [9] Mentiroso   |")
        print("o============================================================o")

