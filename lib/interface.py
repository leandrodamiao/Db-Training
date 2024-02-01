def fcores(text='', cor='', fundo=False, cab=False):
  '''
  -> Função que adiciona cores aos textos.
  :param arg: Texto que será editado
  :param cor: Cor adicionada ao texto
  :param fundo: Padrão False, se verdadeiro altera as cores de fundo
  :param cab: Cabeçalho (padrão False) printa uma linha superior, inferior e centraliza o texto 
  :return: 0
  '''
  if fundo: 
    cores = {
      '' : f'\033[m{text}\033[m',
      'branco' : f'\033[40m{text}\033[m',
      'vermelho' : f'\033[41m{text}\033[m',
      'verde' : f'\033[42m{text}\033[m',
      'amarelo': f'\033[43m{text}\033[m',
      'azul': f'\033[44m{text}\033[m',
      'magenta': f'\043[35m{text}\033[m',
      'ciano': f'\033[46n{text}\033[m',
      'cinza' : f'\033[47m{text}\033[m'
    }
  else:
    cores = {
      '' : f'\033[m{text}\033[m',
      'branco' : f'\033[30m{text}\033[m',
      'vermelho' : f'\033[31m{text}\033[m',
      'verde' : f'\033[32m{text}\033[m',
      'amarelo': f'\033[33m{text}\033[m',
      'azul': f'\033[34m{text}\033[m',
      'magenta': f'\033[35m{text}\033[m',
      'ciano': f'\033[36n{text}\033[m',
      'cinza' : f'\033[37m{text}\033[m'
    }

  if cab:
    fcores(f'{"-"*25}\n{text.center(25)}\n{"-"*25}', cor, fundo)
  else:
    print(cores[cor])

def func_menu(opcoes):
  for i, op in enumerate(opcoes):
    print(f'\033[33m{i+1}\033[m - \033[34m{op}\033[m')
  print('-'*25)


def leia_int(text):
  '''
  -> Le um dado e aceita apenas números inteiros
  :param text: Texto exibido 
  '''
  while True:
    try:
      n=int(input(text))
      return n
    except:
      fcores('Erro! Favor digite apenas números inteiros.', 'vermelho')


