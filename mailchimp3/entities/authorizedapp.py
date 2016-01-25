from ..baseapi import BaseApi


class AuthorizedApp(BaseApi):

    def __init__(self, *args, **kwargs):
        super(AuthorizedApp, self).__init__(*args, **kwargs)
        self.endpoint = 'authorized-apps'

    def all(self):
        return self._mc_client._get(url=self.endpoint)

    def get(self, app_id):
        return self._mc_client._get(url=self._build_path(app_id))
