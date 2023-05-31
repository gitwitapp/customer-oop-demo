class Customer:
    def __init__(self, name: str, age: int, email: str, address: str):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.orders = []
        self.payments = []
        self.reviews = []
