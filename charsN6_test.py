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




if __name__ == '__main__':
	file = open("ejemplo.dla", "r")
	text = file.read()

	#text = "Hola Mundo Con EncryptX	*	* \n%$/"
	text_encode = encode(text, True)
	text_decode = decode(text_encode, True)
	file.close()

	print("{a}\n{b}".format(a = text_encode, b = text_decode))
	#print(text_encode)