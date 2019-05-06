#
# Problems are arranged in increasing difficulty:
#
# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve
#
#

# Warmup

# LESSER OF TWO EVENS:
# Write a function that
# returns the lesser of
# two given numbers if both
# numbers are even, but returns the greater if one or both numbers are odd


def compareData(a, b):

    if a%2 ==0 and b%2 ==0:
        if a < b:
            return a
        elif b<=a :
            return b
    else:
        if a > b:
            return a
        elif b >= a:
            return b


print(compareData(3,4))




#ANIMAL CRACKERS:
# Write a function takes a two-word string and returns True if both words begin with same letter


def animal_cracker(name):
    splitlist = name.upper().split()
    if splitlist[0][0] == splitlist[1][0] :
        return True
    return False

print('animal_cracker: ' + str(animal_cracker("this Ts")))



#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
#if one of the integers is 20. If not, return False


def makes_twenty(int1, int2):
    if int1 + int2 == 20 or int1 == 20 or int2 == 20:
        return True
    return True


print('make_twenty: ' + str(makes_twenty(20,30)))




# Level1

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):

    #newstr = name[0].upper() + name[1:3] + name[3].upper() + name[4::]
    newstr = name[:3].capitalize() + name[3:].capitalize() # this is new
    return newstr


print(old_macdonald('macdonald'))


#MASTER YODA: Given a sentence, return a sentence with the words reversed

def reverseWords(name):

    #test= name.split()
    #returnString=""
    #for i in test[::-1]:
        #returnString =  returnString + i + " "

    returnString = name.split()[::-1]

    returnString =" ".join(returnString) # this is new
    return returnString

print(reverseWords("master yoda"))



#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(number1):
    if abs(100-number1)<=10 or abs(200-number1)<=10:
        return  True
    return False

print('within_numbers:')
print(almost_there(104))



#Level2:

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.


def find33(lstint):
    lstint = [1,2,5,6,3,3,6,7]
    print(lstint[1:1 + 2])
    for i in range(0, len(lstint)-1):
        if lstint[i:i+2] == [3,3]:
            return True
    return False

print('find33')
print(find33([1,2]))



#PAPER DOLL: Given a string,
# return a string where for every character in the original there are three characters

def paper_doll(strinput):
    result = ""
    for char in strinput:
        result += char *3
    return result

print(paper_doll('test'))


#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'


def blackjack(num1,num2, num3):
    lst = [num1,num2,num3]
    sm = sum(lst) # this is new
    if sm <=21:
        return sm
    elif (11 in  lst) and (sm <=31):
        return sm - 10
    return 'BUST'

print('blackjack')
print(blackjack(12,6,5))



#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


def summer_69(numlst):

    result = 0
    add = True
    for  i in numlst:
        while add:
            if (i!= 6):
                result += i
                break
            else:
                add =False
        while not add:
            if i!= 9:
                break;
            else:
                add = True
                break
    return result

print('summer_69')
print(summer_69([2,3,5,6,7,8,6,7,8,9,1]))


# challenging problem

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(lstint):
    code =[0,0,7]

    for i in lstint:
       if i == code[0]:
             code.pop(0)

    return (len(code) == 0)

print(spy_game([1,2,4,5,6,0,7,0,0,7]))


#COUNT PRIMES: Write a function that returns the number of
# prime numbers that exist up to and including a given number


def count_prime(num):
    if num <2:
        return 0
    primenumbers = [2]

    x =3
    while x <= num:
        for y in range(3,x,2):
            if(x%y ==0 ):
                x += 2
                break
        else:
            primenumbers.append(x)
            x += 2
    return(len(primenumbers))


print(count_prime(100))



#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter



