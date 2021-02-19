import json

from igninterage import Igninterage

from gistman import GistMan

"""
          Configurando  COMECE AQUI!


    1. Primeiro faça login na sua conta do forum usando o navegador firefox no seu PC (no momento a lib
       igninterage só roda no windows), depois rode a função printa_seus_cookies_de_login() localmente
       para obter os cookies na forma de um json.
       não esqueca de instalar o modulo igninterage: pip install igninterage.
       
       
    2. Na sua conta do github vá em settings > developer setings > Personal access tokens e clique em 
       generate new token, em Note coloque um nome e selecione apenas a caixa 'gist' e clique em 
       generate token.
       
    3. Mude o valor da variavel TOKEN abaixo com o valor do token gerado e rode a funcao 
       cria_arquivo_de_configuracao()
       OBS: Rode essa funcão apenas localmente nao esqueça que seu token do gist esta aqui.
       
       
    4. No heroku vá em settings e em "Config vars" e adcione tres novas configs:
    
        1. Com a key FORUM_COOKIE e no campo value copie e cole o json da funcao 
        printa_seus_cookies_de_login() ex:
        KEY : FORUM_COOKIE  VALUE: {"xf_user": "9645277439874hiuhlsikjfhslidkjfhn", "xf_csrf": "fhsliufh...."}
        
        2. Com a KEY GIST_TOKEN e o VALUE com seu token do gist gerado no passo 2 ex:
           KEY: GIST_TOKEN  VALUE: 263547263547236542747236454345353453
           
        3. com a KEY FILE_ID eo VALUE com o valor da funcao cria_arquivo_de_configuracao() ex:
           KEY: FILE_ID VALUE: 86a8s787686b78687c8787c6
    """


TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def printa_seus_cookies_de_login():
    ign = Igninterage('https://www.ignboards.com/')
    ign.ign_login()
    print(json.dumps(ign.interact_session.cookies.get_dict()))


def cria_arquivo_de_configuracao():
    gout = GistMan(TOKEN).create_gist('conf.data', '0')
    print(gout["id"])


# if __name__ == '__main__':
     # printa_seus_cookies_de_login()
     # cria_arquivo_de_configuracao()
