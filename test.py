from mailchimp import MailChimp

 
client = MailChimp('didierserrat', 'dde1a01e091c530def679e42f2390b46-us9')

# print client.authorized_app.all()

# print client.authorized_app.get('870970111619')

# print client.automation.all()

# print client.automation.start('870970111619')

print client.growth.all('2822d76480')