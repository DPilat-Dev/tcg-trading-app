from django.urls import path
from .views import GetCardView, GetCollectionView, UpdateCollectionView, PingView, CreateUserView


# URL patterns for the cards app
urlpatterns = [
    path('get_card/', GetCardView.as_view(), name='get-card'),
    path('create_user/', CreateUserView.as_view(), name='create-user'),
    path('get_collection/', GetCollectionView.as_view(), name='get-collection'),
    path('update_collection/', UpdateCollectionView.as_view(), name='update-collection'),
    path('ping/', PingView.as_view(), name='ping')
]
