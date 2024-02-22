import textwrap

from app.mcq_generation import MCQGenerator


def show_result(generated: str, answer: str, context: str, original_question: str = ''):
    
    print('Context:')

    for wrap in textwrap.wrap(context, width=120):
        print(wrap)
    print()
    print("Original Question:")
    print(original_question)

    print('Question:')
    print(generated)

    print('Answer:')
    print(answer)
    print('-----------------------------')


MCQ_Generator = MCQGenerator(True)

context_lol = ''' 
In the heart of history, students at the secondary level embark on a journey to unravel the tales of the past.
 From ancient civilizations to modern revolutions, they explore the events and figures that have shaped our 
 world. Through in-depth studies, students analyze the causes and consequences of historical events, gaining 
 insights into the triumphs and challenges faced by societies throughout time. They examine the political 
 movements, cultural shifts, and technological advancements that have left an indelible mark on humanity. 
 As they navigate the historical landscape, students not only absorb facts and dates but also cultivate 
 critical thinking skills to interpret and evaluate different perspectives. History becomes a living 
 narrative, inviting students to connect with the past and draw lessons for the present and future
'''
MCQ_Generator.generate_mcq_questions(context_lol, 4)
