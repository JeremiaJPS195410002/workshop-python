from dis import findlinestarts


def bool_return():
    try:
        return True
    finally:
        return False

bool_return()

#False (output)
