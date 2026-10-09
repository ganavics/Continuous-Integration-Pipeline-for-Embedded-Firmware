import unittest


ALARM_THRESHOLD = 70


def alarm_state(temp):
    """
    Simulated alarm logic
    """
    return temp >= ALARM_THRESHOLD


class TestAlarm(unittest.TestCase):

    def test_alarm_on(self):
        self.assertTrue(alarm_state(80))

    def test_alarm_off(self):
        self.assertFalse(alarm_state(30))

    def test_alarm_boundary(self):
        self.assertTrue(alarm_state(70))

    def test_alarm_high(self):
        self.assertTrue(alarm_state(125))

    def test_alarm_low(self):
        self.assertFalse(alarm_state(-20))


if __name__ == "__main__":
    unittest.main()