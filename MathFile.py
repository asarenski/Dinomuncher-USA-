'''
For Dinomuncher USA!

This file holds all the math stuff as well as the number generation.
'''
import random

class Mathfile():
    def __init__(self):
        self.num_list = []
        self.num_list2 = []
        self.op_number = 0
        self.number_marker = []
        self.shuffle_list = []
        self.num_dict = {}

    def shuffle_the_list(self):
        for i in range(30):
            self.shuffle_list.append((self.num_list[i], self.num_list2[i],self.op_number,self.number_marker[i]))
        random.shuffle(self.shuffle_list)

    def create_dict(self):
        for i in range(30):
            self.num_dict[i]=self.shuffle_list[i]

class Multiples(Mathfile):
    #this function begins to create the list
    def create_list(self):
        # Multiples only needs one op_number, this is random
        self.op_number = random.randrange(2,9)

        # Multiples only needs one num_list, iterative loop to create randoms
        for i in range(30):
            number = random.randrange(1,81)
            self.num_list.append(number)
            self.num_list2.append(0)

        # makes sure first four entries satisfy equation num_list[i] % op_number == 0
        for i in range(4):
            n = self.num_list[i]
            r = n % self.op_number
            while r!=0:
                n = random.randrange(1,81)
                r = n % self.op_number
                self.num_list[i] = n
        #marks the numbers
        for i in range(30):
            if self.num_list[i] % self.op_number == 0:
                self.number_marker.append(1)
            else:
                self.number_marker.append(0)
        self.shuffle_the_list()
        self.create_dict()

class Multiplication(Mathfile):
    def create_list(self):
        # creates a multiplication table to choose a op_number from
        multiplication_table = []
        for i in range(2,11):
            for j in range (2,11):
                multiplication_table.append(i*j)
        self.op_number = random.choice(multiplication_table)

        #initial random gen
        for i in range(30):
            number = random.randrange(1, 11)
            number2 = random.randrange(1, 11)
            self.num_list.append(number)
            self.num_list2.append(number2)

        #makes sure the first 4 entries satisfy x * y == self.op_number
        for i in range(4):
            x = self.num_list[i]
            y = self.num_list2[i]
            while x * y != self.op_number:
                x = random.randrange(1,11)
                y = random.randrange(1,11)
                self.num_list[i] = x
                self.num_list2[i] = y

        #marks the numbers
        for i in range(30):
            if self.num_list[i] * self.num_list2[i] == self.op_number:
                self.number_marker.append(1)
            else:
                self.number_marker.append(0)
        self.shuffle_the_list()
        self.create_dict()


def math_main(op_type): #note that op_type must be a string to work

    # selection for Multiples operation
    if op_type == "Multiples":
        multi_instance = Multiples()
        multi_instance.create_list()
        num_list = multi_instance.num_list
        num_list2 = multi_instance.num_list2
        op_number = multi_instance.op_number # sets op_number equal to the one in the Multiples instance
        number_marker = multi_instance.number_marker
        num_dict = multi_instance.num_dict

    # selection for Multiplication operation
    if op_type == "Multiplication":
        multic_instance = Multiplication()
        multic_instance.create_list()
        num_list = multic_instance.num_list
        num_list2 = multic_instance.num_list2 # sets op_number equal to the one in the Multiples instance
        op_number = multic_instance.op_number
        number_marker = multic_instance.number_marker
        num_dict = multic_instance.num_dict

    return (num_dict) # returns the entire num_dict