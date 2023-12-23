from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework.views import APIView
from .serializers import BoardSerializers,TopicSerializers,PostSerializers
from rest_framework.response import Response
from rest_framework import status,generics,viewsets

# Create your views here.



class BoardViewsets(viewsets.ModelViewSet):
    queryset=Board.objects.all()
    serializer_class=BoardSerializers


# def bord_list(request):
#     bords=Board.objects.all()
#     data={"results":list(bords.values('pk','name','description'))}
#     return JsonResponse(data)



# class BoardList(generics.ListCreateAPIView):
#     queryset=Board.objects.all()
#     serializer_class=BoardSerializers

# class BoardList(APIView):
#     def get(self,request):
#         boards=Board.objects.all()
#         data=BoardSerializers(boards,many=True).data

#         return Response(data)
#     def post (self,request):
#         serz=BoardSerializers(data=request.data)
#         if serz.is_valid():
#             serz.save()
#             return Response (serz.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response (serz.data,status=status.HTTP_400_BAD_REQUEST)


# def board_topics(request,board_id):
#     board = get_object_or_404(Board,pk=board_id)
#     data={"results":{"name":board.name,"description":board.description}}
#     return JsonResponse(data)


# class BorardTobics (APIView):
#     def get (self,request,board_id):
#         board = get_object_or_404(Board,pk=board_id)
#         tobics=board.topics.all()
#         data=TopicSerializers(tobics,many=True).data
#         return Response(data)
    
#     def post (self,request,board_id):
#         serz=TopicSerializers(data=request.data)
#         topic_detail=request.data
#         if serz.is_valid():
#             topic=serz.save()
#             post_serz=PostSerializers(data={"message":topic_detail['message'],"topic":topic.pk,"created_by":topic.created_by,"created_dt":topic.created_dt})
#             if post_serz.is_valid():
#                 post_serz.save()
#                 return Response (post_serz.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response (post_serz.data,status=status.HTTP_400_BAD_REQUEST)
    

class BorardTobics (generics.ListCreateAPIView):
    queryset=Topic.objects.all()
    serializer_class=TopicSerializers
            
            
# class BorardDetail (APIView):
#     def get (self,request,board_id):
#         board = get_object_or_404(Board,pk=board_id)
#         data=TopicSerializers(board).data
#         return Response(data)

# class BorardDetail (generics.RetrieveUpdateDestroyAPIView):
#     queryset=Board.objects.all()
#     serializer_class=BoardSerializers
#     lookup_field='id'