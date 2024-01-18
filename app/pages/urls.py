from django.urls import path
from .views import IndexView, DetailView, CategoryView, TagView


app_name = "pages"

urlpatterns = [
    # path('', views.index, name='index'),
    path("", IndexView.as_view(), name="index"),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('tag/<str:tag>/', TagView.as_view(), name='tag'),
    path("detail/<int:pk>/", DetailView.as_view(), name="detail"),
]
