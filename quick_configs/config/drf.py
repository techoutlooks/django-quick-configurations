

class DjangorestframeworkSettings(object):

    # requires INSTALLED_APP += ('oauth', 'restframework')
    # pip install django-oauth-toolkit djangorestframework
    CORS_ORIGIN_ALLOW_ALL = True
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        )
    }