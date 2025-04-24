import random
import time
from colorama import init, Fore

init(autoreset=True)

def print_delay(msg, delay=1):
    print(Fore.YELLOW + msg)
    time.sleep(delay)

def mostrar_ultimo_jogo():
    print_delay("\nÚltimo jogo da FURIA:")
    print("FURIA 2 x 1 MIBR - ESL Pro League")
    print("Mapa 1: Mirage - 16x12")
    print("Mapa 2: Inferno - 14x16")
    print("Mapa 3: Nuke - 16x10")

def mostrar_jogadores():
    jogadores = {
        "KSCERATO": "Rifler, conhecido pela mira absurda e clutchs insanos.",
        "yuurih": "Rifler tático, joga com consistência e inteligência.",
        "arT": "IGL agressivo, famoso por suas jogadas malucas.",
        "chelo": "Novo reforço, estilo explosivo.",
        "drop": "Jogador de suporte, sempre joga pro time."
    }
    for nome, desc in jogadores.items():
        print_delay(f"{nome}: {desc}", 0.5)

def iniciar_quiz():
    perguntas = [
        ("Qual mapa é conhecido como casa da FURIA?", "nuke"),
        ("Quem é o IGL da FURIA?", "art"),
        ("Quantos jogadores tem um time de CS?", "5")
    ]
    score = 0
    for pergunta, resposta in perguntas:
        resp = input(pergunta + " ").strip().lower()
        if resp == resposta:
            print(Fore.GREEN + "Certa resposta!")
            score += 1
        else:
            print(Fore.RED + f"Errou! A resposta certa era '{resposta}'.")
    print(Fore.CYAN + f"Você acertou {score}/{len(perguntas)} perguntas!")

def mostrar_ranking():
    print_delay("\nRanking atual ESL (top 5):")
    ranking = ["1. FaZe", "2. Vitality", "3. G2", "4. NAVI", "5. FURIA"]
    for time in ranking:
        print_delay(time, 0.3)

def giria_do_cs():
    g = random.choice([
        ("Eco", "Rodada onde o time economiza dinheiro e não compra armas."),
        ("Ace", "Quando um jogador elimina todos os 5 adversários."),
        ("Varada", "Matar o inimigo atirando através da parede."),
        ("Lurker", "Jogador que joga separado para pegar o flanco do time adversário."),
        ("Clutch", "Situação onde um jogador sozinho tenta vencer a rodada contra dois ou mais adversários."),
        ("Entry", "Jogador responsável por abrir o bombsite, entrando primeiro."),
        ("Spray control", "Controle do recuo da arma durante disparo contínuo."),
        ("Stack", "Quando o time defende com vários jogadores no mesmo bombsite."),
        ("Save", "Quando o jogador decide não lutar e guardar o armamento para a próxima rodada.")
    ])
    print_delay(f"\nGíria: {g[0]}\nSignificado: {g[1]}")

def curiosidade():
    curiosidades = [
        "A FURIA foi o primeiro time brasileiro a investir em uma gaming house nos EUA.",
        "O arT é conhecido por fazer rush no meio da Mirage até mesmo de AWP.",
        "KSCERATO já foi considerado o melhor jogador brasileiro em atividade.",
        "A FURIA tem uma filosofia chamada 'Furia Culture', focada em disciplina e desenvolvimento pessoal.",
        "A lineup atual da FURIA mistura experiência com sangue novo do cenário nacional.",
        "A torcida da FURIA é uma das mais engajadas da América Latina no CS."
    ]
    print_delay("\nCuriosidade aleatória:")
    print(random.choice(curiosidades))

def main():
    while True:
        print(Fore.MAGENTA + "\n=== FALA, FURIOSO! 🔥 ===")
        print("1. Último jogo da FURIA")
        print("2. Conheça os jogadores")
        print("3. Quiz de fã")
        print("4. Ranking atual")
        print("5. Gírias do CS")
        print("6. Curiosidades")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1': mostrar_ultimo_jogo()
        elif opcao == '2': mostrar_jogadores()
        elif opcao == '3': iniciar_quiz()
        elif opcao == '4': mostrar_ranking()
        elif opcao == '5': giria_do_cs()
        elif opcao == '6': curiosidade()
        elif opcao == '7':
            print(Fore.CYAN + "Valeu, FURIOSO! Até a próxima 🔥")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente de novo.")

if __name__ == '__main__':
    main()
