from door import Door


if __name__ == "__main__":
    door = Door()

open_door_users_massege = "открыть"
close_door_users_massege = "закрыть"
check_door_users_massege = "проверить"
enter_system_door_users_massege = "выход"
goodbye_users_massege = "До свидания"

print("УПРАВЛЕНИЕ ДВЕРЬЮ")
print(f"Доступные команды: {open_door_users_massege}, {close_door_users_massege}, {check_door_users_massege}, {enter_system_door_users_massege}")

while True:
    user_command = input("\nВведите команду: ").strip().lower()

    if user_command == open_door_users_massege:
        door.open_door()

    elif user_command == close_door_users_massege:
        door.close_door()

    elif user_command == check_door_users_massege:
        print(f"Дверь сейчас {door.get_door_state()}")

    elif user_command == enter_system_door_users_massege:
        print(goodbye_users_massege)
        break
    else:
        print(f"Неизвестная команда! Используйте толкьо команды: {open_door_users_massege}, {close_door_users_massege}, {check_door_users_massege}, {enter_system_door_users_massege}")
