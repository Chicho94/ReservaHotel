from typing import Optional, Dict


class Reservation:
    def __init__(self, reservation_id: int, customer: Dict[str, object], room_number: int, check_in: str, check_out: str):
        self.reservation_id: int = reservation_id
        self.customer: Dict[str, object] = customer
        self.room_number: int = room_number
        self.check_in: str = check_in
        self.check_out: str = check_out

    def __repr__(self) -> str:
        return (f"Reservation(ID: {self.reservation_id}, Customer: {self.customer}, Room: {self.room_number}, "
                f"Check-in: {self.check_in}, Check-out: {self.check_out})")


class ReservationSystem():
    def __init__(self):
        self.reservations = {}

    def add_reservation(self, reservation: Reservation) -> bool:
        """Adds a new reservation to the system."""
        if reservation.reservation_id in self.reservations:
            print(
                f"La reservacion {reservation.reservation_id} ya existe.")
            return False
        self.reservations[reservation.reservation_id] = reservation
        print('La reservacion ha sido creada exitosamente.')
        return True

    def check_reservation(self, reservation_id: int) -> Optional[Reservation]:
        """Agrega una nueva reserva al sistema."""
        reservation = self.reservations.get(reservation_id)
        if reservation_id:
            return reservation
        print('La reservacion no fue encontrada')
        return None

    def cancel_reservation(self, reservation_id: int) -> bool:
        """Cancela una reserva existente por ID."""
        if reservation_id in self.reservations:
            del self.reservations[reservation_id]
            print(f'La reserva {reservation_id} fue cancelada con exito')
            return True
        print('La reservacion no fue encontrada')
        return False
