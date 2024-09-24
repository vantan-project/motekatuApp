from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('sign_up/', views.sign_up.index, name='sign_up'),
    path('sign_up/save/', views.sign_up.save, name='sign_up.save'),
    path('sign_in/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='app/sign_in/index.html'
        ),
        name='sign_in'),
    path('sign_in/auth/', views.sign_in.auth, name='sign_in.auth'),
    path('top/', views.top.index, name='top'),
    path('post/', views.post.index, name='post'),
    path('post/save', views.post.save, name='post.save'),
    path('review_list/<str:type>/<str:gender>/',  views.review_list.index, name='review_list'),
    path('sign_out/', views.sign_out.index, name='sign_out'),
    path('site/', views.site.index, name='site'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)