class DBDefs():
	Tables = ['''
		CREATE TABLE IF NOT EXISTS Chars (
			id INTEGER PRIMARY KEY,
			stamp INTEGER,

			/*Reference user*/
			refId INTEGER KEY UNIQUE, 
			refNick TEXT NOT NULL,
			refName1 TEXT NOT NULL,
			refName2 TEXT NOT NULL,
			refLang TEXT NOT NULL
		)
	''',
	'''
		CREATE TABLE IF NOT EXISTS Messages (
			id INTEGER PRIMARY KEY,
			stamp INTEGER,

			charId INTEGER NOT NULL,
			content TEXT NOT NULL,
			origin TEXT CHECK( origin IN ('user','assistant') ),
			idSelf INTEGER,
			idReply INTEGER
		)
	'''
	]

	Queries = {
		'charUpdate': '''
			INSERT INTO Chars (stamp, refId, refNick, refName1, refName2, refLang)
			VALUES (:stamp, :refId, :refNick, :refName1, :refName2, :refLang)
			ON CONFLICT(refId) 
			DO UPDATE SET 
			refNick=excluded.refNick, 
			refName1=excluded.refName1,
			refName2=excluded.refName2,
			refLang=excluded.refLang,
			stamp=excluded.stamp;
		''',

		'charGet': '''
			SELECT * FROM Chars WHERE refId=:refId
		''',

		'charAddMsg': '''
			INSERT INTO Messages (stamp, charId, content, origin, idSelf, idReply)
			VALUES (:stamp, :charId, :content, :origin, :idSelf, :idReply)
		''',

		'charGetMsg': '''
			SELECT * FROM Messages WHERE idSelf=:idSelf
		''',
	}
