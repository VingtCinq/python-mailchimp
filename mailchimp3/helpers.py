# coding=utf-8
"""
Helper functions to perform simple tasks for multiple areas of the API
"""
import hashlib
import re

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
    Used as subscriber_hash

    :param member_email: The member's email address
    :type member_email: :py:class:`str`
    :returns: The md5 hash in hex
    :rtype: :py:class:`str`
    """
    check_subscriber_email(member_email)
    member_email = member_email.lower().encode()
    m = hashlib.md5(member_email)
    return m.hexdigest()


def check_subscriber_hash(potential_hash):
    if re.match('^[0-9a-f]{32}$', potential_hash):
        return potential_hash
    else:
        return get_subscriber_hash(potential_hash)


def check_subscriber_email(email):
    if not re.search('@', email):
        raise ValueError('String passed is not a valid email address')
    return


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
