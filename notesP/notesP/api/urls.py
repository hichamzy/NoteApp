
from django.urls import path
from .views import *
urlpatterns = [
    path('', getRoutes),
    path('notes', getNotes),
    #path('note/create/', createnote),
    path('note/<str:pk>/', datareturn),
   # path('note/<str:pk>/', datareturn),
    #path('note/<str:pk>/', datareturn),
    path('notes/create', CreateList.as_view(queryset=User.objects.all(), serializer_class=NoteSerializer)) #using generics view
]
