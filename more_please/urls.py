"""more_please URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
# from . import views # local to more-please app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]

# urlpatterns = [
#     # using an empty string here makes this our root route
#     # views.home refers to a view that renders a file
#     # the name='home' kwarg gives the route a name
#     # naming routes is optional, but best practices
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     # paths for cats
#     path('cats/', views.cats_index, name='index'),
#     path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
#     path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
#     path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
#     path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
#     path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
#     # add association
#     path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
#     # add unassociation
#     path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
#     # add_photo
#     path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
#     # toys down here
#     # index, show, create, update, delete
#     path('toys/', views.ToyList.as_view(), name='toys_index'),
#     path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
#     path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
#     path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
#     path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
#     path('accounts/signup/', views.signup, name='signup')
# ]
