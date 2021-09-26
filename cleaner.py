import os
import trash

def clean():
	_path = ".master/.access/dkcache/"
	os.chdir(_path)

	trash.garbageCollector('file:Xmsgdb1.xrk')
	trash.garbageCollector('file:Xkeydb0.xrk')
	trash.synchronizer(msg_db = "Xmsgdb1.xrk", key_db = "Xkeydb0.xrk")

	os.chdir(str(os.getcwd())[:-23])
