from door import Door


if __name__ == "__main__":
    door = Door()

OPEN_DOOR_USERS_COMMAND = "открыть"
CLOSE_DOOR_USERS_COMMAND = "закрыть"
CHECK_DOOR_USERS_COMMAND = "проверить"
ENTER_SYSTEM_DOOR_USERS_COMMAND = "выход"
GOODBYE_USERS_COMMAND = "До свидания"

print("УПРАВЛЕНИЕ ДВЕРЬЮ")
print(f"Доступные команды: {OPEN_DOOR_USERS_COMMAND}, {CLOSE_DOOR_USERS_COMMAND}, {CHECK_DOOR_USERS_COMMAND}, {ENTER_SYSTEM_DOOR_USERS_COMMAND}")

while True:
    user_command = input("\nВведите команду: ").strip().lower()

    if user_command == OPEN_DOOR_USERS_COMMAND:
        door.open_door()

    elif user_command == CLOSE_DOOR_USERS_COMMAND:
        door.close_door()

    elif user_command == CHECK_DOOR_USERS_COMMAND:
        print(f"Дверь сейчас {door.get_door_state()}")

    elif user_command == ENTER_SYSTEM_DOOR_USERS_COMMAND:
        print(GOODBYE_USERS_COMMAND)
        break
    else:
        print(f"Неизвестная команда! Используйте толкьо команды: {OPEN_DOOR_USERS_COMMAND}, {CLOSE_DOOR_USERS_COMMAND}, {CHECK_DOOR_USERS_COMMAND}, {ENTER_SYSTEM_DOOR_USERS_COMMAND}")
