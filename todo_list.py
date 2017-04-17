# make a list to hold onto items
todo_list = []

# print out the list
def show_list():
    print("Here's your list:")

    for item in todo_list:
        print(item.upper())

# add new items to list
def add_to_list(new_item):
    try:
        todo_list.append(new_item)
    except IndexError:
        print("The list only has " + len(todo_list) + " items! Please try again.")
    else:
        print(("Added {} to list; list now has {} items").format(new_item, len(todo_list)))

# print out instructions on how to use the app
def show_help():
    print("Enter 'HELP' to request instructions")
    print("Enter 'SHOW' to see what the list contains")
    print("Enter 'DELETE' to show list and delete a task")
    print("Enter 'DONE' to stop adding items and save as a .txt file.")
    print("""
Enter tasks to add to the list""")


def main():
    show_help()

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == "DONE":
            break

        # be able to show shopping list while entering items
        elif new_item == "SHOW":
            print('; '.join(todo_list).upper())
            continue

        # be  able to show instructions while entering items
        elif new_item == "HELP":
            show_help()
            continue

        # be able to delete an item from the list
        elif new_item == "DELETE":
            print(todo_list)
            try:
                item_value = int(input("What item would you like to delete (enter integer value for item index in list, starting from item 1 = 0)? "))
                print("Item at index " + str(item_value) + " of list deleted.")
                del todo_list[item_value]
                continue
            except ValueError:
                print("That's not an integer value, please enter the 'DELETE' command again." )
            except IndexError:
                print("There's no item with an index of that integer value, please enter the 'DELETE' command again")
            continue
        add_to_list(new_item)

    show_list()

main()

# be able to save list
with open("todo_list.txt", "w") as out_file:
    print("Here's your list: ", file = out_file)
    for item in todo_list:
        print("* " + item.upper(), file = out_file)