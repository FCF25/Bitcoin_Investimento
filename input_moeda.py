#Colocar novos investimentos
from moeda import Moeda

lista = []

# neste campo você deverá colocar sua  informações exemplo abaixo:
#lista.append(Moeda('Nome que você queira dar para seu investimento', 'SIGLA do bitcoin: BTCUSDT', 'quantidade de biticoin', 'Porcentagem que fica para corretora', "valor desejado para sacar"))
lista.append(Moeda('bitcoin1',  'BTCUSDT', 0.00701548, 1639.30, 0.98, 0.00))
lista.append(Moeda('bitcoin2',  'BTCUSDT', 0.00002162, 5.00   , 0.98, 0.00))
lista.append(Moeda('bitcoin3',  'BTCUSDT', 0.00433097, 1000.00, 0.98, 0.00))
lista.append(Moeda('bitcoin4',  'BTCUSDT', 0.00003650, 8.33   , 0.98, 0.00))
lista.append(Moeda('bitcoin5',  'BTCUSDT', 0.00003505, 8.00   , 0.98, 0.00))



listaInvestBTC =[]
listaQtdBTC = []

listaInvestETH =[]
listaQtdETH = []

# Fazendo a soma de valores e quantidade e adicionando ao final da lista.
def total_lista():
    for o in lista:
        if o.moeda == "BTCUSDT":
            listaInvestBTC.append(o.valor)
            listaQtdBTC.append(o.quantidade)
        else:
            listaInvestETH.append(o.valor)
            listaQtdETH.append(o.quantidade)


    somaInvestBTC = sum(listaInvestBTC)
    somaBtc= sum(listaQtdBTC)

    somaInvestETH =  sum(listaInvestETH)
    somaETH = sum(listaQtdETH)

    
    return  lista.append(Moeda('bitcoin_todos', 'BTCUSDT', somaBtc, somaInvestBTC, 0.98, 5.00)) 

total_lista()
    













# # Estruturando ainda.
# def investimento():
#     nome = str(input('Escreva o nome do seu investimento\n'))
#     moeda = str(input('Escreva o nome da sua Crypto Moeda ex: Ethereum = ETHUSDT - BITCOIN = BTCUSDT\n')).upper()
#     quantidade = float(input('Quantidade adquirida? Sempre utilizando ponto ao invés de virgula\n'))
#     valor = float(input('Valor pago?\n'))
#     porcentagem = float(input('Porcentagem da sua corretora\n'))
#     sacar = float(input('Valor para quando sua moeda estiver dando lucro para você sacar?\n'))
#     classe = 'Moeda'
#     resultado = lista.append(f'{classe}({nome},{moeda},{quantidade},{valor},{porcentagem},{sacar})')
#     print(type(lista))
#     salvar('Investimentos', lista)
#     return resultado
#
# #Funcionando
# def salvar(filename, info):
#     file = open('{}.txt'.format(filename),'a', encoding='UTF-8')
#     file.write(f'{info}\n')
#     file.close()
#
# # Funcionando ler.
# def ler(filename):
#     file = open('{}.txt'.format(filename), 'r', encoding='UTF-8')
#     print(file.read(10))
#     return file.read()


# investimento()
# ler('investimentos')
# salvar('investimentos',investimento)


#print(Moeda.valor_da_crypto(lista[0]))
# Moeda.nome_moeda(lista[0])