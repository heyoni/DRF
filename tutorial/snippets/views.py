from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

# Tutorial 3: Class-based Views
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Tutorial 2: Requests and Responses
# # 코드 리팩토링 -> 거의 비슷하게 동작할 테지만 유효하지 않은 요청에 대해서 더 좋은 오류 처리를 해준다.

# # format suffix를 사용하면 지정된 형식을 명시적으로 참조하는 URL이 되며 API가 http://.../api/items/4.json 과 같은 URL을 처리할 수 있다. 그러려면 format 키워드를 넣어줘야 함.
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # from django.http import HttpResponse, JsonResponse
# # from django.views.decorators.csrf import csrf_exempt
# # from rest_framework.parsers import JSONParser
# # from snippets.models import Snippet
# # from snippets.serializers import SnippetSerializer

# # @csrf_exempt
# # def snippet_list(request):
# #     """
# #     List all code snippets, or create a new snippet.
# #     """
# #     if request.method == 'GET':
# #         snippets = Snippet.objects.all()
# #         serializer = SnippetSerializer(snippets, many=True)
# #         return JsonResponse(serializer.data, safe=False)

# #     elif request.method == 'POST':
# #         data = JSONParser().parse(request)
# #         serializer = SnippetSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data, status=201)
# #         return JsonResponse(serializer.errors, status=400)


# # @csrf_exempt
# # def snippet_detail(request, pk):
# #     """
# #     Retrieve, update or delete a code snippet.
# #     """
# #     try:
# #         snippet = Snippet.objects.get(pk=pk)
# #     except Snippet.DoesNotExist:
# #         return HttpResponse(status=404)

# #     if request.method == 'GET':
# #         serializer = SnippetSerializer(snippet)
# #         return JsonResponse(serializer.data)

# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = SnippetSerializer(snippet, data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors, status=400)

# #     elif request.method == 'DELETE':
# #         snippet.delete()
# #         return HttpResponse(status=204)