from PlayerFile.player_setting import Player
from PlayerFile.player_setting import Work


my_player = Player()



my_player.name = input("Qual é o seu nome: ")

my_player.skills = Work.skills()

print(f"Meus parabens {my_player.name} sua skills vai ser {" | ".join(my_player.skills)}")