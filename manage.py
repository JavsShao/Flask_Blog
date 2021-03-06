from flask_script import Manager

from app import app, db, models
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()