

from kThing import *
from kThing.tools.tool_fusionbrain import *



keyAi = '123...'
keyBot = '456...'

fuzzApi = '234...'
fuzzSecret = '345...'
directiveSystem = "Act strange"
Fuzzb.setKeys(api_key=fuzzApi, secret_key=fuzzSecret)

theThing = kThing(keyAi, keyBot)
theThing.setBehaviorSystem(directiveSystem)

theThing.start()

