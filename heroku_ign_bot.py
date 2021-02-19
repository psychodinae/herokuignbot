import json
from os import environ
from time import sleep

import lxml.html as parser
from igninterage import Igninterage

from gistman import GistMan

FORUM_COOKIE = environ['FORUM_COOKIE']
GIST_TOKEN = environ['GIST_TOKEN']
FILE_ID = environ['FILE_ID']

"""
    ### Ign HerokuBot by Psychodynae - 18/02/2021 ###
    Bot que reage com um joinha ao ser mencionado
    heroku deploy!!!
"""


class HerokuBot:
    def __init__(self, tempo_de_loop=60, tempo_entre_posts=10):
        self.tempo_entre_posts = tempo_entre_posts
        self.ign = Igninterage('https://www.ignboards.com/')
        self.gist = GistMan(GIST_TOKEN)
        self.ign.set_cookie(json.loads(FORUM_COOKIE))
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

    def reage_no_post_de_quem_te_mencionou(self):
        mention_list = self.procura_mention()
        for item in reversed(mention_list):
            post_id = item.split('/')[2]
            ultimo_respondido = self.gist.read_gist(FILE_ID)['files']['conf.data']['content']
            if int(post_id) > int(ultimo_respondido):
                print(f'Reagi ao post!: {post_id}')
                self.ign.react('1', post_id)
                self.gist.update_gist(FILE_ID, 'conf.data', post_id)
                sleep(self.tempo_entre_posts)


if __name__ == '__main__':
    HerokuBot(tempo_de_loop=30)
