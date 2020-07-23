import random

LOW = 1
HIGH= 50

how_many = 5

# question generator
for item in range(1, how_many + 1):
    num_1 = random.randint(LOW, HIGH)
    num_2 = random.randint(LOW, HIGH)

    # states question
    question = "{} + {} ".format(num_1,num_2)

    answer = int(input(question))
    right_ans = eval(question)

    # tell user if they are right
    if answer == right_ans :
        print("kapai my kahi you got it right keep going :)")

    else:
        print("!!!!sorry my g you got it wrong better luck next time!!!!")