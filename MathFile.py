'''
For Dinomuncher USA!

This file holds all the math stuff as well as the number generation.
'''
import random

class Mathfile():
    def __init__(self,num_list):
        self.num_list = num_list
        self.op_number = 0
        for i in range(30):
            number = random.randrange(1,81)
            self.num_list.append(number)


class Multiples(Mathfile):
    def create_list(self):
        multiple_of = random.randrange(2, 9)
        self.op_number = multiple_of
        for i in range(4):
            n = self.num_list[i]
            r = n % multiple_of
            while r!=0:
                n = random.randrange(1,81)
                r = n % multiple_of
                self.num_list[i] = n
        random.shuffle(self.num_list)

def math_main():
    num_list = [] # initializes the num_list in this instance
    op_number = 0 # initializes op_number in this instance

    multi_instance = Multiples(num_list)
    multi_instance.create_list()
    op_number = multi_instance.op_number # sets op_number equal to the one in the Multiples instance

    return (num_list,op_number)
