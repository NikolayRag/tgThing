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
      self.firstName = firstName
      self.lastName = lastName
      self.nickName = nickName
      self.lang = lang


   def getId(self):
      return self.uId



   def getLang(self):
      return 'ru'



   # -todo 40 (interact, char) +0: compose hello
   def getHello(self):
      return f"Hi, {self.firstName}"



   def addQ(self, _msg):
      return


   def addA(self, _msg):
      return



