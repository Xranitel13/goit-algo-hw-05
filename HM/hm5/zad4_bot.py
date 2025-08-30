def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, TypeError, KeyError):
            return "Enter name and phone. Example: add Aleksandra 0932223332."

    return inner
def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, TypeError, KeyError):
            return "Enter name and phone. Example: change Aleksandra 0932223331."

    return inner
def input_error_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, TypeError, KeyError):
            return "Enter person name. Example: [phone Aleksandra]."
    return inner

@input_error_add
def add_contact(contacts: list, name: str, num: str) -> str:
    if not num.isdecimal():
        raise ValueError
    for contact in contacts:
        if contact["number"] == num:
            return f"Contact with phone [{contact['number']}] already exists ({contact['name']})."
        if contact["name"] == name:
            return f"Contact [{contact['name']}] already exists ({contact['number']})."

    contacts.append({"name": name, "number": num})
    return f"Contact [{name}] added successfully with number: {num}."
@input_error_change
def change_contact(contacts:list,name: str, num: str) -> str:
    if not num.isdecimal():
        raise ValueError
    for contact in contacts:
        if contact["name"] == name:
            contact["number"] = num
            return f"Number if contact [{contact['name']}] changed to {contact['number']} "

    return f"Contact [{name}] does not exist"
@input_error_phone
def show_phone(contacts:list,name:str) -> str:
    for contact in contacts:
        if contact["name"] == name:
            return f"[{name}] number is {contact['number']}"

    return f"Contact [{name}] does not exist"

def show_all(contacts:list):
    if not contacts:
        return "No contacts."
    text = "---name----|---number---\n"
    for contact in contacts:
        t = f"{contact['name']}   :   {contact['number']}\n"
        text = text + t
    return text


def main():
    print("Welcome to the assistant bot!")
    contacts = []
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