from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('test', 'test_type', 'test_sound')

    def test_init(self):
        self.assertEqual('test', self.mammal.name)
        self.assertEqual('test_type', self.mammal.type)
        self.assertEqual('test_sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("test makes test_sound", result)

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual('test is of type test_type', self.mammal.info())

if __name__ == '__main__':
    main()