from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, SubmissionSerializer
from .models import User, Submissions
from .utils import create_code_file, execute_file


# Create your views here.
def hello_world(request):
    execute_file("main.cpp", "cpp")
    return HttpResponse("Hello world")


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubmissionsViewSet(ModelViewSet):
    queryset = Submissions.objects.all()
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        request.data["status"] = "P"
        file_name = create_code_file(
            request.data.get("code"), request.data.get("language")
        )
        output = execute_file(file_name, request.data.get("language"))
        request.data["user_output"] = output
        return super().create(request, *args, **kwargs)
