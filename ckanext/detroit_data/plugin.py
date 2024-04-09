import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.detroit_data.cli as cli
import ckanext.detroit_data.helpers as helpers
# import ckanext.detroit_data.views as views
# from ckanext.detroit_data.logic import (
#     action, auth, validators
# )

class DetroitDataPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "detroit_data")

    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator("ignore_missing")
        url_validator = toolkit.get_validator("url_validator")
        remove_whitespace = toolkit.get_validator("remove_whitespace")

        schema.update({
            'ckan.featured_orgs': [ignore_missing, remove_whitespace],
            'ckan.featured_groups': [ignore_missing, remove_whitespace],
            'ckanext.detroit_data.promoted_heading': [ignore_missing, remove_whitespace],
            'ckanext.detroit_data.promoted_url': [ignore_missing, url_validator, remove_whitespace],
            'ckanext.detroit_data.promoted_image_url': [ignore_missing, url_validator, remove_whitespace],
            'ckanext.detroit_data.promoted_image_alt': [ignore_missing, remove_whitespace]
        })

        return schema

    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    def get_helpers(self):
        return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    