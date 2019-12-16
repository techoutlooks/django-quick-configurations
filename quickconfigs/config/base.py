# coding=utf-8

from configurations import values


class DatabasesAppsSettings(object):
    """
    Django settings's DATABASES and INSTALLED_APPS as a Mixin.

    ADMIN_APPS:       Override/extend django.contrib.admin.
    DEV_APPS:         Not for production usage.
    DEFAULT_APPS:     Well-known, usually extensively used apps. Also installed related context_processors.
    PROJECT_APPS:     Custom (current project)'s apps.
    """
    # ----------------------------------------------------------------------------------
    # Databases configuration
    # ----------------------------------------------------------------------------------
    DEFAULT_DATABASE_URL = 'sqlite:///db.sqlite3'
    DATABASES = values.DatabaseURLValue(DEFAULT_DATABASE_URL, alias='default')

    DJANGO_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        # 'django.contrib.markup',
        'django.contrib.humanize',
        'django.contrib.admin',
        'django.contrib.admindocs',
    )

    # DEBUG_APPS may be enabled regardless of Django configuration,
    # ie., no matter whether Dev, Staging or Prod mode is active.
    DEBUG_APPS = (
        'django_extensions',
    )

    # ----------------------------------------------------------------------------------
    # Apps configuration
    # Default to empty: left to implementation
    # ----------------------------------------------------------------------------------
    ADMIN_APPS = ()
    DEV_APPS = ()
    DEFAULT_APPS = ()
    PROJECT_APPS = ()

    # TODO: option to insert in ADMIN_APPS, DEFAULT_APPS, etc.
    def add_apps(self, new_apps):
        """ new_apps to INSTALLED_APPS """
        return self.INSTALLED_APPS.extend(filter(lambda app: app not in self.INSTALLED_APPS, new_apps))

    @property
    def INSTALLED_APPS(self):
        """ Control apps order dynamically
        INSTALLED APPS = ADMIN_APPS + DJANGO_APPS + DEBUG_APPS + DEV_APPS + DEFAULT_APPS + PROJECT_APPS
        """
        _apps = self.ADMIN_APPS + self.DJANGO_APPS + self.DEFAULT_APPS
        if self.DEBUG:
            _apps += self.DEBUG_APPS
        if self.DEV:
            _apps += self.DEV_APPS
        return _apps + self.PROJECT_APPS


class MiddlewareSettings(object):
    """
    Django settings.MIDDLEWARE_CLASSES as a Mixin
    https://docs.djangoproject.com/en/2.0/topics/http/middleware/#upgrading-middleware
    """
    # https://docs.djangoproject.com/en/1.11/topics/i18n/translation/#how-django-discovers-language-preference
    DJANGO_MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    DEBUG_MIDDLEWARE = ()
    DEFAULT_MIDDLEWARE = ()
    PROJECT_MIDDLEWARE = ()

    @property
    def MIDDLEWARE(self):
        out_classes = self.DEFAULT_MIDDLEWARE + self.DJANGO_MIDDLEWARE + self.PROJECT_MIDDLEWARE
        if self.DEBUG:
            out_classes += self.DEBUG_MIDDLEWARE
        return list(out_classes)


class TemplatesSettings(object):
    """
    Django settings.TEMPLATES as a Mixin
    https://docs.djangoproject.com/en/1.11/topics/i18n/translation/#how-django-discovers-language-preference
    """

    @property
    def TEMPLATES(self):
        return [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
                'DIRS':
                    # Insert your templates root directory here
                    # filesystem.Loader: is enabled by default. However it won’t find any templates until
                    # you set DIRS to a non-empty list.
                    # app_directories.Loader: You can enable this loader simply by setting APP_DIRS to True.
                    # If debug is False, these loaders are wrapped in django.template.loaders.cached.Loader.
                    self.TEMPLATES_ROOT,

                'OPTIONS': {
                    'debug': self.DEBUG,
                    'context_processors': [
                        # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                        # list if you haven't customized them:
                        'django.contrib.auth.context_processors.auth',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.media',
                        'django.template.context_processors.static',
                        'django.template.context_processors.tz',
                        'django.contrib.messages.context_processors.messages',
                        'django.template.context_processors.request',
                    ]
                }
            }
        ]

