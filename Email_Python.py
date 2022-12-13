#This code uses the Fernet class from the cryptography library to generate an encryption key, create a Fernet object, and encrypt the password and email message using the key. 
#The encrypted password and message are then used in the code instead of the plain text versions.Note that this is just one example of how you could encrypt the code, and there are other ways to do it using different algorithms and libraries. Encrypting the code can help protect the sensitive data from being accessed by unauthorized parties, but it does not provide complete security on its own. 
#part two is a one time code
#next phase could be 2FA introduced to this code

from cryptography.fernet import Fernet
from pyotp import TOTP
import smtplib

# Generate an encryption key
key = Fernet.generate_key()

# Use the key to create a Fernet object, which can be used to encrypt and decrypt data
fernet = Fernet(key)

# Encrypt the password
encrypted_password = fernet.encrypt(b"beta123")

# Encrypt the email message
encrypted_message = fernet.encrypt(b"Hello World")

# Generate a shared secret key and display the QR code for the user to scan
totp = TOTP('base32secret3232')
print(totp.provisioning_uri(my_email, issuer_name="ProtonMail"))

# Prompt the user for the one-time code and verify it
one_time_code = input("Enter one-time code: ")
if not totp.verify(one_time_code):
    print("Invalid one-time code")
    exit(1)

# If the one-time code is valid, proceed with logging in to the email account

# Use the encrypted password and message in the code
my_email = 'test@proton.me'
connection = smtplib.SMTP('smtp.proton.me', 587)
connection.starttls()
connection.login(user = my_email, password = encrypted_password)
connection.sendmail(from_addr = my_email, to_addrs = 'receipentemail@proton.me', msg = encrypted_message)
connection.close()







