from django.contrib import admin
from django.urls import path
from taskapp.views import home,create,viewtask,delete
from auapp.views import user_signup,user_login,user_logout,user_np,user_cp
from fbapp.views import feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("user_signup/",user_signup,name="user_signup"),
    path("user_login/",user_login,name="user_login"),
    path("user_logout/",user_logout,name="user_logout"),
    path("user_np/",user_np,name="user_np"),
    path("user_cp/",user_cp,name="user_cp"),
    path("viewtask/",viewtask,name="viewtask"),
    path("create/",create,name="create"),
    path("delete/<int:id>",delete,name="delete"),
    path("feedback/",feedback,name="feedback"),
]
