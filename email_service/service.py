from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
# OBRIGATORIAMENTE O EMAIL PRECISA SER CORPORATIVO
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()

    to_email = data.get('to')
    subject = data.get('subject')
    message = data.get('message')

    try:
        email = EmailMessage()
        email['From'] = 'testeo@alunos.utfpr.edu.br'
        email['To'] = to_email
        email['Subject'] = subject
        email.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #chave SMTP precisa ser configurada dentro do usuario corporativo
            smtp.login('teste@alunos.utfpr.edu.br', 'aqes asde nsoq')
            smtp.send_message(email)

        return jsonify({"status": "sucesso"}), 200
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
        #return jsonify({"status": "erro", "detalhes": str(e)})
        raise
