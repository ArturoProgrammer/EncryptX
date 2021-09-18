import io
from sys import argv


# *** <== === FUNCIONES PRIVADAS === ==> ***#

def _match_eliminator (c_dict, h_list, coinc, index = None):
	# ELIMINA LAS COINCIDENCIAS ENCONTRADAS Y RETORNA UNA LISTA LIMPIA
	
	# c_dict 	- 	{}		diccionario con el contenido de { mensaje : hash }
	# h_list	-	[]		hashes disponibles (sin coincidencias)
	# coinc 	- 	[] 		mensajes asociados al mismo hash	
	# index 	-	int 	indice de lista (elemento a dejar intacto)
	# result 	-	{}		diccionario resultante final

	FINAL_RESULT = {}

	if index == None:
		# ELIMINA TODAS LAS COINCIDENCIAS Y EL HASH CORRESPONDIENTE
		for keyToDel in coinc:
			c_dict.pop(keyToDel)

		FINAL_RESULT = c_dict

	elif index != None:
		# ELIMINA TODAS LAS COINCIDENCIAS EXCEPTO LA ELEGIDA
		COIN_SAVED	= coinc[int(index - 1)]		# mensaje salvado
		COIN_DELETE	= []						# lista de elementos a borrar

		coinc.remove(COIN_SAVED)
		COIN_DELETE = coinc 		# Se guarda la lista con los elementos a borrar


		coinc = []
		coinc.append(COIN_SAVED)	# Se guarda la lista con el elemento a dejar

		for keyToDel in COIN_DELETE:
			c_dict.pop(keyToDel)

		FINAL_RESULT = c_dict


	return FINAL_RESULT


def _match_ignore (c_dict, h_list, coinc, index = None):
	# CONFIRMA SI SE DESEA IGNORAR O ELIMINAR COINCIDENCIAS

	print("IGNORANDO COINCIDENCIAS")
	q_req = input("SI SE ENCUENTRA EL MISMO HASH ASOCIADO A MAS DE UN MENSAJE, CAUSA UN MAL FUNCIONAMIENTO EN EL SISTEMA\nSEGURO QUE DESEA IGNORAR LAS COINCIDENCIAS? (Y/n) ")

	if q_req.upper() == "Y":
		# IGNORAR COINCIDENCIAS
		print("IGNORANDO TODAS LAS COINCIDENCIAS")
		FINAL = c_dict
	elif q_req.upper() == "N":
		# ELIMINA LAS COINCIDENCIAS
		FINAL = _match_eliminator(c_dict, h_list, coinc)
		print("TODAS LAS COINCIDENCIAS {} HAN SIDO ELIMINADAS".format(coinc))
		
	else:
		print("IGNORANDO SECUENCIA")
		FINAL = c_dict

	return FINAL





