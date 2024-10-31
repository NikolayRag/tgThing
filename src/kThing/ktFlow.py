from .support import *

from .ktChar import *


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



	def goCmd(self, _cmd, _char):
		log.info(f"Command: {_cmd}")

		if _cmd == '/start':
			return _char.getHello()


		# -todo 36 (issue, review) +0: dont stop at first
		if _cmd == '/stopstop':
			self.botAgent.shut()

			log.error('Stop pending')



	def goAI(self, _char, _msg):
		_char.addQ(_msg)

		aiLang = _char.getLang()
		systemmsg = f"default language - {aiLang}"
		aiA = self.aiAgent.speak([['system',systemmsg],['user',_msg]])

		_char.addA(aiA['answer'])

		return aiA



	def __tgCB(self, _msg, isCommand):
		#sync names every time as they can be changed elsewhere
		cChar = ktChar(
			_msg.from_user.id,
			firstName=_msg.from_user.first_name,
			lastName=_msg.from_user.last_name,
			nickName=_msg.from_user.username,
			lang=_msg.from_user.language_code
		)


		if isCommand:
			cmdSay = self.goCmd(_msg.text, cChar)
			cmdSay and self.botAgent.tgSend(cChar.getId(), cmdSay)

			return


		self.botAgent.tgDecorate(cChar.getId())


		log.info(f"In < {_msg.json} <\n")

		aiA = self.goAI(cChar, _msg.text)
		msgOut = self.botAgent.tgSend(cChar.getId(), f"{aiA['answer']}", replyTo=_msg.id)

		log.info(f"Out > {msgOut.json} >\n")






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


