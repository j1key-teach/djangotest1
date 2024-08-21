from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Test, Bolim
from .serializers import TestSerializer, BolimSerializer
from rest_framework import generics


class TestList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BolimList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bolims = Bolim.objects.all()
        serializer = BolimSerializer(bolims, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BolimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BolimDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer
