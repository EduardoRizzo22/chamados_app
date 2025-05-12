from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from app import db
from app.models.chamado import Chamado
from app.models.user import User


bp = Blueprint('chamado', __name__)

# Rota do dashboard

@bp.route('/dashboard')
@login_required
def dashboard():
    chamados = Chamado.query.all()
    return render_template('dashboard.html', chamados=chamados)

# Rota de criação de novo chamado

@bp.route('/chamado/novo', methods=['GET', 'POST'])
@login_required
def novo_chamado():
    if request.method == 'POST':
        chamado = Chamado(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            usuario_id=current_user.id
        )
        db.session.add(chamado)
        db.session.commit()
        return redirect('/dashboard')
    return render_template('chamados/novo.html')

# Rota de fechamento e exclusão de chamado; o front utiliza um script onde o controller é ativaddo.

@bp.route('/chamado/fechar/<int:id>', methods=['POST'])
@login_required
def fechar_chamado(id):
    chamado = Chamado.query.get(id)
    if chamado:
        chamado.status = 'fechado'
        db.session.commit()
    return redirect('/dashboard')

@bp.route('/chamado/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_chamado(id):
    chamado = Chamado.query.get(id)
    if chamado:
        db.session.delete(chamado)
        db.session.commit()
    return redirect('/dashboard')
