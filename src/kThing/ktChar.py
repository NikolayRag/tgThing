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







	def __init__(self, _id, firstName='', lastName='', nickName='', lang=''):
		self.uId = _id

		self.firstName = firstName
		self.lastName = lastName
		self.nickName = nickName
		self.lang = lang


		kDB.query('charUpdate', {
			'refId': _id,
			'refNick': nickName,
			'refName1': firstName,
			'refName2': lastName,
			'refLang': lang
		})

		dbUser = kDB.query('charGet', {'refId': _id})

		log.info(f"USER: {dbUser}")




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


