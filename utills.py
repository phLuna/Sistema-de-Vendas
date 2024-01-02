import re, sqlalchemy, validate_docbr
from datetime import datetime


def inserir_cpf() -> str:
    cpf_rasc = input('CPF: ')
    info = 0
    for n in cpf_rasc:
        if n not in '0123456789':
            info += 1
    if info >= 1:
        while True:
            info = 0
            cpf_rasc = input('Erro! Um ou mais dígitos foram inseridos errados. Tente novamente: ')
            if info == 0:
                break
    if len(cpf_rasc) > 11:
        while True:
            cpf_rasc = input('Erro! Tamanho excedido. Tente novamente: ')
            if len(cpf_rasc) < 12:
                break
    cpf = formatar_cpf(cpf_rasc)
    return cpf

#Arrumar.
def validar_cpf(cpf: str) -> str:
    """Esta função valida cpf's."""
    if validate_docbr.CPF.validate(cpf):
      return "Válido"
    else:
      return "Inválido"

#Arrumar a validação de CPF.
def formatar_cpf(str: str) -> str:
    """Esta função recebe um cpf, e o formata."""
    a = re.sub('[^0-9]', '', str)
    #validade = validar_cpf(a).upper()
    #if validade == 'INVÁLIDO':
    #    while True:
    #        print('CPF inválido! Tente novamente.')
    #        cpf = inserir_cpf()
    cpf_formatado = f"{a[0]}{a[1]}{a[2]}.{a[3]}{a[4]}{a[5]}.{a[6]}{a[7]}{a[8]}-{a[9]}{a[10]}"
    return cpf_formatado

#Arrumar a formatação do Create At.
def criar_pessoa() -> dict:
    """Esta função cria pessoas."""
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    cpf = inserir_cpf()
    create_at = datetime.now().date()
    pessoa = {'nome': nome, 'telefone': telefone, 'cpf': cpf, 'Create At': create_at}
    return pessoa

a = criar_pessoa()
print(a)