class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email


class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer: Customer)-> bool:
        """Agregando nuevo cliente"""
        nuevo_clinte = self.customers.get(customer.customer_id)
        if nuevo_clinte:
            print(f'El cliente ya existe')
            return False
        self.customers[customer.customer_id] = customer
        print(f'El cliente ha sido creado')
        return True

    def get_customer(self, customer_id: int) -> dict:
        """Obtiene la información de un cliente por ID."""
        cliente_info = self.customers.get(customer_id)
        if cliente_info:
            return cliente_info
        print(f'El cliente no existe')
        return {}