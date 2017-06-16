|mailchimp3 v2.0.13 on PyPi| |MIT license| |Stable|

python-mailchimp-api
====================

A straighforward python client for v3 of MailChimp API using
requests >= 2.7.0.

Getting Started
---------------

Installation
~~~~~~~~~~~~

This client is hosted at PyPi under the name ``mailchimp3``, to install
it, simply run

``pip install mailchimp3``

Upgrading from v1.x
~~~~~~~~~~~~~~~~~~~

The installation procedure for 2.x is the same as before, however there
are a massive number of changes to the naming conventions within this
wrapper and the way in which certain methods are called. Please read
the documentation below carefully for information on the new structure
and expanded functionality. With this release, all documented endpoints
are implemented and all endpoint methods are available.

History
~~~~~~~

Up to date with
`changelog <http://developer.mailchimp.com/documentation/mailchimp/guides/changelog/>`__
features listed thru 1/12/2017.

Initialization
~~~~~~~~~~~~~~

Grab ``YOUR_SECRET_KEY`` from your mailchimp account (Account > Extra >
Api Keys). ``YOUR_USERNAME`` is the one you use to login.

::

    from mailchimp3 import MailChimp

    client = MailChimp('YOUR_USERNAME', 'YOUR_SECRET_KEY')

Pagination
~~~~~~~~~~

Simply add ``count`` and ``offset`` arguments in your function. The
count is how many records to return, the offset is how many records to
skip. For endpoints that allow the pagination parameters, the all()
method has an additional boolean ``get_all`` argument that will loop
through all records until the API no longer returns any to get all
records without manually performing an additional query. By default,
count is 10 and offset is 0 for all endpoints that support it. The
``get_all`` parameter on the all() method on any endpoint defaults to
false, which follows the values that are provided in the call, and
using ``get_all=True`` will ignore the provided count and offset to
ensure that all records are returned.

::

    client.lists.members.all('123456', count=100, offset=0)

Fields
~~~~~~

Many endpoints allow you to select which fields will be returned out of
all available fields (for example, only the email\_address of a
member). Simply add ``fields`` arguments in your function. The
following only display email\_address and id for each member in list
123456:

::

    client.lists.members.all('123456', get_all=True, fields="members.email_address,members.id")

Examples
~~~~~~~~

::

    # returns all the lists (only name and id)
    client.lists.all(get_all=True, fields="lists.name,lists.id")

    # returns all members inside list '123456'
    client.lists.members.all('123456', get_all=True)

    # return the first 100 member's email addresses for the list with id 123456
    client.lists.members.all('123456', count=100, offset=0, fields="members.email_address")

    # returns the list matching id '123456'
    client.lists.get('123456')

    # add John Doe with email john.doe@example.com to list matching id '123456'
    client.lists.members.create('123456', {
        'email_address': 'john.doe@example.com',
        'status': 'subscribed',
        'merge_fields': {
            'FNAME': 'John',
            'LNAME': 'Doe',
        },
    })

    # returns all the campaigns
    client.campaigns.all(get_all=True)

    # You can also disable at runtime with the optional ``enabled`` parameter.
    # Every API call will return None
    client = MailChimp('YOUR USERNAME', 'YOUR SECRET KEY', enabled=False)

    # You are encouraged to specify a value in seconds for the  ``timeout``
    # parameter to avoid hanging requests.
    client = MailChimp('YOUR USERNAME', 'YOUR SECRET KEY', timeout=10.0)

API Structure
-------------

All endpoints follow the structure listed in the official MailChimp API
v3 documentation. The structure will be listed below and then the
individual methods available after.

