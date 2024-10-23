from .support import *


from openai import OpenAI


import requests
import os

'''
Ai Agent is a pipe to foreign answering service.

User query is recomposed with metrics applied as a strict directive.
'''
class ktAIAgent ():
	url = "https://api.openai-proxy.com/v1/chat/completions"

	api_key = ''



	def __init__ (self, _key):
		self.api_key = _key



	def speak(self, messages):
		aiMsg = self.OAICombine(messages)
		log.info(f"AI in {aiMsg}")


		headers = {
		    "Content-Type": "application/json",
		    "Authorization": f"Bearer {self.api_key}",
		}

		data = {
			"model": "gpt-4o",  # assuming "gpt-4o" meant "gpt-4" in context
			"messages": aiMsg,
			"temperature": 1,
			"max_tokens": 2048,
			"top_p": 1,
			"frequency_penalty": 0,
			"presence_penalty": 0,
		}

		response = requests.post(self.url, headers=headers, json=data).json()

		return {
			'answer': response['choices'][0]['message']['content'],
			'full': response
		}




	'''
		Combine list of type:content pairs to be suitable for OpenAi
		messages
	'''
	def OAICombine(self, messages):
		outMsgs = []

		for k,v in messages:
			outMsgs.append(
				{
					"role": k,
					"content": v
				}
			)

		return outMsgs
