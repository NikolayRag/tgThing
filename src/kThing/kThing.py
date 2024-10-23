'''
kThing entrance

			 <> ai
user <> char <> mem
	         <> helper

<> is message flow transport.
*user* is tg or other human/person interface.
*ai* is foreign ai api agent.
*mem* is long-term memory.
*helper* is any technical api agent like search engine or file converter.

*char* is per-user ruleset

*flow* transport manages complex message de/composition based on user request and reaction,
 ai response, long-tenm context db, and technical helpers.
Notice than flow rules are described with *char* which is only bound to user.


`kThing` main function is to establish `ktFlow` flow transport from person generally
 to answering machines (e.g. GPT AI), then back to person.

'''


from .support import *

from .ktBotAgent import *
from .ktAIAgent import *
from .ktMemAgent import *
from .ktFlow import *



class kThing():
	#message dispatcher, the only
	theFlow = None



	def __init__(self, _keyAi, _keyBot):
		aiAgent = ktAIAgent(_keyAi)
		botAgent = ktBotAgent(_keyBot)
		memAgent = ktMemAgent(kDB)

		self.theFlow = ktFlow(botAgent, aiAgent, memAgent)







	def start(self):
		self.theFlow.fuse()

