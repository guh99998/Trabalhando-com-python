def metodo1(nome, sobrenome):
    print(nome, sobrenome)

# metodo1('alberto', 'frigatto')
# metodo1(nome='alberto', sobrenome='frigatto')

def metodo2(nome, idade=18):
    print(nome, idade)

# metodo2('alberto')

def multiplicacao(*numeros):
    resultado = 1

    for n in numeros:
        resultado *= n

    print(resultado)

# multiplicacao(1, 2, 4, 5)

def metodo3(**parametros):
    print(parametros)

# metodo3(nome='jubileu', idade=78)

def metodo4(nome, sobrenome, /, idade):
    print(nome, sobrenome, idade)

# metodo4('alberto', 'ferreira', 20)
# metodo4('alberto', 'ferreira', idade=20)

def metodo5(nome, *, idade, cpf):
    print(nome, idade, cpf)

# metodo5('alberto', idade=18, cpf='123')
