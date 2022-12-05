alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print(f"Original position is {alien_0['x_position']}")

# Move the alien to the right
#The next llop determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The new position is {alien_0['x_position']}")
