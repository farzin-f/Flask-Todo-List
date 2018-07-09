"""AlayaNotes

Usage:
  main.py [run]
  main.py initdb
"""
from docopt import docopt
import subprocess
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from alayatodo import app
from alayatodo.models import db, User, Todo
    
def _init_db():

    # Database initialisation
    db.create_all()

    # Filling the database with records for User and Todo models
    records = [
        User(username='user1',
             password=generate_password_hash('user1')),
        User(username='user2',
             password=generate_password_hash('user2')),
        Todo(user_id=1, description='Vivamus tempus'),
        Todo(user_id=1, description='lorem ac odio'),
        Todo(user_id=1, description='Ut congue odio'),
        Todo(user_id=1, description='Sodales finibus'),
        Todo(user_id=1, description='Accumsan nunc vitae'),
        Todo(user_id=2, description='Lorem ipsum'),
        Todo(user_id=2, description='In lacinia est'),
        Todo(user_id=2, description='Odio varius gravida')
        ]
    
    db.session.bulk_save_objects(records)
    db.session.commit()
    
    
if __name__ == '__main__':
    args = docopt(__doc__)
    if args['initdb']:
        _init_db()
        print "AlayaTodo: Database initialized (alayacare/todos.db)."
    else:
        app.run(use_reloader=True)
