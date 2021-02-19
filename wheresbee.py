import requests
import json
import time


while True:
    r=requests.get('https://ctf.laptophackingcoffee.org/api/v1/users/2641/solves')
    bee_solves=json.loads(r.text)
    data=bee_solves['data']
    if len(data)==0:
        print('no solves yet')
    else:
        print('YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO THERE SEEMS TO HAVE BEEN A SOLVE')
    time.sleep(300)
