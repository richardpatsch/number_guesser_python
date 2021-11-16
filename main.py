import math
import random
import boto3


def generate_random_number(max):
    return random.randrange(max)

def check_number(solution, max_number, modulo, residual_class):
    for i in range(max_number):
        if i % modulo == residual_class:
            #print(i)
            if i == solution:
                return i
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max_number = int(math.pow(10, 10))
    random_number = generate_random_number(max_number)

    print('max: ', max_number)
    print('random: ', random_number)

    modulo = 3

    for i in range(modulo):
        print('mod ' + str(modulo) + ' / ' + str(i))
        result = check_number(random_number, max_number, modulo, i)
        if result:
            print('SOLUTION: ' + str(result))
            break
        else:
            print('try next')



