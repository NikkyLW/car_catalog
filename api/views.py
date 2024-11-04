from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CarSerializer, CommentSerializer
from cars.models import Car
from comments.models import Comment
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse



class CarCreateAPI(APIView):
    @extend_schema(
        summary="Добавление автомобиля",
        description="Добавляет новой автомобиль на сайт.",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Автомобиль успешно Добавлен"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save()
            return Response({"status": "Car created", "id": car.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarListAPI(APIView):
    @extend_schema(
        summary="Список автомобилей",
        description="Список всех автомобилей добавленных на сайт, всеми пользователями.",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Список всех автомобилей"),
        }
    )
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    

class CarDetailAPI(APIView):
    @extend_schema(
        summary="Обновление данных автомобиля",
        description="Обновляет данные уже существующего автомобиля на сайте",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Данные автомобиля обновлены"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def put(self, request, pk):
        car =  Car.objects.get(id=pk)
        serializer = CarSerializer(car, data=request.data) 
        if serializer.is_valid():
            car = serializer.save()
            return Response({"status": "Car update", "id": car.id}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    @extend_schema(
        summary="Удаление автомобиля с сайта",
        description="Удаляет автомобиль с сайта",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Автомобиль удален"),
        }
    )
    def delete(self, request, pk):
        try:
            car = Car.objects.filter(id=pk).delete()
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "Car delete"}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Данные опредленного автомобиля",
        description="Вывод информации об опредленном автомобиле на сайте",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Данные определенного автомобиля"),
        }
    )
    def get(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)


class CommentAPI(APIView):
    @extend_schema(
        summary="Добавление комментария",
        description="Добавление комментария к автомобилю",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Комментарий добавлен"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            car_obj = Car.objects.get(id=pk)
            comment = serializer.save(car=car_obj)
            return Response({
                "status": "Comment created", 
                "id": comment.id,
                "user_id": serializer.data['author'],
                "car_id": serializer.data['car']
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Комментарии опредленного автомобиля",
        description="Вывод комментариев у опредленного автомобиля на сайте",
        request=CarSerializer,
        responses={
            201: OpenApiResponse(response=CarSerializer, description="Комментарии определенного автомобиля"),
        }
    )
    def get(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
            comments = Comment.objects.filter(car=car.id)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)