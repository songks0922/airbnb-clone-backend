from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

@api_view(["GET", "PUT", "DELETE"])
def category_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound("Category does not exist")

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        return Response(serializer.errors)

    if request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)