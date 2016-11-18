from peewee import *
import datetime

DATABASE = MySQLDatabase('REST', host = 'localhost', user = 'root', passwd = 'root')

class Course(Model):
    class Meta:
        database = DATABASE
        db_table = 'courses'

    title = CharField(unique = True, max_length = 250)
    description = TextField()
    created_at = DateTimeField(default = datetime.datetime.now())

    def to_json(self):
        return {'id' : self.id, 'title' : self.title, 'description' : self.description}

def create_course():
    title = 'Curso Ejemplo'
    description = 'Descripcion del curso'

    if not Course.select().where(Course.title == title):
        Course.create(title = title, description = description)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables( [Course], safe = True )
    create_course()
    DATABASE.close()