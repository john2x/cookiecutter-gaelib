#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.repo_name }}
----------------------------------

Tests for `{{ cookiecutter.repo_name }}` module.
"""

import unittest

from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}
from tests.base import BaseGAETestCase


class Test{{ cookiecutter.repo_name|capitalize }}(BaseGAETestCase):
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
