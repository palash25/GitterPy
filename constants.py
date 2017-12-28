URL = 'https://api.gitter.im/v1'
TOKEN = '1e0af4f5ff31002370362a544a702c8d419b31e1'

PAYLOAD = {'access_token': TOKEN}

HEADERS = {"Content-Type" : "application/json; charset=utf-8",
      	   "Accept" : "application/json",
           "Authorization" : "Bearer {}".format(TOKEN)}