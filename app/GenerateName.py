from random import randint

def convert(name):
    name = name.lower()
    name_trans = ''
    for char in name:
        if (char == ' '):
            name_trans += (' ')
        if (char == 'а'):
            name_trans += ('a')
        elif (char == 'б'):
            name_trans += ('b')
        elif (char == 'в'):
            name_trans += ('v')
        elif (char == 'г'):
            name_trans += ('g')
        elif (char == 'д'):
            name_trans += ('d')
        elif (char == 'е') or (char == 'ё'):
            name_trans += ('e')
        elif (char == 'ж'):
            name_trans += ('zh')
        elif (char == 'з'):
            name_trans += ('z')
        elif (char == 'и') or ((char == 'й')):
            name_trans += ('i')
        elif (char == 'к'):
            name_trans += ('k')
        elif (char == 'л'):
            name_trans += ('l')
        elif (char == 'м'):
            name_trans += ('m')
        elif (char == 'н'):
            name_trans += ('n')
        elif (char == 'о'):
            name_trans += ('o')
        elif (char == 'п'):
            name_trans += ('p')
        elif (char == 'р'):
            name_trans += ('r')
        elif (char == 'с'):
            name_trans += ('s')
        elif (char == 'т'):
            name_trans += ('t')
        elif (char == 'у'):
            name_trans += ('u')
        elif (char == 'ф'):
            name_trans += ('f')
        elif (char == 'х'):
            name_trans += ('h')
        elif (char == 'ц'):
            name_trans += ('c')
        elif (char == 'ч'):
            name_trans += ('ch')
        elif (char == 'ш') or (char == 'щ'):
            name_trans += ('sh')
        elif (char == 'ы'):
            name_trans += ('i')
        elif (char == 'э'):
            name_trans += ('e')
        elif (char == 'ю'):
            name_trans += ('u')
        elif (char == 'я'):
            name_trans += ('ya')
    str1 = ''.join(name_trans)
    return str1

def convertPwd(name):
    name = name.lower()
    name_trans = ''
    for char in name:
        if (char == ' '):
            break
        if (char == 'а'):
            name_trans += ('f')
        elif (char == 'б'):
            name_trans += (',')
        elif (char == 'в'):
            name_trans += ('d')
        elif (char == 'г'):
            name_trans += ('u')
        elif (char == 'д'):
            name_trans += ('l')
        elif (char == 'е') or (char == 'ё'):
            name_trans += ('t')
        elif (char == 'ж'):
            name_trans += (';')
        elif (char == 'з'):
            name_trans += ('p')
        elif (char == 'и'):
            name_trans += ('b')
        elif (char == 'й'):
            name_trans += ('q')
        elif (char == 'к'):
            name_trans += ('r')
        elif (char == 'л'):
            name_trans += ('k')
        elif (char == 'м'):
            name_trans += ('v')
        elif (char == 'н'):
            name_trans += ('y')
        elif (char == 'о'):
            name_trans += ('j')
        elif (char == 'п'):
            name_trans += ('g')
        elif (char == 'р'):
            name_trans += ('h')
        elif (char == 'с'):
            name_trans += ('c')
        elif (char == 'т'):
            name_trans += ('n')
        elif (char == 'у'):
            name_trans += ('e')
        elif (char == 'ф'):
            name_trans += ('a')
        elif (char == 'х'):
            name_trans += ('[')
        elif (char == 'ц'):
            name_trans += ('w')
        elif (char == 'ч'):
            name_trans += ('x')
        elif (char == 'ш'):
            name_trans += ('i')
        elif (char == 'щ'):
            name_trans += ('o')
        elif (char == 'ы'):
            name_trans += ('s')
        elif (char == 'э'):
            name_trans += ("'")
        elif (char == 'ю'):
            name_trans += ('.')
        elif (char == 'я'):
            name_trans += ('z')

    nmbr = ''
    for i in range(4):

        nmbr += str(randint(0, 9))

    name_trans += nmbr
    return name_trans

def genlogin(a):
    a.upper()
    try:
        if (len(a.split(' ')) == 1):
            newName = a
        else:
            flname = a.split(' ')
            newName = flname[0] + (flname[1][0].upper())

        return newName
    except:
        return a[0:-1]




def genlogin1(a):
    a.upper()
    index = a.find(' ')
    newName = ''
    for i in range(index + 2):
        if (i < (index + 1)):
            newName += a[i]
        else:
            newName += a[i].upper()
            print(a[i].upper())

    newName = newName.replace(' ', '')
    return newName
