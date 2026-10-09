import unittest


def validate_temperature(temp):
    """
    Simulated firmware validation function.
    Valid range:
    -40°C to 125°C
    """
    if temp < -40 or temp > 125:
        return -1
    return temp


class TestSensor(unittest.TestCase):

    def test_valid_temperature(self):
        self.assertEqual(validate_temperature(25), 25)

    def test_high_temperature(self):
        self.assertEqual(validate_temperature(150), -1)

    def test_low_temperature(self):
        self.assertEqual(validate_temperature(-50), -1)

    def test_edge_low(self):
        self.assertEqual(validate_temperature(-40), -40)

    def test_edge_high(self):
        self.assertEqual(validate_temperature(125), 125)


if __name__ == "__main__":
    unittest.main()