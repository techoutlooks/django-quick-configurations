from configurations import values


class SendMailSettings(object):
    """
    Django settings for sending email.

    Default values:
        EMAIL_USE_TLS = True
        EMAIL_USE_SSL = False
        EMAIL_PORT = 587
        SERVER_EMAIL = EMAIL_HOST_USER          # sends error emails to ADMINS and MANAGERS.
        DEFAULT_FROM_EMAIL = EMAIL_HOST_USER    # ends regular emails thru send_mail()
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    Following have no defaults and will be required from the env:
        EMAIL_HOST,
        EMAIL_HOST_USER,
        EMAIL_HOST_PASSWORD
    """

    EMAIL_USE_TLS = values.BooleanValue(True)
    EMAIL_USE_SSL = not EMAIL_USE_TLS
    EMAIL_HOST = values.Value(environ_required=True)
    EMAIL_PORT = values.Value(587 if EMAIL_USE_TLS else 465 if EMAIL_USE_SSL else 25)
    EMAIL_HOST_USER = values.Value(environ_required=True)
    EMAIL_HOST_PASSWORD = values.Value(environ_required=True)
    DEFAULT_FROM_EMAIL = values.Value(EMAIL_HOST_USER)
    SERVER_EMAIL = values.Value(EMAIL_HOST_USER)
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    def EMAIL_SUBJECT_PREFIX(self):
        return values.Value('[%s][%s] ' % (self.CODENAME, self.HOSTNAME))

