from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def autenticacion(request):

    username = request.data.get('usuario')
    if not username:
        return None

    try:
        user ='ISABE'
        return Response(user)
    
    except Exception as e :
             raise AuthenticationFailed('No such user')

             return Response(e)

# Create your views here.
