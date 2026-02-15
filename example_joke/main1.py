from joke import get_random_joke


def main():  # Вона спочатку запитує у користувача ім'я, а потім вітає його.
    name = input("Будь ласка, введіть ваше ім'я: ")
    print(f"Привіт, {name}!")

    while (
        True
    ):  # цикл while True, програма запитує у користувача, чи хоче він почути анекдот
        user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {name}!")
            break


if (
    __name__ == "__main__"
):  # перевіряє, чи запускається файл безпосередньо, а не імпортується як модуль, і тільки в цьому випадку викликає
    main()
