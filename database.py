from peewee import *

db = PostgresqlDatabase(
    'Parsing',
    user='Parser',
    password='parsing',
    host='127.0.0.1',
    port=5432
)

class ArrayField(Field):
    __delimiter = ' *** '
    field_type = 'TEXT'

    def db_value(self, value: list):
        return self.__delimiter.join(value)

    def python_value(self, value: str):
        return value.split(self.__delimiter)

    def set_delimiter(self,val: str):
        if not isinstance(val,str):
            raise ValueError(f'Not string! {type(val)}')
        self.__delimiter = val


class BaseModel(Model):
    class Meta:
        database = db


class Post(BaseModel):
    id = BigAutoField(primary_key=True,
                      db_column='id')
    title = TextField(db_column='post_title',
                      null=False)
    img_src = TextField(null=True)
    snippets = ArrayField()
    description = TextField()
    raw_html = TextField()








