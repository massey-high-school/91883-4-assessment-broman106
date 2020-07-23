


import random

LOW = 1
HIGH= 50

how_many = 8

for item in range(1, how_many + 1):
    num_1 = random.randint(LOW, HIGH)
    num_2 = random.randint(LOW, HIGH)

    question = "{} + {} ".format(num_1,num_2)

    answer = int(input(question))
    right_ans = 10

    # tell user if they are right

