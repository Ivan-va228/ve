from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views  
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('catalog/', views.catalog_view, name='catalog'),
    path('cart/', views.cart_view, name='cart'),
    path('signup/', views.signup_view, name='signup'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
