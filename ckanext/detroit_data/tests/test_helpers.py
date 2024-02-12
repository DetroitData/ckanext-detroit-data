"""Tests for helpers.py."""

import ckanext.detroit_data.helpers as helpers


def test_detroit_data_hello():
    assert helpers.detroit_data_hello() == "Hello, detroit_data!"
