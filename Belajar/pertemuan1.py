#variable --> int, str, float, bool
print(10)  #integer
print(4.2) #float
print('Hactiv8')
print("Aku lagi belajar Python loh") #str
print(True) #boolean consist 2 value false/true

#Assignment

#Ex 1 --> variable
n = 300
print(n)

a = b = c = 300
print(a, b, c)

var = 23.5
print(var)

var = "Sekarang Value ku berubah jadi str loh dari int"
print(var)

name = "Hactiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)

#ex 2 --> aritmatika +, -, /, %, *
a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

#ex3 --> operators ==, !=, <=, >=
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

#String Manipulation 
s = 'foo'
t = 'bar'
u = 'baz'
print(s + t)
print(s + t + u)
print(s * 4)

#Case Conversion
x = 'HackTIV8'
print(x.capitalize())
print(x.lower())
print(x.swapcase())
print(x.title())
print(x.upper())

#Python Lists
n = ['foo', 'bar', 'baz', 'qux']
m = ['baz', 'qux', 'bar', 'foo']
print(n)
print(n == b)

#Building a Dictionary Incrementally 
person = {}
type(person)
#saat di run, tidak mengeluarkan apa2? kenapa?

person['fname'] = 'Hack'
person['lname'] = 'PTP'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog' : 'Fido', 'cat' : 'Sox'}
print(person['fname'])
print(person['lname'])
print(person['children'])
print(person['children'][1])
print(person['pets'])
print(person['pets']['cat'])