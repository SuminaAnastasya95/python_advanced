from typing import Protocol
from datetime import date


class Room:
    """Комнаты"""

    def __init__(self, number: int, price: float, room_type: str):
        self.number = number
        self.price = price
        self.type = room_type
        self.is_booked = False
        self.date_from = None
        self.date_to = None
        # При создании любой комнаты она попадает в общий список

    # Метод представления, чтобы при print([объект]) видеть данные, а не адрес в памяти
    def __repr__(self):
        status = "Занят" if self.is_booked else "Свободен"
        return f"Room({self.number} - {status})"


class LuxeRoom(Room):
    """Люксовые номера"""

    def mult_room(self, grade: float):
        if self.type.lower() == "luxe":
            return self.price * grade
        return self.price


class Booking:
    """Бронирование/ отмена бронирования"""

    @staticmethod
    def booking_on(room: Room, date_from: date, date_to: date):
        """Бронирование с проверкой пересечения дат"""

        # 1. Проверяем корректность дат
        if date_from >= date_to:
            return "Ошибка: дата начала должна быть раньше даты окончания"

        # 2. Если номер уже занят — проверяем пересечение дат
        if room.is_booked:
            # Проверка пересечения: новое бронирование НЕ должно пересекаться с существующим
            if date_from < room.date_to and date_to > room.date_from:
                return f"Номер {room.number} занят в даты: {room.date_from} - {room.date_to}"

        # 3. Если номер свободен ИЛИ даты не пересекаются — бронируем
        room.is_booked = True
        room.date_from = date_from
        room.date_to = date_to
        return f"Вы забронировали номер {room.number} на даты: {date_from} - {date_to}"

    @staticmethod
    def booking_off(room: Room):
        """Отмена бронирование"""
        if room.is_booked:
            cancel_date = date.today()
            room.is_booked = False
            room.date_from = None
            room.date_to = None
            return f"Отмена бронирования. Номер - {room.number}, в даты - {cancel_date}"
        else:
            return f"Номер {room.number} не был забронирован"


class Hotel:
    """Отель — это отдельный класс. Он управляет списком комнат."""

    def __init__(self):
        self.room_list: list[Room] = []

    def add_room(self, room: Room):
        self.room_list.append(room)

    def get_available_rooms(self, room: Room, start_date: date, end_date: date):
        free_rooms = []
        for r in self.room_list:
            if not room.is_booked:
                free_rooms.append(room)
            elif not (start_date < room.date_to and end_date > room.date_from):
                free_rooms.append(room)
        return free_rooms

    def get_list_rooms(self):
        return self.room_list

    def get_booking_rooms(self):
        booked = [r for r in self.room_list if r.is_booked]
        return booked


hotel = Hotel()
r1 = Room(101, 5000, "Luxe")
r2 = Room(102, 2000, "Simple")
r3 = Room(103, 2000, "Simple")
r4 = Room(104, 2000, "Simple")

# Добавили номера
hotel.add_room(r1)
hotel.add_room(r2)
hotel.add_room(r3)
hotel.add_room(r4)

# Отображение свободных номеров
print(hotel.get_list_rooms())

# # Бронируем номер 101 с 1 по 5 марта
print(Booking.booking_on(r1, date(2025, 3, 1), date(2025, 3, 5)))

print(hotel.get_list_rooms())
# # Пытаемся забронировать тот же номер на пересекающиеся даты
print(Booking.booking_on(r1, date(2025, 3, 3), date(2025, 3, 7)))  # Ошибка

# # Бронируем на непересекающиеся даты
print(Booking.booking_on(r1, date(2025, 3, 10), date(2025, 3, 15)))  # Успех

print(Booking.booking_on(r2, date(2025, 3, 10), date(2025, 3, 15)))

# # Проверяем свободные номера
print(hotel.get_booking_rooms())
# # Вывод: [Room(102 - Свободен)]


print(Booking.booking_off(r1))
print(hotel.get_list_rooms())
