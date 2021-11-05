from flask import Flask, render_template, flash, request, redirect, url_for
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(200), nullable=False)

aplic = db.Table('aplicacoes',
                      db.Column('vaga_id', db.Integer, db.ForeignKey('vaga.id')),
                      db.Column('candidato_id', db.Integer, db.ForeignKey('candidato.id'))
                      )

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    aplicacoes = db.relationship('Vaga', secondary=aplic, backref=db.backref('aplicacoes', lazy='dynamic'))

class Vaga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    criada = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    titulo = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'))

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    vagas = db.relationship('Vaga', backref='vaga.id')

"""Códigos Site de Postagens

@app.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)
    
def get_post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('o título é obrigatório!')
        else:
            post = Posts(title=title, content=content)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('título obrigatório!')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(post.title))
    return redirect(url_for('index'))

"""
@app.route('/')
def index():
    vagas = Vaga.query.all()
    return render_template('index.html', vagas=vagas)

def get_vaga(vaga_id):
    vaga = Vaga.query.filter_by(id=vaga_id).first()
    if vaga is None:
        abort(404)
    return vaga

@app.route('/<int:vaga_id>')
def vaga(vaga_id):
    vaga = get_vaga(vaga_id)
    return render_template('vaga.html', vaga=vaga)

@app.route('/criar_vaga', methods=('GET', 'POST'))
def criar_vaga():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        if not titulo:
            flash('o título é obrigatório!')
        else:
            vaga = Vaga(titulo=titulo, descricao=descricao)
            db.session.add(vaga)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('criar_vaga.html')

@app.route('/<int:id>/editar_vaga', methods=('GET', 'POST'))
def editar_vaga(id):
    vaga = get_vaga(id)

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        if not titulo:
            flash('título obrigatório!')
        else:
            vaga.title = titulo
            vaga.content = descricao
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('editar_vaga.html', vaga=vaga)

@app.route('/<int:id>/apagar_vaga', methods=('POST',))
def apagar_vaga(id):
    vaga = get_vaga(id)
    db.session.delete(vaga)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(vaga.titulo))
    return redirect(url_for('index'))
