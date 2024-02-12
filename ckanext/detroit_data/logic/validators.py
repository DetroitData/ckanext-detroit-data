import ckan.plugins.toolkit as tk


def detroit_data_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "detroit_data_required": detroit_data_required,
    }
