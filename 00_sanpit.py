import random

a = random.randint(1, 5)
b = random.randint(1, 5)

question = "{} + {}".format(a, b)
answer = eval(question)

ask = int(input(question))
print("question", question)
print("answer", answer)