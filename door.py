class Door:
    def __init__(self):
        self.__is_open = False

    def open_door(self):
        if not self.__is_open:
            self.__is_open = True
            print("Дверь открыта!")
        else:
            print("Дверь уже открыта")

    def close_door(self):
        if self.__is_open:
            self.__is_open = False
            print("Дверь закрыта")
        else:
            print("Дверь уже закрыта")

    def check_open_door(self):
        return self.__is_open

    def get_door_state(self):
        if self.__is_open:
            return "Открыта"
        else:
            return "Закрыта"