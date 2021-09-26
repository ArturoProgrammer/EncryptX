#!/usr/bin/env python3

# ARCHIVO CLIENTE DE PRUEBA PARA EL SOFTWARE

from N4Lib import encripNFour
import key_generator
import DBmanipulate
import cleaner

f_io = open("ejemplo.txt", "r")	# EN ESTE CASO ENCRIPTAREMOS EL CONTENIDO DE UN ARCHIVO

encripNFour.module_help()


# SE GENERAN LAS LLAVES CORRESPONDIENTES
key_password = key_generator.gen_privkey(64)
pubkey = key_generator.gen_publickey(key_password)



anyndata = "".join(f_io.readlines())
""""anyndata = "HOLA"""
x = encripNFour.hash_msg_gen(anyndata)	# GENERANDO EL HASH
print("HASH:", x)

# SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
i = key_generator.savedbKey(key_password, x)

# SE ENCRIPTA EL MENSAJE
encrip_msg = encripNFour.encode(anyndata, encripNFour.validation_key(key_password))

# SE GUARDA EL MENSAJE Y EL HASH EN LA DB
encripNFour.savedbMsg(encrip_msg, x)


f_io.close()	# SE CIERRA EL ARCHIVO. TODOS LOS DATOS YA ESTAN ALAMCENADOS EN EL PROGRAMA LOCAL

print("|==> **MENSAJE CODIFICADO Y LLAVE: \n-> {a}\n-> {b}".format(a = encrip_msg, b = key_password))
key_generator.saveKeyOnFile(key_password)	# GUARDA LA LLAVE EN UN ARCHIVO DE TEXTO

print("LONGITUD DE LLAVE PRIVADA: {}".format(len(key_password)))

print("\nLLAVE PUBLICA: {}".format(pubkey))
print("LONGITUD DE LLAVE PUBLICA: {}".format(len(pubkey)))

decodeval = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))
print("\nMENSAJE DESENCRIPTADO: {}".format(decodeval))

encripNFour.update(encrip_msg, x)
key_generator.update(x, key_generator.gen_privkey(64))

cleaner.clean()

print("LA LLAVE ASOCIADA ES: {}".format(DBmanipulate.DB().getKey()))