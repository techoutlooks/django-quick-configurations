# Quick Django Settings

[djang-quickconfigs](https://github.com/techoutlooks/django-quickconfigs)

Speed up Django projects configuration using class-based settings ready for production, staging and development.
Provide mixins for major Django facilities, eg. redis, email, logging, easy_thumbnails, sentry, etc.
Depends on [django-configurations](https://github.com/jazzband/django-configurations).

### Install

```bash
pip install -e git+https://github.com/techoutlooks/django-quick-configs.git#egg=quickconfigs
python manage.py --configurations Dev
```
### Usage

Basic Django configuration leverages common mixins (fits in the project's `settings.py`).
The base `CommonConfig` class inherits the following mixins: `SentrySettings, SecureSettings,  SendMailSettings, 
RedisCacheSettings, LoggingSettings, TemplatesSettings, MiddlewareSettings, DatabasesAppsSettings, Configuration`.
```
import sys
from quickconfigs import CommonConfig
class Dev(DevConfigMixin, CommonConfig):
    """
    Minimal development settings.
    Alternatively, set below settings as env vars in '<path/to/settings.py>/env/*.env'.
    """
    CODENAME = 'demo'
    HOSTNAME = 'localhost'
    ROOT_URLCONF = 'core.urls'
    WSGI_APPLICATION = 'core.wsgi.application'
    SECRET_KEY = '<secret-key-here>'

```

Create default logs dir,
or set `LOGS_ROOT=${PROJECT_ROOT}/logs` in settings.py.

    mkdir -p ${PROJECT_ROOT}/logs

Run the app (alternative ways):
    
    DJANGO_CONFIGURATION=Dev python manage.py runserver
    python manage.py runserver --settings core.settings --configuration Dev
