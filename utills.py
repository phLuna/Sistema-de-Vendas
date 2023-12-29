import datetime, re, sqlalchemy

##Arrumar a formatação.
def formatar_cpf(str):
    """Esta função recebe um cpf, e o formata."""
    a = re.sub('[^0-9]', '', str)
    cpf_formatado = f"{a[0]}{a[1]}{a[2]}.{a[3]}{a[4]}{a[5]}.{a[6]}{a[7]}{a[8]}-{a[9]}{a[10]}"
    return cpf_formatado

def criar_pessoa():
    """Esta função cria pessoas."""
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    cpf_rasc = input('CPF: ')
    info = 0
    for n in cpf_rasc:
        if n not in '0123456789':
            info += 1
    if info >= 1:
        input('Erro! Um ou mais dígitos foram inseridos errados. Tente novamente: ')
    if len(cpf_rasc) > 11:
        cpf = input('Erro! Tamanho excedido. Tente novamente: ')
    else:
        cpf = formatar_cpf(cpf_rasc)
        create_at: datetime.date.today()
        pessoa = {'nome': nome, 'telefone': telefone, 'cpf': cpf, 'create_at': create_at}
        return pessoa

a = criar_pessoa()
print(a)