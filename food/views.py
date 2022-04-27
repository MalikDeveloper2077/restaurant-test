from django.db.models import Count, Q
from rest_framework.generics import ListAPIView

from food.models import FoodCategory
from food.serializers import FoodListSerializer


class FoodListView(ListAPIView):
    queryset = FoodCategory.objects.annotate(
        published_food_count=Count('food', filter=Q(food__is_publish=True))
    ).filter(published_food_count__gte=1)
    serializer_class = FoodListSerializer
