from django.urls import path
from main.views import show_main, create_item, show_xml, show_xml_by_id, \
                        show_json, show_json_by_id, register, login_user, logout_user, \
                        inc_amount, dec_amount, delete, edit_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('item/<int:id>/increase/', inc_amount, name='inc_amount'),
    path('item/<int:id>/decrease/', dec_amount, name='dec_amount'),
    path('item/<int:id>/delete/', delete, name='delete'),
    path('edit-product/<int:id>', edit_product, name='edit_product')
]