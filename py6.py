import smtplib

try:
    # Create your SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Use TLS to add security
    smtp.starttls()

    # User Authentication
    smtp.login("your email", "password")

    #  Message
    message = "Message"

    smtp.sendmail("your email", "receiver email", message)


    smtp.quit()
    print("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....", ex)
