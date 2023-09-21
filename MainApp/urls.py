from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home_Page"),
    path('post/<slug:post_url>', views.full_post, name='full_post'),
]