::

    MailChimp
    +- Root
    +- Authorized Apps
    +- Automations
    |  +- Actions
    |  +- Emails
    |  |  +- Actions
    |  |  +- Queues
    |  +- Removed Subscribers
    +- Batch Operations
    +- Campaign Folders
    +- Campaigns
    |  +- Actions
    |  +- Content
    |  +- Feedback
    |  +- Send Checklist
    +- Conversations
    |  +- Messages
    +- Stores
    |  +- Carts
    |  |  +- Lines
    |  +- Customers
    |  +- Orders
    |  |  +- Lines
    |  +- Products
    |     +- Variants
    +- File Manager Files
    +- File Manager Folders
    +- Lists
    |  +- Abuse Reports
    |  +- Activity
    |  +- Clients
    |  +- Growth History
    |  +- Interest Categories
    |  |  +- Interests
    |  +- Members
    |  |  +- Activity
    |  |  +- Goals
    |  |  +- Notes
    |  +- Merge Fields
    |  +- Segments
    |  |  +- Segment Members
    |  +- Signup Forms
    |  +- Twitter Lead Generation Carts
    |  +- Webhooks
    +- Reports
    |  +- Campaign Abuse
    |  +- Campaign Advice
    |  +- Click Reports
    |  |  +- Members
    |  +- Domain Performance
    |  +- EepURL Reports
    |  +- Email Activity
    |  +- Location
    |  +- Sent To
    |  +- Sub-Reports
    |  +- Unsubscribes
    +- Seach Campaigns
    +- Search Members
    +- Template Folders
    +- Templates
       +- Default Content

API Endpoints
-------------

Below is the list of all endpoints and the methods that can be called
against them. Any endpoint that has a method that takes an ID argument
(for example the app\_id in the authorized\_apps endpoint or the
subscriber\_hash in the list members endpoints) will record all IDs
passed as well as those generated by methods that will only ever return
a single result such as the create() method present on some endpoints.
These stored attributes are only available at the level that they were
passed or created at and must be passed again to interact with a lower
or higher level such as accessing a list and then a member. The below
code assumes that you have initialized the MailChimp class as listed
above with the name ``client``.

Root
~~~~

Root
^^^^

::

    client.root.get()

Authorized Apps
~~~~~~~~~~~~~~~

Authorized Apps
^^^^^^^^^^^^^^^

::

    client.authorized_apps.create(data={})
    client.authorized_apps.all(get_all=False)
    client.authorized_apps.get(app_id='')

Automations
~~~~~~~~~~~

Automations
^^^^^^^^^^^

::

    client.automations.all(get_all=False)
    client.automations.get(workflow_id='')

Automation Actions
^^^^^^^^^^^^^^^^^^

::

    client.automations.actions.pause(workflow_id='')
    client.automations.actions.start(workflow_id='')

Automation Emails
^^^^^^^^^^^^^^^^^

::

    client.automations.emails.all(workflow_id='')
    client.automations.emails.get(workflow_id='', email_id='')

Automation Email Actions
^^^^^^^^^^^^^^^^^^^^^^^^

::

    client.automations.emails.actions.pause(workflow_id='', email_id='')
    client.automations.emails.actions.start(workflow_id='', email_id='')

Automation Email Queues
^^^^^^^^^^^^^^^^^^^^^^^

::

    client.automations.emails.queues.create(workflow_id='', email_id='', data={})
    client.automations.emails.queues.all(workflow_id='', email_id='')
    client.automations.emails.queues.get(workflow_id='', email_id='', subscriber_hash='')

Automation Removed Subscribers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    client.automations.removed_subscribers.create(workflow_id='', data={})
    client.automations.removed_subscribers.all(workflow_id='')

Batch Operations
~~~~~~~~~~~~~~~~

Batches
^^^^^^^

::

    client.batches.create(data={})
    client.batches.all(get_all=False)
    client.batches.get(batch_id='')
    client.batches.delete(batch_id='')

Campaigns
~~~~~~~~~

Folders
^^^^^^^

::

    client.campaign_folders.create(data={})
    client.campaign_folders.all(get_all=False)
    client.campaign_folders.get(folder_id='')
    client.campaign_folders.update(folder_id='', data={})
    client.campaign_folders.delete(folder_id='')

Campaigns
^^^^^^^^^

::

    client.campaigns.create(data={})
    client.campaigns.all(get_all=False)
    client.campaigns.get(campaign_id='')
    client.campaigns.update(campaign_id='')
    client.campaigns.delete(campaign_id='')

Campaign Actions
^^^^^^^^^^^^^^^^

::

    client.campaigns.actions.cancel(campaign_id='')
    client.campaigns.actions.pause(campaign_id='')
    client.campaigns.actions.replicate(campaign_id='')
    client.campaigns.actions.resume(campaign_id='')
    client.campaigns.actions.schedule(campaign_id='', data={})
    client.campaigns.actions.send(campaign_id='')
    client.campaigns.actions.test(campaign_id='', data={})
    client.campaigns.actions.unschedule(campaign_id='')

