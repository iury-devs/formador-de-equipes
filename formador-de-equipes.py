import random

def criar_equipes(jogadores, num_equipes):
    random.shuffle(jogadores)  # Embaralha os jogadores

    tamanho_equipe = len(jogadores) // num_equipes
    equipes = [jogadores[i:i+tamanho_equipe] for i in range(0, len(jogadores), tamanho_equipe)]

    # Se o número de jogadores não for divisível pelo número de equipes,
    # distribui os jogadores restantes
    if len(jogadores) % num_equipes != 0:
        i = 0
        for jogador in jogadores[len(equipes) * tamanho_equipe:]:
            equipes[i % len(equipes)].append(jogador)
            i += 1

    return equipes

# Exemplo de jogadores
jogadores = []
quantidade_jogadores = int(input('Quantos jogadores você quer? '))
for indice in range(quantidade_jogadores):
    jogadores.append(input('Digite o nome do jogador: '))

# Número de equipes desejadas
num_equipes = 2
num_equipes = int(input('Quantas equipes você quer? '))
# Criar equipes
equipes = criar_equipes(jogadores, num_equipes)

# Imprimir as equipes
for i, equipe in enumerate(equipes, start=1):
    print(f"Equipe {i}: {equipe}")
