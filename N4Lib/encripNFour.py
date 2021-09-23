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
	"""VERIFICA LA VALIDEZ DE UNA LLAVE, EN LA DB"""
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
			

			# # NOTE: Garbage Collector no funciona - solucionar en trash.py
			import trash
			trash.garbageCollector('file:Xmsgdb1.xrk')
			trash.synchronizer(msg_db = "Xmsgdb1.xrk", key_db = "Xkeydb0.xrk")

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
			trash.synchronizer(msg_db = "Xmsgdb1.xrk", key_db = "Xkeydb0.xrk")

			# Nos retornamos al directorio raiz
			actual_dir = str(os.getcwd())
			actual_dir = actual_dir[:-23]

			os.chdir(actual_dir)

			if oldhash != newhash:
				print("*-= {a} HAS BEEN REPLACED BY {b} =-*".format(a = oldhash, b = newhash))



# # NOTE: funcion terminada
def hash_msg_gen (message):
	"""GENERA UN HASH UNICO PARA CADA MENSAJE"""

	
	# Hay que convertir de lista a cadena para poder manejarla
	if isinstance(message, list) == True:
		message = str("".join(message))
		
	elif isinstance(message, list) == False: 
		if isinstance(message, str) == True:
			if len(message) >= 1:
				message = str(message.split())
				output = hashlib.sha256(message.encode("utf-8"))
				output = str(output)
				output = output[20:-1]

				return output
	else:
		print("ERROR - THE TYPE OF DATA IS WRONG. {}".format(type(message)))




def decode (message, keystatus):
	"""CODIFICA LOS MENSAJES RECIBIDOS"""

	if keystatus == True and type(message) != None:

		# LISTA DE CARACTERES ASCII IMPRIMIBLES ADMITIDOS
		# # NOTE: SI UN CARACTER NO ESTA AQUI, PUEDE QUE EL PROGRAMA AUN ASI FUNCIONE
		chars 		=	[]	# Lista con los caracteres de la cadena
		pair_chars	=	[]	# Caracteres de 'chars' traducidos
		pair_index	=	0

		CHARDIC = { "s" : "a", "v" : "b", "2" : "c", "ñ" : "d", "7" : "e", "n" : "f", "p" : "g", 
		"6" : "h", "z" : "i", "u" : "j", "4" : "k", "r" : "l", "y" : "m", "f" : "n", "d" : "ñ",
		"9" : "o", "g" : "p", "3" : "q", "l" : "r",  "a" : "s", "8" : "t", "j" : "u", "b" : "v",
		"1" : "w", "0" : "x", "m" : "y", "i" : "z", "w" : "1", "c" : "2", "q" : "3", "k" : "4", 
		"5" : "5", "h" : "6", "e" : "7", "t" : "8", "o" : "9", "x" : "0", "\n" : "\n", "\t" : "\t",
		"¶" : " " }

		#print(message)
		index_counter = 0	# Contador del indice del mensaje
		
		for char in message[pair_index:]:
			index_counter 	+= 1
			try:
				msg_fragment = message[pair_index:]
				pair_index += 2
				OBJ_CHAR = str("{a}".format(a = msg_fragment[:2]))
			except IndexError as e:
				pass
			else:
				if msg_fragment != "":
					#print("*", msg_fragment)
					#print(OBJ_CHAR)
					pair_chars.append(OBJ_CHAR)
					index_counter = 0

		#print(pair_chars)

		DEC_CHARS	= []	# Lista de caracteres modificados

		for i_c in pair_chars:
			#print(i_c)
			if i_c[:1] == "±":
				OBJ_CHAR = CHARDIC[i_c[1:2]].upper()
				#print("***", OBJ_CHAR)
				DEC_CHARS.append(OBJ_CHAR)
			elif i_c[:1] == "£":
				OBJ_CHAR = CHARDIC[i_c[1:2]].lower()
				#print("***", OBJ_CHAR)
				DEC_CHARS.append(OBJ_CHAR)
			elif i_c == "_¶":
				OBJ_CHAR = " "
				#print("***", OBJ_CHAR)
				DEC_CHARS.append(OBJ_CHAR)
			elif i_c[:1] == "æ":
				OBJ_CHAR = "{}".format(i_c[1:2])
				#print("***", OBJ_CHAR)
				DEC_CHARS.append(OBJ_CHAR)
			elif i_c[:1] == "¢":
				if i_c[1:2] == "n":
					OBJ_CHAR = "\n"
					#print("***", OBJ_CHAR)
					DEC_CHARS.append(OBJ_CHAR)
				if i_c[1:2] == "t":
					OBJ_CHAR = "\t"
					#print("***", OBJ_CHAR)
					DEC_CHARS.append(OBJ_CHAR)
			
		print(DEC_CHARS, "\n")
		
		final_message = str("".join(DEC_CHARS))
		#print(final_message)

		return final_message



