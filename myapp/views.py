from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from myapp.models import Url
from myapp.serializers import LinkSerializer
import uuid
from django.http import HttpResponseNotFound, Http404, HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

def index(request):
    urls = Url.objects.all()
    return render(request, 'index.html', {'urls': urls})

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)

@api_view(['GET'])
def get_long_url(request, uuid):
    try:
        url = Url.objects.get(uuid=uuid)
        serializer = LinkSerializer(url)
        return Response(serializer.data)
    except Url.DoesNotExist:
        return Response({'error': 'Short URL not found.'}, status=status.HTTP_404_NOT_FOUND)


def redirect_long_url(request, uuid):
    try:
        url = get_object_or_404(Url, uuid=uuid)
        return redirect(url.link)
    except Http404:
        return HttpResponseNotFound("Short URL not found.")



