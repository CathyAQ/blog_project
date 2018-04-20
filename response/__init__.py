from django.http.response import JsonResponse
from django.core import serializers
from django.db.models import QuerySet
import json


def render_response(request,code,data=None):
    extra = {
        "code":code
    }
    if isinstance(data,list) or isinstance(data,dict):
        extra.update({"data":data})
    return JsonResponse(extra)


def _serialize_to_json(data):
    if isinstance(data,QuerySet):
        param = serializers.serialize("json",data)
        return json.loads(param)
    return data


class ErrorCode(object):
    OK = 0
    NOT_FOUND = 404