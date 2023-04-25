import http.client
import json

##########################################################
# Método que recebe a api da receita e faz a consulta do cnpj
# e usei replace para tirar os pontos e traços do cnpj caso o cliente coloque
##########################################################


def tirarPontos(string: str):
    return string.replace('.', '').replace('/', '').replace('-', '').strip()


def consultaCnpj(cnpj: str):

    conn = http.client.HTTPSConnection("receitaws.com.br")

    headers = {'Accept': "application/json"}

    conn.request("GET", "/v1/cnpj/{}".format(tirarPontos(cnpj)),
                 headers=headers)

    res = conn.getresponse()
    data = res.read()
    try:
        if not tirarPontos(cnpj).isdigit():
            print('Não é um dígito')
            return 'NOTISDIGIT'
        resp = json.loads(data.decode())
        nome = resp.get('nome')
        logradouro = resp.get('logradouro')
        numero = resp.get('numero')
        complemento = resp.get('complemento')
        bairro = resp.get('bairro')
        municipio = resp.get('municipio')
        uf = resp.get('uf')
        cep = resp.get('cep')
        telefone = resp.get('telefone')
        email = resp.get('email')
        return nome, logradouro, numero, complemento, bairro, municipio, \
            uf, cep, telefone, email
    except (ValueError, KeyError):
        return None
        # Tratar a exceção aqui, talvez imprimindo uma mensagem de erro ou
        #  retornando um valor padrão
