import sys
from quick_configs import CommonConfig, DevConfigMixin


class Dev(DevConfigMixin, CommonConfig):
    """
    Minimal development settings.

    # refactor manage.py with minimal setup below:
    if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.core.settings")
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')
    from configurations.management import execute_from_command_line
    execute_from_command_line(sys.argv)

    # then run project with:
    DJANGO_CONFIGURATION=Dev python manage.py runserver
    """

    # Minimum required settings,
    # Alternatively below envs in demo/core/env/.env
    # Note: CODENAME, HOSTNAME are no Django defaults!
    CODENAME = 'demo'
    HOSTNAME = 'localhost'
    ROOT_URLCONF = 'core.urls'
    WSGI_APPLICATION = 'core.wsgi.application'
    SECRET_KEY = '(kfz2&2w9d+ktjp3m4!i(3v$ua4=-hcp6%%3b-d3)m#dm_rp6-'

    # Demo project's apps.
    # PROJECT_APPS = (
    #     'core',
    # )




