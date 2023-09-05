from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ItemListSerializer 
from .models import Item
from accounts.models import Account
#from organisation.models import Role_Scenario

from rest_framework import status,viewsets
from django.db.models import F
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser 
from accounts.serializers import UserSerializer


# Create your views here.

#listing scenarios

@api_view(['GET']) 
def item_list(request):
    
    item_list = Item.objects.all().order_by('-id')
    serializer = ItemListSerializer(item_list, many=True)

    # if there is something in items else raise error
    if item_list:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

"""
@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def itemlist(request):
    user = UserSerializer(request.user)

    if (user.userorg_roles == Role_Scenario.role_scenario):
        item_list = Item.objects.all().order_by('-id')
        serializer = ItemListSerializer(item_list, many=True)

    # if there is something in items else raise error
        if item_list:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response("No records")        
"""