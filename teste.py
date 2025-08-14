


skills_player = ["Interpessoal", "Musical", "Negócios"]

def about_professional(skills_player):
    professionals_player = []


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

    for k, v in professionals.items():
        for sp in skills_player:

            if sp is k:
                professionals_player.append(v)

    return professionals_player

professionals_player = about_professional(skills_player)


a = []
for pp in professionals_player:
    for p in pp:
        a.append(p)
print(a)
