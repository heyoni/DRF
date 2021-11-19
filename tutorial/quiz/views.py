from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random


@api_view(['GET'])
def helloAPI(request):
    return Response('hello world')
    

@api_view(['GET'])
def randomQuizAPI(request,id):
    totalQuizes = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizes),id)
    serializer = QuizSerializer(randomQuizs,many=True) # many=True 다량의 데이터에서도 직렬화 지원
    return Response(serializer.data)