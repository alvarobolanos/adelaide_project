import smtplib, getpass

def mail(mailing_list,message):

    # Connecting to outgoing email server
    connection = smtplib.SMTP('smtp.gmail.com', '587')

    # Start TLS encryption
    connection.starttls()

    # Logging in
    from_email = 'noreply.alvarobolanos@gmail.com'
    password = getpass.getpass("What's your password? ")
    connection.login(from_email, password)

    # Send email for each recipient in mailing_list
    for name, to_email in mailing_list.items():
        body = "Subject: Your daily weather forecast.\n"
        body += 'Hi ' + name + '!\n\n'
        body += message + '\n\n'
        body += 'Enjoy your day :)'
        connection.sendmail(from_email, to_email, body)

    connection.quit()
