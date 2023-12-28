import datetime
import re

def formatar_cpf(str):
    """Esta função recebe um cpf, e o formata."""
    cpf_limpo = re.sub('[^0-9]', '', str)
    a = list(cpf_limpo)
    cpf_formatado = f'{a[0], a[1], a[2]}.{a[3], a[4], a[5]}.{a[6], a[7], a[8]}-{a[9], a[10]}'
    return cpf_formatado

def criar_pessoa():
    """Esta função cria pessoas."""
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    cpf = input('CPF: ')
    create_at: datetime.date.today()
    pessoa = {'nome': nome, 'telefone': telefone, 'cpf': cpf, 'create_at': create_at}
    return pessoa