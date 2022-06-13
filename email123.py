import smtplib
import random
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("rachel18.rc11@gmail.com", "password" )
    server.sendmail("rc5409@srmist", to, content)
    server.close()

if __name__ == "__main__":
    mail = input()
   
    # sendmail(mail, content)
    try:
        print("Please provide the content for the mail")
        teamname = input()
        password = input()
        content = teamname + password
        to = "rc5409@srmist.edu.in"
        sendmail(to, content)
        print("Mail sent successfully..")
    except Exception as e:
        print(e)
        print("unable to send the message")
