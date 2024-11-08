from .support import *


'''
Virtual character

Character is responsible of providing user-specific settings, conversations and so on.
It is specifically focused on impersonated AI behavior - interpreting and response.
'''
class ktChar():
	uId = 0

	exists = False

	refId = 0
	firstName = ''
	lastName = ''
	nickName = ''
	lang = 'en'

	defHello: 'hi'







	def __init__(self, refId, firstName='', lastName='', nickName='', lang=''):
		self.refId = refId

		self.firstName = firstName
		self.lastName = lastName
		self.nickName = nickName
		self.lang = lang


		kDB.query('charUpdate', {
			'refId': refId,
			'refNick': nickName,
			'refName1': firstName or "",
			'refName2': lastName or "",
			'refLang': lang or 'en'
		})

		dbUser = kDB.query('charGet', {'refId': refId})
		self.uId = dbUser[0][0]

		log.info(f"Char {self.uId}: id {refId}, {nickName}, {firstName}, {lastName}, {lang}")





	def getId(self):
		return self.refId
		

   # -todo 40 (interact, char) +0: compose hello


	def getLang(self):
		return 'ru'



	def getHello(self):
		return f"Hi, {self.firstName}"



	'''
	Add message to personal history as user query
	'''
	def addHistory(self, _content, origin, idSelf, idReply):
		kDB.query('charAddMsg', {
			'charId': self.uId,
			'content': _content,
			'origin': origin,
			'idSelf': idSelf,
			'idReply': idReply
		})


	
	def collect(self, _anchorId):
		outMsgA = []


		while _anchorId:
			cMsg = kDB.query('charGetMsg', {
				'idSelf': _anchorId
			})
			if cMsg:
				msgText = cMsg[0][3]
				msgOrigin = cMsg[0][4]
				msgReplyId = cMsg[0][6]

				outMsgA.append( [msgOrigin, msgText] )

			
			_anchorId = msgReplyId


		return reversed(outMsgA)



	def perform(self, _action):
		self.getRule(_action) or getDefault(_action) or ""



	'''
	Add message to personal history as AI answer
	'''


