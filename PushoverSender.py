import httplib
import urllib


class PushoverSender:
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key = api_key

    def send(self, message):
        c = httplib.HTTPSConnection('api.pushover.net:443')
        post_data = {'user': self.user_key, 'token': self.api_key, 'message':
                     message}
        c.request('POST', '/1/messages.json', urllib.urlencode(post_data),
                  {'Content-type': 'application/x-www-form-urlencoded'})
        # print(c.getresponse().read())
