import os
from django.core.cache import DEFAULT_CACHE_ALIAS
from configurations import values, pristinemethod


_CELERY_ENV_PREFIX = 'CELERY'
_DEFAULT_REDIS_DB = 0
_DEFAULT_BROKER_DB = 1
_DEFAULT_RESULT_DB = 2
_DEFAULT_REDIS_PORT = 6379

mk_redis_db_url = lambda db: 'redis://%s:%s/%s' % (RedisSettings.REDIS_HOST, RedisSettings.REDIS_PORT, db)


class RedisSettings(object):

    REDIS_HOST = values.Value('localhost',  environ_prefix=None, environ_required=False)
    REDIS_PORT = values.IntegerValue(_DEFAULT_REDIS_PORT, environ_prefix=None, environ_required=False)
    REDIS_DB = values.IntegerValue(_DEFAULT_REDIS_DB, environ_prefix=None, environ_required=False)

    @property
    def REDIS_URL(self):
        return os.getenv('REDIS_URL', mk_redis_db_url(_DEFAULT_REDIS_DB))


class RedisBrokerSettings(RedisSettings):
    """
    For using Redis as a broker for celery
    redis://:password@hostname:port/db_number
    """
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['pickle']

    @property
    def BROKER_URL(self):
        return os.getenv('%s_BROKER_URL' % _CELERY_ENV_PREFIX, mk_redis_db_url(_DEFAULT_BROKER_DB))

    @property
    def RESULT_BACKEND(self):
        return os.getenv('%s_RESULT_BACKEND' % _CELERY_ENV_PREFIX, mk_redis_db_url(_DEFAULT_RESULT_DB))


class RedisCacheSettings(RedisSettings):
    """
    Sets up Redis if active configuration is not Dev.
    https://django-redis-cache.readthedocs.io/

    Leaves intact default (LocMem) implementation for Dev;
    Outside Dev, REDIS_URL must be made required to enable DEFAULT_REDIS_URL to get overridden by the env.
    """
    # TODO: set result backend in celery based on active config; # celery_app.conf.result_backend = 'django-db'
    # TODO: move broker to RabbitMQ? https://www.linkedin.com/pulse/redis-vs-rabbitmq-message-broker-vishnu-kiran-k-v

    @property
    def CACHES(self):
        _CACHES = super(RedisCacheSettings, self).CACHES

        prod = {
            "BACKEND": "redis_cache.RedisCache",
            "LOCATION": self.REDIS_URL,
            "OPTIONS": {
            }
        }

        if not self.DEV:
            _CACHES[DEFAULT_CACHE_ALIAS] = prod
        return _CACHES


class RedisChannelLayersSettings(RedisSettings):
    """
    django-channels.
    """
    @property
    def CHANNEL_LAYERS(self):
        return {
            "default": {
                "BACKEND": "channels_redis.core.RedisChannelLayer",
                "CONFIG": {
                    "hosts": [(self.REDIS_HOST, self.REDIS_PORT)],
                },
            },
        }
