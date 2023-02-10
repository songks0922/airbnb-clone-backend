from categories.models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from categories.serializers import CategorySerializer


@api_view()
def categories_view(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data
        }
    );