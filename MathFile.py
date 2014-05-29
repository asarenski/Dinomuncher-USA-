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

class Division(Mathfile):
    def create_list(self):
        multiplication_table = []
        self.op_number = random.randrange(3,11)
        for i in range(3,11):
            for j in range (3,11):
                multiplication_table.append(i*j)
        for i in range(30):
            number = random.choice(multiplication_table)
            number2 = random.randrange(1, 11)
            self.num_list.append(number)
            self.num_list2.append(number2)

        #makes sure the first 4 entries satisfy op
        for i in range(4):
            x = self.num_list[i]
            y = self.num_list2[i]
            while self.num_list2[i] * self.op_number != self.num_list[i]:
                y = random.randrange(1,11)
                x = self.op_number * y
                self.num_list[i] = x
                self.num_list2[i] = y

        #marks the numbers
        for i in range(30):
            if self.num_list[i] // self.num_list2[i] == self.op_number \
                                  and self.num_list[i] % self.num_list2[i] == 0:
                self.number_marker.append(1)
            else:
                self.number_marker.append(0)
        self.shuffle_the_list()
        self.create_dict()

class Addition(Mathfile):
    def create_list(self):
        addition_table = []
        for i in range(1,11):
            for j in range (1,11):
                addition_table.append(i+j)
        self.op_number = random.choice(addition_table)
        for i in range(30):
            number = random.randrange(1,11)
            number2 = random.randrange(1, 11)
            self.num_list.append(number)
            self.num_list2.append(number2)
        for i in range(4):
            x = self.num_list[i]
            y = self.num_list2[i]
            while self.num_list[i] + self.num_list2[i] != self.op_number:
                y = random.randrange(1,11)
                x = self.op_number - y
                self.num_list[i] = x
                self.num_list2[i] = y
        for i in range(30):
            if self.num_list[i] + self.num_list2[i] == self.op_number:
                self.number_marker.append(1)
            else:
                self.number_marker.append(0)
        self.shuffle_the_list()
        self.create_dict()

class Subtraction(Mathfile):
    def create_list(self):
        addition_table = []
        for i in range(1,25):
            for j in range (1,25):
                addition_table.append(i+j)
        self.op_number = random.choice(addition_table)
        for i in range(30):
            number = random.randrange(3,50)
            number2 = random.randrange(1, 20)
            self.num_list.append(number)
            self.num_list2.append(number2)
        for i in range(4):
            x = self.num_list[i]
            y = self.num_list2[i]
            while self.num_list2[i] + self.op_number != self.num_list[i] :
                y = random.randrange(1,20)
                x = self.op_number + y
                self.num_list[i] = x
                self.num_list2[i] = y
        for i in range(30):
            if self.num_list[i] - self.num_list2[i] == self.op_number:
                self.number_marker.append(1)
            else:
                self.number_marker.append(0)
        self.shuffle_the_list()
        self.create_dict()

def math_main(op_type): #note that op_type must be a string to work
    op_type = op_type
    # selection for Multiples operation
    if op_type == "Multiples":
        op_instance = Multiples()
    # selection for Multiplication operation
    elif op_type == "Multiplication":
        op_instance = Multiplication()
    elif op_type == "Division":
        op_instance = Division()
    elif op_type == "Addition":
        op_instance = Addition()
    elif op_type == "Subtraction":
        op_instance = Subtraction()


    op_instance.create_list()
    num_list = op_instance.num_list
    num_list2 = op_instance.num_list2 # sets op_number equal to the one in the Multiples instance
    op_number = op_instance.op_number
    number_marker = op_instance.number_marker
    num_dict = op_instance.num_dict

    #print num_dict
    return (num_dict) # returns the entire num_dict