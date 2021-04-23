import json

from .models import State

from django.http.response import HttpResponse


def state_create(request):
    
    response = HttpResponse()
    query = State.objects.all()
    data = json.loads(request.body)
    query.create(**data).save()
    return response


def state_index(request):
    response = state_create(request)
    return response
