import io
from sys import argv


def garbageCollector (file):
	"""Elimina las coincidencias de una misma cadena de datos en el mismo archivo"""
	file = file[5:]

	dbfile = io.open(file, "r")

	if file == "Xmsgdb1.xrk":
		# Primer proceso - 	repeticion de linea
		_lines 			= []	# Lista con el contenido para concatenar en archivo resultante
		_message_DIR	= {}	# { Linea : N. Coincidencias }

		DB_RD = dbfile.readlines()
		dbfile.close()

		for a_line in DB_RD:
			# Contador inicial de coincidencias -> 1
			if a_line in DB_RD:
				_message_DIR[a_line] = 1

		# GUARDADO DE RESULTADOS
		new_file = open(file, "w+")
		
		for i in _message_DIR:
			_lines.append(i)		

		new_file.write("".join(_lines))
		new_file.close()

		# Segundo proceso - por repeticion de HASH
		_HASH_lines	=	{}	# { mensaje : HASH }
		_HASHES		= 	[]	# Lista con los haches existentes





	elif file == "Xkeydb0.xrk":
		# Tercer proceso de limpieza - por repeticion de hash (Key DB)
		# Primer proceso - 	repeticion de linea

		_lines 			= []	# Lista con el contenido para concatenar en archivo resultante
		_message_DIR	= {}	# { Linea : N. Coincidencias }

		DB_RD = dbfile.readlines()
		dbfile.close()

		for a_line in DB_RD:
			# Contador inicial de coincidencias -> 1
			if a_line in DB_RD:
				_message_DIR[a_line] = 1

		# GUARDADO DE RESULTADOS
		new_file = open(file, "w+")
		
		for i in _message_DIR:
			_lines.append(i)		

		new_file.write("".join(_lines))
		new_file.close()


	# ARCHIVO DE PRUEBA - ELIMINAR CUANDO SEA NECESARIO
	elif file == "DB_test.xrk":	
		# *** Primer proceso - Lineas duplicadas *** #
		_lines 			= []	# Lista con el contenido para concatenar en archivo resultante
		_message_DIR	= {}	# { Linea : N. Coincidencias }

		DB_RD = dbfile.readlines()
		dbfile.close()

		for a_line in DB_RD:
			# Contador inicial de coincidencias -> 1
			if a_line in DB_RD:
				_message_DIR[a_line] = 1

		# GUARDADO DE RESULTADOS
		new_file = open("RESULTADOS.txt", "w")
		
		for i in _message_DIR:
			_lines.append(i)


		new_file.write("".join(_lines))
		new_file.close()


		# *** Segundo proceso - Duplicado de HASH *** #
		_Line_DICT	=	{}	# { mensaje : HASH }
		_HASHES		= 	[]	# Lista con los hashes existentes (UNICOS)

		MK_FILE			= "RESULTADOS.txt"
		reopen_file		= open(MK_FILE, "r")
		reopen_fileACT	= reopen_file.readlines()

		for line in reopen_fileACT:
			delimeter	= " -->"
			_message 	= line[0:line.find(delimeter)]			# Detector del mensaje / Todo entre los corchetes (listas)
			_HASH 		= line[int(line.find(delimeter) + 4):]	# Detector de HASH / Ejemplo: @ 0xb776b7d0

			_Line_DICT[_message] = _HASH

			if not _HASH in _HASHES:
				_HASHES.append(_HASH)	# Se almacenan el HASH sin repeticion

		print(_HASHES)
		print(_Line_DICT)
		reopen_file.close()

		"""
		# # NOTE: AÑADIR GUARDADO DE RESULTADOS / REESCRITURA DE ARCHIVO
		# GUARDADO DE RESULTADOS
		new_file = open(MK_FILE, "w")

		for i in _message_DIR:
			_lines.append(i)		

		new_file.write(str("".join(_lines)))
		print(str("".join(_lines)))
		new_file.close()


		# *** Tercer proceso - Mensaje duplicado *** #
		_Message_LIST	= 	[]	# Lista con los mensajes
		_LineToWrite	=	{}	# Diccionario listo para escritura

		for line in DB_RD:
			delimeter	= " -->"
			_MsgOnLine	= line[0:line.find(delimeter)]	# Detector del mensaje en la linea
			_Message_LIST.append(_MsgOnLine)

		for msg in _Message_LIST:
			_LineToWrite[msg] = "HASH"

		counter	= -1
		for key in _LineToWrite:
			counter += 1
			_LineToWrite[key] = _HASHES[counter]
		
		print(_LineToWrite)
		"""

def synchronizer (file):
	"""
	Sincroniza las todas las bases de datos para evitar la acumulacion de hashes inexistentes en el resto de bases.
	"""
	pass

if __name__ == '__main__':
	garbageCollector(argv[1])