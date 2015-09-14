python-mailchimp-api
====================

A python client for v3 of MailChimp API

About
-----

This package aims to provide a straighforward python client to interact
with Mailchimp API v3.

Installation
------------

This client is hosted at PyPi under the name ``mailchimp3``, to install
it, simply run

``pip install mailchimp3``

Dependencies
------------

requests >= 2.7.0

Examples
--------

::

    from mailchimp3 import MailChimp

    client = MailChimp('YOUR USERNAME', 'YOUR SECRET KEY')

    client.lists.all()  # returns all the lists
    client.lists.get('123456')  # returns the list matching id '123456'
    client.campaign.all() # returns all the campaigns

Usage
-----

Authorized Apps
~~~~~~~~~~~~~~~

::

    client.authorizedapp.all()
    client.authorizedapp.get(app_id='')

Automation
~~~~~~~~~~

::

    client.automation.all()
    client.automation.get(workflow_id='')
    client.automation.pause(workflow_id='')
    client.automation.start(workflow_id='')

    client.email.all(workflow_id='')
    client.email.get(workflow_id='', email_id='')
    client.email.pause(workflow_id='', email_id='')
    client.email.start(workflow_id='', email_id='')

Campaigns
~~~~~~~~~

::

    client.campaign.all()
    client.campaign.get(campaign_id='')
    client.campaign.delete(campaign_id='')

    client.feedback.all(campaign_id='')
    client.feedback.create(campaign_id='', data={})
    client.feedback.get(campaign_id='', feedback_id='')
    client.feedback.update(campaign_id='', feedback_id='', data={})
    client.feedback.delete(campaign_id='', feedback_id='')

Conversations
~~~~~~~~~~~~~

TODO

Files
~~~~~

TODO

Lists
~~~~~

TODO

Reports
~~~~~~~

TODO

Templates
~~~~~~~~~

TODO

Support
-------

If you are having issues, please let us know.

License
-------

The project is licensed under the MIT License.
