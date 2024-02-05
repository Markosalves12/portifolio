# from dados import sender_email, receiver_email, receiver_email2, password
# from html import html


import smtplib, ssl

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


"""
sender_email = seuemail@gmail.com
receiver_email = emailquerecebe@gmail.com -- pode ser qualquer conta @outlook, @yahoo, @suaempresa
receiver_email2 = emailquerecebe2@gmail.com -- pode ser qualquer conta @outlook, @yahoo, @suaempresa
password = sua senha de app "sem espaços
""""


mensagem = MIMEMultipart()
mensagem['Subject'] = "Teste"
mensagem['From'] = sender_email
mensagem['To'] = receiver_email
mensagem['Body'] = html --- > "pode ser uma string ou um codigo html no corpo da mensagem"

mensagem.attach(MIMEText(mensagem['Body'], _subtype='html'))

# mensagem.attach(MIMEText(mensagem['Body'], _subtype='plain')) -- > caso seja uma string
# mensagem.attach(MIMEText(mensagem['Body'], _subtype='html')) --> caso seja um html

#Primeiro anexo é um png
anexo1 = r"C:\Users\Markos Alves\Downloads\logo_branca.png".replace("\\","/")
with open(anexo1, 'rb') as anexo1:
    # para PNG _maintype = Image, _subtype = png
    parte = MIMEBase('Image', 'png')
    parte.set_payload(anexo1.read())

encoders.encode_base64(parte)

parte.add_header(
    "Content-Disposition",
    f"attachment; filename={anexo1}",
)

mensagem.attach(parte)

# segundo anexo é um pdf
anexo1 = r"C:\Users\Markos Alves\Downloads\PySpark SQL Recipes.pdf".replace("\\","/")
with open(anexo1, 'rb') as anexo1:
    # para pdf _maintype = application, _subtype = pdf
    parte = MIMEBase('application', 'pdf')
    parte.set_payload(anexo1.read())

encoders.encode_base64(parte)

parte.add_header(
    "Content-Disposition",
    f"attachment; filename={anexo1}",
)

mensagem.attach(parte)

# Gerenciador de contexto ssl
contexto = ssl.create_default_context()
# servidor smtp local
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=contexto) as servidor:
    servidor.login(sender_email, password=password)
    servidor.sendmail(
        sender_email, [receiver_email, receiver_email2], mensagem.as_string()
    )












