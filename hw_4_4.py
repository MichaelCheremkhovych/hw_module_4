contacts = {} # Створюємо порожній словник для зберігання контактів

def parse_input(command): # Функція для розбору введеної команди
    parts = command.split() # Розбиваємо введений рядок на окремі частини
    if len(parts) < 1: # Перевіряємо, чи введена команда не пуста
        return None, []
    
    return parts[0].lower(), parts[1:] # Повертаємо перше слово в нижньому регістрі як дію, а решту як аргументи


def add_contact(name, phone_number): # Функція для додавання контакту
    contacts[name] = phone_number # Додаємо ім'я та номер телефону в словник контактів
    print("Contact added.") # Виводимо повідомлення про успішне додавання контакту


def change_contact(name, new_phone_number): # Функція для зміни номеру телефону контакту
    if name in contacts: # Перевіряємо, чи існує контакт з таким ім'ям
        contacts[name] = new_phone_number # Змінюємо номер телефону для вказаного контакту
        print("Contact updated.") # Виводимо повідомлення про успішну зміну контакту
    else:
        print("Contact not found.") # Виводимо повідомлення, якщо контакт не знайдено


def show_phone(name): # Функція для відображення номеру телефону контакту
    if name in contacts: # Перевіряємо, чи існує контакт з таким ім'ям
       print(contacts[name]) # Виводимо номер телефону вказаного контакту
    else:
       print("Contact not found.") # Виводимо повідомлення, якщо контакт не знайдено


def show_all(): # Функція для відображення усіх контактів
    for name, phone_number in contacts.items(): # Проходимося по всім парам (ім'я, номер телефону) у словнику контактів
        print(f"{name}: {phone_number}") # Виводимо ім'я та номер телефону кожного контакту


def main(): # Основна функція, яка керує виконанням програми
    print("Welcome to the assistant bot!") # Виводимо привітальне повідомлення
    # Безкінечний цикл для обробки команд користувача
    while True:
        command = input("Enter command: ") # Очікуємо введення команди від користувача
        action, args = parse_input(command) # Розбираємо введену команду на дію та аргументи
        if action == "exit" or action == "close": # Виконуємо відповідну дію в залежності від команди
            print("Good bye!") # Виводимо прощальне повідомлення та завершуємо програму
            break
        elif action == "hello":
            print("How can I help you?") # Виводимо запитання "How can I help you?"
        elif action == "add":
            if len(args) != 2: # Додаємо контакт за введеними аргументами
                print("Invalid arguments for 'add' command.")
            else:
                add_contact(args[0], args[1])
        elif action == "change":
            if len(args) != 2: # Змінюємо контакт за введеними аргументами
                print("Invalid arguments for 'change' command.")
            else:
                change_contact(args[0], args[1])
        elif action == "phone":
            if len(args) != 1: # Виводимо номер телефону за введеним аргументом
                print("Invalid arguments for 'phone' command.")
            else:
                show_phone(args[0])
        elif action == "all":
            show_all() # Виводимо усі контакти
        else:
            print("Unknown command.") # Виводимо повідомлення про невідому команду

if __name__ == "__main__": # Перевіряємо, чи цей файл є головним, і викликаємо основну функцію
    main()
