from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.core import serializers
from django.db.models import Q
import json
# from django.contrib.auth.hashers import make_password
################################## DRF IMPORTS #######################################
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from works.models import Works, Description, Tags, Skills, ProgLang, About
from works.serializers import WorksSerializer, DescriptionSerializer, SkillsSerializer, ProgLangSerializer, AboutSerializer
import re
import os
from datetime import datetime
import codecs
from django.core.files import File
from django.core.mail import send_mail


class SearchPattern():

    """
    search and return search query patterns
    patterns:
        # website
        # website+app+... | website,app,pwa
        # > date | < date | = date
        # website > date | website < date | website = date
        # website,cli > date | website,pwa < date website,pwa = date
        # website+cli > date | website+pwa < date website+pwa = date
        # newest | oldest
    Args:
        query (string): [user search query]
    """

    def __init__(self):
        pass
        # self.query = query
        # self.pattern_recognizer(query)

    def date_re(self, date):
        """
        date regular expression
        Args:
            date (date): []
        """

        regex = [
            # year-month-day
            {'date': 'ymd', "re": "([1-9]{4}),([0-9]{2}),([0-9]{2})"},
            # year-month
            {'date': 'ym', "re": "([1-9]{4}),([0-9]{1})"},
            {'date': 'y', "re": "([1-9]{4})"},  # year
            {'date': 'm', "re": "([0-9]{1})"},  # month
        ]
        # date_type = None
        # for reg in regex:
        #     match = re.findall(reg['re'], date)
        #     if match:
        #         date_type = reg['date']
        #     else:
        #         data_type = 'None'
        i = 0
        while i < len(regex):
            match = re.findall(regex[i]['re'], date)
            if match:
                date_type = regex[i]['date']
                break
            i += 1
        else:
            date_type = None
        return date_type

    def pattern_recognizer(self, query):
        """
        determine the form of the query and call the associated function
        Args:
            query (string): [user search query]
        """
        # regular expression migh be a better solution
        if "+" in query:
            # split query string into a list
            queries = query.split("+")
            # for q in queries:
            func = self.search_by_words(queries)

        elif "," in query:
            # split query string into a list
            queries = query.split(",")
            # for q in queries:
            func = self.search_by_words(queries)

        elif ">" in query:
            string, date = query.split(">")  # split query string into a list
            if "," in string:
                words = string.split(",")  # split query string into a list
                # for word in words:
                func = self.search_by_gt_words(date, words)

            elif "+" in string:
                words = string.split("+")  # split query string into a list
                # for word in words:
                func = self.search_by_gt_words(date, words)
            else:
                func = self.search_by_gt(date)

        elif "<" in query:
            string, date = query.split(">")  # split query string into a list
            if "," in string:
                words = string.split(",")  # split query string into a list
                # for word in words:
                func = self.search_by_lt_words(date, words)
            elif "+" in string:
                words = string.split("+")  # split query string into a list
                # for word in words:
                func = self.search_by_lt_words(date, words)
            else:
                func = self.search_by_lt(date)

        elif "=" in query:
            string, date = query.split("=")  # split query string into a list
            if "," in string:
                words = string.split(",")  # split query string into a list
                # for word in words:
                func = self.search_by_equal_words(date, words)

            elif "+" in string:
                words = string.split("+")  # split query string into a list
                # for word in words:
                func = self.search_by_equal_words(date, words)
            else:
                func = self.search_by_equal(date)

        elif query == "newest":
            func = self.search_by_words("newest")

        elif query == "oldest":
            func = self.search_by_words("oldest")

        else:
            func = self.search_by_word(query)
        # retrun founded data
        return func

    def search_by_word(self, query):
        """
        search by word
        pattern:
            # pattern: 
        Args:
            query (string): user search query or queries]
        """
        works = Works.objects.filter(tags__icontains=query)
        return serializers.serialize('json', works)

    def search_by_words(self, words):
        """
        search by words
        pattern:
            # pattern: 
            # # website, 
            # # website+app+... | website,app,pwa
        Args:
            words (array): user search query or queries]
        """

        works_data = []
        for word in words:
            works = Works.objects.all().filter(
                tags__icontains=word)
            works_data.extend(works)
        # remove duplcated works
        rm_duplicate = list(dict.fromkeys(works_data))

        return serializers.serialize('json', rm_duplicate)

    def search_by_equal(self, date):
        """
        search by = date
        pattern:
            # = date
        Args:
            date (string): [user search query]
        """

        date_regex = self.date_re(date)
        # if date_regex == 'ymd':  # year-month-day date format
        #     works = Works.objects.filter(
        #         added_on__date=datetime.date(date))
        # elif date_regex == 'ym':  # year-month date format
        #     year, month = date.split("-")
        #     works = Works.objects.filter(
        #         Q(added_on__year=year) & Q(added_on__month=month))
        # elif date_regex == "y":  # year date format
        #     works = Works.objects.filter(added_on__year=date)
        # else:  # month date format
        #     works = Works.objects.filter(added_on__month=date)
        works = Works.objects.filter(
            added_on__year=date)
        print(date)
        return serializers.serialize('json', works)
        # return date_regex

    def search_by_gt(self, date):
        """
        search by > date
        pattern:
            # > date
        Args:
            date (string): [user search query or queries]
        """

        date_regex = self.date_re(date)
        if date_regex == 'ymd':  # year-month-day date format
            works = Works.objects.filter(
                added_on__date__gt=datetime.date(date))
        elif date_regex == 'ym':  # year-month date format
            year, month = date.split("-")
            works = Works.objects.filter(
                Q(added_on__year__gt=year) & Q(added_on__month__gt=month))
        elif date_regex == "y":  # year date format
            works = Works.objects.filter(added_on__year__gt=date)
        else:  # month date format
            works = Works.objects.filter(added_on__month__gt=date)

        return serializers.serialize('json', works)

    def search_by_lt(self, date):
        """
        search by < date
        pattern:
            # < date
        Args:
            date (string): [user search query or queries]
        """

        date_regex = self.date_re(date)
        if date_regex == 'ymd':  # year-month-day date format
            works = Works.objects.filter(
                added_on__date__lt=datetime.date(date))
        elif date_regex == 'ym':  # year-month date format
            year, month = date.split("-")
            works = Works.objects.filter(
                Q(added_on__year__lt=year) & Q(added_on__month__lt=month))
        elif date_regex == "y":  # year date format
            works = Works.objects.filter(added_on__year__lt=date)
        else:  # month date format
            works = Works.objects.filter(added_on__month__lt=date)
        # pub_date__gte=datetime.date(2005, 1, 30)
        return serializers.serialize('json', works)

    def search_by_equal_words(self, date, words):
        """
        search by = date
        pattern:
            # = date
            # website > date
            # website,cli = date
            # website+cli = date
        Args:
            date (string): [date query or queries]
            words (array): [word query or queries]
        """
        date_regex = self.date_re(date)
        if date_regex == 'ymd':  # year-month-day date format
            works = Works.objects.filter(
                Q(added_on__date=datetime.date(date)) & Q(tags__in=words)
            )
        elif date_regex == 'ym':  # year-month date format
            year, month = date.split("-")
            works = Works.objects.filter(
                Q(added_on__year=year) & Q(
                    added_on__month=month) & Q(tags__in=words)
            )
        elif date_regex == "y":  # year date format
            works = Works.objects.filter(
                Q(added_on__year=date) & Q(tags__in=words))
        else:  # month date format
            works = Works.objects.filter(
                Q(added_on__month=date) & Q(tags__in=words))
        # pub_date__gte=datetime.date(2005, 1, 30)
        return serializers.serialize('json', works)

    def search_by_gt_words(self, date, words):
        """
        search by > date
        pattern:
            # > date
            # website > date
            # website,cli > date
            # website+cli > date
        Args:
            date (string): [date query or queries]
            words (array): [word query or queries]
        """

        date_regex = self.date_re(date)
        if date_regex == 'ymd':  # year-month-day date format
            works = Works.objects.filter(
                Q(added_on__date__gt=datetime.date(date)) & Q(tags__in=words)
            )
        elif date_regex == 'ym':  # year-month date format
            year, month = date.split("-")
            works = Works.objects.filter(
                Q(added_on__year__gt=year) & Q(
                    added_on__month__gt=month) & Q(tags__in=words)
            )
        elif date_regex == "y":  # year date format
            works = Works.objects.filter(
                Q(added_on__year__gt=date) & Q(tags__in=words))
        else:  # month date format
            works = Works.objects.filter(
                Q(added_on__month__gt=date) & Q(tags__in=words))

        return serializers.serialize('json', works)

    def search_by_lt_words(self, date, words):
        """
        search by < date
        pattern:
            # < date
            # website < date
            # website,cli < date
            # website+cli < date
        Args:
            date (string): [date query or queries]
            words (array): [word query or queries]
        """

        date_regex = self.date_re(date)
        if date_regex == 'ymd':  # year-month-day date format
            works = Works.objects.filter(
                Q(added_on__date__lt=datetime.date(date)) & Q(tags__in=words)
            )
        elif date_regex == 'ym':  # year-month date format
            year, month = date.split("-")
            works = Works.objects.filter(
                Q(added_on__year__lt=year) & Q(
                    added_on__month__lt=month) & Q(tags__in=words)
            )
        elif date_regex == "y":  # year date format
            works = Works.objects.filter(
                Q(added_on__year__lt=date) & Q(tags__in=words))
        else:  # month date format
            works = Works.objects.filter(
                Q(added_on__month__lt=date) & Q(tags__in=words))
        # pub_date__gte=datetime.date(2005, 1, 30)
        return serializers.serialize('json', works)


