#%%
#imports
import requests
import json

# definindo a url da API a ser consultada
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

# utilizando o get do requests vamos armazenar o resultado 
# no formato texto
ret = requests.get(url).text

# usando o json vamos armazenar o resultado do ret 
# já filtrando as chaves
dolar = json.loads(ret)['USDBRL']['bid']

# vamos mostrar o resultado
print(f"20 Dólares hoje custam {float(dolar)*20} reais")

# %%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func


@error_check
def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    exchange = json.loads(requests.get(url).text)[moeda.replace('-','')]['bid']
    print(f'{valor} {moeda[:3]} hoje custam {float(exchange) * valor} {moeda[-3:]}')


cotacao(20, "USD-BRL")
cotacao(20, "EUR-BRL")
cotacao(20, "BTC-BRL")
cotacao(20, "RPL-BRL")
cotacao(20, "JPY-BRL")

# %%
import backoff
import random


@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"

#%%
import logging

#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f" RND: {rnd} ")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"
