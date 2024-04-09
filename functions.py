FILE_NAME = "todos.txt"


# Try to create the file if it doesn't exist
def create_file(file_name=FILE_NAME):
    try:
        file = open(file_name, 'x')
    except FileExistsError:  # read file if it exists
        pass
    else:
        file.close()


def read_todos(filename=FILE_NAME):
    with open(filename, 'r') as file:
        return file.readlines()


def write_todos(todos, filename=FILE_NAME):
    with open(filename, 'w') as file:
        file.writelines(todos)


def display_list(item_list, is_title: bool = True):
    for i, _ in enumerate(item_list):
        if is_title:
            _ = _.capitalize()
        print(f"{i + 1}. {_.strip()}")


def display_existing_todos(todos):
    print("-" * 20, "Here are your existing todos: ", sep="\n")
    display_list(todos)
    print("-" * 20)


def get_todo_from_file():
    todos = read_todos()
    return todos


def get_user_input(user_input):
    parsed = user_input.lower().strip().split(maxsplit=1)
    action = ""
    todo = ""

    try:
        action = parsed[0]
        todo = parsed[1] + "\n"
    except IndexError:
        pass

    result = {'is_empty': (user_input == ""),
              'action': action,
              'todo': todo
              }

    return result


if __name__ == "__main__":
    print("Hello")
    print(get_todo_from_file())