class Works_view(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def all_works(self, request):
        """
         get all works from DB

        Args:
            request ([get]): [get works]
        """
        order_by = request.query_params.get('order_by')
        offset = request.query_params.get('offset')
        limit = request.query_params.get('limit')
        if order_by == 'default':
            works = Works.objects.all().order_by('-pk')[int(offset):int(limit)] \
                if offset != 0 and limit != 0 \
                else Works.objects.all().order_by('-pk')
        elif order_by == 'asc':
            works = Works.objects.all().order_by('pk')[int(offset):int(limit)] \
                if offset != 0 and limit != 0 \
                else Works.objects.all().order_by('pk')
        else:
            works = Works.objects.all().order_by('-pk')[int(offset):int(limit)] \
                if offset != 0 and limit != 0 \
                else Works.objects.all().order_by('-pk')
        # works = self.get_queryset()

        # serializer = self.get_serializer_class()(works)
        return Response(serializers.serialize('json', works))
        # return Response(serializer.data)

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def works_count(self, request):
        # get number of works in DB
        works_count = Works.objects.all().count()
        return Response(works_count)

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def search_works(self, request):
        search_query = request.query_params.get('query')
        # instantiate searchpattern class
        pattern = SearchPattern()
        response = pattern.pattern_recognizer(search_query)
        return Response(response)

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def related_works(self, request):
        """
        get work related works
        Args:
            request (get): [get works base on current work tags]

        Returns:
            [json]: [works objects data]
        """
        work_name = request.query_params.get('work_name')  # current work name
        related_works_data = []
        # get current work tags
        current_work_tags = Works.objects.get(name=work_name).work_type
        work_types = current_work_tags.split(",")  # split tags into array

        for wtype in work_types:
            # filter works on tags and exclude the current work
            works_related = Works.objects.exclude(name=work_name).filter(
                tags__icontains=wtype)
            related_works_data.extend(works_related)

        # remove duplcated works
        rm_duplicate = list(dict.fromkeys(related_works_data))

        return Response(serializers.serialize('json', rm_duplicate))

    @csrf_exempt
    @action(methods=['post'], detail=False)
    def sendmail(self, request):
        name = request.data['body']['name']
        email = request.data['body']['email']
        message = request.data['body']['message']
        # send email
        send_mail(
            f'Portfolio mail van {name}',
            message,
            email,
            ['yanick007.dev@gmail.com']
        )

        return Response(request.data)


class Description_view(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def work_desc(self, request):
        """
         get current work description from DB

        Args:
            request ([get]): [get description]
        """
        work_name = request.query_params.get('work_name')
        # get description id with work name
        description_id = Works.objects.get(name=work_name).description_id
        # get description by id
        description = Description.objects.get(id=description_id)
        # description_file = codecs.open(
        #     description.description, "r", "utf-8").read()
        f = open(f'{os.getcwd()}/media/{description.description.name}',
                 mode='r', encoding='utf8')
        myfile = File(f)

        desc_content = ""
        for i in myfile:
            desc_content += f' {i}'

        return Response([
            {
                'description': desc_content,
                'menu': description.menu,
                'url': description.url,
                'repository': description.repository
            }
        ])


class Skills_view(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def all_skills(self, request):
        """
        get skills from DB

        Args:
            request ([get]): [get skills]
        """
        categories = ['language', 'framework', 'database', 'other']
        skills_arr = []
        prog_langs_arr = []
        for category in categories:
            skills = Skills.objects.filter(category=category).values()
            skills_arr.append({category: skills})

        prog_langs = ProgLang.objects.all()
        for pl in prog_langs:
            prog_langs_arr.append({'name': pl.name})

        return Response({'skills': skills_arr, 'prog_langs': prog_langs_arr})


class ProgLang_view(viewsets.ModelViewSet):
    queryset = ProgLang.objects.all()
    serializer_class = ProgLangSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def get_pl(self, request):
        """
        get programming language base on id from DB

        Args:
            request ([get]): [get skills]
        """
        pl_arr = []
        pl_id = request.query_params.get('plId')
        pl = ProgLang.objects.get(id=pl_id)
        pl_arr.append({'name': pl.name, 'logo': pl.logo})
        return Response(pl_arr)


class About_view(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def about_content(self, request):
        """
         get about content from DB

        Args:
            request ([get]): [get about content]
        """
        about = About.objects.all()
        return Response(serializers.serialize('json', about))
