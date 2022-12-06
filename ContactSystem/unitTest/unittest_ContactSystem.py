import unittest
from ContactSystem import ContactSystem
from unittest.mock import patch


class TestContactSystem(unittest.TestCase):

    @patch('builtins.print')
    def test_add_contact(self, mock_print):
        contactSystem = ContactSystem()
        contactSystem.addContact('first', 'last', '+919644049059')
        mock_print.assert_called_with('Contact added successfully')

    @patch('builtins.print')
    def test_delete_contact(self, mock_print):
        contactSystem = ContactSystem()
        contactSystem.addContact('first', 'last', '+919644049059')
        contactSystem.deleteContact('+919644049059')
        mock_print.assert_called_with('Contact with number +919644049059 deleted successfully.')

    @patch('builtins.print')
    def test_update_contact_firstname(self, mock_print):
        contactSystem = ContactSystem()
        contactSystem.addContact('first', 'last', '+919644049059')
        contactSystem.updateContact('+919644049059', "FIRSTNAME", 'Monkey')
        mock_print.assert_called_with('Updated first name successfully for +919644049059')

    @patch('builtins.print')
    def test_update_contact_lastname(self, mock_print):
        contactSystem = ContactSystem()
        contactSystem.addContact('first', 'last', '+919644049059')
        contactSystem.updateContact('+919644049059', "LASTNAME", 'Luffy')
        mock_print.assert_called_with('Updated last name successfully for +919644049059')

    @patch('builtins.print')
    def test_update_contact_number(self, mock_print):
        contactSystem = ContactSystem()
        contactSystem.addContact('first', 'last', '+919644049059')
        contactSystem.updateContact('+919644049059', "PHONENUMBER", '9644049059')
        mock_print.assert_called_with('Updated phone number successfully for 9644049059')

    def test_search_contact_by_number(self):
        contactSystem = ContactSystem()
        contactSystem.addContact('first', 'last', '+919644049059')
        val = contactSystem.searchContact("PHONENUMBER", "964")
        assert val is not None

    def test_search_contact_by_name(self):
        contactSystem = ContactSystem()
        contactSystem.addContact('monkey', 'Leluffy', '+919644049059')
        val = contactSystem.searchContact("NAME", "luffy")
        assert val is not None


if __name__ == '__main__':
    unittest.main()
