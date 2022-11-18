from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import Utils
import json
 

@api_view(['GET'])
def list_user(request):
    queryset = User.objects.all()
    data = UserSerializer(queryset, many=True)
    dados_json = data.data
    with open("data.json", "w") as outfile: 
        json.dump(dados_json, outfile , indent=4)
    Utils.write_csv(dados_json)
    Utils.write_xsls(dados_json)
    return Response(dados_json)



@api_view(['POST'])
def create_user(request):
    utils = Utils()
    request.data['dataNascimento'] = utils.format_date(request.data["dataNascimento"])
    print(request.data['dataNascimento'])
    user = UserSerializer(request.data, many=True)

    User.objects.create(
        login=request.data['login'],
        senha=request.data['senha'],
        dataNascimento=request.data['dataNascimento']
    )

    return Response(request.data["login"])