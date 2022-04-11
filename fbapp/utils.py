import random 

from .models import Content, Gender

def find_content(gender):
    contents = Content.query.filter(Content.gender == Content[gender]).all()
    return random.choice(contents)
