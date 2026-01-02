"""
Mad Libs
"""

# Todo: prompt the user to provide the missing words

text = """
Roses are {colour},
Violets are blue,
Sugar is {adjective},
And so are you!
"""

colour = input("Enter a colour: ")
adjective = input("Enter an adjective: ")
# Todo: print the final text
print(text.format(colour=colour, adjective=adjective))