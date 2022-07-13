from email.message import EmailMessage
import smtplib
import ssl


class Mail():
    def send_email(info):
        port = 465
        sender = 'SENDER EMAIL' # email@example.com
        receiver = 'RECIEVER EMAIL' #email@example.com
        password = '16 DIGIT CODE FOR SENDER EMAIL'  # e.g. afkalakdjfaowpat

        # info[0][0] is the title of the item thats on sale
        subject = f'{info[0][0]}'
        # Layout for the body of the email
        body = f'Current price: £{info[1]}\nOriginal price: £{info[0][1]}\nDiscount: -{info[2]}%\n\nLink:{info[3]}'

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)

        # Context makes a secure connection
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, em.as_string())
            print('Mail Sent')
