from unittest import TestCase

from suger import csv


@csv
class MockData:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.email = "qq.com"


class Test(TestCase):
    def test_csv(self):
        data = MockData(id=1, name='neko', age=18)

        # print("{},{},{}".format(data.id, data.name, data.age))

        print(data.csv_format())
        print(data.csv_str())
