from ..baseapi import BaseApi


class Template(BaseApi):

    def __init__(self, *args, **kwargs):
        super(Template, self).__init__(*args, **kwargs)
        self.endpoint = 'templates'
        self.list_id = None

    def all(self):
        """
        returns a list of available templates.
        """
        return self._mc_client._get(url=self.endpoint)

    def get(self, template_id):
        """
        returns a specific template.
        """
        return self._mc_client._get(url=self._build_path(template_id))

    def update(self, template_id, data):
        """
        updates a specific template
        """
        return self._mc_client._patch(url=self._build_path(template_id), data=data)

    def delete(self, template_id):
        """
        removes a specific template.
        """
        return self._mc_client._delete(url=self._build_path(template_id))
