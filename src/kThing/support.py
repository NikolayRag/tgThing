import logging as log
defLogLevel = log.INFO
log.basicConfig(level=defLogLevel)


from .kDB import *
#  todo 32 (refactor, db) +0: db entrance
#defDBLocation = 'db.sql'
#kDB.init(defDBLocation)
