from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Zombie
from .helpers import *
from .serializers import ZombieSerializer
from rest_framework.decorators import list_route


class ZombieViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class ZombieModelViewSet(viewsets.ModelViewSet):
    queryset = Zombie.objects.all()
    serializer_class = ZombieSerializer
    permission_classes = (permissions.AllowAny,)

    @list_route()
    def generate(self, request):
        name = generate_name()
        z = Zombie.objects.create(
            name=name,
            bio=generate_bio(name),
            date_of_birth=generate_date_of_birth(),
            date_of_rebirth=generate_date_of_rebirth(),
            avatar=generate_avatar()
        )
        serializer = ZombieSerializer(z)
        return Response(serializer.data)