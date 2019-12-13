"""
@lesson leson1 - dict,sets,frozensets,tuples,strings,list,ifel
"""
##lists:- not-unique mutable/changeable ordered collection, use [] to create a list
def learnList(list = []):
    list.append(13)
    list.append(13)
    list.append(103)
    print(list)
learnList()

##tuple:- not-unique immutable/unchangeable ordered collection, use () to create a tuple
## they are faster and less mem-intensive. it is a constant
def learnTuple(tuple = (12,56,77,77)):
    print(tuple)
learnTuple()

##Dict:- unique-key mutable/changeable unordered indexed collection, use {} to create a dict
## they are a key-value pair. Keys must be unique
def learnDict(dict = {}):
    dict.update({'one':1,'two':2,'three':3})
    print(dict)
learnDict()

##Set:- unique mutable/changeable unordered & unindexed collection, use set() or {} to create a set
def learnSet(set = set()):
    set.update('a')
    set.update('b','c','d','e','f')
    print(set)
learnSet()

##String:- unique immutable sequence of characters, use '' or "" to create a string
def learnString(s = 'python learn trail'):
    s = s.upper()
    print(len(s))
    print(s)
learnString()

##Frozenset:- an immutable set, use frozenset() to create a Frozenset
def learnFrozenset():
    fset = frozenset([11,22])
    fset1 = frozenset([0,0,1])
    print(fset.union(fset1))
learnFrozenset()

# ######## Python if else ##################
def learnIfelse():
    list = [1,3,4,5,6]
    if len(list) >= 5:
        print('list is a long one')
    else:
        print('list is a short one!')
learnIfelse()

# ######## while ##################
def learnWhile():
    i = 23
    while i > 0:
        print(i*i)
        if i == 15:
            break
        i -= 1
learnWhile()

# ######## forloop ##################
def learnForloop():
    myfruits = ["Cherry","Apple","Money","Banana","Choco","Pears","Pery","Grape"]
    chars = 'This is idd otuya string of characters'
    for fruit in myfruits:
        print(fruit)
    for char in chars:
        print(char)
        if char == ' ':
            break
learnForloop()

# lambda functions
l = lambda a, b, c : a*b*c*c
print(l(1,1,12))

# Python classes and objects
# basic
class learn:
    x = 3*10
learnClass = learn()
print(learnClass.x)

print('######################################################################')


# class object with init()
class learn1:
    def __init__(self, lesson, duration):
        self.lesson = lesson
        self.duration = duration
l = learn1("Python classes", "4 hours")
print(l.lesson)


print('######################################################################')


# class object with init() and functions
class learn2:
    def __init__(self, lesson, duration):
        self.lesson = lesson
        self.duration = duration
    def doing(self):
        d = 'I have been learning ' + self.lesson + ' for ' + self.duration     
        return d
l = learn2("Python classes", "4 hours")
doing = l.doing()
print(doing)
"""
//notes
the keyword self is a reference parameter.. it is used to access variables
is not a must to use "SELF" , you can use any other name as long as it is the first param in any function of the class
"""

#### use of keyword pass
class classwithnocontent:
    pass
"""
the pass keyword tells py to 
skip the class with no content, otherwise errors 
"""

print('######################################################################')

############ INHERITANCE in python
class parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def showname(self):
        print(self.fname, self.lname)
p = parent('Idd', 'Juma')
p.showname()
""" parent/base class methods being used by a child class.
for a child class to inherit from parent pass parent() class as parameter in child class, and if the child has no other implementations
use 'pass' to avoid errors
"""
# child with no init()
class child(parent):
    pass # this allows child to use parent init()
c = child('Irene K.', 'Kinley')
c.showname()


print('######################################################################')


# child with init() that appends third name
class child1(parent):
    def __init__(self, fname, mname, lname):#this overrides parent init()
        self.fname = fname
        self.mname = mname
        self.lname = lname
    def showMore(self):
        print(self.fname, self.mname, self.lname)

c1 = child1('Irene K.', 'Kinley', 'Juma')
c1.showMore()


print('######################################################################')


# child with init() that appends third name but keeps parent init using Parent keyword
class child2(parent):
    def __init__(self, fname, mname, lname):#this overrides parent init()
        self.fname = fname
        self.mname = mname
        self.lname = lname
        parent.__init__(self, fname,lname)
    def showMore(self):
        print(self.fname, self.mname, self.lname)

c2 = child2('Kim', 'Kinley', 'Kinangoi')
c2.showMore()
c2.showname()


print('######################################################################')


# child with init() that appends third name but keeps parent init using Super() keyword
class child3(parent):
    def __init__(self, fname, mname, lname):#this overrides parent init()
        self.fname = fname
        self.mname = mname
        self.lname = lname
        super().__init__(fname, lname)
    def showMore(self):
        print(self.fname, self.mname, self.lname)

c3 = child3('Alita', 'Skylar', 'Juma')
c3.showMore()
c3.showname()


print('######################################################################')


