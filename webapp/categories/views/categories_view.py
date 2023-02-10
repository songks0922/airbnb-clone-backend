from categories.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories.serializers import CategorySerializer
from rest_framework.views import APIView


class Categories(APIView):

    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
