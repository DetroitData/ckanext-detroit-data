from typing import (Any)
import logging

from ckan.common import config
from ckan.logic.converters import as_list
from ckan.lib.helpers import featured_group_org

def detroit_data_get_featured_organizations(count: int = 1) -> list[dict[str, Any]]:
    '''Returns a list of favourite organization in the form
    of organization_list action function
    '''
    config_orgs = config.get('ckan.featured_orgs')
    orgs = featured_group_org(get_action='organization_show',
                              list_action='organization_list',
                              count=count,
                              items=as_list(config_orgs))
    return orgs


def detroit_data_get_promoted_area():
    '''Returns configuration data for the home page promotion area
    '''

    return {
        "heading": config.get("ckanext.detroit_data.promoted_heading"),
        "url": config.get("ckanext.detroit_data.promoted_url"),
        "image_url": config.get("ckanext.detroit_data.promoted_image_url"),
        "image_alt": config.get("ckanext.detroit_data.promoted_image_alt"),
    }


def get_helpers():
    return { 
        'detroit_data_get_featured_organizations': detroit_data_get_featured_organizations,
        'detroit_data_get_promoted_area': detroit_data_get_promoted_area
    }
