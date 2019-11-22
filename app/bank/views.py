from bank.models import Branch
from rest_framework import viewsets
from .serializers import Branch_Serializer


class Branch_Viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = Branch_Serializer
