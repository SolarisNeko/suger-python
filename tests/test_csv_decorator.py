from unittest import TestCase

from suger import csv


@csv
class MockData:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.csv = ''




class Test(TestCase):
    def test_csv(self):
        data = MockData(name='neko', age=18)

        print(data.csv_str())
        print(data.csv_format())
