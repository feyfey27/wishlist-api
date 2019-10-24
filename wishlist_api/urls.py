"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from items import views as itemsviews
from django.conf import settings
from django.conf.urls.static import static
from api import views as apiviews
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('items/list/', itemsviews.item_list, name='item-list'),
    path('items/detail/<int:item_id>/', itemsviews.item_detail, name='item-detail'),
    path('items/wishlist/', itemsviews.wishlist, name='wishlist' ),

    path('user/register/', itemsviews.user_register, name='user-register'),
    path('user/login/', itemsviews.user_login, name='user-login'),
    path('user/logout/', itemsviews.user_logout, name='user-logout'),

    path('items/<int:item_id>/favorite/', itemsviews.item_favorite, name='item-favorite'),

    path('api/list/', apiviews.ItemListView.as_view(), name='item-list'),
    path('api/detail/<int:object_id>/', apiviews.ItemDetailView.as_view(), name='item-detail'),

    path('api/login/', TokenObtainPairView.as_view(), name='login'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)