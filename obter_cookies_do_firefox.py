import json

from igninterage import Igninterage


def printa_seus_cookies_de_login():
    """
    1. Primeiro faça login na sua conta usando o navegador firefox no seu PC (no momento a lib
       igninterage só roda no windows), depois rode esta função localmente para obter os cookies
       na forma de um json.
       não esqueca de instalar o modulo igninterage: pip install igninterage.


    2. No heroku vá em settings e em "Config vars" e adcione uma nova config, com a key FORUM_COOKIE
       e no campo value copie e cole o json que esta funcao retorna ex:
       KEY : FORUM_COOKIE  VALUE: {"xf_user": "9645277439874hiuhlsikjfhslidkjfhn", "xf_csrf": "fhsliufh...."}

    """
    ign = Igninterage('https://www.ignboards.com/')
    ign.ign_login()
    print(json.dumps(ign.interact_session.cookies.get_dict()))


if __name__ == '__main__':
    printa_seus_cookies_de_login()
