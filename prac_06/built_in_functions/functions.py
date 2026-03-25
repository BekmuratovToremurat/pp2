def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True



def any(iterable):
    for element in iterable:
        if element:
            return True
    return False




class C:
    @classmethod
    def f(cls, arg1, arg2): ...



complex('+1.23')

complex('-4.5j')

complex('-1.23+4.5j')

complex('\t( -1.23+4.5J )\n')

complex('-Infinity+NaNj')

complex(1.23)

complex(imag=-4.5)

complex(-1.23, 4.5)



import struct
dir()   # show the names in the module namespace

dir(struct)   # show the names in the struct module

class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']

s = Shape()
dir(s)




seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))

list(enumerate(seasons, start=1))


def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1



x = 1
eval('x+1')


float('+1.23')

float('   -12345\n')

float('1e-003')

float('+1E6')

float('-Infinity')



hex(255)

hex(-42)

'%#x' % 255, '%x' % 255, '%X' % 255

format(255, '#x'), format(255, 'x'), format(255, 'X')

f'{255:#x}', f'{255:x}', f'{255:X}'



s = input('--> ')

s


int(123.45)

int('123')

int('   -12_345\n')

int('FACE', 16)

int('0xface', 0)

int('01110011', base=2)

oct(8)

oct(-56)


'%#o' % 10, '%o' % 10

format(10, '#o'), format(10, 'o')

f'{10:#o}', f'{10:o}'


import os
dir_fd = os.open('somedir', os.O_RDONLY)
def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)

with open('spamspam.txt', 'w', opener=opener) as f:
    print('This will be written to somedir/spamspam.txt', file=f)

os.close(dir_fd)  # don't leak a file descriptor



pow(38, -1, mod=97)

23 * 38 % 97 == 1


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
    


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __repr__(self):
      return f"Person('{self.name}', {self.age})"
   


class C:
    @staticmethod
    def f(arg1, arg2, argN): ...



def regular_function():
    ...

class C:
    method = staticmethod(regular_function)


class X:
    a = 1

X = type('X', (), dict(a=1))    



for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)



list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))


for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):
    print(item)


x = [1, 2, 3]
y = [4, 5, 6]
list(zip(x, y))

x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)


spam = __import__('spam', globals(), locals(), [], 0)

spam = __import__('spam.ham', globals(), locals(), [], 0)

_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage