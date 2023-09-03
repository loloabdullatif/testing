from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from members.models import Member
from api.serializer import MemberSerializer


@api_view(['GET'])
def members(request):
    '''
    List all the members
    '''
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def member1(request,id):
    '''
    List all the members
    '''
    member = Member.objects.get(id=id)
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def member(request):
    '''
        create the member with given member data
    '''
    data={
        'firstname': request.data.get('firstname'),
        'lastname': request.data.get('lastname'),
        'email': request.data.get('email'),
        
    }
    serializer= MemberSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    