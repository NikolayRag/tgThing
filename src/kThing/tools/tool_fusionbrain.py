import logging as log
import json
import time

import requests



class Fuzzb:
	URL = 'https://api-key.fusionbrain.ai/'
	AUTH_HEADERS = {}


	@classmethod
	def setKeys(cls, api_key, secret_key):
		cls.AUTH_HEADERS = {
			'X-Key': f"Key {api_key}",
			'X-Secret': f"Secret {secret_key}",
		}



	def __get_model(self):
		response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
		data = response.json()
		return data[0]['id']



	def __init__(self, api_key=None, secret_key=None, prompt=None, images=1, width=1024, height=1024):
		if api_key and secret_key:
			self.AUTH_HEADERS = {
				'X-Key': f"Key {api_key}",
				'X-Secret': f"Secret {secret_key}",
			}
		
		if prompt:
			self.gen(prompt, images, width, height)



	def gen(self, prompt, images=1, width=1024, height=1024):
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
		self.uuid = response.json()['uuid']
		log.info(f"Fuzzb start {self.uuid}")


	def check_generation(self, attempts=50, delay=5):
		while attempts > 0:
			log.info(f"Fuzzb check {self.uuid}...")

			response = requests.get(self.URL + 'key/api/v1/text2image/status/' + self.uuid, headers=self.AUTH_HEADERS)
			data = response.json()
			if data['status'] == 'DONE':
				return data['images']

			attempts -= 1
			time.sleep(delay)
