
# _______________________ POST APP'in URL'İ _____________________ """



from django.urls  import  path
from .views import * #Bütün view'leri içeri aktardık..


urlpatterns = [
    path('index/', post_index, name="post_index"),
    path('create/', post_create, name='post_create'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/update/', post_update, name='post_update'),
    path('<slug:slug>/delete/', post_delete, name='post_delete'),

]