from os import path


class BaseApi(object):

    """
    Simple class to buid path for entities
    """

    def __init__(self, mc_client):
        """
        Initialize the class with you user_id and secret_key
        """
        super(BaseApi, self).__init__()
        self._mc_client = mc_client

    def _build_path(self, *args):
        """
        Build path width endpoint and args
        """
        return "/".join([self.endpoint,] + list(args))
