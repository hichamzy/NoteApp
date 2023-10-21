from rest_framework.serializers import ModelSerializer
from .models import *

class NoteSerializer(ModelSerializer):
    class Meta:
        model=Note
        fields='__all__' #serializer tous les attributs si on doit just serialize un des attribut ajouter ['body',..]
