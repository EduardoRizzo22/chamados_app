from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from app import db
from app.models.chamado import Chamado

bp = Blueprint('chamado', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    chamados = Chamado.query.all()
    return render_template('dashboard.html', chamados=chamados)

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
