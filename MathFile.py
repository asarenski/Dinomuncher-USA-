'''
For Dinomuncher USA!

This file holds all the math stuff as well as the number generation.
'''
import random

class Mathfile():
    def __init__(self,num_list):
        self.num_list = num_list
        self.op_number = 0
        self.op_number2 = 0
        self.op_type = Multiples
        for i in range(30):
            number = random.randrange(1,81)
            self.num_list.append(number)
        self.op_number = random.randrange(2,9)
        self.op_number2 = random.randrange(2,9)


class Multiples(Mathfile):
    def create_list(self):
        multiple_of = self.op_number
        for i in range(4):
            n = self.num_list[i]
            r = n % multiple_of
            while r!=0:
                n = random.randrange(1,81)
                r = n % multiple_of
                self.num_list[i] = n
        random.shuffle(self.num_list)

class Multiplication(Mathfile):
    def create_list(self):
        for i in range(4):
            n = self.num_list[i]
            while n!=self.op_number*self.op_number2:
                n = random.randrange(1,81)
                self.num_list[i] = n
        #random.shuffle(self.num_list)

def math_main(op_type): #note that op_type must be a string to work
    num_list = [] # initializes the num_list in this instance
    op_number = 0 # initializes op_number in this instance
    op_number2 = 0

    if op_type == "Multiples":
        multi_instance = Multiples(num_list)
        multi_instance.create_list()
        op_number = multi_instance.op_number # sets op_number equal to the one in the Multiples instance
        op_number2 = multi_instance.op_number2
    if op_type == "Multiplication":
        multic_instance = Multiplication(num_list)
        multic_instance.create_list()
        op_number = multic_instance.op_number # sets op_number equal to the one in the Multiples instance
        op_number2 = multic_instance.op_number2

    print num_list
    print op_number
    print op_number2

    return (num_list,op_number,op_number2)
math_main("Multiples")