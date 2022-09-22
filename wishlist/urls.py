from django.urls import path
from wishlist.views import show_wishlist, retrieve_xml, retrieve_json
from wishlist.views import retrieve_xml_by_id, retrieve_json_by_id
from wishlist.views import register, login_user, logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', retrieve_xml, name='retrieve_xml'),
    path('json/', retrieve_json, name='retrieve_json'),
    path('xml/<int:id>', retrieve_xml_by_id, name='retrieve_xml_by_id'),
    path('json/<int:id>', retrieve_json_by_id, name='retrieve_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]


    