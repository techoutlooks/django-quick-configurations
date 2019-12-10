# coding=utf-8
from __future__ import absolute_import
import logging.config
from os.path import join, realpath, abspath, dirname as up

from django.utils.text import slugify


class LoggingSettings(object):
    """
    Drop in replacement of Django's Logging Configuration:
    Sends INFO level or higher to the console AND file (Django defaults to console only)
        File is auto-rotated, and named after CODENAME slugified.
    Sends ERROR and CRITICAL levels to the ADMINS if DEBUG=True (same as Django defaults).

    https://docs.djangoproject.com/en/1.11/topics/logging/#disabling-logging-configuration
    http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger
    https://lincolnloop.com/blog/django-logging-right-way/
    """

    @property
    def LOGGING(self):

        # Reset logging first
        self.LOGGING_CONFIG = None
        _LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'verbose': {
                    'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
                    'datefmt': "%d/%b/%Y %H:%M:%S"
                },
                'simple': {
                    'format': '%(levelname)s %(message)s'
                },
            },
            'filters': {
                'require_debug_true': {
                    '()': 'django.utils.log.RequireDebugTrue',
                },
            },
            'handlers': {
                'file': {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': join(str(self.PROJECT_LOGS_ROOT), '%s.log' % slugify(str(self.CODENAME))),
                    'maxBytes': 15728640,  # 1024 * 1024 * 15B = 15MB
                    'backupCount': 10,
                    'formatter': 'verbose',
                },
                'console': {
                    'level': 'DEBUG',
                    'filters': ['require_debug_true'],
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose'
                },

                'mail_admins': {
                    # send an email to the site admins on every HTTP 500 error.
                    'level': 'ERROR',
                    'filters': ['require_debug_true'],
                    'class': 'django.utils.log.AdminEmailHandler',
                    'include_html': True,
                }
            },

            # If the log level of the message meets or exceeds the log level of the logger itself,
            # the message will undergo further processing. If it doesn’t, the message will be ignored.
            # INFO, DEBUG, WARNING, ERROR, CRITICAL
            'loggers': {
                # root logger
                '': {
                    'handlers': ['console', 'file'],
                    'level': self.DJANGO_LOG_LEVEL,
                    'propagate': True,
                },
                'django.request': {
                    'handlers': ['mail_admins'],
                    'level': 'ERROR',
                    'propagate': True,
                },
            }
        }

        logging.config.dictConfig(_LOGGING)

