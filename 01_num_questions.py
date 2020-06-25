# Integer checking function
def intcheck(question, low, high):
    valid = False
    error = "please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                 return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# *** Main Routine ****
how_many = intcheck("How many questions to you want? ", 1, 50)

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

lowest = intcheck("Low Number: ")
highest = intcheck("High Number: ", lowest + 1)