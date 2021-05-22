###
## Exercicios
###


# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.


def define_default_city(state):
    ''' Define a capital do estado de origem como city_origin para um professor existente no arquivo. Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.

    Keyword arguments:
        state -- O estado de origem do professor
    '''
    import csv

    with open('capitais-BR.csv', encoding='utf-8') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=';')

        csv_reader.__next__()

        for row in csv_reader:
            if state == row[0]:
                return True
        else:
            return False


professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

resultado = define_default_city(professor1['state_origin'])
print(resultado)



# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente. Ela deve executar sem erro mesmo que alguns dados estejam faltando.


# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro. O algoritmo precisa ser eficiente, nesse caso especifico a melhor a melhor complexidade que pode ser acancada é linear. Algoritmos de complexidade quadratica, cubica, fatorial, etc. não sao considerados como eficientes pois a complexidade linear eh garantida. Como regra geral, se seu algoritmo demorar mais do que alguns segundos, ele, provavelmente, nao eh linear.
