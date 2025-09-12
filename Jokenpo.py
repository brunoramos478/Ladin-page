import random

jogadas = ['pedra', 'papel', 'tesoura'] # Lista de jogadas possíveis

# Função para o jogador fazer sua escolha
def jogador_escolhe(): 
 global jogador_joga
 
 lista = [] 

 while True and len(lista) < 3:
   jogador_joga = input('Escolha pedra, papel, ou tesoura: ').lower()

   if jogador_joga not in jogadas:
      print('Jogada inválida. Tente novamente.') # Mensagem de erro para jogada inválida
      continue

   elif jogador_joga in jogadas:
      lista.append(jogador_joga) # Adiciona a jogada válida à lista

 return lista

# Pc faz sua escolha aleatória
def play_computer():
  global pc_joga
  pc_sorteia = [] #lista para armazenar as jogadas do pc

  for i in range(3):
    pc_joga = random.choice(jogadas)
    pc_sorteia.append(pc_joga)
  return pc_sorteia


def derrota(jogador_joga, pc_joga): # Cenario onde o jogador perde

  msg = 'Você perdeu!'

  if jogador_joga == 'pedra' and pc_joga == 'papel':
    return msg
  elif jogador_joga == 'papel' and pc_joga == 'tesoura':
    return msg
  elif jogador_joga == 'tesoura' and pc_joga == 'pedra':
    return msg
  

def vitoria(jogador_joga, pc_joga): # Cenario onde o jogador vence

  msg = 'Você ganhou!'

  if jogador_joga == 'pedra' and pc_joga == 'tesoura':
    return msg
  elif jogador_joga == 'papel' and pc_joga == 'pedra':
    return msg
  elif jogador_joga == 'tesoura' and pc_joga == 'papel':
    return msg
  

def empate(jogador_joga, pc_joga): # Cenario onde há empate

  msg = 'Empate!'
  if jogador_joga == pc_joga:
    return msg    
  

def resultado(jogador_joga, pc_joga): # Função que exibe o resultado da rodada

  if derrota(jogador_joga, pc_joga):
    print(derrota(jogador_joga, pc_joga))

  elif vitoria(jogador_joga, pc_joga):
    print(vitoria(jogador_joga, pc_joga))

  elif empate(jogador_joga, pc_joga):
    print(empate(jogador_joga, pc_joga))

# Início do jogo
print('Bem-vindo ao Jokenpo! Você jogará 3 rodadas contra o computador.')

jogador_joga = jogador_escolhe()
pc_joga = play_computer()

for i in range(3):
  resultado(jogador_joga[i], pc_joga[i])
  


   