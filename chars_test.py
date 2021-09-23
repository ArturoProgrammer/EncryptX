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

		chars 		= []	# LISTA DE CARACTERES ORIGINALES DE TODO EL MENSAJE
		encodecharc	= []	# LISTA DE CARACTERES CODIFICADOS DE TODO EL MENSAJE
		

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


if __name__ == '__main__':
	text = "Hola Mundo Con EncryptX"
	text_encode = encode("Hola Mundo Con EncryptX", True)
	text_decode = decode(text_encode, True)

	print("{a} -- {b}".format(a = text_encode, b = text_decode))