import json
import urllib.request


class Moeda:
    def __init__(self, nome, moeda, quantidade, valor, porcentagem, sacar):
        self.nome = nome
        self.moeda = moeda
        self.quantidade = float(quantidade)
        self.valor = valor
        self.porcentagem = porcentagem
        self.sacar = sacar

# Vai verificar as siglas colocadas e vai converter para o nome da crypto moeda.
    def nome_moeda(self):
        sigla_destino = self.moeda  # # Ethereum = ETHUSDT - BITCOIN = BTCUSDT
        if sigla_destino == 'BTCUSDT':
            sigla ='Biticoin'
        else:
            sigla = 'Ethereum'
        moeda_escolhida = f'{sigla}'
        return moeda_escolhida


# Irá acessar a api da Binance para trazer o valor atual da moeda escolhida.
    def valor_da_crypto(self):
        sigla_destino = self.moeda  
        try:
            url = "https://api.binance.com/api/v3/ticker/price"
            with urllib.request.urlopen(url) as url:
                response = url.read()
                data = json.loads(response.decode('utf-8'))
                i = 0
                while i < len(data):
                    i += 1
                    vlr = data[i]['symbol']
                    if sigla_destino.upper() == vlr:
                        index = i
                        valor = float(data[index]['price'])
                        return valor


        except urllib.error.HTTPError:
            print('URL Não esta funcionando!')

# Vai acessar a Api da AWESOMEAPI e vai nos trazer a cotação do dolar atual.
    @staticmethod
    def usd_brl():
        try:
            url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
            with urllib.request.urlopen(url) as url:
                response = url.read()
                data = json.loads(response.decode('utf-8'))
                valor = float(data['USDBRL']['bid'])
                dolar = (f'{valor:,.2f}')
                return dolar
        except urllib.error.HTTPError:
            print('URL Não esta funcionando!!')

