from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CartViewSet
from .views import  ListProduct, ProductDetailView, ProductCreateView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('cart', CartViewSet, basename='cart')
router.register('carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-list', ListProduct.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('product-create/', ProductCreateView.as_view(), name='product_create'),
    path('carts/<int:pk>/list_cart_items/', CartViewSet.as_view({'get': 'list_cart_items'}), name='cart-list-items'),

]