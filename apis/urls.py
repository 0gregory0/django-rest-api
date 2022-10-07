from django.urls import path
from .views import UsersAPIView, UsersDetail

urlpatterns = [
    path("<int:pk>/", UsersDetail.as_view(), name="post_detail"),
    path("", UsersAPIView.as_view(), name = "user_list"),
]