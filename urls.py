from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('cont/',views.cont,name='cont'),
    path('tracker/',views.tracker,name='tracker'),
    path('productview/<int:myid>',views.productview,name='productview'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('checkout/',views.checkout,name='checkout'),
    path('search/',views.search,name='search'),
    #path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
