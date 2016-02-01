import hashlib


HTTP_METHOD_ACTION_MATCHING = {
    'get': 'GET',
    'create': 'POST',
    'update': 'PATCH',
    'create_or_update': 'PUT',
    'delete': 'DELETE'
}


def get_subscriber_hash(member_email):
    """
    The MD5 hash of the lowercase version
    of the list member's email.
    Uses as memeber_id
    """
    member_email = member_email.lower()
    m = hashlib.md5(member_email)
    return m.hexdigest()
