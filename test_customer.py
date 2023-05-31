import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('John Doe', 30, 'johndoe@example.com', '123 Main St')

    def test_customer_name(self):
        self.assertEqual(self.customer.name, 'John Doe')

    def test_customer_age(self):
        self.assertEqual(self.customer.age, 30)

    def test_customer_email(self):
        self.assertEqual(self.customer.email, 'johndoe@example.com')

    def test_customer_address(self):
        self.assertEqual(self.customer.address, '123 Main St')

    def test_serialize_deserialize(self):
        s = self.customer.serialize()
        c = Customer.deserialize(s)
        self.assertEqual(self.customer.name, c.name)
        self.assertEqual(self.customer.age, c.age)
        self.assertEqual(self.customer.email, c.email)
        self.assertEqual(self.customer.address, c.address)

if __name__ == '__main__':
    unittest.main()
