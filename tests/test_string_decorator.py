from unittest import TestCase

from suger import string


@string
class MockData:
    def __init__(self, age):
        self.age = age


class Test(TestCase):
    def test_string(self):
        data = MockData(18)

        target_str = "MockData(age=18)"

        printStr = data.__str__()
        print(printStr)


        self.assertEqual(printStr, target_str, "not equals string")
