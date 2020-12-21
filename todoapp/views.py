from django.http import request
from django.shortcuts import render
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
def home(request):
    """
    Home view
    """
    return render(request, "home.html")


class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def update(parameter_list):
        """
        docstring
        """
        print("update has been overidden")
