movies = ["The Holy Grail", 1975, "Terry Jones & Terry Giliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

#This way the code only fix the print for the first nested list.
print("Printing until the first nested list.\n")
#--------------------------------------------------
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)
print("\n")
#--------------------------------------------------

#This way the code prints all the nested list, but using several lines to do the task.
print("Printing first and second nested lists.\n")
#--------------------------------------------------
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
print("\n")
#--------------------------------------------------