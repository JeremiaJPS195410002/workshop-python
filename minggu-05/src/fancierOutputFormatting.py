s = 'Hello, world.'
str(s)
##(Output)
##>>> str(s)
##'Hello, world.'

repr(s)
##(Output)
##>>> repr(s)
##"'Hello, world.'"

str(1/7)
##(Output)
##>>> str(1/7)
##'0.14285714285714285'

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
##(Output)
##>>> print(s)
##The value of x is 32.5, and y is 40000...

hello = 'hello, world/n'
hellos = repr(hello)
print(hellos)
##(Output)
##>>> print(hellos)
##'hello, world/n'

repr((x, y, ('spam', 'eggs')))
##"(32.5, 40000, ('spam', 'eggs'))" (Output)