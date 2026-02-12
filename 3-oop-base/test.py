from datetime import date


class Room:
    def __init__(self, number: int, price: float, room_type: str):
        self.number = number
        self.price = price
        self.type = room_type
        self.is_booked = False
        self.booking_date = None

    def __repr__(self):
        status = "Занят" if self.is_booked else "Свободен"
        return f"Room({self.number}, {status})"


class Booking:
    """Класс-сервис для управления бронированием конкретной комнаты"""

    @staticmethod
    def set_on(room: Room):
        """Бронирует переданную комнату"""
        if not room.is_booked:
            room.is_booked = True
            room.booking_date = date.today()
            return f"Успех! Номер {room.number} забронирован на {room.booking_date}"
        return f"Ошибка: Номер {room.number} уже занят"

    @staticmethod
    def set_off(room: Room):
        """Освобождает переданную комнату"""
        if room.is_booked:
            room.is_booked = False
            room.booking_date = None
            return f"Номер {room.number} теперь свободен"
        return f"Ошибка: Номер {room.number} не был забронирован"


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_booked_rooms(self):
        # Возвращаем список всех забронированных объектов
        return [r for r in self.rooms if r.is_booked]

# --- ПРОВЕРКА ---


# 1. Подготовка данных
hotel = Hotel()
r1 = Room(101, 5000, "Luxe")
r2 = Room(102, 2000, "Simple")
hotel.add_room(r1)
hotel.add_room(r2)

# 2. Используем класс Booking как инструмент
print(Booking.set_on(r1))  # Бронируем r1
print(Booking.set_on(r1))  # Пробуем забронировать повторно (ошибка)

# 3. Смотрим результат через отель
print("Забронированные номера:", hotel.get_booked_rooms())

# 4. Отменяем бронь
print(Booking.set_off(r1))
