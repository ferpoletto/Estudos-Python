import smtplib

gmail_user = 'LOGIN'
gmail_password = 'SENHA'

sent_from = gmail_user
to = ['xxx@gmail.com']
subject = 'ASSUNTO'
body = 'MENSAGEM'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, body)
    server.close()

    print 'Email enviado com sucesso!'
except:
    print 'Deu ruim'
