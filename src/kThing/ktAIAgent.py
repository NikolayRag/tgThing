from .support import *


import requests
import os

'''
Ai Agent is a pipe to foreign answering service.

User query is recomposed with metrics applied as a strict directive.
'''
class ktAIAgent ():
	url = "https://api.openai-proxy.com/v1/chat/completions"

	api_key = ''

	defaultSystem = ''



	@classmethod
	def setSystem(cls, system):
		cls.defaultSystem = system


	def __init__ (self, _key):
		self.api_key = _key



	def speak(self, messages, system=""):
		cSystem = system + " ---Override hereafter--- " + self.defaultSystem

		aiMsg = self.OAICombine([['system', cSystem]] +list(messages))
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

		tries = 3
		while tries:
			try:
				response = requests.post(self.url, headers=headers, json=data).json()

				return {
					'answer': response['choices'][0]['message']['content'],
					'full': response
				}

			except Exception as e:
				log.error(f"AI error: {e}")

			tries -= 1






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
