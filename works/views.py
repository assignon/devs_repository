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

from works.models import Works, Description, Tags
from works.serializers import WorksSerializer, DescriptionSerializer


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
        # user_id = request.query_params.get('userId')
        works = Works.objects.all().order_by('-pk')
        # works = self.get_queryset()

        # serializer = self.get_serializer_class()(works)
        return Response(serializers.serialize('json', works))
        # return Response(serializer.data)


class Description_view(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def work_desc(self, request):
        work_name = request.query_params.get('work_name')
        # get description id with work name
        description_id = Works.objects.get(name=work_name).description_id
        # get description by id
        description = Description.objects.get(id=description_id)
        return Response([{'description': description.description, 'menu': description.menu}])
        # return Response('hallo')
