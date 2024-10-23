
from .support import *


'''
Conversation context manager, character-oriented
'''
class ktMemAgent():
	db = None


	
	def __init__(self, _db):
		self.db = _db