Campaign Content
^^^^^^^^^^^^^^^^

::

    client.campaigns.content.get(campaign_id='')
    client.campaigns.content.update(campaign_id='', data={})

Campaign Feedback
^^^^^^^^^^^^^^^^^

::

    client.campaigns.feedback.create(campaign_id='', data={})
    client.campaigns.feedback.all(campaign_id='', get_all=False)
    client.campaigns.feedback.get(campaign_id='', feedback_id='')
    client.campaigns.feedback.update(campaign_id='', feedback_id='', data={})
    client.campaigns.feedback.delete(campaign_id='', feedback_id='')

Campaign Send Checklist
^^^^^^^^^^^^^^^^^^^^^^^

::

    client.campaigns.send_checklist.get(campaign_id='')

Conversations
~~~~~~~~~~~~~

Conversations
^^^^^^^^^^^^^

::

    client.conversations.all(get_all=False)
    client.conversations.get(conversation_id='')

Conversation Messages
^^^^^^^^^^^^^^^^^^^^^

::

    client.conversations.messages.create(conversation_id='', data={})
    client.conversations.messages.all(conversation_id='')
    client.conversations.messages.get(conversation_id='', message_id='')

E-Commerce
~~~~~~~~~~

Stores
^^^^^^

::

    client.stores.create(data={})
    client.stores.all(get_all=False)
    client.stores.get(store_id='')
    client.stores.update(store_id='', data={})
    client.stores.delete(store_id='')

Store Carts
^^^^^^^^^^^

::

    client.stores.carts.create(store_id='', data={})
    client.stores.carts.all(store_id='', get_all=False)
    client.stores.carts.get(store_id='', cart_id='')
    client.stores.carts.update(store_id='', cart_id='', data={})
    client.stores.carts.delete(store_id='', cart_id='')

Store Cart Lines
^^^^^^^^^^^^^^^^

::

    client.stores.carts.lines.create(store_id='', cart_id='', data={})
    client.stores.carts.lines.all(store_id='', cart_id='', get_all=False)
    client.stores.carts.lines.get(store_id='', cart_id='', line_id='')
    client.stores.carts.lines.update(store_id='', cart_id='', line_id='', data={})
    client.stores.carts.lines.delete(store_id='', cart_id='', line_id='')

Store Customers
^^^^^^^^^^^^^^^

::

    client.stores.customers.create(store_id='', data={})
    client.stores.customers.all(store_id='', get_all=False)
    client.stores.customers.get(store_id='', customer_id='')
    client.stores.customers.update(store_id='', customer_id='', data={})
    client.stores.customers.create_or_update(store_id='', customer_id='', data={})
    client.stores.customers.delete(store_id='', customer_id='')

Store Orders
^^^^^^^^^^^^

::

    client.stores.orders.create(store_id='', data={})
    client.stores.orders.all(store_id='', get_all=False)
    client.stores.orders.get(store_id='', order_id='')
    client.stores.orders.update(store_id='', order_id='', data={})
    client.stores.orders.delete(store_id='', order_id='')

Store Order Lines
^^^^^^^^^^^^^^^^^

::

    client.stores.orders.lines.create(store_id='', order_id='', data={})
    client.stores.orders.lines.all(store_id='', order_id='', get_all=False)
    client.stores.orders.lines.get(store_id='', order_id='', line_id='')
    client.stores.orders.lines.update(store_id='', order_id='', line_id='', data={})
    client.stores.orders.lines.delete(store_id='', order_id='', line_id='')

Store Products
^^^^^^^^^^^^^^

::

    client.stores.products.create(store_id='', data={})
    client.stores.products.all(store_id='', get_all=False)
    client.stores.products.get(store_id='', product_id='')
    client.stores.products.update(store_id='', product_id='')
    client.stores.products.delete(store_id='', product_id='')

Store Product Variants
^^^^^^^^^^^^^^^^^^^^^^

::

    client.stores.products.variants.create(store_id='', product_id='', data={})
    client.stores.products.variants.all(store_id='', product_id='', get_all=False)
    client.stores.products.variants.get(store_id='', product_id='', variant_id='')
    client.stores.products.variants.update(store_id='', product_id='', variant_id='', data={})
    client.stores.products.variants.create_or_update(store_id='', product_id='', variant_id='', data={})
    client.stores.products.variants.delete(store_id='', product_id='', variant_id='')

