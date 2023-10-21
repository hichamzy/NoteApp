from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import *


def getNotes(request):
    notes=Note.objects.all().order_by('-updated')
    serializer=NoteSerializer(notes,many=True) #many for multiple objets
    return Response(serializer.data)



def getNote(request,pk):
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(note,many=False) #many for multiple objets
    return Response(serializer.data)


def updateNote(request,pk):
    note=Note.objects.get(id=pk)
    data=request.data
    serializer=NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
         serializer.save() # modify the data of note with the new data from the request
   
    return Response(serializer.data)
 


def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete();
    return Response('Note was deleted')

