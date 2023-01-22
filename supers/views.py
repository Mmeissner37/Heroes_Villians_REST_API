from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers



@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('super_type')
        queryset = Supers.objects.all()
        if super_type:
            queryset = queryset.filter(super__type=super_type)
        serializer = SupersSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    super_types = Supers.objects.all()
    for super_type in super_types:
        super = Supers.objects.filter(super_type=super_type)
        super.serializer = SupersSerializer(super, many=True)
        custom_response_dictionary[super_type] = {
            'Heroes': [],
            'Villains': [],
        }
        return Response(custom_response_dictionary) 

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_list_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        super = get_list_or_404(Supers, pk=pk)
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


