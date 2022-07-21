
from django.contrib import admin
from django.urls import path
from Task_app.views import home, ulogin ,usignup ,add_task ,view_task ,ulogout ,delete_task, change_status,info1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ulogin/', ulogin, name='ulogin'),
    path('usignup/', usignup, name='usignup'),
    path('add_task/', add_task ,name='add_task' ),
    path('view_task/', view_task ,name='view_task' ),
    path('delete_task/<int:id>', delete_task ,name='delete_task' ),
    path('change_status/<int:id>/<str:status>', change_status ,name='change_status' ),
    path('ulogout/', ulogout, name='ulogout'),
    path("info1/", info1, name="info1")

]
