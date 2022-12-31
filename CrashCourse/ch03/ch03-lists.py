"""
Exercise Chapter 3, page 42.
Creating and modifying a list
"""

people = ['albert', 'john', 'george', 'paul']

print("\n" f"Hi {people[0].title()}, you're invited to dinner!")
print(f"Hi {people[1].title()}, you're invited to dinner!")
print(f"Hi {people[2].title()}, you're invited to dinner!")
print(f"Hi {people[3].title()}, you're invited to dinner!\n")

N = 2
non_assistant = people[N]
people.remove(non_assistant)
print(f"We'll miss you this night {non_assistant.title()}\n")

people.insert(N, 'emerson')

print("Messages for the new list:\n")
print(f"Hi {people[0].title()}, you're invited to dinner!")
print(f"Hi {people[1].title()}, you're invited to dinner!")
print(f"Hi {people[2].title()}, you're invited to dinner!")
print(f"Hi {people[3].title()}, you're invited to dinner!\n")

print('I found a bigger table for this night!\n')

people.insert(0, 'lyle')
people.insert(int(1 + len(people)/2), 'james')
people.append('alex')

invited_num = len(people)

print(f"Hi {people[0].title()}, you're invited to dinner!")
print(f"Hi {people[1].title()}, you're invited to dinner!")
print(f"Hi {people[2].title()}, you're invited to dinner!")
print(f"Hi {people[3].title()}, you're invited to dinner!")
print(f"Hi {people[4].title()}, you're invited to dinner!")
print(f"Hi {people[5].title()}, you're invited to dinner!")
print(f"Hi {people[6].title()}, you're invited to dinner!")