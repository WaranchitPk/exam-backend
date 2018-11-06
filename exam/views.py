from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stack
from .serializer import ListStackSerializer, RetrieveStackSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def get_or_post_data_in_stack(request):
    if request.method == 'GET':
        model_stack = Stack.objects.all()
        serializer_stack = ListStackSerializer(model_stack.order_by('-id'), many=True)
        item = {'id': '61', 'stack_data': '2'}
        # item.update(serializer_stack.data)
        new_serializer_data = list(serializer_stack.data)
        new_serializer_data.insert(2, item)
        print(new_serializer_data)
        return Response(new_serializer_data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer_stack = RetrieveStackSerializer(data=request.data)
        if serializer_stack.is_valid():
            serializer_stack.save()
            return Response(serializer_stack.data, status=status.HTTP_201_CREATED)
        return Response(serializer_stack.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def insert_at_stack(request):
    if request.method == 'POST':
        model_stack = Stack.objects.all()
        serializer_stack = ListStackSerializer(model_stack.order_by('-id'), many=True)
        stack_insert_at = list(serializer_stack.data)
        # item = {'id': '61', request.data}
        query_params = request.query_params.get('aa')
        print(query_params)
        stack_insert_at.insert(int(query_params), request.data)
        return Response(stack_insert_at)


@api_view(['GET', 'PUT', 'DELETE'])
def retrieve_stack(request, pk):
    try:
        model_stack = Stack.objects.get(pk=pk)
    except Stack.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_stack = ListStackSerializer(model_stack)
        return Response(serializer_stack.data)

    elif request.method == 'PUT':
        serializer = RetrieveStackSerializer(model_stack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model_stack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