""" 
When using super() the init() for supper does not have reference "self"
"""

## Python Iterators
"""
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
iterate means = go through from first to last or vice vasa
Py iterators implements iterator protocol.
They are objects(or classes) that implement __iter__() and __next__() methods
"""
## Iterator vs Iterable
"""
Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
Note that you can also use a for loop to iterate iterables(check use of for loop above)
"""
thyTuple = ("Irene","Is","Juma's","beloved", "wife")
thyiter = iter(thyTuple)
print(next(thyiter))
print(next(thyiter))
print(next(thyiter))
print(next(thyiter))
print(next(thyiter)) 

print('###############################myIterable()#######################################')

## Creating iterable using _iter_() and _next_()
""" the following creates an endless iterable) """
class myIterable:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 3
        return x
myit = myIterable()
my = iter(myit)
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))

print('##############################myStoppableIterable()########################################')

""" Sometime, endless iterables are risk, to control how long to iterate, use StopIteration key word as follows """
class myStoppableIterable:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 17:
            x = self.a
            self.a += 3
            return x
        else:
            StopAsyncIteration
myit2 = myStoppableIterable()
my2 = iter(myit2)
print(next(my2))
print(next(my2))
print(next(my2))
print(next(my2))
print(next(my2))
print(next(my2))
print(next(my2))
print(next(my2))

print('############################## MyModule() ########################################')
"""
modules are code libs or system departments or application use cases etc
"""
import MyModule
MyModule.modulefunc()

print('############################## iterate on a dict from anothef module ########################################') 
print('###### by keys=>value #####')
names = MyModule.names
for k, v in names.items() :
    print(v)
print('###### by keys #####')
for k in names.keys() :
    print(k, ' => ', names[k])

## built in modules 
import platform
x = platform.machine()
print(x)

##  IMPORT using FROM keyword
""" we use from keyword to import just part of the module
for example Mymodule has a func and a dict
let us import just the dict """
from MyModule import names

## Regex - regular expressions
""" performing searches on python data """
import re
#find out if a string starts with "The" and ends with "Alita"
s = "Her name is Alita"
# get match count do len() on findAll
x = re.findall("^The.*Alita$", s)
if x :
    print('match found')
else:
    print ('no match found')

# python json
""" python uses import json, a json module to manipulate json data
json.loads(jsondata) method parses json as a py dict
json.dumps(pythonstructure) converts python data to json
"""
import json
w =  '{ "name":"John", "age":30, "city":"New York"}'
x = json.loads(w)
print(x)
y = {'name': 'John', 'age': 30, 'city': 'New York'}
z = json.dumps(y)
print(z)

#Python PIP
""" this is python's package manager 
we are going to install camelcase using pip
pip install camelcase on terminal
"""
import camelcase
text = 'hallo guys... I\'m hereeeeeee!'
c = camelcase.CamelCase()
ctxt = c.hump(text)
print(ctxt)
"""
use uninstall to remove packages
use list to show all your installed packages
"""
## Python Try Except
"""
The 'try' block lets you test a block of code for errors.
The 'except' block lets you handle the error.
The 'finally' block lets you execute code, regardless of the result of the try- and except blocks
"""
try:
    print(d)
except:
    print('error!')

""" using the FINALLY """

try:
    print(f)
except:
    print('missing d element')
finally:
    print('program proceeding anyway')
## EXAMPLE 2
try:
    fl = open("learn.txt")
    if fl :
        pass
    else:
      raise Exception('Writing failed')  
    if fl.write("Some learning material"):
        pass
    else:
        raise Exception('Writing failed')
except:
    print('missing files')
finally:
    fl.close()
### Raising errors
x = {}

try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except:
    print(EOFError)
finally:
    print('ignoring errors')

#Python User Input
"""
py3.6 uses input()
py2.7 uses raw_input()
"""
# username = input("Enter Staff ID: ")
# print('You entered ' + username)
# password = input("Enter Password: ")
# print('You entered ' + password)

### Python String Formatting
"""
make use of format() method 
we use {} to tell format() where to insert our beloved value
example:- --------
"""
message = "We have gotten {} apples"
message2 = "my shoe costs KES {:.2f}"# to 2dp
count = 45
cost = float(43999.478)
print(message.format(count))
print(message2.format(cost))

""" example using multiple values
"""
message = "We have gotten {} apples, each costing {:.1f} and total we spent KES {:.2f}"
count = 45
print(message.format(count, cost, count*cost))
""" u can also use Index Numbers in {} to ensure values are correctly placed e.g """
message = "We have gotten {0} apples, each costing {1:.1f} and total we spent KES {2:.2f}"
""" format() will place 1st value in {0}, then 2nd value in {1} and lastly {2}
#### Named Indexes #####################
You can also use named indexes by entering a name inside the curly brackets {car}, 
but then you must use names when you pass the parameter values txt.format(car = "hillux"): """
order = "I have a {car}, it is a {model}."
print(order.format(car = "Hillux", model = "Toyota"))











