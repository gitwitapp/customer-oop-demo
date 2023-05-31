class Customer:
    def __init__(self, name: str, age: int, email: str, address: str):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def serialize(self) -> str:
        return f"{self.name},{self.age},{self.email},{self.address}"

    @classmethod
    def deserialize(cls, s: str) -> "Customer":
        name, age, email, address = s.split(",")
        return cls(name, int(age), email, address)
