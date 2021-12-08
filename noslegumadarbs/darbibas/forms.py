from django.forms import (
    Form,
    CharField,
    FloatField,
)


class StudentForm(Form):

    name = CharField()
    grades = CharField()