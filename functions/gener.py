def generate_code(long):
    code=""
    for i in range(long):
        code+=str(randint(0,9))
    return code
def generate_chaine(long):
    chaine=""
    min=randint(0,1)
    for i in range(long):
        if min==1:
            chaine+=chr(randint(ord('A'),ord('Z')))
        else:
            chaine+=chr(randint(ord('a'),ord('z')))
    return chaine