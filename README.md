# Minor-Project-T5-Transformers-MCQ-Generation
#### Multiple Choice Questions Generation using T5 Transformers.

This project focuses on generating multiple-choice questions (MCQs) using T5 Transformers. 
Two T5-small models have been fine-tuned. One has been fine-tuned on the SQuAD dataset for question-answer pair generation. And the other has been fine-tuned on the RACE dataset for generation of distractors (wrong answers).


## Features
- Utilizes two instances of fine-tuned T5 transformers, one for Question-Answer Pair Generation and the other for Distractors Generation.
- Also utilizes Sense-2-Vec to generate additional distractors in-case of insufficient number of distractors.
- Generates MCQs based on the input text.
- Also, provides a feature for inputting text directly through a PDF file.
- A web-interface built using Python Flask for easy interaction of users with the model.

## Pre-requisites
- This project has been built using the Python 3.8 and the packages associated with Python 3.8. So, if any problems arise while using newer Python version, please consider using a virtual environment using Python 3.8 and try again.
'''
This is not working.
'''