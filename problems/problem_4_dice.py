"""
Simulate rolling 2 dice
"""

# Todo: Get two random integers between 1 and 6 (inclusive)
import random

value_1 = random.randint(1, 6)
value_2 = random.randint(1, 6)

print(f"You rolled a {value_1} and {value_2} (total: {value_1 + value_2})")
