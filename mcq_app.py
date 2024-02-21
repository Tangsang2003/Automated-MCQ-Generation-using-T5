# mcq_app.py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from app.mcq_generation import MCQGenerator
# from pdftextract import XPdf
import fitz
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pass'  # Replace with a strong secret key


class MCQForm(FlaskForm):
    context = TextAreaField('Paragraphs', validators=[DataRequired()])
    number_of_questions = IntegerField('Number of MCQs', validators=[
        DataRequired(), NumberRange(min=1, message='Please enter a positive integer.')])


class FileUploadForm(FlaskForm):
    # file = FileField('File')

    def validate_file(self, field):
        if field.data:
            if not field.data.filename.lower().endswith('.pdf'):
                raise ValidationError('Only PDF files are allowed.')

    number_of_questions = IntegerField('Number of MCQs',
                                       validators=[DataRequired(),
                                                   NumberRange(min=1, message='Please enter a positive integer.'
                                                               )])

    submit = SubmitField('Upload')
    file = FileField('File', validators=[
        DataRequired(),
        validate_file
    ])


MCQ_Generator = MCQGenerator(True)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MCQForm()
    file_upload_form = FileUploadForm()

    if form.validate_on_submit():
        paragraphs = form.context.data
        questions = MCQ_Generator.generate_mcq_questions(paragraphs, form.number_of_questions.data
                                                         )[0:form.number_of_questions.data]
        title = "Results"
        return render_template('results.html', mcqs=questions, title=title)

    if file_upload_form.validate_on_submit():
        # Process the file data (e.g., print the content)
        uploaded_file = file_upload_form.file.data
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, uploaded_file.filename)
        uploaded_file.save(file_path)
        file_path = "./uploads/" + uploaded_file.filename
        reader = fitz.open(file_path)
        number_of_pages = reader.page_count
        text = ""

        for i in range(number_of_pages):
            page = reader[i]
            text += page.get_text("text") + ' '

        text = ' '.join(text.split())  # Remove extra spaces and line breaks
        # print(txt)
        paragraphs = text
        questions = MCQ_Generator.generate_mcq_questions(paragraphs,
                                                         file_upload_form.number_of_questions.data
                                                         )[0:form.number_of_questions.data]
        reader.close()
        os.remove(file_path)
        title = "Results"
        return render_template('results.html', mcqs=questions, title=title)
    title = "Home"
    return render_template('New-index.html', form=form, file_upload_form=file_upload_form, title=title)


if __name__ == '__main__':
    app.run(debug=True)
