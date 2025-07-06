from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import User
from flask_login import login_required, current_user
from app import db
import requests

def notificar_email(destinatario, assunto, mensagem):
    payload = {
        "to": destinatario,
        "subject": assunto,
        "message": mensagem
    }
    try:
        requests.post("http://localhost:5001/send-email", json=payload)
    except Exception as e:
        print("Erro ao enviar e-mail:", e)


bp = Blueprint('user', __name__)

# Rota de listagem de usuário

@bp.route('/listar')
@login_required
def listar_usuarios():
    usuarios = User.query.all()
    return render_template('listar.html', usuarios=usuarios)

# Rota de criação de usuário

@bp.route('/user/novo')
@login_required
def novo_usuario():
    return render_template('user/novo.html')

# Rota de envio de dados para o banco de usuário

@bp.route('/user/criar', methods=['POST'])
@login_required
def criar_usuario():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    novo = User(username=username, password=password, role=role)
    db.session.add(novo)
    db.session.commit()
    notificar_email(username, "Bem-vindo!", "Seu usuário foi criado com sucesso.")
    return redirect(url_for('user.listar_usuarios'))

# Rota de deleção de usuário

@bp.route('/user/deletar/<int:id>', methods=['POST'])
@login_required
def deletar_usuario(id):
    usuario = User.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('user.listar_usuarios'))
