from unittest import TestCase

from suger.string_decorator import class_str


@class_str
class MockData:
    def __init__(self, age):
        self.age = age


class Test(TestCase):
    def test_string(self):
        data = MockData(18)

        target_str = "MockData(age=18)"
        self.assertEqual(data.__str__(), target_str, "not equals string")
