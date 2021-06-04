"""
Tests for calc app
"""
import calc


class TestCalc:
    def test_add(self):
        assert calc.add(3, 2) == 5

    def test_sub(self):
        assert calc.sub(10, 5) == 5
