#!/usr/bin/python3.7
# -*-coding:utf-8 -*

class OrDictIterator:
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



class OrDict:

	#We can give in arg any container object that has .keys() and .values() methods returning a list castable object
	def __init__(self, pDict={}, **pPattern):
		if (pPattern is not None):
			self._dKeys = list(pPattern.keys())
			self._dValues = list(pPattern.values())
		else:
			self._dKeys = []
			self._dValues = []

		self._dKeys.extend(list(pDict.keys()))
		self._dValues.extend(list(pDict.values()))

	#---------------------------
	#--[self._keys] MANAGEMENT |
	#---------------------------
	@property
	def dKeys(self):
		return self._dKeys

	def keys(self):
		return list(self.dKeys)

	@dKeys.setter
	def dKeys(self, value):
		raise AttributeError('You are not allowed to modify the keys this way')


	#-----------------------------
	#--[self._values] MANAGEMENT |
	#-----------------------------
	@property
	def dValues(self):
		return self._dValues

	def values(self):
		return list(self.dValues)

	@dValues.setter
	def dValues(self, value):
		raise AttributeError('You are not allowed to modify the values this way')

	#--Items management
	def __getitem__(self, pKey):
		try:
			return self._dValues[self._dKeys.index(pKey)]
		except ValueError:
			raise ValueError("'{0}' is not in OrDict".format(pKey))

	def items(self):
		return list(zip(self._dKeys, self._dValues))

	#--------------------------------
	#--__specialsMeths__ MANAGEMENT |
	#--------------------------------

	def __len__(self):
		return len(self._dKeys)

	def __repr__(self):
		return dict(self.items()).__repr__()

	def __add__(self, other):
		if (type(other) == type(self)):
			ret = OrDict(self)
			ret._dKeys.extend(other.keys())
			ret._dValues.extend(other.values())
		else:
			raise TypeError('Can only add OrDict with another OrDict')

		return ret

	def __iter__(self):
		return OrDictIterator(self)


o = OrDict({'test': 'caca', 'addr': 'chezy'}, moi=42, toi=24)
o2 = OrDict({'salut': 'toi', 44: 35})

print(('test', 'caca') in o)
