def add(int1,int2):

    try:
        a = float(int1)
        b = float(int2)
    except ValueError:
        return None
    else:
        return a + b

add(2,4)