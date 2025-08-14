from PlayerFile.player_setting import Player
from PlayerFile.player_setting import Skill
from PlayerFile.work_player import Work
# from Interface_terminal.interface import Interface

my_player = Player()

my_player.name = input("Qual é o seu nome: ")

my_player.skills = Skill.skills()