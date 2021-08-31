from io import open
import hashlib
import os
import crypto
import DBmanipulate

# VALORES DE ENCRIPTACION N3 (E_N3)
# CAMBIAR A N4 (E_N4)

# # NOTE: CONCLUIR CON LA MANIPULACION DE BASE DE DATOS
class KeyDB(DBmanipulate.DB):
	def __init__(self):
		pass



# # WARNING: PRIMERO SE DEBE CONCLUIR LOS METODOS RELACIONADOS A LA MANIPULACION DE DB
def validation_key (key):
	"""VERIFICA LA VALIDEZ DE UNA LLAVE"""
	_path = ".master/.access/dkcache/"
	os.chdir(_path)

	key_status = False

	dblink = open("Xkeydb0.xrk", "r")
	keyOnLine = ""

	priv_dbkey = []
	publ_dbkey = []

	for line_lecture in dblink.readlines():
		delimeter = " --> "
		del_index = line_lecture.find(delimeter)
		LINE_HASH = line_lecture[0:del_index]

		keyOnLine = line_lecture[del_index+5:]

		priv_dbkey.append(keyOnLine[0:-1])
		limit = int(len(keyOnLine) / 4)
		publ_dbkey.append(keyOnLine[:limit])

	if key in priv_dbkey:
		key_status = True
	elif key in publ_dbkey:
		key_status = True
	else:
		key_status = False

	# Nos retornamos al directorio raiz
	actual_dir = str(os.getcwd())
	actual_dir = actual_dir[:-23]
	os.chdir(actual_dir)

	return key_status


# # NOTE: funcion terminada
def savedbMsg (msg, ahash):
	"""GUARDA EL MENSAJE ASOCIADO A SU HASH EN LA BD"""
	if isinstance(msg, str) == True:
		if len(msg) >= 1:
			try:
				directory = ".master/.access/dkcache/"

				if os.path.exists(directory):
					os.chdir(directory)
					dbfile = open("Xmsgdb1.xrk", "a")
					
					msg = msg.split()
					DIC_LINE = "{b} --> {a}\n".format(a = ahash, b = msg)

					dbfile.write(DIC_LINE)
					dbfile.close()

					# Nos retornamos al directorio raiz
					actual_dir = str(os.getcwd())
					actual_dir = actual_dir[:-23]
					os.chdir(actual_dir)
				else:
					print("THE DIRECTORY DOESN'T EXIST!")
			except FileNotFoundError as e:
				raise e
			else:
				pass



