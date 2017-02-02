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
    if leftover2 > 0:
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


def whatBases():
    # User selects initial and final base. Validity testing included.
    while True:
        msg1 = 'What base do you want to convert from and what base do you want to convert to? (e.g. to convert from decimal to binary, type: 10,2):'
        in1 = raw_input(msg1)
        bases = in1.split(',')
##        print '1bases =', bases
        if len(bases) == 2:
            for i, base in enumerate(bases):
                if not base.isdigit():
                    print 'Invalid input. Bases must be 2-36 and in format: baseA,baseB.'
                    break
                elif int(base) <2 or int(base) > 36:
                    print 'Invalid input. Bases must be 2-36'
                    break
                elif i == 1:
                    return bases
        else: # if input not in format: baseA,baseB
            print 'Invalid input. Must input two bases with values in range 2-36 '\
                  +'and in the format: x,y where x is the base of the value you '\
                  +'wish to input and y is the base you wish to convert to.'

            
def querry(baseA):
    # Where user inputs value to convert. Uses seperate func for valitity testing.
    msg2 = '\nInput value to convert:'
    number = raw_input(msg2).lower()
    if number == 'diff': # Indicates user wants to change settings.
        return 'diff'
    elif validInput(number, baseA):
        return number

    
def continue1():
    # Checks if user wants to continue at all.
    msg = "Do you want to go again? (y, n, or quit):"
    blarg = raw_input(msg)
    if blarg == 'quit':
        quit()
    return blarg


def continue2():
    # Further checks if user wants to continue doing calculations with same settings.
    msg = '\nDo you want to keep doing conversions with the same bases? '\
          +"If so, type 'same', and you can continue with these settings "\
          +" without interuption, until you type 'diff'."
    blarg = raw_input(msg)
    return blarg


def mainish(number, baseA, baseB):
    # Determines what combinations of the two main functions to use depending on
    # user input, and implements them to get an answer.
    if baseA == 10:
        part2 = dec_to_other(int(number), baseB)
    else:
        part1 = other_to_dec(number, baseA)
        part2 = dec_to_other(part1, baseB)
    return part2


##############################
# Calling the functions
# This part could certainly be improved if it ever seems like it's worth it...


intro = 'Welcome to numeric base conversion, which converts between any two '\
       +'bases in the range 2-36 (binary to hexadecimal), using the characters '\
       +'0-9 and a-f. Supports positive whole numbers only.\n'

print intro

number = 'diff'
alnums = makeAlnums() # Or could call this later, only if base>10...
while True:
    if number == 'same':
        while True:# number != 'diff':
            number = querry(baseA)
            if number == 'diff':
                break
            else:
                if number:
                    answer = mainish(number, baseA, baseB)
                    print '\nBase', str(baseA) + ':', number, '= Base', str(baseB) + ':', answer 
    bases = whatBases()
    baseA = int(bases[0])
    baseB = int(bases[1])
    number = querry(baseA)
    if number:
        answer = mainish(number, baseA, baseB)
        print '\nBase', str(baseA) + ':', number, '= Base', str(baseB) + ':', answer, '\n'
    else:
        number = 'diff'
    blarg = continue1()
    if blarg.lower().startswith('y'):
        number = continue2()
    else:
        print '\nWelcome to my idea of testing mode. If you want to know what '\
              +'funtions there are to play around with......read the code ^_^'
        break
