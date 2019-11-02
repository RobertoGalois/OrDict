# OrDict
class OrDict(builtins.object)
 |  OrDict(pDict={}, **pPattern)
 |  
 |  This class is a combination of dict class and list class.
 |  It works like a dict, but can be ordered by keys or by values.
 |  Its attributes are:
 |  - _dKeys = [(key1, indx1), (key2, indx2), ...] = a list of couples of:
 |    . a key of the OrDict
 |    . the index of the corresponding value to the key, in self._dValues storage
 |  - _dValues = [v1, v2, ...] = a list of the values stored in the OrDict
 |  
 |  To create an OrDict, we do as follow:
 |  myObject = OrDict()  #Empty OrDict
 |  or
 |  myObject = OrDict({'a': 1, 'b': 2})  #OrDict initialized with a dict
 |  or
 |  myObject = OrDict(k1=v1, k2=v2)      #OrDict initialized with named arguments
 |  or
 |  myObject = OrDict({'a': 1, 'b': 2}, k1=v1, k2=v2)    #combination of the 2 previous ways
 |  
 |  The user is not able to modify directly the attributes
 |  
 |  The user can:
 |  --> Read the content of _dKeys, with
 |      myObject.dKeys
 |  --> Read the content of _dValues, with
 |      myObject.dValues
 |          or
 |          myObject.values()
 |  --> have a list of the keys stored in the OrDict, with
 |      myObject.keys()
 |  
 |  Methods defined here:
 |  
|  __add__(self, other)
 |      Permit the user to concatenate 2 OrDicts, doing as follow:
 |      myNewOrDict = myOrDict1 + myOrDict2
 |  
 |  __delitem__(self, pKey)
 |      Permit the user to delete keys, doing as follow:
 |      del myOrDict['pouet']
 |  
 |  __getitem__(self, pKey)
 |      Permit the user to get items as follow:
 |      myOrDict['key'] #return the associated value
 |      --> if the key doesn't exist, a ValueError is raised
 |  
 |  __init__(self, pDict={}, **pPattern)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self)
 |      It uses the OrDictIterator class to enable the browse property
 |  
 |  __len__(self)
 |      Returns the length of the OrDict, that is the number of the keys
 |  
 |  __repr__(self)
 |      Returns a string converted version of the ordict, that is exactly the same rule of dict's class
 |  
 |  __setitem__(self, pKey, pValue)
 |      Permit the user to do as follow:
 |      myOrDict['key'] = value
 |      --> if the key already exists, it updates its value in self._dValues
 |      --> if not, the key is created and links to the value
 |  
 |  items(self)
 |      Returns a list of all couples (key, value) of the OrDict, doing as follow
 |      myOrDict.items() #[(k1, v1), (k2, v2), (k3, v3)]
 |  
 |  keys(self)
 |      Returns a list of all the keys of the OrDict
 |  
|  pop(self, pKey)
 |      Another way to delete a key in the OrDict.
 |      But unlike
 |      del myOrDict['key']
 |      which returns None,
 |      here,
 |      myOrDict.pop('key')
 |      will return the value of the deleted key, exactly like in list class
 |  
 |  reverse(self)
 |      Reverse the order of the elements in the OrDict and returns itself to permit to chain functions
 |      For example:
 |      myOrDict = OrDict({'foo': 42, 'bar': 24, 'hello': 'world'})
 |      myOrDict.reverse() # myOrDict = OrDict({'hello': 'world', 'bar': 24, 'foo': 42})
 |  
 |  sortByKeys(self)
 |      Sort the elements in the OrDict based on the KEYS and returns itself to permit to chain functions
 |      For example:
 |      myOrDict = OrDict({'foo': 42, 'bar': 24, 'hello': 'world'})
 |      myOrDict.sortByKeys() # myOrDict = OrDict({'bar': 24, 'foo': 42, 'hello': 'world'})
 |  
 |  sortByValues(self)
 |      Sort the elements in the OrDict based on the VALUES and returns itself to permit to chain functions
 |      For example:
 |      myOrDict = OrDict({'foo': 82, 'bar': 24, 'hello': 42})
 |      myOrDict.sortByValues() # myOrDict = OrDict({'bar': 24, 'hello': 42, 'foo': 84})
 |  
 |  values(self)
 |      Returns the array of all values stored in the OrDict
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  dKeys
 |      Getter for self._dKeys
 |  
 |  dValues
 |      Getter for self._dValues

