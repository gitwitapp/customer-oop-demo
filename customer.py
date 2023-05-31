class Customer:
    def __init__(self, name: str, age: int, email: str, address: str):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def serialize(self):
        return f"{self.name},{self.age},{self.email},{self.address}"

    @staticmethod
    def deserialize(s):
        name, age, email, address = s.split(",")
        return Customer(name, int(age), email, address)
