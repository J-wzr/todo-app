
def get_todos():
    with open("todos.txt") as file:
        todos = file.readlines()
    return todos