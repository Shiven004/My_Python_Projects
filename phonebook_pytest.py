class Phonebook:

    def __init__(self) -> None:
        self.numbers = {}

    def add(self,name,number):
        self.numbers[name] = name

    def lookup(self):
        pass

    def test_lookup(self,name):
        phonebook = Phonebook()
        phonebook.add('Bob','12345')
        assert "12345" == phonebook.lookup("Bob")
