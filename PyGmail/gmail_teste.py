from PyGmail.gmail import enviar_email

destinatario = input('Digite o destinatário: ')
assunto = input("Digite o assunto do email: ")
mensagem = input('Digite a mensagem do email: ')

enviar_email(destinatario, assunto, mensagem)
