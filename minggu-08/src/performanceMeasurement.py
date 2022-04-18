from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
#0.098877900003572 (output)

Timer('a,b = b,a', 'a=1; b=2').timeit()
#0.06012529999134131 (output)