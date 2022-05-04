from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import *

router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

router.register('admin/category', AdminCategoryViewset, basename='admin-category')

from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset


router = routers.SimpleRouter()
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

router.register('admin/category', AdminCategoryViewset, basename='admin-category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
<<<<<<< HEAD
    path('api/', include(router.urls)),
=======
    path('api/', include(router.urls))
>>>>>>> upstream/P2C4_exercice
]