File Manager
~~~~~~~~~~~~

Files
^^^^^

::

    client.files.create(data={})
    client.files.all(get_all=False)
    client.files.get(file_id='')
    client.files.update(file_id='', data={})
    client.files.delete(file_id='')

Folders
^^^^^^^

::

    client.folders.create(data={})
    client.folders.all(get_all=False)
    client.folders.get(folder_id='')
    client.folders.update(folder_id='', data={})
    client.folders.delete(folder_id='')

Lists
~~~~~

Lists
^^^^^

::

    client.lists.create(data={})
    client.lists.update_members(list_id='', data={})
    client.lists.all(get_all=False)
    client.lists.get(list_id='')
    client.lists.update(list_id='', data={})
    client.lists.delete(list_id='')

List Abuse Reports
^^^^^^^^^^^^^^^^^^

::

    client.lists.abuse_reports.all(list_id='', get_all=False)
    client.lists.abuse_reports.get(list_id='', report_id='')

List Activity
^^^^^^^^^^^^^

::

    client.lists.activity.all(list_id='')

List Clients
^^^^^^^^^^^^

::

    client.lists.clients.all(list_id='')

List Growth History
^^^^^^^^^^^^^^^^^^^

::

    client.lists.growth_history.all(list_id='', get_all=False)
    client.lists.growth_history.get(list_id='', month='')

List Interest Categories
^^^^^^^^^^^^^^^^^^^^^^^^

::

    client.lists.interest_categories.create(list_id='', data={})
    client.lists.interest_categories.all(list_id='', get_all=False)
    client.lists.interest_categories.get(list_id='', category_id='')
    client.lists.interest_categories.update(list_id='', category_id='', data={})
    client.lists.interest_categories.delete(list_id='', category_id='')

List Interest Category Interests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    client.lists.interest_categories.interests.create(list_id='', category_id='', data={})
    client.lists.interest_categories.interests.all(list_id='', category_id='', get_all=False)
    client.lists.interest_categories.interests.get(list_id='', category_id='', interest_id='')
    client.lists.interest_categories.interests.update(list_id='', category_id='', interest_id='', data={})
    client.lists.interest_categories.interests.delete(list_id='', category_id='', interest_id='')

List Members
^^^^^^^^^^^^

::

    client.lists.members.create(list_id='', data={})
    client.lists.members.all(list_id='', get_all=False)
    client.lists.members.get(list_id='', subscriber_hash='')
    client.lists.members.update(list_id='', subscriber_hash='', data={})
    client.lists.members.create_or_update(list_id='', subscriber_hash='', data={})
    client.lists.members.delete(list_id='', subscriber_hash='')

List Member Activity
^^^^^^^^^^^^^^^^^^^^

::

    client.lists.members.activity.all(list_id='', subscriber_hash='')

List Member Goals
^^^^^^^^^^^^^^^^^

::

    client.lists.members.goals.all(list_id='', subscriber_hash='')

List Member Notes
^^^^^^^^^^^^^^^^^

::

    client.lists.members.notes.create(list_id='', subscriber_hash='', data={})
    client.lists.members.notes.all(list_id='', subscriber_hash='', get_all=False)
    client.lists.members.notes.get(list_id='', subscriber_hash='', note_id='')
    client.lists.members.notes.update(list_id='', subscriber_hash='', note_id='', data={})
    client.lists.members.notes.delete(list_id='', subscriber_hash='', note_id='')

List Merge Fields
^^^^^^^^^^^^^^^^^

::

    client.lists.merge_fields.create(list_id='', data={})
    client.lists.merge_fields.all(list_id='', get_all=False)
    client.lists.merge_fields.get(list_id='', merge_id='')
    client.lists.merge_fields.update(list_id='', merge_id='', data={})
    client.lists.merge_fields.delete(list_id='', merge_id='')

List Segments
^^^^^^^^^^^^^

