# coding=utf-8
"""
Some basic tests to verify that the wrapper is working
"""
from os import getenv

from dotenv import load_dotenv, find_dotenv
from mailchimp3 import MailChimp

load_dotenv(find_dotenv())

client = MailChimp(getenv('MAILCHIMP_USERNAME'), getenv('MAILCHIMP_SECRET'))

print(client.lists.all(fields="lists.name,lists.id"))

print(client.authorized_apps.all(get_all=False))

print(client.automations.all(get_all=True))

oauth_client = MailChimp(access_token=getenv('MAILCHIMP_ACCESS_TOKEN'))

print(client.lists.all(fields="lists.name,lists.id"))

print(client.authorized_apps.all(get_all=False))

print(client.automations.all(get_all=True))

try:
    bad_client = MailChimp(access_token="foobarIdontwork")
except Exception:
    print("Exception raised for bad access_token")

