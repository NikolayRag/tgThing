from .support import *


'''
Virtual character

Character is responsible of providing user-specific settings, conversations and so on.
It is specifically focused on impersonated AI behavior - interpreting and response.
'''
class ktChar():
	uId = 0

	firstName = ''
	lastName = ''
	nickName = ''
	lang = 'en'

	defHello: 'hi'






	def __init__(self, _id):
		self.uId = _id



	def setup(self, firstName='', lastName='', nickName='', lang=''):
		log.info(f"Start user {nickName}")

		self.firstName = firstName
		self.lastName = lastName
		self.nickName = nickName
		self.lang = lang



	def getId(self):
		return self.uId
		

   # -todo 40 (interact, char) +0: compose hello


	def getLang(self):
		return 'ru'



	def getHello(self):
		return f"Hi, {self.firstName}"



	'''
	Add message to personal history as user query
	'''
	def addQ(self, _msg):
		return


	'''
	Add message to personal history as AI answer
	'''
	def addA(self, _msg):
		return


