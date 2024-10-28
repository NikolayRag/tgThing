'''
DB engine singletone
'''


import logging as log

import sqlite3
from datetime import datetime


from .DBDefs import *



class kDB():
	dbName = ''



	@staticmethod
	def __queryExec(_query, _argsA={}):
#  todo 13 (issue, db) +0: movedb connection out
		dbConnection = sqlite3.connect(kDB.dbName)

		cursor = dbConnection.cursor()
		
		log.debug(f"DB Apply {_argsA} to {_query}")
		try:
			cursor.execute(_query, _argsA) 
			results = cursor.fetchall()
		except Exception as x:
			log.error(f"DB exec error: {x}")
			results = None


		dbConnection.commit()
		dbConnection.close()


		return results



###########



	@staticmethod
	def init(_fn):
		kDB.dbName = _fn


		try:
			for dbDef in DBDefs.Tables:
				kDB.__queryExec(dbDef)
		except Exception as e:
			log.error(f"DB init error: {e}")



	@staticmethod
	def query(_q, _v):
		utc = int(datetime.utcnow().timestamp()*1000)
		try:
			out = kDB.__queryExec(DBDefs.Queries[_q], dict(_v,stamp=utc))
		except:
			log.error('DB error')

		return out









