from PlayerFile.player_setting import Player
from PlayerFile.player_setting import Skill
from PlayerFile.work_player import Work


my_player = Player()

my_player.name = input("Qual é o seu nome: ")



my_player.skills = Skill.skills()


def about_professional():
    professionals_player = []
    final_professionals = []

    professionals = {
        "Lógico-Matemática" : ("Engenheiro", "Físico", "Mecânico"),  # 1
        "Interpessoal" : ("político", "jornalista", "Professor"),  # 2
        "Naturalista" : ("Biológo", "Geólogo", "Veterinário."),  # 3
        "Musical" : ("Cantor", "Violinista", "Pianista"), # 4
        "Cinestésica Corporal" : ("Treinador", "Jogador de basquete", "Dançarino"), # 5
        "Linguística" : ("Dublador", "Escrito", "Palestrantes"), # 6
        "Tecnologia" : ("Hacker", "Programador Java", ""), # 7
        "Religioso" : ("Padre", "Teólogo", "Papa"), # 8
        "Negócios" : ("Empreededor", "Ecnonomista") # 9
    }  

    for key, value in professionals.items():
        for skill in my_player.skills:

            if key == skill:
                professionals_player.append(value)
    
    for pp in professionals_player:
        for p in pp:
            final_professionals.append(p)
    
    return final_professionals

    

print(f"Meus parabens {my_player.name} sua skills vai ser {" | ".join(my_player.skills)}")

print(Work.about_professional())