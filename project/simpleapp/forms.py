from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import New


class NewForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = New
        fields = ['name', 'description', 'category', 'check_box']  # не забываем включить галочку в поля иначе она не будет показываться на странице!


