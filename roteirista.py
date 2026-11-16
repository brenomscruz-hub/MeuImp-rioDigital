def gerar_roteiro(nicho):
    print(f"--- Gerando Roteiro para o nicho: {nicho} ---")
    roteiro = f"""
    [INTRO]: Voce sabia que {nicho} esta mudando o mundo agora?
    [DESENVOLVIMENTO]: Pouca gente sabe, mas isso vai afetar seu bolso nos proximos meses.
    [FECHAMENTO]: Quer saber mais? Se inscreva no canal e comente 'IA'.
    """
    with open("roteiro_final.txt", "w", encoding="utf-8") as f:
        f.write(roteiro)
    print("Roteiro salvo em 'roteiro_final.txt'.")

if __name__ == "__main__":
    nicho_escolhido = input("Qual o nicho do video de hoje? ")
    gerar_roteiro(nicho_escolhido)
