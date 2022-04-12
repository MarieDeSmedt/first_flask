import random 

from .models import Content, Gender

def find_content():
    contents = Content.query.all()
    return random.choice(contents)
