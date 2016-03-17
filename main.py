from __future__ import division
import sys

def tip_calculator(a, b):
    while True:
        tip = (a * b) / 100
        total = a + tip
        print 'The total amount of your bill is {0}, with the tip amount being {1}.'.format(total, tip)
        inp = raw_input('Press [Y] to enter in new bill, or [N] to exit!: ').lower()
        if inp == 'y':
            pricing()
            break
        elif inp == 'n':
            sys.exit()
        else:
            print 'Not a valid command.'
            continue

def pricing():
    print 'Welcome to the Pydive Tip Calculator.'
    while True:
        inp_a = input('Please enter the price of your meal: ')
        if inp_a != 0:
            inp_b = input('Please enter desired tip percentage in whole integers: ')
            if inp_b != 0:
                tip_calculator(inp_a, inp_b)

if __name__ == '__main__':
    pricing()
