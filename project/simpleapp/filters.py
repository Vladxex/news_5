from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import New


# создаём фильтр
class NewFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация о news
    class Meta:
        model = New
        fields = {
            'name': ['icontains'], # по названию
            'auto_time': ['gt'], # позже какой-либо даты
        }