from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/renew/', views.renew_post, name='renew-post'),
    path('post/<int:pk>/like/', views.PostLikeCreate.as_view(), name='post-like'),
    path('delete_like/<int:pk>/',views.delete_like,name='delete_like'),
    path('post/<int:pk>/comment/', views.PostCommentCreate.as_view(), name='post-comment'),

    path('delete_post/<int:pk>/',views.delete_post,name='delete_post'),
    path('rotate_avatar/',views.rotate_avatar_by_90_degrees, name="rotate_avatar"),
    path('rotate_background/',views.rotate_background, name="rotate_background"),

    path('password_change/',auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change.html',
            success_url='password_changed'
        ),name='password_change'),
    path('password_changed/', views.password_changed, name='password_changed'),
    path('sign_up/',views.sign_up, name="sign_up"),

    path('activation_sent/', views.activation_sent, name="activation_sent"),
    # path('reactivate/<str:email>/', views.reactivate_user, name='reactivate_user'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('activation/success/', views.activation_success, name='activation_success'),
    path('activation/error/', views.activation_error, name='activation_error'),
    path('logout/', views.logout_view, name="logout"),


    #feeds
    path('infinite/',views.infinite, name="infinite"),
    path('posts-paginator/', views.PostListView.as_view(), name='posts'),
    path('posts-feed/',views.InfinitePostsView.as_view(), name="posts-feed"),
    path('Community/', views.Community.all, name='community'),

]