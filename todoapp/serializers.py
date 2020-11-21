from django.contrib.auth.models import User
from todoapp.models import Todo
from rest_framework import serializers
from authentication.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    # the_owner = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(), source="owner", write_only=True
    # )
    # owner = UserSerializer()

    class Meta:
        model = Todo
        fields = ["id", "title", "done", "owner"]
        # read_only_fields = ["owner"]
        # depth = 1
