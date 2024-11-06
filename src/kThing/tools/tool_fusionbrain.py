import logging as log
import json
import time

import requests



class Fuzzb:
	def __get_model(self):
		response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
		data = response.json()
		return data[0]['id']



	def __init__(self, url, api_key, secret_key):
		self.URL = url
		self.AUTH_HEADERS = {
			'X-Key': f"Key {api_key}",
			'X-Secret': f"Secret {secret_key}",
		}
  
  

	def generate(self, prompt, images=1, width=1024, height=1024):
		model = self.__get_model()

		params = {
			"type": "GENERATE",
			"numImages": images,
			"width": width,
			"height": height,
			"generateParams": {
				"query": f"{prompt}"
			}
		}

		data = {
			'model_id': (None, model),
			'params': (None, json.dumps(params), 'application/json')
		}
		response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
		data = response.json()
		return data['uuid']



	def check_generation(self, request_id, attempts=50, delay=5):
		while attempts > 0:
			log.info(f"Check Fuzzb {request_id}...")

			response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
			data = response.json()
			if data['status'] == 'DONE':
				return data['images']

			attempts -= 1
			time.sleep(delay)
