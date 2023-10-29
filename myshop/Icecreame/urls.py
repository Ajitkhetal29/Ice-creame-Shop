from . import views
from django.urls import path
app_name = 'Icecreame'
urlpatterns = [
    path('',views.index,name='index'),
    path('icecreame/', views.icecreame, name='icecreame'),
    path('softy/', views.softy, name='softy'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('softy/<int:item1_id>/', views.detail1, name='detail1'),
    path('add/',views.create_item, name="create_item"),
    path('add/softy/',views.create_item1, name="create_item1"),
    path("contact/",views.contact,name="contact"),
    path("review/",views.review,name="review"),
    path("update/<int:id>/",views.update_item,name="update_item"),
    path("update/softy/<int:id>/",views.update_item1,name="update_item1"),
    path("delete/<int:id>",views.delete_item,name="delete_item"),
    path("delete/softy/<int:id>",views.delete_item1,name="delete_item1"),
    path('add_to_wishlist/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('add_to_wishlist1/<int:item1_id>/', views.add_to_wishlist1, name='add_to_wishlist1'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('remove_from_wishlist1/<int:item1_id>/', views.remove_from_wishlist1, name='remove_from_wishlist1'),
    path('order/<int:item_id>/' , views.cust_order , name='cust_order'),
    path('order1/<int:item1_id>/' , views.cust_order1 , name='cust_order1'),
    path('order_list/', views.order_list, name='order_list'),
    path('update_order/<int:item_id>/<int:upd_order_id>', views.update_order , name='update_order'),
    path('update_order1/<int:item1_id>/<int:upd_order1_id>', views.update_order1 , name='update_order1')



    



    




]