import json
from os import environ
from time import sleep

import lxml.html as parser
from igninterage import Igninterage

FORUM_COOKIE = environ['FORUM_COOKIE']

"""
    ### Ign Bot2 Demo by Psychodynae - 24/07/2020 ###
    Bot que reage com um joinha ao ser mencionado
"""


def save_cache_file(f_name, content):
    with open(f_name, 'w') as f:
        f.write(content)


def load_cache_file(f_name):
    with open(f_name) as f:
        return f.read()


class Bot2:
    def __init__(self, cache_file, tempo_de_loop=60):
        self.ign = Igninterage('https://www.ignboards.com/')
        self.ign.set_cookie(json.loads(FORUM_COOKIE))
        self.cache_file = cache_file
        while True:
            print('rodando...')
            self.reage_no_post_de_quem_te_mencionou()
            sleep(tempo_de_loop)

    def procura_mention(self):
        html = self.ign.interact_session.get('https://www.ignboards.com/account/alerts').text
        tree = parser.fromstring(html)
        alerts = tree.find_class('contentRow-main contentRow-main--close')
        mention_uris = []
        for alert in alerts:
            msg_text = alert.xpath('text()')[1]
            if ('mentioned' or 'mencionou') in msg_text:
                mention_uris.append(alert.xpath('a/@href')[1])
        return mention_uris

    def ultimo_respondido_cache(self):
        try:
            return int(load_cache_file(self.cache_file))
        except FileNotFoundError:
            return exit(1)

    def reage_no_post_de_quem_te_mencionou(self):
        mention_list = self.procura_mention()
        for item in reversed(mention_list):
            post_id = item.split('/')[2]
            ultimo_respondido = self.ultimo_respondido_cache()
            if int(post_id) > ultimo_respondido:
                print(f'Reagi ao post!: {post_id}')
                self.ign.react('1', post_id)
                save_cache_file(self.cache_file, post_id)


if __name__ == '__main__':
    Bot2('mention.data', tempo_de_loop=20)
