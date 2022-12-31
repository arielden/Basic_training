"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""

simple_foods = ("pasta", "sandwich", "cheesecake", "hotdog", "omelette")

# The line below shows that tuples does not support item assignment
# simple_foods[0] = "soup"

for food in simple_foods:
    print(food)
print("\n")

simple_foods = ("pasta", "sandwich", "cheesecake", "cake", "pizza")

for food in simple_foods:
    print(food)

