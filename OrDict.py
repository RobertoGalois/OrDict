#!/usr/bin/python3.7
# -*-coding:utf-8 -*

def newRange(pStart, pSteps):
	return range(pStart, pStart + pSteps)

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
			self._dKeys = list(zip(pPattern.keys(), range(0, len(pPattern.keys()))))
			self._dValues = list(pPattern.values())
		else:
			self._dKeys = []
			self._dValues = []

		self._dKeys.extend(list(zip(pDict.keys(), newRange(len(self._dKeys), len(pDict.keys())))))
		self._dValues.extend(list(pDict.values()))

	#---------------------------
	#--[self._keys] MANAGEMENT |
	#---------------------------
	@property
	def dKeys(self):
		return self._dKeys

	def keys(self):
		return [ x[0] for x in self._dKeys]

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

	#-----------------------------
	#--[self.items()] MANAGEMENT |
	#-----------------------------
	def __getitem__(self, pKey):
		try:
			return self._dValues[self.keys().index(pKey)]
		except ValueError:
			raise ValueError("'{0}' is not in OrDict".format(pKey))

	def __setitem__(self, pKey, pValue):
		indx = [el[1] for el in self._dKeys if el[0] == pKey]

		if (len(indx) == 0):
			indx = len(self._dValues)
			self._dKeys.append((pKey, indx))
			self._dValues.append(pValue)

		else:
			self._dValues[indx[0]] = pValue

	def items(self):
		return list(zip(self.keys(), [ self._dValues[el[1]] for el in self._dKeys ]))

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
			ret._dKeys.extend(list(zip(other.keys(), newRange(len(ret._dKeys), len(other.keys())))))
			ret._dValues.extend(other.values())
		else:
			raise TypeError('Can only add OrDict with another OrDict')

		return ret

	def __iter__(self):
		return OrDictIterator(self)

	def __delitem__(self, pKey):
		if (pKey in self.keys()):
			indx = [el[1] for el in self._dKeys if el[0] == pKey][0]
			self._dKeys = [el for el in self._dKeys if el[0] != pKey]
			self._dKeys = list(map(lambda el : ((el[0], el[1]) if el[1] < indx else (el[0], el[1] - 1)), self._dKeys))
			del self._dValues[indx]
		else:
			raise KeyError(pKey)


	#------------------
	#-- Class Methods |
	#------------------
	def sortByKeys(self):
		self._dKeys = sorted(self._dKeys, key=lambda tupl: tupl[0])
		return self

	def sortByValues(self):
		self._dKeys = sorted(self._dKeys, key=lambda tupl: self._dValues[tupl[1]])
		return self

	def reverse(self):
		self._dKeys  = self._dKeys[::-1]
		return self



o = OrDict({'test': 'caca', 'addr': 'chezy', 'nombre': 'cinquante-quatre'}, moi='le meilleur', toi='le nul')
o2 = OrDict({'salut' : 'toi', 'comment tu' : 'vas ?'})
o3 = o + o2
test = OrDict({'zorro': 42, 'Marcel': 34, 'Abdul': 56, 'Victor': 3, 'Jean-Louis': 1})

print(test)
del test['zorro']
print(test)
del test['Victor']
print(test.sortByKeys())

