from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    #path('', views.home),

    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(),name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
   
    path('cart/', views.show_cart,name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
