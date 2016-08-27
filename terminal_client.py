import requests
import time
import os
import json


class Interface():
    user = None
    running = True
    logged = False

    def __init__(self, user, server):
        self.user = user
        self.server = server

    @classmethod
    def log_in(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            action = input("Who's posting? (Type in 'exit' or press Ctrl-C if you want to quit) ")
            if action != 'exit':
                cls.user = action
                cls.logged = True
            else:
                cls.logged = False
                cls.running = False
        except KeyboardInterrupt:
            print('\n')
            raise SystemExit

    def tweet(self):
        try:
            message = input('Whats in your mind? ')
            requests.post(self.server + '/tweet', json = ({'poster': self.user, 'content': message}))
        except KeyboardInterrupt:
            print('\n')
            raise SystemExit

    def posts(self):
        r = requests.get(self.server + '/tweet')
        for tweet in r.json():
            date_time = time.strftime('%Y-%m-%d, %H:%M', time.localtime(int(tweet['timestamp'])))
            print('posted at {} by {} : {}'.format(date_time, tweet['poster'], tweet['content']) + '\n')
