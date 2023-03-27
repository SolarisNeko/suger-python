from unittest import TestCase

from suger.common import ObjectUtils


class TestObjectUtils(TestCase):
    def test_is_null(self):
        self.assertTrue(ObjectUtils.isNull(None), 'ok')

    def test_is_not_null(self):
        self.assertTrue(ObjectUtils.isNotNull(self), 'ok')
