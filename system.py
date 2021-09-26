import os

def initialize ():
	_actual_dir = os.getcwd()
	name = "EncryptX"

	print(name, len(name))
	if _actual_dir[-8:] != name:
		print("No estas en el lugar correcto")
		print(_actual_dir)
		os.chdir(str(_actual_dir + "/" + name))

	print(os.getcwd())