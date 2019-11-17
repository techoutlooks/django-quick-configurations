from configurations import values
from django.core.exceptions import ImproperlyConfigured


class SentrySettings(object):
    """
    Base Settings class for Sentry integration
      Steps up after Django is done initializing itself.
    DjangoIntegration disables Django loggers for server and request modules as per:
      https://github.com/getsentry/sentry-python/blob/master/sentry_sdk/integrations/django/__init__.py#L90
    """

    SENTRY_DSN = values.Value(environ_required=False, environ_prefix=None)

    @classmethod
    def post_setup(cls):
        try:
            import sentry_sdk
            from sentry_sdk.integrations.django import DjangoIntegration
            from sentry_sdk.integrations.celery import CeleryIntegration
            from sentry_sdk.integrations.redis import RedisIntegration
        except ImportError:
            raise ImproperlyConfigured(
                "`django-quick-configs: SentrySettings` "
                "sentry_sdk not installed. "
                "try `pip install -e git+https://github.com/getsentry/sentry-python.git#egg=sentry_sdk.`"
            )

        super(SentrySettings, cls).post_setup()
        if cls.SENTRY_DSN:
            sentry_sdk.init(
                dsn=cls.SENTRY_DSN, integrations=[
                    DjangoIntegration(),
                    CeleryIntegration(),
                    RedisIntegration()
                ]
            )