::

    client.lists.segments.create(list_id='', data={})
    client.lists.segments.all(list_id='', get_all=False)
    client.lists.segments.get(list_id='', segment_id='')
    client.lists.segments.update(list_id='', segment_id='', data={})
    client.lists.segments.update_members(list_id='', segment_id='', data={})
    client.lists.segments.delete(list_id='', segment_id='')

List Segment Members
^^^^^^^^^^^^^^^^^^^^

::

    client.lists.segments.members.create(list_id='', segment_id='', data={})
    client.lists.segments.members.all(list_id='', segment_id='', get_all=False)
    client.lists.segments.members.delete(list_id='', segment_id='', subscriber_hash='')

List Signup Forms
^^^^^^^^^^^^^^^^^

::

    client.lists.signup_forms.create(list_id='', data={})
    client.lists.signup_forms.all(list_id='')

List Webhooks
^^^^^^^^^^^^^

::

    client.lists.webhooks.create(list_id='', data={})
    client.lists.webhooks.all(list_id='')
    client.lists.webhooks.get(list_id='', webhook_id='')
    client.lists.webhooks.update(list_id='', webhook_id='', data={})
    client.lists.webhooks.delete(list_id='', webhook_id='')

Reports
~~~~~~~

Reports
^^^^^^^

::

    client.reports.all(get_all=False)
    client.reports.get(campaign_id='')

Campaign Abuse Reports
^^^^^^^^^^^^^^^^^^^^^^

::

    client.reports.abuse_reports.all(campaign_id='')
    client.reports.abuse_reports.get(campaign_id='', report_id='')

Campaign Advice
^^^^^^^^^^^^^^^

::

    client.reports.advice.all(campaign_id='')

Click Details Report
^^^^^^^^^^^^^^^^^^^^

::

    client.reports.click_details.all(campaign_id='', get_all=False)
    client.reports.click_details.get(campaign_id='', link_id='')

Click Details Report Members
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    client.reports.click_details.members.all(campaign_id='', link_id='', get_all=False)
    client.reports.click_details.members.get(campaign_id='', link_id='', subscriber_hash='')

Domain Performance Reports
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    client.reports.domain_performance.all(campaign_id='')

EepURL Reports
^^^^^^^^^^^^^^

::

    client.reports.eepurl.all(camnpaign_id='')

Email Activity Reports
^^^^^^^^^^^^^^^^^^^^^^

::

    client.reports.email_activity.all(campaign_id='', get_all=False)
    client.reports.email_activity.get(campaign_id='', subscriber_hash='')

Locations Report
^^^^^^^^^^^^^^^^

::

    client.reports.locations.all(campaign_id='')

Sent To Reports
^^^^^^^^^^^^^^^

::

    client.reports.sent_to.all(campaign_id='', get_all=False)
    client.reports.sent_to.get(campaign_id='', subscriber_hash='')

Sub-Reports
^^^^^^^^^^^

::

    client.reports.subreports.all(campaign_id='')

Unsubscribes
^^^^^^^^^^^^

::

    client.reports.unsubscribes.all(campaign_id='', get_all=False)
    client.reports.unsubscribes.get(campaign_id='', subscriber_hash='')

Search
~~~~~~

Campaigns
^^^^^^^^^

::

    client.search_campaigns.get()

Members
^^^^^^^

::

    client.search_members.get()

Templates
~~~~~~~~~

Folders
^^^^^^^

::

    client.template_folders.create(data={})
    client.template_folders.all(get_all=False)
    client.template_folders.get(folder_id='')
    client.template_folders.update(folder_id='', data={})
    client.template_folders.delete(folder_id='')

Templates
^^^^^^^^^

::

    client.templates.create(data={})
    client.templates.all(get_all=False)
    client.templates.get(template_id='')
    client.templates.update(template_id='', data={})
    client.templates.delete(template_id='')

Default Content
^^^^^^^^^^^^^^^

::

    client.templates.default_content.all(template_id='')

Support
-------

If you are having issues, please let us know or submit a pull request.

License
-------

The project is licensed under the MIT License.

.. |mailchimp3 v2.0.13 on PyPi| image:: https://img.shields.io/badge/pypi-2.0.13-green.svg
   :target: https://pypi.python.org/pypi/mailchimp3
.. |MIT license| image:: https://img.shields.io/badge/licence-MIT-blue.svg
.. |Stable| image:: https://img.shields.io/badge/status-stable-green.svg

