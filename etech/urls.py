from django.urls import path
from .views import IndexView, create_portfolio, Detail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio/', create_portfolio, name='portfolio'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail')
]