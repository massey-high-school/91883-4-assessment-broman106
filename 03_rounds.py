# Integer checking function


#number checking function goes here
def intcheck(question, low=None, high=None):

    #sets up error messages
    if low is not None and high is not None:
            error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low,high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "please  enter an integer that is less tha or " \
                "equal to {}".format(high)
    else:
        error = "please enter an integer"

    while True:

         try:

            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

         except ValueError:
            print(error)
            continue


# *** Main Routine ****
how_many = intcheck("How many questions do you want? ", 1, 50)

lowest = intcheck("Low Number: ")
highest = intcheck("High Number: ", lowest + 1)



# answers for quiz
import random

LOW = 1
HIGH= 50

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

