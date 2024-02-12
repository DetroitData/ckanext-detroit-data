"""Tests for views.py."""

import pytest

import ckanext.detroit_data.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "detroit_data")
@pytest.mark.usefixtures("with_plugins")
def test_detroit_data_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("detroit_data.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, detroit_data!"
