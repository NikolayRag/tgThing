from .support import *


'''
Virtual character

Character is responsible of providing user-specific settings, conversations and so on.
It is specifically focused on impersonated AI behavior - interpreting and response.
'''
class ktChar():
   uId = 0

   defHello: 'hi'




   def __init__(self, _id):
   	self.uId = _id


   def getId(self):
      return self.uId



   def addQ(self, _msg):
      return


   def addA(self, _msg):
      return



