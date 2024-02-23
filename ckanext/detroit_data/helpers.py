from typing import (Any, Callable)
import logging

from ckan.common import config
from ckan.logic.converters import as_list
from ckan.lib.helpers import featured_group_org
import ckan.plugins.toolkit as toolkit

@toolkit.chained_helper
def humanize_entity_type(next_helper: Callable[..., Any], entity_type: str, object_type: str, purpose: str):
    if entity_type == "group" and object_type == "category":
        if purpose == "add link":
            return toolkit._("Add Category")
        if purpose == "breadcrumb":
            return toolkit._("Categories")
        if purpose == "content tab":
            return toolkit._("Categories | Groups | Activity")
        if purpose == "create label":
            return toolkit._("Home / ... / Create Category")
        if purpose == "create title": 
          return toolkit._("Create a Category")
        if purpose == "delete confirmation": 
          return toolkit._("Are you sure you want to delete this Category?")
        # if purpose == "description placeholder": 
          # Placeholder for description field on form
        if purpose == "edit label": 
          return toolkit._("Edit Category")
        if purpose == "facet label": 
          return toolkit._("Categories")
        if purpose == "form label": 
          return toolkit._("Category Form")
        if purpose == "main nav": 
          return toolkit._("Categories")
        if purpose == "view label": 
          return toolkit._("View Categories")
        if purpose == "my label": 
          return toolkit._("My Categories")
        if purpose == "name placeholder": 
          return toolkit._("<category>")
        if purpose == "no any objects": 
           return toolkit._("There are currently no categories for this site")
        if purpose == "no associated label":
            return toolkit._("There are no categories associated with this dataset")
        # if purpose == "no description": object has no description
        # if purpose == "no label": package with no organization
        if purpose == "page title": 
          return toolkit._("Categories")
        if purpose == "save label":
          return toolkit._("Save Category")
        if purpose == "search placeholder": 
          return toolkit._("Search Categories...")
        if purpose == "update label": 
          return toolkit._("Update Category")
        if purpose == "you not member":
           return toolkit._("You are not a member of any categories.")
        if purpose == "has been deleted":
           return toolkit._("Category")
    return next_helper(entity_type, object_type, purpose)


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

def detroit_data_get_stats():
   '''Returns statistics for the home page statistics block'''
   stats = {}
   stats['showcase_count'] = toolkit.get_action('package_search')({}, {"rows": 1, 'fq': '+dataset_type:showcase'})['count']
   stats['dataset_count'] = toolkit.get_action('package_search')({}, {"rows": 1, 'fq': '!dataset_type:showcase'})['count']
   stats['category_count'] = len(toolkit.get_action('group_list')({}, {'type': 'category'}))
   stats['organization_count'] = len(toolkit.get_action('organization_list')({}, {}))
   return stats


def get_helpers():
    return { 
        'detroit_data_get_featured_organizations': detroit_data_get_featured_organizations,
        'detroit_data_get_promoted_area': detroit_data_get_promoted_area,
        'detroit_data_get_stats': detroit_data_get_stats,
        'humanize_entity_type': humanize_entity_type
    }
