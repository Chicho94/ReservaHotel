class Room:
    def __init__(self, room_number: int, room_type: str, price: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True


class RoomManagement():
    def __init__(self):
        self.rooms = {}

    def add_room(self, new_room: int, room: dict) -> None:
        """Agrega una nueva habitación al sistema."""
        self.rooms[new_room] = room
        print(f'La habitacion {new_room} se ha creado con exito')

    def check_availability(self, room_number: int) -> bool:
        """Verifica si una habitación está disponible."""
        available = False
        if room_number in self.rooms:
            available = self.rooms[room_number].available
        return available

    def mark_unavailable(self, room_number):
        """cambiando disponibilidad de la habitacion a False."""
        if room_number in self.rooms:
            self.rooms[room_number]['available'] = False

    def mark_available(self, room_number):
        """cambiando disponibilidad de la habitacion a True."""
        if room_number in self.rooms:
            self.rooms[room_number]['available'] = True

# Pruebas del archivo

# room_mgmt = RoomManagement()

