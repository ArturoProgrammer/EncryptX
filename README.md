
# EncryptX
![](rsc/estable.svg)
![](rsc/dev.svg)

Sistema de encriptacion multiplataforma para proyectos en Python 3.X.

## Contenidos
1. [Informacion General](#informacion-general)
2. [Releases](#releases)
4. [Novedades](#novedades)
3. [Instalacion](#instalacion)
6. [Aplicaciones y uso](#aplicaciones-y-uso)
7. [Documentacion](#documentacion)
***

## Informacion General
EncryptX es un sistema de encriptacion avanzado de nueva generacion diseñado para principiantes y uso avanzado.

Ideal para usos personales, desde encriptacion de mensajes sencillos, archivos hasta algo mayor como grandes proyectos a gran escala.

## Releases
- EncryptX v0.80 [descargar aqui](link) estable
- EncryptX v0.85 [descargar aqui](link) dev

## Novedades
- Adicion de Garbage Collector
- Gestor de contenido en la base de datos
- Sincronizador de base de datos
- Capacidad de encriptacion para multiples archivos simultaneamente
- Nuevo sistema de codificacion **N-6**

## Instalacion
Por pip:
`python -m pip install EncryptX-stable`

O clona este repositorio para realizar aportaciones al proyecto:
`git clone https://github.com/ArturoProgrammer/EncryptX.git`

## Aplicaciones y uso
Una vez instalado el paquete, podemos aplicar el siguiente codigo de ejemplo:

```
from EncryptX.N4Lib import encripNFour
import EncryptX.key_generator


data = "Hola Mundo!"

# SE GENERAN LAS LLAVES CORRESPONDIENTES
key_password = EncryptX.key_generator.gen_privkey(32)
pubkey = EncryptX.key_generator.gen_publickey(key_password)


msg_hash = encripNFour.hash_msg_gen(data)	# GENERANDO EL HASH
print("HASH DEL MENSAJE:", msg_hash)

# SE GUARDA LA LLAVE PRIVADA Y EL HASH EN LA DB
EncryptX.key_generator.savedbKey(key_password, msg_hash)

# SE ENCRIPTA EL MENSAJE
encrip_msg = encripNFour.encode(data, encripNFour.validation_key(key_password))

# SE GUARDA EL MENSAJE Y EL HASH EN LA DB
encripNFour.savedbMsg(encrip_msg, msg_hash)
print("|==> **MENSAJE CODIFICADO: \n{a}\n".format(a = encrip_msg))

# GUARDA LA LLAVE EN UN ARCHIVO DE 	TEXTO
EncryptX.key_generator.saveKeyOnFile(key_password)

print("*LLAVE PRIVADA: {}".format(key_password))
print("*LLAVE PUBLICA: {}".format(pubkey))

# DESENCRIPTAMOS EL MENSAJE
decode_msg = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))
print("\nMENSAJE DESENCRIPTADO: {}".format(decode_msg))


encripNFour.update(encrip_msg, msg_hash)
key_generator.update(msg_hash, key_generator.gen_privkey(32))
```

Bien, explicaremos y vamos paso a paso. Primero se importan las librerias correspondientes.
```
from EncryptX.N4Lib import encripNFour
import EncryptX.key_generator
```
Despues, podemos declaramos una variable con el contenido que deseamos trabajar. En este caso de ejemplo solo sera un sencillo y tradicional "Hola Mundo!".
```
data = "Hola Mundo!"
```
Luego, definimos las llaves publicas y privadas que usaremos, asi como su longitud en multiplos de 2.
```
key_password = EncryptX.key_generator.gen_privkey(32)
pubkey = EncryptX.key_generator.gen_publickey(key_password)
```
Generamos y declaramos el HASH de este mensaje.
```
msg_hash = encripNFour.hash_msg_gen(data)
```
Almacenamos la llave en la base de datos local.
```
EncryptX.key_generator.savedbKey(key_password, msg_hash)
```
Se encripta el mensaje deseado.
```
encrip_msg = encripNFour.encode(data, encripNFour.validation_key(key_password))
```
Guardamos el mensaje y su HASH unico generado en la base de datos.
```
encripNFour.savedbMsg(encrip_msg, msg_hash)
```
Se guardan (opcional) en un archivo de texto plano la llave publica.
```
EncryptX.key_generator.saveKeyOnFile(key_password)
```
Desencriptamos el mensaje que hemos encriptado posteriormente.
```
decode_msg = encripNFour.decode(encrip_msg, encripNFour.validation_key(pubkey))
```
***
Si posteriormente deseamos hacer una actualizacion en la base de datos, podemos actualizar el HASH de la siguiente forma:
```
encripNFour.update(encrip_msg, msg_hash)
```
Y para actualizar la llave:
```
key_generator.update(msg_hash, key_generator.gen_privkey(32))
```

## Documentacion
*Por escribir*
