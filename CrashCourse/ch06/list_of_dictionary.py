# Make an empty list for store some aliens.

aliens = []

# Make 30 green aliens.

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.

for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created.

print(f"The total number of aliens is: {len(aliens)}")

# Converting aliens to yellow.

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

green_num = 0
yellow_num = 0
red_num = 0

for alien in aliens:
    if alien['color'] == 'green':
        green_num = green_num + 1
    elif alien['color'] == 'yellow':
        yellow_num = yellow_num + 1
    elif alien['color'] == 'red':
        red_num = red_num + 1

print(f"we have:{green_num} aliens green, {yellow_num} aliens yellow and {red_num} aliens red.")