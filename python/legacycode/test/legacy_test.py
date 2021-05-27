# -*- coding: utf-8 -*-

import pytest
from src.production import Production

test_cases = [
    (0, 1),
    ]


class TestLegacy:
    @pytest.mark.parametrize('input, expected_output',
                             test_cases)
    def test_failing_parameterized_test(self, input, expected_output):
        assert input == expected_output

    def test_failing_test(self):
        assert 0 == 1
