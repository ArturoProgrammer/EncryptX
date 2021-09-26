#!/usr/bin/env python3

import io
from sys import argv
import os


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

	# *** <== === PROCESOS PARA DB MSG === ==> *** #
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


		# *** Tercer proceso - Duplicado de mensajes *** #
		reopen_file 	= open(file, "r")
		reopen_fileACT	= reopen_file.readlines()
		reopen_file.close()

		_Line_DICT		=	{}	# Diccionario de { mensaje : HASH }
		_MSG 			=	[]	# Lista de mensajes existentes sin repeticiones
		_HASHES			= 	[]	# Lista de todos los hashes
		codeToWrite 	= 	[]	# Lista con el contenido a escribir


		for line in reopen_fileACT:
			delimeter 	=	" -->"
			actual_MSG 	=	line[:line.find(delimeter)]
			actual_HASH	=	line[int(line.find(delimeter) + 4):]

			_MSG.append(actual_MSG)
			_Line_DICT[actual_MSG] = actual_HASH

			if actual_HASH not in _HASHES:
				_HASHES.append(actual_HASH)

		for msg in _Line_DICT:
			OBJ_LINE = "{a}{b}{c}".format(a = msg, b = delimeter, c = _Line_DICT[msg])
			codeToWrite.append(OBJ_LINE)


		reopen_file = open(file, "w")
		reopen_file.write("".join(codeToWrite))
		reopen_file.close()




	# *** <== === PROCESOS PARA DB KEY === ==> *** #
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




def synchronizer (msg_db = "", key_db = ""):
	"""Sincroniza las todas las bases de datos para evitar la acumulacion de hashes inexistentes en el resto de bases."""
	MSG_DICT	=	{}		# Diccionario de { message : hash }
	KEY_DICT	=	{}		# Diccionario de { hash : key }
	delimeter	=	" --> "	# Delimitador

	msg_dbFile		=	open(msg_db, "r")
	msg_db_content	= 	msg_dbFile.readlines()
	for line in msg_db_content:
		_message 	=	line[0:line.find(delimeter)]
		_hash 		=	line[int(line.find(delimeter) + 5):-1]
		MSG_DICT[_hash] = _message

	msg_dbFile.close()

	key_dbFile	 	=	open(key_db, "r")
	key_db_content	=	key_dbFile.readlines()
	for line in key_db_content:
		_hash 	=	line[0:line.find(delimeter)]
		_key 	= 	line[int(line.find(delimeter) + 5):]
		KEY_DICT[_hash]	= _key

	key_dbFile.close()

	HASH_LIST		=	[]	# Lista con los hashes de la DB Msg a dejar intactos en DB Key
	NEW_KEY_DICT	=	{}	# Diccionario con { hash : key } sincronizados
	for i_hash in MSG_DICT:
		HASH_LIST.append(i_hash)

	for key_hash in KEY_DICT:
		if key_hash not in MSG_DICT:
			pass
		else:
			NEW_KEY_DICT[key_hash] = KEY_DICT[key_hash]

	"""
	for hash_in_key in KEY_DICT:
		#print(hash_in_key)
		for hash_in_msg in MSG_DICT:
			#print(hash_in_msg)
			if hash_in_key == hash_in_msg:
				print("ENCONTRADO")
				print(hash_in_key, "", hash_in_msg)
			else:
				del KEY_DICT[hash_in_key]
	"""

	file_content = []
	for i in NEW_KEY_DICT:
		OBJ_LINE = "{a} --> {b}".format(a = i, b = NEW_KEY_DICT[i])
		file_content.append(OBJ_LINE)

	dbFileToWrite = open(key_db, "w")
	dbFileToWrite.write(str("".join(file_content)))
	dbFileToWrite.close()



if __name__ == '__main__':
	synchronizer(msg_db = argv[1], key_db = argv[2])