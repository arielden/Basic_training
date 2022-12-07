alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
# The line below overrides the value for the key 'speed' previously setted.
alien_0['speed'] = 'medium'

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


# If i delete the key 'y_position' and then I call it using brackets, I'll get an error.
del alien_0['y_position']

#print(alien_0['y_position'])

# To avoid the error presented above, I'll call the key using get()
ypos = alien_0.get('y_position', 'Y position is not available')
print(ypos)
