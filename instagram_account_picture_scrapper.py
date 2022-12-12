import instaloader

test = instaloader.instaloader()

# Prompt the user to enter an Instagram account name
account = input('Enter an Instagram account name: ')

# Check if the account name is valid before attempting to download its profile
if test.check_account_exists(account):
  test.download_profile(account)
else:
  print('Sorry, the account name you entered is not valid.')
