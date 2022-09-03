import random
import inflect

fname = open('output.txt', 'w')

def default(x):
    xy = str(x)
    fname.write(xy)
    fname.write('\n')
    i = 0
    while i != 3:
        rand = random.randint(1000, 9999)
        rx = str(rand)
        fname.write(rx)
        fname.write('\n')
        i = i+1
    fname.write('\n')

def numerals():
    fname.write('Write the numerals for the given numbers\n')
    i = 0
    while i != 3:
        rand = random.randint(1000, 9999)
        p = inflect.engine()
        x = p.number_to_words(rand)
        rx = str(x)
        fname.write(rx)
        fname.write('\n')
        i = i+1
    fname.write('\n')

def main():
    default('Write the number names for the following: ')
    default('Expand the numbers: ')
    default('What comes after: ')
    default('What comes before: ')
    numerals()

main()