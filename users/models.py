from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.forms import widgets
from django.forms.fields import ChoiceField
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple, RadioSelect, Widget
from django import forms
class User(models.Model):
    name = CharField(max_length=70)
    surname = CharField(max_length=70)
    number = CharField(max_length=13)
    age = CharField(max_length=2)
    darajalar=(('beginner', 'baginner'),("elemantry","elemantry"), ("pre","pre"), ("inter", "inter"), ("upper", "upper"))
    daraja=CharField(choices=darajalar, null=True, default='beginner', max_length=30)
    vaqtlar=(('8:00','8:00'),('9:00','9:00'),('10:00','10:00'),('11:00','11:00'),('12:00','12:00'),('13:00','13:00'),('14:00','14:00'),('15:00','15:00'),('16:00','16:00'),('17:00','17:00'),('farqi yo`q', 'farqi yo`q'))
    vaqt=CharField(choices=vaqtlar, max_length=20, null=True)
    def __str__(self):
        return self.name

# Create your models here.
