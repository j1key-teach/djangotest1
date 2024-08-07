from rest_framework import viewsets, generics
from .models import Test, Bolim, UserTestAttempt
from .serializers import TestSerializer, BolimSerializer, UserTestAttemptSerializer
from rest_framework import permissions
from rest_framework.response import Response


class TestViewSet(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class BolimViewSet(viewsets.ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserTestAttemptViewSet(viewsets.ModelViewSet):
    queryset = UserTestAttempt.objects.all()
    serializer_class = UserTestAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        bolim_id = request.data.get('bolim')
        bolim = Test.objects.get(id=bolim_id)

        attempt, created = UserTestAttempt.objects.get_or_create(user=user, bolim=bolim)

        if not created:
            if attempt.attempt_count >= 2:
                return Response({"error": "siz allaqachon 2marta urunib ko'rgnsiz"}, status=400)
            if attempt.error_count >= 3:
                return Response({"error": "3tadan ko'p xato qildingiz shuning uchun ham keyingi bosqicha o'tmaysiz."},
                                status=400)

        attempt.attempt_count += 1
        attempt.save()
        return super().create(request, *args, **kwargs)