# # NOTE: funcion terminada
def update (msg, newhash):
	"""ACTUALIZA LA BASE DE DATOS CON UN NUEVO HASH"""
	 
	# Si se repite un mensaje pero tienen diferente hash
	# Se realiza el reemplazo del viejo con el nuevo
	
	# PROCESO DE ACTUALIZACION EN MSG DB
	if isinstance(msg, str) == True:
		if len(msg) >= 1:
			_path = ".master/.access/dkcache/"
			os.chdir(_path)

			# Se abre primeramente para el modo lectura
			db = open("Xmsgdb1.xrk", "r")

			existent_lines = [] # Lineas de texto
			msg = msg.split()
			oldhash = ""

			for line in db.readlines():
				if line.find(str(msg)) != -1:
					OBJ_MSG = line[0:int(len(str(msg)) + 5)]
					OBJ_LINE = "{a} --> {b}\n".format(a = msg, b = newhash)
					
					existent_lines.append(OBJ_LINE)

					oldhash = line[int(len(str(msg)) + 5):-1]
				else:
					existent_lines.append(line)

			db.close() 	# Una vez finalzado el almacenamiento de cierra el enlace

			file_lines = "".join(existent_lines)

			# Se abre el archivo nuevamente para escribir el nuevo contenido
			_db = open("Xmsgdb1.xrk", "w")
			_db.write(file_lines)
			_db.close()	# Se cierra el enlace nuevamente tras concluir la re-escritura
			import trash
			trash.garbageCollector('file:Xmsgdb1.xrk')
			

			# PROCESO DE ACTUALIZACION EN KEY DB
			k_db 			= open("Xkeydb0.xrk", "r")
			_hash 			= newhash
			_key	 		= ""
			kexistent_lines = []

			for line in k_db.readlines():
				if line.find(str(oldhash)) != -1:
					OBJ_HASH = line[0:int(len(str(_hash)) + 5 )]

					_key = line[int(len(str(_hash)) + 9):-1]
					OBJ_LINE = "{a} --> {b}\n".format(a = _hash, b = _key)
					
					kexistent_lines.append(OBJ_LINE)
				else:
					kexistent_lines.append(line)

			k_db.close() 	# Una vez finalzado el almacenamiento de cierra el enlace

			kfile_lines = "".join(kexistent_lines)

			# Se abre el archivo nuevamente para escribir el nuevo contenido
			_kdb = open("Xkeydb0.xrk", "w")
			_kdb.write(kfile_lines)
			_kdb.close()	# Se cierra el enlace nuevamente tras concluir la re-escritura
			import trash
			trash.garbageCollector('file:Xkeydb0.xrk')


			# Nos retornamos al directorio raiz
			actual_dir = str(os.getcwd())
			actual_dir = actual_dir[:-23]

			os.chdir(actual_dir)

			# # BUG: ENCONTRAR EL PINCHE EROR
			if oldhash == newhash:
				print("*-= {a} HAS BEEN REPLACED BY {b} =-*".format(a = oldhash, b = newhash))



# # NOTE: funcion terminada
def hash_msg_gen (message):
	"""GENERA UN HASH UNICO PARA CADA MENSAJE"""

	# Hay que convertir de lista a cadena para poder manejarla
	if isinstance(message ,list) == True:
		message = str("".join(message))

	if isinstance(message, str) == True:
		if len(message) >= 1:
			message = str(message.split())
			output = hashlib.sha256(message.encode("utf-8"))
			output = str(output)
			output = output[20:-1]

			return output
	else:
		print("ERROR - THE TYPE OF DATA IS WRONG. {}".format(type(message)))



