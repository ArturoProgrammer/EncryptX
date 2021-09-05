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



	elif file == "DB_test.xrk":	
		_lines 			= []	# Lista con el contenido para concatenar en archivo resultante
		_message_DIR	= {}	# { Linea : N. Coincidencias }

		DB_RD = dbfile.readlines()
		dbfile.close()

		for a_line in DB_RD:
			# Contador inicial de coincidencias -> 1
			if a_line in DB_RD:
				_message_DIR[a_line] = 1

		# GUARDADO DE RESULTADOS
		new_file = open("RESULTADOS.txt", "w+")
		
		for i in _message_DIR:
			_lines.append(i)		

		new_file.write("".join(_lines))
		new_file.close()


		_Line_DICT	=	{}	# { mensaje : HASH }
		_HASHES		= 	[]	# Lista con los hashes existentes

		for line in DB_RD:
			_message 	= line[0:line.find("-->")]			# Detector del mensaje / Todo entre los corchetes (listas)
			_HASH 		= line[int(line.find("-->") + 4):]	# Detector de HASH / Ejemplo: @ 0xb776b7d0


			print(_message)
			print(_HASH)

			_Line_DICT[_message] = _HASH
		print(_Line_DICT)

def synchronizer (file):
	"""
	Sincroniza las todas las bases de datos para evitar la acumulacion de hashes inexistentes en el resto de bases.
	"""
	pass

if __name__ == '__main__':
	garbageCollector(argv[1])