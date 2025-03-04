from rest_framework.response import Response
from rest_framework import status, generics
from .models import User, ToDoList
from .serializers import UserSerializer, ToDoListSerializer
import math


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create_user(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoBoard(generics.GenericAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    def create_todo(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_todo(self, request, *args, **kwargs):
        page_num = request.GET.get('page', 1)
        page_limit = request.GET.get('limit', 10)
        start_num = (page_num - 1) * page_limit
        end_num = page_limit * page_num
        search_param = request.GET.get("search")
        notes = ToDoList.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains=search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "last_page": math.ceil(total_notes / page_limit),
            "notes": serializer.data
        })


class ToDoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
