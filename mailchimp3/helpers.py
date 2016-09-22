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
    :returns: The MD5 hash in hex
    :rtype: :py:class:`str`
    """
    check_email(member_email)
    member_email = member_email.lower().encode()
    m = hashlib.md5(member_email)
    return m.hexdigest()


def check_subscriber_hash(potential_hash):
    """
    Check the passed value to see if it matches a 32 character hex number that
    MD5 generates as output, or compute that value assuming that the input is
    an email address.

    :param potential_hash: A value to be passed to any of the endpoints that
    expect an MD5 of an email address
    :type potential_hash: :py:class:`str`
    :returns: A valid MD5 hash in hex
    :rtype: :py:class:`str`
    """
    if re.match('^[0-9a-f]{32}$', potential_hash):
        return potential_hash
    else:
        return get_subscriber_hash(potential_hash)


def check_email(email):
    """
    Function that verifies that the string passed is a valid email address.

    Regex for email validation from http://emailregex.com/

    :param email: The potential email address
    :type email: :py:class:`str`
    :return: Nothing
    """
    if not re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        email
    ):
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
