from categories.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories.serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories_view(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