# # NOTE: funcion terminada 
def encode (message, keystatus):
	"""DECODIFICA LOS MENSAJES RECIBIDOS"""

	if keystatus == True and type(message) != None:

		# LISTA DE CARACTERES ASCII IMPRIMIBLES ADMITIDOS
		# # NOTE: SI UN CARACTER NO ESTA AQUI, PUEDE QUE EL PROGRAMA AUN ASI FUNCIONE
		chars 		=	[]	# Lista con los caracteres de la cadena
		enc_chars	=	[]	# Caracteres de 'chars' traducidos

		CHARDIC = { "a" : "s", "b" : "v", "c" : "2", "d" : "ñ", "e" : "7", "f" : "n", "g" : "p", 
		"h" : "6", "i" : "z", "j" : "u", "k" : "4", "l" : "r", "m" : "y", "n" : "f" ,"ñ" : "d",
		"o" : "9", "p" : "g", "q" : "3", "r" : "l",  "s" : "a", "t" : "8", "u" : "j", "v" : "b",
		"w" : "1", "x" : "0", "y" : "m", "z" : "i", "1" : "w", "2" : "c", "3" : "q", "4" : "k", 
		"5" : "5", "6" : "h", "7" : "e", "8" : "t", "9" : "o", "0" : "x", "\n" : "æn", "\t" : "æt",
		" " : "¶" }

		for i in message:
			chars.append(i)
		#print(chars)

		for i in chars:
			if i.islower() == True:
				#print("{} Es minuscula".format(i))
				OBJ_CHAR = "£{}".format(CHARDIC[i])
				enc_chars.append(OBJ_CHAR)
			elif i.isupper() == True:
				#print("{} Es mayuscula".format(i))
				OBJ_CHAR = "±{}".format(CHARDIC[i.lower()])
				enc_chars.append(OBJ_CHAR)
			elif i == " ":
				#print(i)
				enc_chars.append(str("_" + CHARDIC[i]))
			else:
				if i not in CHARDIC:
					# ALMACENA EL RESTO DE CARACTERES QUE NO SE ENCUENTREN DE FORMA ESPECIAL
					#print(i , "NO ESTA")
					enc_chars.append(str("æ{}".format(i)))
				elif i == "\n":
					#print("ES UNA SECUENCIA")
					OBJ_CHAR = "¢n"
					enc_chars.append(OBJ_CHAR)
				elif i == "\t":
					#print("ES UNA SECUENCIA")
					OBJ_CHAR = "¢t"
					enc_chars.append(OBJ_CHAR)
				else:
					#print(i)
					OBJ_CHAR = "æ{}".format(i)
					enc_chars.append(OBJ_CHAR)

		#print(enc_chars, "\n")
		#print(str("".join(enc_chars)))
		final_message = str("".join(enc_chars))

		return final_message
def module_help ():
	print("encode() 	   | Funcion -> {}".format(encode.__doc__))
	print("decode() 	   | Funcion -> {}".format(decode.__doc__))
	print("validation_key()   | Funcion -> {}".format(validation_key.__doc__))
	print("hash_msg_gen()     | Funcion -> {}".format(hash_msg_gen.__doc__))
	print("savedbMsg()   	   | Funcion -> {}".format(savedbMsg.__doc__))
	print("update()   	   | Funcion -> {}".format(update.__doc__))
	print("")