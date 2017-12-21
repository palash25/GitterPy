import requests
import json

api_url = 'https://api.gitter.im/v1'
token = '1e0af4f5ff31002370362a544a702c8d419b31e1'

payload = {'access_token': token}

headers = {"Content-Type" : "application/json; charset=utf-8",
      	   "Accept" : "application/json",
           "Authorization" : "Bearer {}".format(token)}


def get_user(query=None):
	r = requests.get('https://api.gitter.im/v1/user', params=payload)
	user_data = json.loads(r.content)
	response = json.dumps(user_data, indent =4, sort_keys=True) # str
	print(response)
	
def get_rooms(query=None):
	rooms = requests.get('https://api.gitter.im/v1/rooms', params=payload)
	print(rooms.content)
	
def run():
	get_user()
	#get_rooms()

if __name__ ==  '__main__':
	run()
	
	
	
	
	
	
	
#from tqdm import trange
#from random import random, randint
#from time import sleep

#t = trange(100)
#for i in t:
    #t.set_description('GEN %i' % i)
    #t.set_postfix(loss=random(), gen=randint(1,999), str='h', lst=[1, 2])
    #sleep(0.1)