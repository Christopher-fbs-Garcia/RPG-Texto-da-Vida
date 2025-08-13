import os


class Work:


    def skills():
        skills_player = []

        habilidades = [
            "Lógico-Matemática",  # 1
            "Interpessoal",  # 2
            "Naturalista",  # 3
            "Musical", # 4
            "Cinestésica Corporal", # 5
            "Linguística", # 6
            "Tecnologia", # 7
            "Religioso", # 8
            "Negócios" # 9
        ]

        while len(skills_player) < 3:
            os.system("cls" if os.name == "nt" else "clear")

            Work.screen_skills()
            print("Escolha suas habilidades:")

            try:
                choice_skill = int(input("Escolha: "))

                if choice_skill < 1 or choice_skill > len(habilidades):
                    print("[ERRO] Escolha inválida!")
                    input("Pressione Enter para continuar...")
                    continue

                habilidade_escolhida = habilidades[choice_skill - 1]

                if habilidade_escolhida in skills_player:
                    print("[ERRO] Você já possui essa habilidade!")
                    input("Pressione Enter para continuar...")
                    continue

                skills_player.append(habilidade_escolhida)
                print(f"Habilidade '{habilidade_escolhida}' adicionada!")
                input("Pressione Enter para continuar...")

            except ValueError:
                print("[ERRO] Digite um número válido!")
                input("Pressione Enter para continuar...")

        return skills_player
    

    
    def screen_skills():
        print("o======================================================================o")
        print("|                         ESCOLHA 3 HABILIDADES                        |")
        print("o======================================================================o")
        print("| [1] Lógico-Matemática | [2] Interpessoal          | [3] Naturalista  |")
        print("o=======================+===========================+==================o")
        print("| [4] Musical           | [5] Cinestésica Corporal  | [6] Linguística  |")
        print("o=======================+===========================+==================o")
        print("| [7] Tecnologia        | [8] Religioso             | [9] Negócios     |")
        print("o======================================================================o")