def send_email(destinatario, assunto, mensagem):
    import smtplib

    user = 'login'
    pwd = 'senha'

    FROM = user
    TO = destinatario if isinstance(destinatario, list) else [destinatario]
    SUBJECT = assunto
    TEXT = mensagem

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('Enviado com sucesso')
    except:
        print("Deu ruim...")
