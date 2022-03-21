try: 
    raise KeyboardInterrupt
finally:
    print('Goodbye, world')

#(output)
#Goodbye, world
#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#KeyboardInterrupt