
def statement_decorator(statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))
    return ""

feedback = "*** kapai my kahi keep going ****"
decoration = "*"

statement_decorator(feedback, decoration)
print()
statement_decorator("!! Incorrect !!", "!")