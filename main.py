import parse, acquire, read_file, mailer

def main():

    # Obtain weather data
    data = acquire.acquire()

    # Organize data
    output = parse.parse(data)
    print(output)

    # Obtain mailing list
    csv_file = 'emails.txt'
    mailing_list = read_file.read_file(csv_file)

    # Sending the emails
    # mailer.mail(mailing_list,output)



main()

