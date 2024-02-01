from replit import db
from lib.interface import *
from time import sleep


def func_lercadastro():
  dados=db.keys()
  print(f'{"NOME":<17}{"NOTA"}')
  for aluno in dados:
    print(f'{aluno:<15} {db[aluno]:>4}')


def func_cadastra():
  while True:
    try:
      nome=str(input('Nome (Sair para retornar ao menu principal): ')).strip().capitalize()
    except:
      nome='Dado não digitado'
    finally:
      if nome in db.keys():
        print(f'{nome} já existenta, não poderá ser cadastrado')
      else:
        break

  if nome != 'Sair':
    nota= leia_int('Nota: ')
    db[nome]=nota
    fcores(f'{nome} cadastrado com sucesso', 'verde')
  else:
    print('Retornando ao menu principal')
    sleep(1.5)

def func_alterar():
  dados=db.keys()
  print(f'{"NOME":<17}{"NOTA"}')
  for aluno in dados:
    print(f'{aluno:<15} {db[aluno]:>4}')

  print('Qual aluno deseja alterar?')
  alt = str(input('(Sair para retornar ao menu principal): ')).strip().capitalize()
  if alt == 'Sair':
    print('retornando ao menu principal.')

  del db[alt]
  nome=str(input('Novo Nome (Sair para retornar ao menu principal): ')).strip().capitalize()

  if alt != 'Sair':
    nota= leia_int('Nota: ')
    db[nome]=nota
    fcores(f'Alterado com sucesso', 'verde')
  else:
    print('Retornando ao menu principal')


def func_del():
  #Lendo Cadastro
  dados=db.keys()
  print(f'{"NOME":<17}{"NOTA"}')
  for aluno in dados:
    print(f'{aluno:<15} {db[aluno]:>4}')

  print('Qual aluno deseja excluir?')
  ex = str(input('(Sair para retornar ao menu principal): ')).strip().capitalize()
  if ex == 'Sair':
    print('Retornando ao menu principal')
  else:
    try:
      del db[ex]
      fcores('Excluído com sucesso.', 'vermelho')
    except:
      print('Aluno não encontrado')
    finally:
      print('Retornando ao menu principal.')
    
    
  
