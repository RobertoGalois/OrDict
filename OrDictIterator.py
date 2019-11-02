#!/usr/bin/python3.7
# -*-coding:utf-8 -*

class OrDictIterator:
	"""Iterator used to browse an OrDict Object.
	"""
	def __init__(self, obj):
		if (type(obj == type(OrDict()))):
			self.pos = 0
			self.obj = obj
			self.lenObj = len(obj)
		else:
			raise TypeError("Object passed in arg must be an OrDict object")

	def __next__(self):
		if (self.pos >= self.lenObj):
			raise StopIteration

		self.pos += 1
		return (self.obj.items()[self.pos - 1])
