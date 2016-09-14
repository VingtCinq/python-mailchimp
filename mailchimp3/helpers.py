# coding=utf-8
"""
Helper functions to perform simple tasks for multiple areas of the API
"""
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
    The MD5 hash of the lowercase version of the list member's email.
    Uses as memeber_id

    :param member_email: The member's email address
    :type member_email: :py:class:`str`
    :returns: The md5 hash in hex
    :rtype: :py:class:`str`
    """
    member_email = member_email.lower().encode()
    m = hashlib.md5(member_email)
    return m.hexdigest()

def merge_two_dicts(x, y):
    """
    Given two dicts, merge them into a new dict as a shallow copy.

    :param x: The first dictionary
    :type x: :py:class:`dict`
    :param y: The second dictionary
    :type y: :py:class:`dict`
    :returns: The merged dictionary
    :rtype: :py:class:`dict`
    """
    z = x.copy()
    z.update(y)
    return z
