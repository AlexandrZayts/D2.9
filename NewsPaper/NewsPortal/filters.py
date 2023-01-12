from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category



class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='Сategory',
        queryset=Category.objects.all(),
        label='Категория поста',
        empty_label='Все'
    )

    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

