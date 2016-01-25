from ..baseapi import BaseApi


class MemberActivity(BaseApi):

    def __init__(self, *args, **kwargs):
        super(MemberActivity, self).__init__(*args, **kwargs)
        self.endpoint = 'lists'

    def all(self, list_id, member_id):
        """
        returns last 50 events of a member's activity on a specific list,
        including opens, clicks, and unsubscribes.
        """
        return self._mc_client._get(url=self._build_path(list_id, 'members', member_id, 'activity'))
