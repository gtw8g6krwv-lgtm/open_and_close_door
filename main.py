from door import Door


if __name__ == "__main__":
    door = Door()

print("УПРАВЛЕНИЕ ДВЕРЬЮ")
print("Доступные команды: открыть, закрыть, проверить, выход")

while True:
    command = input("\nВведите команду: ").strip().lower()

    if command == "открыть":
        door.open_door()

    elif command == "закрыть":
        door.close_door()

    elif command == "проверить":
        print(f"Дверь сейчас {door.get_door_state()}")

    elif command == "выход":
        print("До свидания")
        break
    else:
        print("Неизвестная команда! Используйте толкьо команды: открыть, закрыть, проверить, выход")
