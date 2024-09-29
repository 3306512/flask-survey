from models import db, Survey, Answer
from main import app


with app.app_context():
    db.session.query(Answer).delete()
    db.session.query(Survey).delete()
    new_survey = Survey(question='test11111111111111111111111111111111111111111111111111111111111')
    db.session.add(new_survey)
    second_survey = Survey(question='test111111111wesrdftyguhyiuopkdxzfdx11111111111111111')
    db.session.add(second_survey)
    new_answer = Answer(answer='answer to test1', survey_id=1)
    db.session.add(new_answer)
    db.session.commit()
