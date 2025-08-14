from .player_setting import my_player

class Work:
    def about_professional(my_player):
        professionals_player = []
        final_professionals = []

        professionals = {
            "Lógico-Matemática": {"Engenheiro": 0, "Físico": 0, "Mecânico": 0},
            "Interpessoal": {"Político": 0, "Jornalista": 0, "Professor": 0},
            "Naturalista": {"Biólogo": 0, "Geólogo": 0, "Veterinário": 0},
            "Musical": {"Cantor": 0, "Violinista": 0, "Pianista": 0},
            "Cinestésica Corporal": {"Treinador": 0, "Jogador de basquete": 0, "Dançarino": 0},
            "Linguística": {"Dublador": 0, "Escritor": 0, "Palestrante": 0},
            "Tecnologia": {"Hacker": 0, "Programador Java": 0, "Técnico de TI": 0},
            "Religioso": {"Padre": 0, "Teólogo": 0, "Papa": 0},
            "Negócios": {"Empreendedor": 0, "Economista": 0}
        }
        
        for key, value in professionals.items():
            
            for skill in my_player.skills: 

                if key == skill:
                    professionals_player.append((key, value))
        
        for pp in professionals_player:
            for p in pp:
                final_professionals.append(p)
        
        return professionals_player