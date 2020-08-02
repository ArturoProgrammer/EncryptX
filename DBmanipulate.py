#!/usr/bin/env python

import os
from io import open


class DB (object):
	def __init__(self, data_type):
		self.data_type = data_type

	def getKey(self):
		pass

	def getMsg(self):
		pass