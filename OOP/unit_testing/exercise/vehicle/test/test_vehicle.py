from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    fuel = 35.6
    horse_power = 112.5


    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25 , self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(29.35, self.vehicle.fuel)

    def test_drive_error(self):
        self.vehicle.fuel = 1
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(3)
        self.assertEqual('Not enough fuel', str(ex.exception))


if __name__ == '__main__':
    main()