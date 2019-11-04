# Quick Django Settings

[djang-quick-configurations](https://github.com/techoutlooks/django-quick-configurations)

Speed up Django projects configuration using class-based settings ready for production, staging and development.
Provide mixins for major Django facilities, eg. redis, email, logging, easy_thumbnails, sentry, etc.
Depends on [django-configurations](https://github.com/jazzband/django-configurations).

### Install

```bash
pip install -e git+https://github.com/techoutlooks/django-quick-configurations.git#egg=quick_configs
```
### Usage

Basic Django configuration (fits in the project's `settings.py`)
Expects env vars in 'settings/env/*.env' of current project.
```
from quick_configs import CommonConfig
class MyDjangoSettings(CommonConfig):
    CODENAME = 'my'
    HOSTNAME = 'localhost'
    ROOT_URLCONF = 'my.urls'
    WSGI_APPLICATION = 'my.wsgi'

DJANGO_CONFIGURATION=MyDjangoSettings
python manage.py runserver
```

slightly more complex usage leveraging the common mixins. The base `CommonConfig` class inherits the following mixins : 
    SentrySettings, SecureSettings,  SendMailSettings, RedisCacheSettings, LoggingSettings, TemplatesSettings, 
    MiddlewareSettings, DatabasesAppsSettings, Configuration

```
import sys
from quick_configs import CommonConfig
class Dev(CommonConfig):
    """
    Dev settings
    """
    # Turn all debug flags on
    DEV = True
    PROD = STAGING = not DEV
    HTTPS_ONLY = False

    # Turn off debug while imported by Celery with a workaround
    # See http://stackoverflow.com/a/4806384
    if "celery" in sys.argv[0]:
        DEBUG = False

    # SendMailSettings mixin override
    DJANGO_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DJANGO_CONFIGURATION=Dev
python manage.py runserver
```