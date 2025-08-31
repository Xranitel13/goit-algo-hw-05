def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Phone number must be an integer."
        except TypeError:
            return "Invalid arguments."
    return inner

@input_error
def add_contact(contacts: dict, name: str, num: str) -> str:
    if not num.isdecimal():
        raise ValueError
    if num in contacts.values():
        for k, v in contacts.items():
            if v == num:
                return f"Contact with phone [{v}] already exists ({k})."
    if name in contacts:
        return f"Contact [{name}] already exists ({contacts[name]})."

    contacts[name] = num
    return f"Contact [{name}] added successfully with number: {num}."
@input_error
def change_contact(contacts:dict,name: str, num: str) -> str:
    if not num.isdecimal():
        raise ValueError
    if name in contacts:
        contacts[name] = num
        return f"Number of contact [{name}] changed to {num}"
    return f"Contact [{name}] does not exist"
@input_error
def show_phone(contacts:dict,name:str) -> str:
    if name in contacts:
        return f"[{name}] number is {contacts[name]}"
    return f"Contact [{name}] does not exist"

def show_all(contacts:dict):
    if not contacts:
        return "No contacts."
    text = "---name----|---number---\n"
    for name, num in contacts.items():
        text += f"{name}   :   {num}\n"
    return text


def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    while True:
        user_input = input("Enter a command: ")
        if not user_input.split():
            continue
        p, *args = user_input.split()
        p = p.strip().lower()
        if p == "exit" or p == "close":
            print("Goodbye")
            return
        elif p == "hello":
            print("How can I help you?")
        elif p == "add":
            print(add_contact(contacts, *args))
        elif p == "change":
            print(change_contact(contacts, *args))
        elif p == "phone":
            print(show_phone(contacts, *args))
        elif p == "all":
            print(show_all(contacts))
        else:
            print("Invalid command")



if __name__ == "__main__":
    main()