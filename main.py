from replit import db
from lib.interface import *
from lib.dados import *
from time import sleep

'''
Programa destinado a cadastrar, ler e manipular os dados de alunos.
  - Menu interativo
  - Cadatro de alunos em um banco de dados
  - Leitura do banco de dados
  - Alteração dos dados
  - Explusão de alunos do banco de dados
'''


opcoes=["Ver Alunos", "Cadastrar Aluno", "Alterar Aluno",  "Expluir Aluno",  "Sair"]

while True:
  fcores('Cadastro de Alunos', fundo=True, cab=True)
  func_menu(opcoes)
  match leia_int('Opção'):
    case 1:
      fcores('Ver Alunos', 'verde', fundo=True, cab=True)
      func_lercadastro()
      sleep(1.5)
    case 2:
      fcores('Cadastra Aluno')
      func_cadastra()
      sleep(1.5)
    case 3:
      fcores('Alterar Aluno')
      func_alterar()
      sleep(1.5)
    case 4:
      fcores('Expluir Aluno', 'vermelho', fundo=True, cab=True)
      func_del()
      sleep(1.5)

    case 5:
      fcores('Saindo do sistema')
      sleep(1.5)
      fcores('Até logo')
      break
    case _:
      fcores('Erro! Opção inválida', 'vermelho')
      continue

fcores('Fim do programa', 'magenta')      