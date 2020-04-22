from . import db


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    descricao = db.Column(db.String(128))

    def __repr__(self):
        return '<Curso {}>'.format(self.nome)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def data(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao
        }


class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    quantidade_alunos = db.Column(db.Integer)
    codigo_turma = db.Column(db.String(6))
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'))

    def __repr__(self):
        return '<Turma {}>'.format(self.nome)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_aluno = db.Column(db.String(64))
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'))

    def __repr__(self):
        return '<Aluno {}>'.format(self.nome_aluno)

    def save(self):
        db.session.add(self)
        db.session.commit()
