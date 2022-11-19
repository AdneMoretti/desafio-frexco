from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import Utils
import json
import uuid
 

@api_view(['GET'])
def list_user(request ):
    queryset = User.objects.all()
    data = UserSerializer(queryset, many=True)
    data_json = data.data

    Utils.write_csv(data_json)
    Utils.write_xsls(data_json)
    return Response(data_json)



@api_view(['POST'])
def create_user(request):
    utils = Utils()
    request.data['dataNascimento'] = utils.format_date(request.data["dataNascimento"])
    if 'senha' in request.data:
        request.data['senha']
    else: 
        request.data['senha'] = uuid.uuid4()

    User.objects.create(
        login=request.data['login'],
        senha=request.data['senha'],
        dataNascimento=request.data['dataNascimento']
    )
    user = UserSerializer(request.data)
    
    return Response(data=json.dumps(user.data), status=201)