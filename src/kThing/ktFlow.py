import base64
import io
import json
import threading


from .support import *

from .ktChar import *
from .tools.tool_fusionbrain import *


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



	def goImg(self, _cDescr, _charId, _label):
		log.info(f"Image try: {_cDescr}")

		fuzzb = Fuzzb(prompt=_cDescr)
		image = fuzzb.check_generation()[0]

		if not image:
			self.botAgent.tgSend(_charId , "Image generation delayed")
			log.error('Image error')
			return

		outFile = base64.decodebytes(image.encode('ascii'))
		self.botAgent.tgSend(_charId, _label, photoOut=io.BytesIO(outFile))

		log.info('Image ok')



	def goCmd(self, _cmd, _char):
		log.info(f"Command: {_cmd}")

		cmdA = _cmd.split()
		if cmdA[0] == '/start':
			return _char.getHello()


		# -todo 36 (issue, review) +0: dont stop at first
		if cmdA[0] == '/stopover':
			log.error('Stop pending')

			self.botAgent.shut()


		if cmdA[0] == '/img':
			cDescr = " ".join(cmdA[1:])
			self.goImg(cDescr, _char.getId(), f"Image: {cDescr}")



	'''
		anchorId: Message walkback Id to restore conversation
	'''
	def goAI(self, _char, anchorId):
		aiLang = _char.getLang()
		systemmsg = f"default language - {aiLang}"

		cConversation = _char.collect(anchorId)
		aiA = self.aiAgent.speak( cConversation, system=systemmsg )['answer']
		aiJS = json.loads(aiA)

		if aiJS['queryActSpecific'] == 'do image creation':
			threading.Thread(target=lambda:self.goImg(aiJS['exact task description'], _char.getId(), "")).start()

		return aiJS['answerText']


	'''
		Flow entry
	'''
	def __tgCB(self, _msg, isCommand=False, isSystem=False):
		if isSystem:
			return


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

		#Store message chain
		replyId = _msg.reply_to_message and _msg.reply_to_message.message_id
		cChar.addHistory(_msg.text, origin='user', idSelf=_msg.message_id, idReply=replyId)

		aiA = self.goAI(cChar, _msg.message_id)
		msgOut = self.botAgent.tgSend(cChar.getId(), aiA, replyTo=_msg.id)

		log.info(f"Out > {msgOut.json} >\n")

		replyId = msgOut.reply_to_message and msgOut.reply_to_message.message_id
		cChar.addHistory(aiA, origin='assistant', idSelf=msgOut.message_id, idReply=replyId)






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


