from flask import Flask, render_template, request, jsonify
from models import db, Survey, Answer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app=app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html', surveys=Survey.query.all())


@app.route('/submit', methods=["POST"])
def submit():
    request_data = request.get_json()
    answer = request_data.get('answer')
    survey_id = request_data.get('survey_id')
    answer_model = Answer(survey_id=survey_id, answer=answer)
    db.session.add(answer_model)
    db.session.commit()
    return jsonify({'status': "success"})


if __name__ == '__main__':
    app.run(debug=True)
