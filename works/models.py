from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.response import Response
from django.core import serializers
import json
# from account.models import Restaurants
import xml.etree.cElementTree as et


class Description(models.Model):
    """[Descriptio model]

    Args:
        models ([type]): [description]
    """
    description = models.TextField()
    menu = models.CharField(max_length=155)

    # def __str__(self):
    #     pass
    #     # return str(self.name)


class Tags(models.Model):
    """[Tags table]

    Args:
        models ([type]): [description]
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class ProgLang(models.Model):  # programming language
    """[programming language table]

    Args:
        models ([type]): [description]
    """
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='prog_langs')

    def __str__(self):
        return str(self.name)

    def is_svg(self, filename):
        tag = None
        with open(filename, "r") as f:
            try:
                for event, el in et.iterparse(f, ('start',)):
                    tag = el.tag
                    break
            except et.ParseError:
                pass
        return tag == '{http://www.w3.org/2000/svg}svg'

    def validate_svg(self, file, valid):
        if not is_svg(file):
            print('not svg')
            # raise ValidationError("File not svg")


class Works(models.Model):
    """
    create projects rable in DB

    Args:
        models ([type]): [description]

    Returns: 
    """
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='works')
    prog_lang = models.CharField(max_length=200)
    # prog_lang = models.ManyToManyField(
    #     ProgLang, blank=True)  # programming language []
    work_type = models.CharField(
        max_length=100)  # ex. web, app etc... []
    description = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    tags = models.CharField(max_length=200)  # []
    # tags = models.ManyToManyField(Tags, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
