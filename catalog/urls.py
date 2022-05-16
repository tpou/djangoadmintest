from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name='index'), # name param is unique identifier for this URL mapping, can be dynamically pointed from other page like: <a href="{% url 'index' %}"></a>
    path('books/', views.BookListView.as_view(), name='books'), # inheriting Django class-based views
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]