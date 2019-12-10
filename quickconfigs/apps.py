"""
Smart Models

requires djangorestframework
"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__version__ = '0.1.0dev'


class SmartSettingsAppConfig(AppConfig):
    name = 'quickconfigs'
    verbose_name = _('Smart Settings')


