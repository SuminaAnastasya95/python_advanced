from typing import Protocol
from datetime import date


class Room:
    """Комнаты"""
    room_list = []

    def __init__(self, number: int, price: float, room_type: str):
        self.number = number
        self.price = price
        self.type = room_type
        self.is_booked = False
        self.booking_date = None
        # При создании любой комнаты она попадает в общий список
        Room.room_list.append(self)

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


class Booking(Protocol):
    """Бронирование/ отмена бронирования"""
    @staticmethod
    def booking_on(room: Room): ...

    def booking_off(room: Room): ...


class Hotel:
    """Отель — это отдельный класс. Он управляет списком комнат."""

    @staticmethod
    def booking_on(room: Room):
        """Бронирование"""
        if not room.is_booked:
            room.is_booked = True
            room.booking_date = date.today()
            return f"Номер забронирован- {room.number}, в даты - {room.booking_date}"
        else:
            return f"Номер {room.number} уже занят"

    @staticmethod
    def booking_off(room: Room):
        """Отмена бронирование"""
        if room.is_booked:
            cancel_date = date.today()
            room.is_booked = False
            room.booking_date = None
            return f"Отмена бронирования. Номер - {room.number}, в даты - {cancel_date}"
        else:
            return f"Номер {room.number} не был забронирован"

    def get_list_rooms(self):
        return Room.room_list

    def get_booking_rooms(self):
        booked = [r for r in Room.room_list if r.is_booked]
        return booked


hotel = Hotel()
r1 = Room(101, 5000, "Luxe")
r2 = Room(102, 2000, "Simple")

# 2. Используем класс Booking как инструмент
print(Hotel.booking_on(r1))
print(Hotel.booking_on(r1))  # Повторная попытка

# 2. Получаем список через экземпляр отеля
print("Забронированные номера:", hotel.get_booking_rooms())

# 3. Отменяем бронь
print(Hotel.booking_off(r1))
print("После отмены:", hotel.get_booking_rooms())
