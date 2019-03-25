#coding:utf-8
import random
import time
import hmac
import hashlib
import requests
import uuid
import json
# public : cafab6d0-4c94-11e9-991c-5d1a8bc7cbdc
# private: 77b7bd76-93d6-49e3-b8f8-f0951fe08ab6

# 23d49850-4e31-11e9-9ffe-65642668820b
# 2adad99b-395c-45d3-a956-7c8cf7c95d7e

PUBLIC_KEY = "c84f2410-494d-11e9-9a1d-69cf5d593363"
PRIVATE_KEY = b"5c7ddcf9-a123-40ba-a9c0-bf56d32abb4d"
PUBLIC_PARAM = "apiKey={0}&timestamp={1}&random={2}"
BALANCE_URL = "http://www.eirenex.net/openapi/balance"
ORDER_URL = "http://www.eirenex.net/openapi/ordersend"

def sign_param():
	millonsecond = int(round(time.time() * 1000))
	rand_num = random.randint(100000,999999)
	return PUBLIC_PARAM.format(PUBLIC_KEY,millonsecond,rand_num)

def hmac_param(param):
	if len(param) == 0:
		return ""
	h = hmac.new(PRIVATE_KEY,param.encode(encoding="utf-8"),digestmod = "sha256")
	return h.hexdigest()

def get_balance():
	params = sign_param()
	params = "{0}&sign={1}".format(params,hmac_param(params))
	r = requests.get(BALANCE_URL,params=params)
	print(r.text)

def post_order():
	params = sign_param()
	params = "{0}&sign={1}".format(params,hmac_param(params))
	data = {"clientorderid":str(uuid.uuid1()),
			"contract":"ETH_BTC",
			"side":"Buy",
			"insertprice":0.041787,
			"insertvolume":0.1234,
			"pricetype":"Limit"
	}
	r = requests.post(url,params=params,json=data)
	print(r.text)


if __name__ == "__main__":
	get_balance()


