import ckan.plugins.toolkit as tk
import ckanext.detroit_data.logic.schema as schema


@tk.side_effect_free
def detroit_data_get_sum(context, data_dict):
    tk.check_access(
        "detroit_data_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.detroit_data_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'detroit_data_get_sum': detroit_data_get_sum,
    }
