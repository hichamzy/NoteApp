from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import *
from .CRUD import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# Create your views here.



@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)





@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all().order_by('-updated')
    serializer=NoteSerializer(notes,many=True) #many for multiple objets
    return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])

def datareturn(request,pk):
    if request.method=='GET':
        return getNote(request,pk)
    if request.method=='PUT':
        return updateNote(request,pk)
    if request.method=='DELETE':
        return deleteNote(request,pk)    


#@api_view(['POST'])
#def createnote(request):
   # data=request.data 
  #  note=Note.objects.create(
   #     body=data['body']
  #  )
  #  serialiser =NoteSerializer(note,many=False)
   # return Response(serialiser.data)


#using generics class from restfreamwork
class CreateList(generics.CreateAPIView):
     queryset = Note.objects.all()
     serializer_class = NoteSerializer
  
