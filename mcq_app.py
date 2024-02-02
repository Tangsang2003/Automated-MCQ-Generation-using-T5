# mcq_app.py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired
from app.mcq_generation import MCQGenerator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pass'  # Replace with a strong secret key


class MCQForm(FlaskForm):
    context = TextAreaField('Paragraphs', validators=[DataRequired()])
    number_of_questions = IntegerField('Number of MCQs', validators=[DataRequired()])


MCQ_Generator = MCQGenerator(True)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MCQForm()

    if form.validate_on_submit():
        paragraphs = form.context.data
        questions = MCQ_Generator.generate_mcq_questions(paragraphs, form.number_of_questions.data
                                                         )[0:form.number_of_questions.data]
        return render_template('results.html', mcqs=questions)

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
