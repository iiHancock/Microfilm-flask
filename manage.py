'''
Author: iiHancock
Time: 2021/11/6 10:43

'''
import os

from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app

env = os.environ.get('FLASK_ENV') or "default"

app = create_app(env)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
if __name__ == '__main__':
    manager.run()