# # NOTE: funcion terminada
def encode (message, keystatus):
	"""CODIFICA LOS MENSAJES RECIBIDOS"""

	if keystatus == True and type(message) != None:

		# LISTA DE CARACTERES ASCII IMPRIMIBLES ADMITIDOS
		# # NOTE: SI UN CARACTER NO ESTA AQUI, PUEDE QUE EL PROGRAMA AUN ASI FUNCIONE
		charlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
		"n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1",
		"2", "3", "4", "5", "6", "7", "8", "9", "0","A","B", "C", "D", "E", "F", "G",
		"H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U",
		"V", "W", "X", "Y", "Z", ".", "\n", "\t", "!", '"', " ", "#", "%", "$", "&,",
		"'", "(", ")", "*", "+", ",", "-", "", ":", ";", "<", "=", ">", "?", "@", "[",
		"]", "^", "_", "`", "{", "|", "}", "~", "¡", "¿"]

		# DICCIONARIO DE VALORES DE ENCRIPTACION
		chardic = { "a" : "s", "b" : "o",  "c" : "p",  "d" : "q",  "e" : "z",  "f" :
		"n",  "g" : "x",  "h" : "k", "i" : "l", "j" : "y",  "k" : "u",  "l" : "e",
		"m" : "b",  "n" : "a",  "ñ" : "ñ",  "o" : "v",  "p" : "g",  "q" : "1",  "r" :
		"3",  "s" : "9", "t" : "7",  "u" : "5",  "v" : "2",  "w" : "4",  "x" : "8", 
		"y" : "0",  "z" : "6", "1" : "t", "2" : "c", "3" : "d", "4" : "f", "5" : "h",
		"6" : "i", "7" : "j", "8" : "m", "9" : "r", "0" : "w", "A" : "S", "B" : "O", 
		"C" : "P",  "D" : "Q",  "E" : "Z",  "F" : "N",  "G" : "X",  "H" : "K", "I" :
		"L", "J" : "Y",  "K" : "U",  "L" : "E", "M" : "B",  "N" : "A",  "Ñ" : "Ñ", 
		"O" : "V",  "P" : "G",  "Q" : "1",  "R" : "3",  "S" : "9", "T" : "7",  "U" :
		"5",  "V" : "2",  "W" : "4",  "X" : "8",  "Y" : "0",  "Z" : "6", "\n" :
		"\n", "\t" : "\t", "." : ".", " " : " "	}

		chars = []			# LISTA DE CARACTERES ORIGINALES DE TODO EL MENSAJE
		encodecharc = []	# LISTA DE CARACTERES CODIFICADOS DE TODO EL MENSAJE
		

		# EXAMINA Y GUARDA LOS CARACTERES EN SUS RESPECTIVAS LISTAS
		for line in message:
			linetext 	= []	# LINEA DE TEXTO ACTUAL
			charl 		= []	# LISTA DE CARACTERES DE LA LINEA

			linetext.append(line)

			for i in line:
				"""
				print(i)
				"""
				charl.append(i)
				chars.append(i)

				"""
				if i in charlist:
					print("SE ENCUENTRA EN LA LISTA: {}".format(i))
				else:
					print("EL CARACTER: {} \nNO SE ENCUENTRA EN LA LISTA".format(i))
				"""
			"""
			print(chars)
			print(linetext)
			print(charl)
			"""

		# COMIENZA EL PROCESO DE ENCRIPTACION

		"""
		1 => SE ENCRIPTA EN N4
		2 => SE ENCRIPTA EN BINARIO
		3 => SE GENERA y ENCRIPTA LA LLAVE PRIVADAE EN SHA256
		4 => CODIFICACION FINAL FINAL
		"""

		for c in chars:
			if c in chardic:
				cval = chardic[c]
				encodecharc.append(cval)
				"""
				print("ENCRIPATANDO: {a} -> {b}".format(a = c, b = cval))
				"""
			else:
				encodecharc.append(c)
		"""
		print(encodecharc)
		print("\nMENSAJE ORIGINAL:\n{}".format("".join(chars)))
		print("\nMENSAJE ENCRIPTADO:\n{}".format("".join(encodecharc)))
		"""

		# INICIO DE LOS 3 PASOS
		x = str("".join(encodecharc))			# CARACTERES UNIDOS
		"""
		y = hashlib.sha256(x.encode("utf-8"))	# ENCRIPTADO EN SHA-256
		z = None							# GUARDADO LOCAL DE LA LLAVE CRIPTOGRAFICA
		"""
		final_message = x

		return final_message


