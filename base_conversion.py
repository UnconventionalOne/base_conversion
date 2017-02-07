################################################################################
# Conversion functions 


# Input value as sting and base as integer
def other_to_dec(value, base):
    # Converts any supported base to base-10
    chars = [x for x in value]
    chars.reverse()
##    print 'reversed chars =', chars
    dec = 0
    for i, char in enumerate(chars):
        if char.isalpha():
            char = alnums[char]
##        print dec
        dec = dec + (int(char) * base**i)
    return dec


# Input values as integers
def dec_to_other(number, base):
    # Converts base-10 to any other supported base
    fin = []
    div = number / base
    leftover1 = number % base
##    print 'number =', number, 'leftover =', leftover1
    fin.append(leftover1)
    leftover2 = div % base
##    print 'div =', div, 'leftover =', leftover2
    if div != 0:
        fin.append(leftover2)
    while div >= base:
        div = div /base
        leftover = div % base
##        print 'div =', div, 'leftover =', leftover
        fin.append(leftover)
##    print 'Final integer list in reverse order:', fin
    if base > 10:
        for j, char in enumerate(fin):
            if char > 9:
                fin[j] = alnums[char]
    fin.reverse()
    final = [str(x) for x in fin]
    if base <=  10:
        return int(''.join(final))
    else:
        return ''.join(final)


def makeAlnums():
    # Makes dict of numeric values to use for all letters in the alphabet
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abcnums = range(10, 36)
    alnums = dict(zip(abc, abcnums))
    temp_dict = dict(zip(abcnums, abc))
    alnums.update(temp_dict)
    return alnums


################################################################################
# Support functions

def validInput(value, baseA):
    # Assures that the user input value-to-convert is valid for the base selected
    # In general, no values can be larger than (base - 1)
    if not value.isalnum():
        print 'Invalid input. The input must be alphanumeric.'
        return False
    elif baseA <= 10: 
        for val in value:
            if (val.isdigit() and int(val) >= baseA) or val.isalpha():
                print 'Invalid input. The character', val, 'is not base-' + str(baseA)
                return False
    else: # if base > 10
        for val in value:
            if val.isdigit():
                # if int, valid int?
                if int(val) >= baseA:                
                    print 'Invalid input. The number', val, 'is too large for base-' + str(baseA)
                    return False
            elif (not val.isalpha()) or (val > alnums[baseA-1]): # since 'a'<'b'...<'z'
                # if letter, valid letter?
                print 'Invalid input. The character', val, 'is not base-' + str(baseA)
                return False
    return True      


def validBases(bases):
    # Validity testing for user selected initial and final base.
    if len(bases) == 2:
        for i, base in enumerate(bases):
            if not base.isdigit():
                print 'Invalid input. Bases must be 2-36 and in format: baseA,baseB.'
                return False
            elif int(base) <2 or int(base) > 36:
                print 'Invalid input. Bases must be 2-36'
                return False
    else: # if input not in format: baseA,baseB
        print 'Invalid input. Must input two bases with values in range 2-36 '\
              +'and in the format: x,y where x is the base of the value you '\
              +'wish to input and y is the base you wish to convert to.'
    return True


def querry(Type, baseA = None):
    # Handles all querries
    while True:
        msg1 = 'Input bases (baseA,baseB):'
        msg2 = '\nInput value to convert:'
        if Type == 'bases':
            value = raw_input(msg1)
            if value == '@help':
                Help()
            elif value == '@quit':
                quit()
            else:
                bases = value.split(',')
                if validBases(bases):
                    intbases = [int(x) for x in bases]
                    return intbases
        else:
            value = raw_input(msg2)
            if value == '@help':
                Help()
            elif value == '@diff':
                return value
            elif value == '@quit':
                quit()
            elif validInput(value, baseA):
                return value


def Help():
    # Some potentially helpful info
    print '\n' + '*'*40 + '\nWelcome to the help doc for Base Conversion.'
    print 'For information on how to use this tool, type "how".'
    print 'To see the intro again, type "intro".'
    print 'For a reminder of all commands, type "commands".'
    print 'To exit help, type "exit".'
    while True:
        stuff = raw_input().lower()
        if stuff == 'exit':
            print '*'*40 + '\n'
            break
        elif stuff == 'how':
            print 'To convert a number, first input the bases you want to '\
                  +'convert from (baseA) and to (baseB) in the form: baseA,baseB.'\
                  +' Then simply input the number to convert, when prompted.\n'\
                  +'Once base settings are set, they are maintained untill changed.'\
                  +' You can change them by typing "@diff".'
        elif stuff == 'commands':
            print '"@help" to get back to help.\n' +\
                  '"@diff" to change base conversion settings.\n' +\
                  '"@quit" to quit.'
        elif stuff == 'intro':
            print intro
            

def mainish(number, baseA, baseB):
    # Determines what combination of the two main functions to use depending on
    # user input, and implements them to get an answer.
    if baseA == 10:
        part2 = dec_to_other(int(number), baseB)
    elif baseB == 10:
        part2 = other_to_dec(number, baseA)
    else:
        part1 = other_to_dec(number, baseA)
        part2 = dec_to_other(part1, baseB)
    return part2


##############################
# Calling the functions


intro = 'Welcome to numeric base conversion, which converts between any two '\
       +'bases in the range 2-36 (binary to hexatrigesimal), using the characters '\
       +'0-9 and a-z. Supports positive whole numbers only. \nType "@help" at any '\
       +'time for the help doc.\n'
global intro
print intro

number = '@diff'
alnums = makeAlnums() 
while True:
    if number == 'same':
        while True:
            number = querry('other', baseA)
            if number == '@diff' or not number:
                break
            else:
                answer = mainish(number, baseA, baseB)
                print '\nBase', str(baseA) + ':', number, '= Base', str(baseB) + ':', answer
    baseA, baseB = querry('bases')
    number = querry('other', baseA)
    if number:
        answer = mainish(number, baseA, baseB)
        print '\nBase', str(baseA) + ':', number, '= Base', str(baseB) + ':', answer, '\n'
        number = 'same'
    else:
        number = '@diff'
