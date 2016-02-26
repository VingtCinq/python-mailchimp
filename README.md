[![mailchimp3 v1.0.14 on PyPi](https://img.shields.io/badge/pypi-1.0.14-green.svg)](https://pypi.python.org/pypi/mailchimp3)
![MIT license](https://img.shields.io/badge/licence-MIT-blue.svg)
![Stable](https://img.shields.io/badge/status-stable-green.svg)

# python-mailchimp-api

A python client for v3 of MailChimp API

## About

This package aims to provide a straighforward python client to interact with Mailchimp API v3.

## Installation

This client is hosted at PyPi under the name `mailchimp3`, to install it, simply run

`pip install mailchimp3`

## Dependencies

requests >= 2.7.0

## Examples

    from mailchimp3 import MailChimp
    
    client = MailChimp('YOUR USERNAME', 'YOUR SECRET KEY')
    
    client.list.all()  # returns all the lists
    client.list.get('123456')  # returns the list matching id '123456'
    client.campaign.all() # returns all the campaigns

## Usage

### Authorized Apps

    client.authorizedapp.all()
    client.authorizedapp.get(app_id='')

### Automation

#### Automation

    client.automation.all()
    client.automation.get(workflow_id='')
    client.automation.pause(workflow_id='')
    client.automation.start(workflow_id='')

#### Automation Email

    client.automationemail.all(workflow_id='')
    client.automationemail.get(workflow_id='', email_id='')
    client.automationemail.pause(workflow_id='', email_id='')
    client.automationemail.start(workflow_id='', email_id='')

#### Automation Email Queue

    client.automationemailqueue.all(workflow_id='', email_id='')
    client.automationemailqueue.get(workflow_id='', email_id='', member_id='')
    client.automationemailqueue.create(workflow_id='', email_id='', data='')

#### Automation Removed Subscribers

    client.automationeremovedsubscriber.all(workflow_id='')
    client.automationeremovedsubscriber.create(workflow_id='', data='')

### Campaign

#### Campaign

    client.campaign.all()
    client.campaign.get(campaign_id='')
    client.campaign.delete(campaign_id='')

#### Campaigns feedback

    client.feedback.all(campaign_id='')
    client.feedback.create(campaign_id='', data={})
    client.feedback.get(campaign_id='', feedback_id='')
    client.feedback.update(campaign_id='', feedback_id='', data={})
    client.feedback.delete(campaign_id='', feedback_id='')
  
### Conversations
  
    client.conversation.all()
    client.conversation.get(conversation_id='')
  
### Files
  
    client.file.all()
    client.file.create(data='')

### Interest

    client.interest.all(list_id, category_id, count=100)
    client.interest.create(list_id, category_id, post_data)
    client.interest.get(list_id, category_id, interest_id)
    client.interest.update(list_id, category_id, interest_id, post_data)
    client.interest.delete(list_id, category_id, interest_id)

### Lists
  
    client.list.all()
    client.list.get(list_id='')
    client.list.create(data='')
    client.list.update(list_id='', data='')
    client.list.delete(list_id='')
  
### Reports
  
    client.report.all()
    client.report.get(report_id='')
  
### Templates
  
    client.template.all()
    client.template.get(template_id='')
    client.template.update(template_id='', data='')
    client.template.delete(template_id='')

## Support

If you are having issues, please let us know.

## License

The project is licensed under the MIT License.
