#!/usr/bin/env python

from N4Lib import encripNFour
import key_generator

f_io = open("ejemplo.txt", "r")

encripNFour.module_help()

i = 25536782

key_password = key_generator.gen_privkey(64)
#key_password = '9ac23cb8ec74b0e5542005e8a800043257eecf884250bc641e76c96bd49442f8'
pubkey = key_generator.gen_publickey(key_password)


#x = encripNFour.hash_msg_gen(f_io.readlines())	# MENSAJE NO ENCRIPTADO
x = i
#x = "@ 0x7f1ca150ac38"
print(x)
# SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
key_generator.savedbKey(key_password, x)


#encrip_msg = encripNFour.encode(f_io.readlines(), encripNFour.validation_key(key_password))
encrip_msg = "KVES"
print("\nHASH DE LLAVE: {}".format(x))

# SE GUARDA EL MENSAJE Y EL HASH EN LA DB
encripNFour.savedbMsg(encrip_msg, x)

f_io.close()	# SE CIERRA EL ARCHIVO. TODOS LOS DATOS YA ESTAN ALAMCENADOS EN EL PROGRAMA LOCAL

print("|==> **MENSAJE CODIFICADO Y LLAVE: \n-> {a}\n-> {b}".format(a = encrip_msg, b = key_password))
key_generator.saveKeys(key_password)

print("LONGITUD DE LLAVE PRIVADA: {}".format(len(key_password)))

print("\nLLAVE PUBLICA: {}".format(pubkey))
print("LONGITUD DE LLAVE PUBLICA: {}".format(len(pubkey)))

decodeval = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))
print("\nMENSAJE DESENCRIPTADO: {}".format(decodeval))


encripNFour.update(encrip_msg, x)
key_generator.update(x, key_generator.gen_privkey(64))
