import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime, timedelta

async def main():
    # Inicializar sistemas
    reservation_system = ReservationSystem()
    room_mgmt = RoomManagement()
    customer_mgmt = CustomerManagement()

    # Crear habitaciones
    room_1 = Room(101, 'habitacion doble', 1000)
    room_2 = Room(102, 'habitacion simple', 200)
    room_3 = Room(103, 'habitacion simple', 200)
    room_4 = Room(104, 'habitacion doble', 1000)

    # Agregar habitaciones al manejador
    room_mgmt.add_room(room_1.room_number, room_1)
    room_mgmt.add_room(room_2.room_number, room_2)
    room_mgmt.add_room(room_3.room_number, room_3)
    room_mgmt.add_room(room_4.room_number, room_4)

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    # Verificar disponibilidad de habitaciones
    while True:
        room = int(input('Seleccione una habitacion: '))
        is_available = room_mgmt.check_availability(room)

        if is_available:
            print(f'Realizando reserva de la habitacion {room}...')

            # Hacer reserva de la habitacion
            reservation_1 = Reservation(1, customer1, room, datetime.now(), timedelta(days=7))
            reservation_system.add_reservation(reservation_1)
            has_reserved = reservation_system.check_reservation(reservation_1.reservation_id)
            if has_reserved:
                print(reservation_1)

            # Procesar pago asincrónicamente
            await process_payment(customer1, 100)

            # Procesar pago asincrónicamente
            print('La habitacion ha sido reservada con exito')
            break
        else:
            print('La habitacion no esta disponible, lo sentimos')


if __name__ == "__main__":
    asyncio.run(main())

