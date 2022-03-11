import contas
import enviarEmail
from contas import *

#@@@@@@@@@@ OBSERVAÇÃO essa função nunca termina então você terá que parar manualmente.@@@@@@@@

# Essa função é para iniciar - vai pegar todos os valores e ir printando um por um em nosso terminal: 
def mostrar_valores(self):
    nome_da_moeda = str(contas.nameinv(self))
    sigla_moeda = str(self.moeda[0:3].upper())
    dolar = float(self.usd_brl())
    crypto_reais = float(conversao(self))
    crypto_dolar = float(self.valor_da_crypto())
    investido = float(self.valor)
    moeda = float(self.quantidade)
    meu_moeda_rs = float(crypto_reais * moeda)
    sacar = valor_ganho(self)
    sacando = float(meu_moeda_rs * self.porcentagem)

    nova_cotacao = True
    print(f'\n\33[1;140m\033[1;34m {str(nome_da_moeda)} vale:\33[0m'
          f'\nDólares: ${crypto_dolar:,.2f}'
          f'\nReais: R${crypto_reais:,.2f}'
          f'\n___________________________________'
          f'\nMinha carteira {sigla_moeda}: {moeda:,.8f}'
          f'\nMinha carteira: {investido:,.2f}'
          f'\nCarteira atual: {meu_moeda_rs:,.2f}'
          f'\nCarteira Sacar: {sacando:,.2f} {sacar / investido * 100:,.2f}%'
          f'\n{sigla_moeda}:R$ {sacar:,.2f}'
          f'\nvalor do dolar $ {dolar:,.2f}\n')
    while True:
        valor_antigo = contas.conversao(self)
        valor_atual = float(contas.conversao(self))
        enviarEmail.ganhando_envia_email(self)
       

        if valor_atual > valor_antigo:
            print(f'\n\033[;1m\033[92m---> Subindo <---\n\033[0m'
                  f'\033[1;33mPreço de 1 {nome_da_moeda}:\033[0m\n'
                  f'Reais: $ {valor_atual:,.2f}\n')
            for o in lista:
                lucro = valor_ganho(o)
                mlucro = o.nome
                qtd = o.valor
                r3 = contas.quantidade_moeda_lucrar(o)
                if lucro > 0:
                    print(
                        f'Investimento {mlucro} Qtd: R$ {qtd} Lucro '
                        f'\033[92m{lucro:,.2f}\033[0m {r3} \033[92m{lucro / qtd * 100:,.2f} \033[0m'
                        f'\033[1;33m%\033[0m')
                else:
                    print(
                        f'Investimento {mlucro} Qtd: R$ {qtd} Lucro '
                        f'\033[91m{lucro:,.2f}\033[0m {r3} \033[91m{lucro / qtd * 100:,.2f} \033[0m'
                        f'\033[1;33m%\033[0m')
            mostrar_valores(self)

        elif valor_atual < valor_antigo:
            print(f'\n\033[;1m\033[91m---> Caindo <---\n\033[0m'
                  f'\033[1;33mPreço de 1 {nome_da_moeda}:\033[0m\n'
                  f'Dólares: $ {valor_atual:,.2f}\n'
                  f'Minha carteira: {investido:,.2f}'
                  f'\nCarteira atual: {sacando:,.2f}\n')
            for o in lista:
                lucro = valor_ganho(o)
                mlucro = o.nome
                qtd = o.valor
                r3 = contas.quantidade_moeda_lucrar(o)
                if lucro < 0:
                    print(
                        f'Investimento {mlucro} Qtd: R$ {qtd} Lucro '
                        f'\033[91m{lucro:,.2f}\033[0m {r3} \033[91m{lucro / qtd * 100:,.2f} \033[0m'
                        f'\033[1;33m%\033[0m')
                else:
                    print(
                        f'Investimento {mlucro} Qtd: R$ {qtd} Lucro '
                        f'\033[92m{lucro:,.2f}\033[0m {r3} \033[92m{lucro / qtd * 100:,.2f} \033[0m'
                        f'\033[1;33m%\033[0m')
            mostrar_valores(self)
            nova_cotacao = True
        else:
            if nova_cotacao:
                print('\n\033[1;33mAguardando nova cotação...\033[0m\n')
                nova_cotacao = False


mostrar_valores(lista[-1])
