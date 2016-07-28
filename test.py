from mailchimp3 import MailChimp


client = MailChimp('MAILCHIMP_USER', 'MAILCHIMP_SECRET')

print client.list.all(fields="lists.name,lists.id")

print client.authorized_app.all()

print client.automation.all()
