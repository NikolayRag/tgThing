from .support import *
'''
Conversation fabric.

Message is exchanged between person side, AI side, and db as memory.

Incoming person messages decomposed, then some stuff is fetched from memory,
and then composed and sent to AI.
AI responce is parsed to store context in memory, and verbal part is sent back to person.


?? review ??
Cycle is:
- TG to AI
	- parse message
	- retreive context
	- update Character
	- compose message with
		- Character semantic
		- technical rules
	- send message to AI

- AI to TG
	- split Metrics from reply
		- adjust Character
	- send User part of reply to TG

'''
class ktFlow():
	botAgent = None
	aiAgent = None
	memAgent = None










	def goCmd(self, _user, _cmd):
		# -todo 36 (issue, review) +0: dont stop at first
		log.info(f"Command: {_cmd}")


		if _cmd == '/stopstop':
			self.botAgent.shut()

			log.error('Stop pending')



	def goAI(self, _user, _msg):
		aiLang = 'EN'
		systemmsg = f"default language - {aiLang}"
		
		aiA = self.aiAgent.speak([['system',systemmsg],['user',_msg.text]])
		return aiA



	def __tgCB(self, _msg, isCommand):
		cUser = _msg.from_user.id
		log.info(f"User {cUser}")

		if isCommand:
			self.goCmd(cUser, _msg.text)
			return


		self.botAgent.tgDecorate(cUser)

		aiA = self.goAI(cUser, _msg)

		self.botAgent.tgSend(cUser, f"{aiA['answer']}", replyTo=_msg.id)






	def __init__(self, _instanceBot, _instanceAI, _instanceMem):
		self.botAgent = _instanceBot
		self.aiAgent = _instanceAI
		self.memAgent = _instanceMem

		self.botAgent.setMessageCB(self.__tgCB)


	

	'''
	Start listening
	'''
	def fuse(self):
		log.warning('Flow Powered')

		self.botAgent.listen()


