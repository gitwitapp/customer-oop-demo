class Customer:
    def __init__(self, name: str, age: int, email: str, address: str):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def serialize(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "address": self.address,
            "orders": self.orders,
            "payments": self.payments,
            "reviews": self.reviews
        }

    @classmethod
    def deserialize(cls, data):
        customer = cls(
            name=data["name"],
            age=data["age"],
            email=data["email"],
            address=data["address"]
        )
        customer.orders = data["orders"]
        customer.payments = data["payments"]
        customer.reviews = data["reviews"]
        return customer
