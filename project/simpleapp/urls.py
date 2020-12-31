from django.urls import path
from .views import NewsList, NewDetail, NewCreateView, NewDeleteView, NewUpdateView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем новостям у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('create/', NewCreateView.as_view(), name='new_create'),  # Ссылка на create new
    path('delete/<int:pk>/', NewDeleteView.as_view(), name='new_delete'),  # Ссылка на delete new
    path('create/<int:pk>/', NewUpdateView.as_view(), name='new_update'),  # Ссылка на update new

]