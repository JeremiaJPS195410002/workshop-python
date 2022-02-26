basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket

'crabgrass' in basket

a = set('abracadabra')
b = set('alacazam')
a           #unique letters in a
a - b       #letters in a but not in b
a | b       #letters in a or b or both
a & b       #leters in both a and b
a ^ b       #lettersin a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a