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
			print(a_line)	
			# Contador inicial de coincidencias -> 1
			if a_line in DB_RD:
				_message_DIR[a_line] = 1

		# GUARDADO DE RESULTADOS
		new_file = open(file, "w+")
		
		for i in _message_DIR:
			_lines.append(i)		

		new_file.write("".join(_lines))
		new_file.close()


		"""
		_lines = -1
		_linescount = {}
		plus = lambda line: _linescount.get(line) + 1

		for line_lecture in dbfile.readlines():
			_lines += 1
			if len(line_lecture) > 1:
				_linescount[line_lecture] = 1
			else:
				None
		dbfile.close()
		
		print(_lines)
		print(_linescount)

		f_db = open(file, "a")
		
		filelines = _linescount.keys()
		f_db.write("".join(filelines))
		f_db.close()
		"""



		# Segundo proceso - por repeticion de HASH


	elif file == "Xkeydb0.xrk":
		# Tercer proceso de limpieza - por repeticion de hash (Key DB)

		"""
		# CODIGO ELIMINADO POR BUGS Y MAL FUNCIONAMIENTO
		"""

		"""
		_lines 		= 0		# numero total de lineas 					=> Enteros
		_linesdir	= {}	# {'n. linea' : 'contenido de linea'}	=> Cadenas y Enteros
		_hashline 	= {}	# {'hash' : 'resto de linea'}		=> Cadenas
		_hashes		= []	# ['hash NO repetido']						=> Cadenas

		for line_lecture in dbfile.readlines():
			_lines += 1
			if len(line_lecture) > 1:
				delimeter	= " --> "
				del_index	= line_lecture.find(delimeter)
				LINE_HASH 	= line_lecture[0:del_index]

				_linesdir[_lines] = line_lecture

				if not LINE_HASH in _hashes:
					_hashes.append(LINE_HASH)
					lineval = line_lecture[del_index:]
					_hashline[LINE_HASH] = '{b}'.format(b = lineval)
		key 	= ""
		value 	= ""
		fal_txt	= []

		for i in _hashes:
			key 	= i
			value 	= _hashline[i]

			OBJ_LINE = "{a}{b}".format(a = key, b = value)
			fal_txt.append(OBJ_LINE)

			#Si no esta registrado, añades la linea a la lista
			#Si ya esta registrado, añades a la lista la primer linea con ese hash registrado
		dbfile.close()

		f_db = open(file, "a")
		f_db.write("".join(fal_txt))
		f_db.close()
		"""
		dbfile.close()

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


if __name__ == '__main__':
	garbageCollector(argv[1])