for x in range(1, 11): 
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

'12'.zfill(5)
#'00012' (Output)

'-3.14'.zfill(7)
#'-003.14' (Output)

'3.14159265359'.zfill(5)
#'3.14159265359' (Output)