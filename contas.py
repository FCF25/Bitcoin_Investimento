from moeda import Moeda
from input_moeda import lista, total_lista



# recebe os dados da Crypto moeda e multiplica pelo valor do dolar.
def conversao(self):
        
        reais = float(Moeda.usd_brl())
        crypto = Moeda.valor_da_crypto(self)
        valor = reais * crypto
        return valor

# Verifica os valores e nos informa quanto esta sendo o nosso lucro.
def valor_ganho(self):
    investido = self.valor  
    moeda = self.quantidade  
    moeda_reais = conversao(self) 
    total_atual_menos_porcentagem = moeda_reais * moeda * self.porcentagem   
    lucro = total_atual_menos_porcentagem - investido  
    return lucro

#informa o valor investido -  usado para o email
def inv(self):
    investido = self.valor
    return investido
#informa o nome do investimento - usado para o email
def nameinv(self):
    nome = self.nome
    return nome


#Pega todos os valores unitário dos lucros => Utilizar para quando for enviar o email.
def lucro_unitario():
    lista_de_lucro = []
    for i, o in enumerate(lista):
        if float(valor_ganho(o)) > o.sacar:
            print(valor_ganho(o),o.nome)
            lista_de_lucro.append(i)
    return lista_de_lucro



# Verifica o valor que a moeda tem que ter para conseguirmos ter lucro.
def quantidade_moeda_lucrar(self):                           
    minha_moeda = self.quantidade             
    pago = self.valor                         
    bitcoin = 1                               
    x1 = bitcoin * pago / minha_moeda         
    x2 = x1 / bitcoin                         
    valor_para_começar_a_lucrar = f'{x2:,.2f}'
    return valor_para_começar_a_lucrar        


