from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    answer = db.Column(db.String(250), nullable=False)
    survey = db.relationship('Survey', backref=db.backref('answers', lazy=True))

    @validates('answer')
    def validate_answer(self, key, value: str):
        if value.strip() == '':
            raise ValueError('can not be an empty string')
        return value

