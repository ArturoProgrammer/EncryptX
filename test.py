#!/usr/bin/env python

from N4Lib import encripNFour
import key_generator

f_io = open("ejemplo.txt", "r")

encripNFour.module_help()



key_password = key_generator.gen_privkey(64)
pubkey = key_generator.gen_publickey(key_password)



anyndata = "".join(f_io.readlines())
""""anyndata = "HOLA"""
x = encripNFour.hash_msg_gen(anyndata)	# MENSAJE NO ENCRIPTADO

# SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
i = key_generator.savedbKey(key_password, x)

# SE ENCRIPTA EL MENSAJE
encrip_msg = encripNFour.encode(anyndata, encripNFour.validation_key(key_password))

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
