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


	def __tgCB(self, _msg, isCommand):
		if isCommand:
			# -todo 36 (issue, review) +0: dont stop at first
			if _msg.text == '/stop':

				log.error('Stop all')
				
				self.botAgent.shut()

				return


		cUser = _msg.from_user.id
		log.info(f"User {cUser}")
#		cChar = ktChar(cUser)

		self.botAgent.tgDecorate(cUser)


		aiLang = 'EN'
		systemmsg = f"default language - {aiLang}"
		
		aiA = self.aiAgent.speak([['system',systemmsg],['user',_msg.text]])
		log.info(f"Ai anwser: {aiA}")


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


