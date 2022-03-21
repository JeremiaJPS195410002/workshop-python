try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

#(output)
#Traceback (most recent call last):
#  File "<stdin>", line 4, in <module>
#RuntimeError