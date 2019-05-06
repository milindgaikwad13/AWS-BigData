import re


patterns = ['term1', 'term2']


text = " this is the string with term1 but not the other term"




if re.search('hello','hello world!'):
    print('pattern found')



match = re.search('hello','hello world!')

print(match.start())
print(match.end())


split_term = '@'

phrase = 'what is your email, is it hello@gmail.com?'

print(re.split(split_term,phrase))
print(phrase.split("@"))