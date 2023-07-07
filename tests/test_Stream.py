from unittest import TestCase

from suger.stream.Stream import Stream

globalData = [1, 2, 3, 3, 4, 5]


class TestStream(TestCase):

    def test_demo(self):
        data = [1, 2, 3, 3, 4, 5]

        result = Stream(data)\
            .filter(lambda x: x % 2 == 0) \
            .sort(reverse=True) \
            .map(lambda x: x * 2) \
            .toSet()
        self.assertEqual(result, {8, 4})

    def test_sort_numeric(self):
        data = [5, 2, 8, 3, 1, 7, 4, 6]
        result = Stream(data).sort(sortedFunc=lambda x: x).toList()
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sort_numeric_reverse(self):
        data = [5, 2, 8, 3, 1, 7, 4, 6]
        result = Stream(data).sort(sortedFunc=lambda x: x, reverse=True).toList()
        self.assertEqual(result, [8, 7, 6, 5, 4, 3, 2, 1])

    def test_sort(self):
        data = [5, 2, 8, 3, 1, 7, 4, 6]
        result = Stream(data).sort().toList()
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sort_reverse(self):
        data = [5, 2, 8, 3, 1, 7, 4, 6]
        result = Stream(data).sort(reverse=True).toList()
        self.assertEqual(result, [8, 7, 6, 5, 4, 3, 2, 1])

    def test_sort_key(self):
        data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        result = Stream(data).sort(sortedFunc=len).toList()
        self.assertEqual(result, ['date', 'apple', 'banana', 'cherry', 'elderberry'])

    def test_map(self):
        # 使用map操作将每个元素加倍
        result = Stream(globalData).map(lambda x: x * 2).toList()
        self.assertEqual(result, [2, 4, 6, 6, 8, 10])

    def test_flat_map(self):
        # 一维数组矩阵叉积
        result = Stream(globalData).flatMap(lambda x: [x, x]).toList()
        self.assertEqual(result, [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5])

        # 二维数组平铺
        data2 = [[1, 2, 3], [3, 4, 5]]
        result2 = Stream(data2).flatMap(lambda x: x).toList()
        self.assertEqual(result2, [1, 2, 3, 3, 4, 5])

    def test_filter(self):
        result = Stream(globalData).filter(lambda x: x % 2 == 0).toList()
        self.assertEqual(result, [2, 4])

    def test_first(self):
        result = Stream(globalData).first()
        self.assertEqual(result, 1)

    def test_count(self):
        result = Stream(globalData).count()
        self.assertEqual(result, 6)

    def test_to_list(self):
        result = Stream(globalData).toList()
        self.assertEqual(result, [1, 2, 3, 3, 4, 5])

    def test_to_dictionary(self):
        result = Stream(globalData).toDictionary(lambda x: x, lambda x: x * 2)
        self.assertEqual(result, {1: 2, 2: 4, 3: 6, 4: 8, 5: 10})

    def test_to_set(self):
        result = Stream(globalData).toSet()
        self.assertEqual(result, {1, 2, 3, 4, 5})



    def test_reduce(self):
        stream = Stream([1, 2, 3, 4, 5])
        result = stream.reduce(lambda x, y: x + y, 0)
        self.assertEqual(result, 15)

    def test_reduce_with_initial_value(self):
        stream = Stream([1, 2, 3, 4, 5])
        result = stream.reduce(lambda x, y: x + y, 10)
        self.assertEqual(result, 25)

    def test_group_by(self):
        stream = Stream(['apple', 'banana', 'cherry', 'date'])
        result = stream.groupBy(lambda x: len(x))
        expected = {4: ['date'], 5: ['apple'], 6: ['banana', 'cherry']}
        self.assertEqual(result, expected)

    def test_group_by_multiple_keys(self):
        stream = Stream(['apple', 'banana', 'cherry', 'date'])
        result = stream.groupBy(lambda x: x[0])
        expected = {'a': ['apple'], 'b': ['banana'], 'c': ['cherry'], 'd': ['date']}
        self.assertEqual(result, expected)
