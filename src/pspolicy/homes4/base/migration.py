# -*- coding: utf-8 -*-
"""Migration steps for pspolicy.homes4.base."""

# zope imports
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from zope.component import getUtility


PROFILE_ID = 'profile-pspolicy.homes4.base:default'


def migrate_to_1001(context):
    """Migrate from 1000 to 1001.

    * Update installed add-ons.
    """
    site = getUtility(IPloneSiteRoot)
    qi = getToolByName(site, 'portal_quickinstaller')
    qi.installProduct('theming.toolkit.views')
