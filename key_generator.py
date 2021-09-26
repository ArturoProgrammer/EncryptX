import base64
import random
import hashlib
import sys
import os
from io import open
import EncryptX.trash

"""
Metodo de llaves de encriptacion n.1
"""

#Arreglo con las llaves criptograficas aceptadas por el software
CriptoKeys = []




def _stringGate (code, let):
	if let == True:
		return code


#Funcion terminada
def _IntegerValor():
	for i in range(1, 9):
		x = random.randint(1, 122299291)
		xs = str(x)

		return xs


#Funcion terminada
def _StringValor ():
	letters = ["a","b","c","d","e","f","Q","L"]	#Arreglo de strings

	for i in range(1, 9):
		x = random.randint(0, 7)
		xa = letters[x]

		return xa

#Funcion terminada
def _Base64Valor(data):
	xb64 = base64.b64encode(data)
	xb64s = str(xb64)

	return xb64s


#Funcion terminada
def _BinaryValor (let):
	letx = int(let)
	bincode = bin(letx)

	return bincode


#Funcion terminada
def _Aleador (intv, b64v, strv, binv):
	val = intv + b64v
	val2 = val + strv
	val3 = val2 + binv
	final_val = val3

	return final_val + '\n' #Retorna el valor para el momento en el que se ejecuta la funcion


# Funcion terminada
def gen_privkey (length):

	times = int(length / 64)

	for i in range(0, times):
		#cvi = int(cv)

		# DATOS PARA EL VALOR BINARIO
		DataIntegerVal = [4554551321564, 3923739124124, 5785613546845, 7974814678934, 1002454214010, 9146700547288, 9797210104120]
		yi = random.randint(0, 6)
		dataint = DataIntegerVal[yi]
		# DATOS PARA EL VALOR BASE 64
		DataStringVal = ["f56f54gs485asdfa", "oasd8uasiasf9293", "oansd9823rbkwegf", "basnmafbahjsfk55", "km2wmsf904kks5fa", "q886858g899asd2a", "f9apsdm3wkansdaa", "i8s34ut0wio23df9", "kamjsfdiqwjroi2u39874"]
		ys = random.randint(0, 8)
		b64carter_valor = (DataStringVal[ys])	# Carburador del valor para el Base64Valor

		key = _Aleador(_IntegerValor(), _Base64Valor(b64carter_valor.encode('ascii')), _StringValor(), _BinaryValor(dataint))

		rkey = hashlib.sha256(key.encode('utf-8')).hexdigest()
		CriptoKeys.insert(i, str(rkey))


	output = "".join(CriptoKeys)	# Junta los elementos de la lista eliminando el delimitador (" ")

	return output


# Funcion terminada
def gen_publickey(keyval):
	"""Crea la llave publica"""
	a = int(len(keyval) / 4)
	return keyval[:a]


# Funcion termianda
def savedbKey (key, hash):
	"""
	Guarda la llave y su hash asociado en la BD
	
	Argumentos:
	Key [Str]
	HASH [Str]
	"""

	# COMPROBACION DE RECEPCION DE ARGUMENTOS -> VERDADERO
	#print("LLAVE: {a}\nHASH: {b}".format(a = key, b = hash))


	if hash != None:
		directory = ".master/.access/dkcache/"
		
		if os.path.exists(directory):
			os.chdir(directory)

			dbfile = open("Xkeydb0.xrk", "a")

			DIC_LINE = "{b} --> {a}\n".format(a = key, b = hash)
			dbfile.write(DIC_LINE)
			dbfile.close()

			# Nos retornamos al directorio raiz
			actual_dir = str(os.getcwd())
			actual_dir = actual_dir[:-23]
			os.chdir(actual_dir)
		else:
			"""Crea los directorios faltantes"""
			root_1 = ".master/" 
			root_2 = ".access/"
			root_3 = "dkcache/"

			os.mkdir(root_1)
			os.chdir(root_1)
			os.mkdir(root_2) 
			os.chdir(root_2)
			os.mkdir(root_3)
			os.chdir(root_3)

			dbfile = open("Xkeydb0.xrk", "a")

			DIC_LINE = "{b} --> {a}\n".format(a = key, b = hash)

			dbfile.write(DIC_LINE)
			dbfile.close()
			
			EncryptX.trash.garbageCollector('file:Xkeydb0.xrk')
			EncryptX.trash.synchronizer(msg_db = "Xmsgdb1.xrk", key_db = "Xkeydb0.xrk")

			# Nos retornamos al directorio raiz
			actual_dir = str(os.getcwd())
			actual_dir = actual_dir[:-23]
			os.chdir(actual_dir)




def update (hash, newkey):
	"""Actualiza la DB reemplazando la antigua clave privada asociada a un hash, por una nueva clave"""

	if isinstance(hash, str) == True:
		if len(hash) >= 1:
			_path =  ".master/.access/dkcache/"
			os.chdir(_path)

			f_db = open("Xkeydb0.xrk", "r")
			existent_lines	= [] 	# Lineas de texto del archivo
			_hash			= hash 	# HASH a buscar
			oldkey			= ""	# Llave antigua

			for line in f_db.readlines():
				if line.find(_hash) != -1:
					OBJ_KEY = line[0:int(len(_hash) + 5 )]
					OBJ_LINE = "{a} --> {b}\n".format(a = _hash, b = newkey)
					
					oldkey = line[int(len(_hash) + 5):-1]

					existent_lines.append(OBJ_LINE)
				else:
					existent_lines.append(line)

			f_db.close()	# Una vez finalzado el almacenamiento de cierra el enlace

			file_lines = "".join(existent_lines)

			# Se abre el archivo nuevamente para escribir el nuevo contenido
			_db = open("Xkeydb0.xrk", "w")
			_db.write(file_lines)
			_db.close()	# Se cierra el enlace nuevamente tras concluir la re-escritura


			import trash
			trash.garbageCollector('file:Xkeydb0.xrk')
			trash.synchronizer(msg_db = "Xmsgdb1.xrk", key_db = "Xkeydb0.xrk")

			# Nos retornamos al directorio raiz
			actual_dir = str(os.getcwd())
			actual_dir = actual_dir[:-23]

			os.chdir(actual_dir)

			if oldkey != newkey:
				print("*-= THE OLD KEY HAS BEEN REPLACED BY {b} =-*".format(b = str(newkey)[:int(len(newkey)/4)]))


# Funcion terminada
def saveKeyOnFile(keyvalue):
	"""Guarda en un archivo de texto plano la llave criptografica asociada a su hash correspondiente"""
	file = open("MyProjectKey.txt", "w")
	file.write(str(keyvalue)[:int(len(keyvalue)/4)])
	file.close()