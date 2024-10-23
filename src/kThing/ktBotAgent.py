from .support import *

# https://core.telegram.org/bots/api
# https://pytba.readthedocs.io/en/latest/sync_version/index.html
import telebot



'''
TG interface.

* Incoming message is launched into provided callback.
* Send messages to TG.
* Maintains TG UI (update keyboard from WebApp)

'''
class ktBotAgent():
	TGTypesSystem = ['web_app_data'] #, 'invoice', 'successful_payment', 'connected_website', 'game']
	TGTypesUser = ['text', 'audio', 'document', 'animation', 'photo', 'sticker', 'video', 'video_note', 'voice', 'contact', 'location', 'venue', 'dice', 'poll', 'passport_data']


	tgBotInstance = None

	messageCB = None #callable

	cKeyboard = {}



	'''Make keyboard object

	Make keyboard object for sending To TG with message.

	returns: ReplyKeyboardMarkup

	Args:
		_width (int): columns
	'''
	def __webAppKeyboard(self, _width=1):
		if not self.cKeyboard:
			return

		cBoard = telebot.types.ReplyKeyboardMarkup(row_width=_width)

		for btnLabel in self.cKeyboard:
			cApp = telebot.types.WebAppInfo(self.cKeyboard[btnLabel])
			tgButton = telebot.types.KeyboardButton(text=btnLabel, web_app=cApp)
			cBoard.add(tgButton)

		return cBoard



	'''Procceed incoming TG messages
	
	Update Keyboard for WebApp.

	Call previously defined callback with message.
	Send callback result back if any.

	Args:
		_message (json): from tg
		isApp (bool): is WebApp reply flag

	Returns:
		None
	'''
	def __listener (self, _message, isApp=False):
		_chatId = _message.chat.id
		msgReply= None

		#CB with 
		if isApp:
			webAppData = _message.web_app_data

			if webAppData.button_text in self.cKeyboard:
				self.cKeyboard[webAppData.button_text] = webAppData.data

			msgReply = webAppData.button_text
			self.tgSend( _chatId, msgReply)

		else:
			if telebot.util.is_command(_message.text):
				None


		if self.messageCB:
			self.messageCB(_message)



	# decorate
	def tgDecorate(self, _chatId, mode='typing', timeout=10):
		self.tgBotInstance.send_chat_action(_chatId, 'typing', timeout=timeout)





	'''Send message to TG

	Args:
		_id (int): TG chat id
		_msgOut (string): message
		replyTo (int): message to reply
	'''
	def tgSend(self, _id, _msgOut, replyTo=None):
		sendFn = self.tgBotInstance.send_message

		markKeys = self.__webAppKeyboard()

		sendFn(_id,
			_msgOut,
			reply_to_message_id= replyTo,
			parse_mode= "Markdown",
			reply_markup= markKeys
		)



### PUBLIC ###



	'''Set TG interface
	
	Set elements of TG interface: keyboard.
	
	Args:
		_keyboard (dict): {"label": "URL", ...}
	'''
	@classmethod
	def defInterface(cls, tgKeyboard=None):
		cls.cKeyboard = dict(tgKeyboard)



	def __init__(self, _key):
		self.tgBotInstance = telebot.TeleBot(_key)

		self.tgBotInstance.register_message_handler(self.__listener, content_types=self.TGTypesUser)
		self.tgBotInstance.register_message_handler(lambda m:self.__listener(m,isApp=True), content_types=self.TGTypesSystem)




	'''Set callback for message listener.
	
	Args:
		_cb (callable): Function to be called
	'''
	def setMessageCB(self, _cb):
		if not callable(_cb):
			return

		self.messageCB = _cb



	'''
	Run
	'''
	def listen(self):
		self.tgBotInstance.infinity_polling()
