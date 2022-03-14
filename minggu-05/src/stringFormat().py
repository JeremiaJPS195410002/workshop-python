print('We are the {} who say "{}!"'.format('knight','Ni'))
##We are the knight who say "Ni!" (Output)

print('{0} and {1}'.format('spam', 'eggs'))
##spam and eggs(Output)

print('{1} and {0}'.format('spam', 'eggs'))
##eggs and spam(Output)

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
##This spam is absolutely horrible.(Output)

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
##The story of Bill, Manfred, and Georg.(Output)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
##Jack: 4098; Sjoerd: 4127; Dcab: 8637678(Output)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11): 
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# 1   1    1
# 2   4    8
# 3   9   27
# 4  16   64
# 5  25  125
# 6  36  216
# 7  49  343
# 8  64  512
# 9  81  729
# 10 100 1000   (Output)