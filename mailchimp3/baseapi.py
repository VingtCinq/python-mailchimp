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
        Build path with endpoint and args
        """
        return "/".join(str(component) for component in ([self.endpoint,] + list(args)))
