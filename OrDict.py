#!/usr/bin/python3.7
# -*-coding:utf-8 -*

from OrDictIterator import OrDictIterator

def newRange(pStart, pSteps):
	"""range() kind of function, but instead of giving pStart and pEnd args,
	   (2 and 7 for example to get [2, 3, 4, 5, 6])
	   we give pStart and pSteps where pSteps is the len of the final list.
	   (2 and 5 for example to get [2, 3, 4, 5, 6])
		There must be a basic python function that make the job but I didn't find it
	"""
	return range(pStart, pStart + pSteps)

class OrDict:
	"""This class is a combination of dict class and list class.
	   It works like a dict, but can be ordered by keys or by values.
	   Its attributes are:
	   - _dKeys = [(key1, indx1), (key2, indx2), ...] = a list of couples of:
	     . a key of the OrDict
	     . the index of the corresponding value to the key, in self._dValues storage
	   - _dValues = [v1, v2, ...] = a list of the values stored in the OrDict

	   To create an OrDict, we do as follow:
	   myObject = OrDict()	#Empty OrDict
	   or
	   myObject = OrDict({'a': 1, 'b': 2})	#OrDict initialized with a dict
	   or
	   myObject = OrDict(k1=v1, k2=v2)	#OrDict initialized with named arguments
	   or
	   myObject = OrDict({'a': 1, 'b': 2}, k1=v1, k2=v2)	#combination of the 2 previous ways

	   The user is not able to modify directly the attributes

	   The user can:
	   --> Read the content of _dKeys, with
	       myObject.dKeys
	   --> Read the content of _dValues, with
	       myObject.dValues
		   or
		   myObject.values()
	   --> have a list of the keys stored in the OrDict, with
	       myObject.keys()
	"""
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
		"""Getter for self._dKeys
		"""
		return self._dKeys

	def keys(self):
		"""Returns a list of all the keys of the OrDict
		"""
		return [ x[0] for x in self._dKeys]

	@dKeys.setter
	def dKeys(self, value):
		"""Setter for self._dKeys, raise directly an AttributeError
		"""
		raise AttributeError('You are not allowed to modify the keys this way')


	#-----------------------------
	#--[self._values] MANAGEMENT |
	#-----------------------------
	@property
	def dValues(self):
		"""Getter for self._dValues
		"""
		return self._dValues

	def values(self):
		"""Returns the array of all values stored in the OrDict
		"""
		return self.dValues

	@dValues.setter
	def dValues(self, value):
		"""Setter for self._dValues, raise directly an AttributeError
		"""
		raise AttributeError('You are not allowed to modify the values this way')

	#-----------------------------
	#--[self.items()] MANAGEMENT |
	#-----------------------------
	def __getitem__(self, pKey):
		"""Permit the user to get items as follow:
		   myOrDict['key'] #return the associated value
		   --> if the key doesn't exist, a ValueError is raised
		"""
		try:
			return self._dValues[self.keys().index(pKey)]
		except ValueError:
			raise ValueError("'{0}' is not in OrDict".format(pKey))

	def __setitem__(self, pKey, pValue):
		"""Permit the user to do as follow:
		   myOrDict['key'] = value
		   --> if the key already exists, it updates its value in self._dValues
		   --> if not, the key is created and links to the value
		"""
		indx = [el[1] for el in self._dKeys if el[0] == pKey]

		if (len(indx) == 0):
			indx = len(self._dValues)
			self._dKeys.append((pKey, indx))
			self._dValues.append(pValue)

		else:
			self._dValues[indx[0]] = pValue

	def items(self):
		"""Returns a list of all couples (key, value) of the OrDict, doing as follow
		   myOrDict.items() #[(k1, v1), (k2, v2), (k3, v3)]
		"""
		return list(zip(self.keys(), [ self._dValues[el[1]] for el in self._dKeys ]))

	#--------------------------------
	#--__specialsMeths__ MANAGEMENT |
	#--------------------------------

	def __len__(self):
		"""Returns the length of the OrDict, that is the number of the keys
		"""
		return len(self._dKeys)

	def __repr__(self):
		"""Returns a string converted version of the ordict, that is exactly the same rule of dict's class
		"""
		return dict(self.items()).__repr__()

	def __add__(self, other):
		"""Permit the user to concatenate 2 OrDicts, doing as follow:
		   myNewOrDict = myOrDict1 + myOrDict2
		"""
		if (type(other) == type(self)):
			ret = OrDict(self)
			ret._dKeys.extend(list(zip(other.keys(), newRange(len(ret._dKeys), len(other.keys())))))
			ret._dValues.extend(other.values())
		else:
			raise TypeError('Can only add OrDict with another OrDict')

		return ret

	def __iter__(self):
		"""It uses the OrDictIterator class to enable the browse property
		"""
		return OrDictIterator(self)

	def __delitem__(self, pKey):
		"""Permit the user to delete keys, doing as follow:
		   del myOrDict['pouet']
		"""
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
		"""Sort the elements in the OrDict based on the KEYS and returns itself to permit to chain functions
		   For example:
		   myOrDict = OrDict({'foo': 42, 'bar': 24, 'hello': 'world'})
		   myOrDict.sortByKeys() # myOrDict = OrDict({'bar': 24, 'foo': 42, 'hello': 'world'})
		"""
		self._dKeys = sorted(self._dKeys, key=lambda tupl: tupl[0])
		return self

	def sortByValues(self):
		"""Sort the elements in the OrDict based on the VALUES and returns itself to permit to chain functions
		   For example:
		   myOrDict = OrDict({'foo': 82, 'bar': 24, 'hello': 42})
		   myOrDict.sortByValues() # myOrDict = OrDict({'bar': 24, 'hello': 42, 'foo': 84})
		"""
		self._dKeys = sorted(self._dKeys, key=lambda tupl: self._dValues[tupl[1]])
		return self

	def reverse(self):
		"""Reverse the order of the elements in the OrDict and returns itself to permit to chain functions
		   For example:
		   myOrDict = OrDict({'foo': 42, 'bar': 24, 'hello': 'world'})
		   myOrDict.reverse() # myOrDict = OrDict({'hello': 'world', 'bar': 24, 'foo': 42})
		"""
		self._dKeys  = self._dKeys[::-1]
		return self

	def pop(self, pKey):
		pass

if (__name__ == '__main__'):
	o = OrDict({'test': 'caca', 'addr': 'chezy', 'nombre': 'cinquante-quatre'}, moi='le meilleur', toi='le nul')
	o2 = OrDict({'salut' : 'toi', 'comment tu' : 'vas ?'})
	o3 = o + o2
	test = OrDict({'zorro': 42, 'Marcel': 34, 'Abdul': 56, 'Victor': 3, 'Jean-Louis': 1})

	print(test.dValues)