# *** <== === FUNCIONES PUBLICAS === ==> *** #

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


		# *** Segundo proceso - Duplicado de HASH *** #
		_Line_DICT	=	{}	# { mensaje : HASH }
		_HASHES		= 	[]	# Lista con los hashes existentes (UNICOS)

		MK_FILE			= file
		reopen_file		= open(MK_FILE, "r")
		reopen_fileACT	= reopen_file.readlines()

		for line in reopen_fileACT:
			delimeter	=	" -->"
			_message 	=	line[0:line.find(delimeter)]			# Detector del mensaje / Todo entre los corchetes (listas)
			_HASH 		=	line[int(line.find(delimeter) + 4):]	# Detector de HASH / Ejemplo: @ 0xb776b7d0
			_H_Counter	=	0										# Contador de coincidencias
			coin_list	=	[] # LISTA DE COINCIDENCIAS

			_Line_DICT[_message] = _HASH

			f_dict		= 	{}	# Diccionario de datos a convertir
			ToWriteFile	=	[]	# Lista con datos para escribir en el archivo

			if not _HASH in _HASHES:
				_HASHES.append(_HASH)	# Se almacenan el HASH sin repeticion
			else:

				for value in _Line_DICT:
					if _HASH == _Line_DICT[value]:
						#print(value)
						_H_Counter 	+= 	1
						coin_list.append(value)

		message_u = str("".join(coin_list))
		if _H_Counter != 0:
			print("*** EL HASH {a} SE REPITE {n} VECES. ASOCIADO A: {m_c}".format(a = _HASH[:-1], n = _H_Counter, m_c = message_u))
			opt	= input("*** QUE MENSAJE DESEA DEJAR ASOCIADO AL HASH {a}? (P. Ej.: 1 en caso de {msg_sel}/A para eliminar todas las coincidencias/I para ignorar): ".format(a = _HASH[:-1], msg_sel = coin_list[0]))


			if opt.upper() == "A" or opt.upper() == "I":
				if opt.upper() == "A":
					# BORRADO DE TODAS LAS COINCIDENCIAS
					f_dict = _match_eliminator(_Line_DICT, _HASHES, coin_list)
				if opt.upper() == "I":
					# IGNORAR COINCIDENCIAS
					f_dict = _match_ignore(_Line_DICT, _HASHES, coin_list, index = 1)
			else:
				try:
					opt = int(opt)
				except ValueError as e:
					# IGNORAR COINCIDENCIAS
					f_dict = _match_ignore(_Line_DICT, _HASHES, coin_list, index = 1)

				else:
					# ELIMINA COINCIDENCIAS NO SELECCIONADAS
					try:
						msg_select = coin_list[opt - 1]	
					except IndexError as e:
						print("SIN COINCIDENCIAS ENCONTRADAS EN LISTA")
					else:
						print("ELIMINANDO COINCIDENCIAS.\nDEJANDO EN PIE ASOCIACION: {b} --> {a}".format(a = _HASH[:-1], b = msg_select))
						f_dict = _match_eliminator(_Line_DICT, _HASHES, coin_list, index = opt)

			for msg in f_dict:
				OBJ_LINE = "{a} -->{b}".format(a = msg, b = f_dict[msg])
				ToWriteFile.append(OBJ_LINE)
			
			re_file	= open(file, "w")
			re_file.write(str("".join(ToWriteFile)))
			re_file.close()
			
			#print(_HASHES)
			#print(_Line_DICT)
			reopen_file.close()




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
		new_file	=	open("RESULTADOS.txt", "w")
		
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
			delimeter	=	" -->"
			_message 	=	line[0:line.find(delimeter)]			# Detector del mensaje / Todo entre los corchetes (listas)
			_HASH 		=	line[int(line.find(delimeter) + 4):]	# Detector de HASH / Ejemplo: @ 0xb776b7d0
			_H_Counter	=	0										# Contador de coincidencias
			coin_list	=	[] # LISTA DE COINCIDENCIAS

			_Line_DICT[_message] = _HASH

			f_dict		= 	{}	# Diccionario de datos a convertir
			ToWriteFile	=	[]	# Lista con datos para escribir en el archivo

			if not _HASH in _HASHES:
				_HASHES.append(_HASH)	# Se almacenan el HASH sin repeticion
			else:

				for value in _Line_DICT:
					if _HASH == _Line_DICT[value]:
						#print(value)
						_H_Counter 	+= 	1
						coin_list.append(value)

		message_u = str("".join(coin_list))
		print("EL HASH {a} SE REPITE {n} VECES. ASOCIADO A: {m_c}".format(a = _HASH[:-1], n = _H_Counter, m_c = message_u))
		opt	= input("QUE MENSAJE DESEA DEJAR ASOCIADO AL HASH {a}? (P. Ej.: 1 en caso de {msg_sel}/A para eliminar todas las coincidencias/I para ignorar): ".format(a = _HASH[:-1], msg_sel = coin_list[0]))


		if opt.upper() == "A" or opt.upper() == "I":
			if opt.upper() == "A":
				# BORRADO DE TODAS LAS COINCIDENCIAS
				f_dict = _match_eliminator(_Line_DICT, _HASHES, coin_list)
			if opt.upper() == "I":
				# IGNORAR COINCIDENCIAS
				f_dict = _match_ignore(_Line_DICT, _HASHES, coin_list, index = 1)
		else:
			try:
				opt = int(opt)
			except ValueError as e:
				# IGNORAR COINCIDENCIAS
				f_dict = _match_ignore(_Line_DICT, _HASHES, coin_list, index = 1)

			else:
				# ELIMINA COINCIDENCIAS NO SELECCIONADAS
				try:
					msg_select = coin_list[opt - 1]	
				except IndexError as e:
					print("SIN COINCIDENCIAS ENCONTRADAS EN LISTA")
				else:
					print(coin_list[opt - 1])
					print("ELIMINANDO COINCIDENCIAS.\nDEJANDO EN PIE ASOCIACION: {b} --> {a}".format(a = _HASH[:-1], b = msg_select))
					f_dict = _match_eliminator(_Line_DICT, _HASHES, coin_list, index = opt)

		print(f_dict)
		
		for msg in f_dict:
			OBJ_LINE = "{a} --> {b}".format(a = msg, b = f_dict[msg])
			ToWriteFile.append(OBJ_LINE)
		
		re_file 	= open("RESULTADOS.txt", "w")
		re_file.write(str("".join(ToWriteFile)))
		re_file.close()

		#print(_HASHES)
		#print(_Line_DICT)
		reopen_file.close()



def synchronizer (file):
	"""
	Sincroniza las todas las bases de datos para evitar la acumulacion de hashes inexistentes en el resto de bases.
	"""
	pass

if __name__ == '__main__':
	garbageCollector(argv[1])