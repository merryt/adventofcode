import math

def original_fuel_needed(weight):
    if(weight < 0):
        return 0
    return math.floor(weight/3) - 2

def fuel_needed(weight):
    current_fuel_need = math.floor(weight/3) - 2
    if(current_fuel_need < 0):
        return 0

    return current_fuel_need + fuel_needed(current_fuel_need)



def question1(filename):
    question1_data = open(filename,"r")
    counter = 0
    for line in question1_data.read().splitlines():
        counter += original_fuel_needed(int(line))
    return counter

def question2(filename):
    question1_data = open(filename,"r")
    counter = 0
    for line in question1_data.read().splitlines():
        counter += fuel_needed(int(line))
    return counter


print(question2("prob1_input.txt"))