# # NOTE: funcion terminada 
def decode (message, keystatus):
	"""DECODIFICA LOS MENSAJES RECIBIDOS"""

	if keystatus == True and type(message) != None:

		# LISTA DE CARACTERES ASCII IMPRIMIBLES ADMITIDOS
		# # NOTE: SI UN CARACTER NO ESTA AQUI, PUEDE QUE EL PROGRAMA AUN ASI FUNCIONE
		charlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
		"n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1",
		"2", "3", "4", "5", "6", "7", "8", "9", "0","A","B", "C", "D", "E", "F", "G",
		"H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U",
		"V", "W", "X", "Y", "Z", ".", "\n", "\t", "!", '"', " ", "#", "%", "$", "&,",
		"'", "(", ")", "*", "+", ",", "-", "", ":", ";", "<", "=", ">", "?", "@", "[",
		"]", "^", "_", "`", "{", "|", "}", "~", "¡", "¿"]

		# DICCIONARIO DE VALORES DE ENCRIPTACION
		chardic = { "s" : "a", "o" : "b",  "p" : "c",  "q" : "d",  "z" : "e",  "n" :
		"f",  "x" : "g",  "k" : "h", "l" : "i", "y" : "j",  "u" : "k",  "e" : "l",
		"b" : "m",  "a" : "n",  "ñ" : "ñ",  "v" : "o",  "g" : "p",  "1" : "q",  "3" :
		"r",  "9" : "s", "7" : "t",  "5" : "u",  "2" : "v",  "4" : "w",  "8" : "x", 
		"0" : "y",  "6" : "z", "t" : "1", "c" : "2", "d" : "3", "f" : "4", "h" : "5",
		"i" : "6", "j" : "7", "m" : "8", "r" : "9", "w" : "0", "S" : "A", "O" : "B", 
		"P" : "C",  "Q" : "D",  "Z" : "E",  "N" : "F",  "X" : "G",  "K" : "H", "L" :
		"I", "Y" : "J",  "U" : "K",  "E" : "L", "B" : "M",  "A" : "N",  "Ñ" : "Ñ", 
		"V" : "O",  "G" : "P",  "1" : "Q",  "3" : "R",  "9" : "S", "7" : "T",  "5" :
		"U",  "2" : "V",  "4" : "W",  "8" : "X",  "0" : "Y",  "6" : "Z", "\n" :
		"\n", "\t" : "\t", "." : ".", " " : " "	}

		chars = []			# LISTA DE CARACTERES ORIGINALES DE TODO EL MENSAJE
		encodecharc = []	# LISTA DE CARACTERES CODIFICADOS DE TODO EL MENSAJE
		

		# EXAMINA Y GUARDA LOS CARACTERES EN SUS RESPECTIVAS LISTAS
		for line in message:
			linetext = []		# LINEA DE TEXTO ACTUAL
			charl = []			# LISTA DE CARACTERES DE LA LINEA

			linetext.append(line)

			for i in line:
				"""
				print(i)
				"""
				charl.append(i)
				chars.append(i)

				"""
				if i in charlist:
					print("SE ENCUENTRA EN LA LISTA: {}".format(i))
				else:
					print("EL CARACTER: {} \nNO SE ENCUENTRA EN LA LISTA".format(i))
				"""
			"""
			print(chars)
			print(linetext)
			print(charl)
			"""

		# COMIENZA EL PROCESO DE ENCRIPTACION

		"""
		1 => SE ENCRIPTA EN N4
		2 => SE ENCRIPTA EN BINARIO
		3 => SE GENERA y ENCRIPTA LA LLAVE PRIVADAE EN SHA256
		4 => CODIFICACION FINAL FINAL
		"""

		for c in chars:
			if c in chardic:
				cval = chardic[c]
				encodecharc.append(cval)
				"""
				print("ENCRIPATANDO: {a} -> {b}".format(a = c, b = cval))
				"""
			else:
				encodecharc.append(c)
		"""
		print(encodecharc)
		print("\nMENSAJE ORIGINAL:\n{}".format("".join(chars)))
		print("\nMENSAJE ENCRIPTADO:\n{}".format("".join(encodecharc)))
		"""

		# INICIO DE LOS 3 PASOS
		x = str("".join(encodecharc))			# CARACTERES UNIDOS
		"""
		y = hashlib.sha256(x.encode("utf-8"))	# ENCRIPTADO EN SHA-256
		z = None							# GUARDADO LOCAL DE LA LLAVE CRIPTOGRAFICA
		"""
		final_message = x

		return final_message


def module_help ():
	print("encode() 	   | Funcion -> {}".format(encode.__doc__))
	print("decode() 	   | Funcion -> {}".format(decode.__doc__))
	print("validation_key()   | Funcion -> {}".format(validation_key.__doc__))
	print("hash_msg_gen()     | Funcion -> {}".format(hash_msg_gen.__doc__))
	print("savedbMsg()   	   | Funcion -> {}".format(savedbMsg.__doc__))
	print("update()   	   | Funcion -> {}".format(update.__doc__))
	print("")