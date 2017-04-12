# coding=utf-8
"""
Some basic tests to verify that the wrapper is working
"""
from mailchimp3 import MailChimp


client = MailChimp('MAILCHIMP_API_KEY')

print client.lists.all(fields="lists.name,lists.id")

print client.authorized_apps.all(get_all=False)

print client.automations.all(get_all=True)
