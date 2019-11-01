
class SecureSettings(object):

    @property
    def CSRF_COOKIE_SECURE(self):
        """ chained dynamic setting """
        return self.HTTPS_ONLY

    @property
    def SESSION_COOKIE_SECURE(self):
        """ chained dynamic setting """
        return self.HTTPS_ONLY