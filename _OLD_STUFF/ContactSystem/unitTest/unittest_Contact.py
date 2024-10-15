import unittest
from Contact import Contact


class TestContact(unittest.TestCase):

    def test_get_first_name(self):
        c = Contact('first', 'last', '+919644049059')
        val = c.getFirstName()
        self.assertTrue(val, 'first')

    def test_get_last_name(self):
        c = Contact('first', 'last', '+919644049059')
        val = c.getLastName()
        self.assertTrue(val, 'last')

    def test_get_phone_number(self):
        c = Contact('first', 'last', '+919644049059')
        val = c.getPhoneNumber()
        self.assertTrue(val, '+919644049059')

    def test_update_phone_number(self):
        c = Contact('first', 'last', '+919644049059')
        c.updatePhoneNumber('9644049059')
        val = c.getPhoneNumber()
        self.assertTrue(val, '9644049059')

    def test_update_first_name(self):
        c = Contact('first', 'last', '+919644049059')
        c.updateFirstName('Abhishek')
        val = c.getFirstName()
        self.assertTrue(val, 'Abhishek')

    def test_update_last_name(self):
        c = Contact('first', 'last', '+919644049059')
        c.updateLastName('AN')
        val = c.getLastName()
        self.assertTrue(val, 'AN')


if __name__ == '__main__':
    unittest.main()



