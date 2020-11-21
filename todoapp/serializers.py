from django.contrib.auth.models import User
from todoapp.models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    the_owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="owner", write_only=True
    )

    class Meta:
        model = Todo
        fields = ["id", "title", "done", "owner", "the_owner"]
        depth = 1
