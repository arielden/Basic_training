movies = ["The Holy Grail", 1975, "Terry Jones & Terry Giliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#--------------------------------------------------
print("Using a recursive function!")

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)