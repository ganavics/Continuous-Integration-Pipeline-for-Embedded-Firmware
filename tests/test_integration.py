import unittest

ALARM_THRESHOLD = 70


def validate_temperature(temp):
    """
    Simulated sensor validation
    """
    if temp < -40 or temp > 125:
        return -1
    return temp


def alarm_state(temp):
    """
    Simulated alarm logic
    """
    return temp >= ALARM_THRESHOLD


class TestIntegration(unittest.TestCase):

    def test_valid_temp_alarm_off(self):
        temp = validate_temperature(30)
        self.assertEqual(temp, 30)
        self.assertFalse(alarm_state(temp))

    def test_valid_temp_alarm_on(self):
        temp = validate_temperature(80)
        self.assertEqual(temp, 80)
        self.assertTrue(alarm_state(temp))

    def test_invalid_temperature(self):
        temp = validate_temperature(150)
        self.assertEqual(temp, -1)

    def test_boundary_temperature(self):
        temp = validate_temperature(70)
        self.assertTrue(alarm_state(temp))

    def test_low_boundary(self):
        temp = validate_temperature(-40)
        self.assertFalse(alarm_state(temp))


if __name__ == "__main__":
    unittest.main()