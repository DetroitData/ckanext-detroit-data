"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.detroit_data.logic import validators


def test_detroit_data_reauired_with_valid_value():
    assert validators.detroit_data_required("value") == "value"


def test_detroit_data_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.detroit_data_required(None)
