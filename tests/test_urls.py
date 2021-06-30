from django.urls import reverse, resolve
from blog.views import PostListView, PostDetailView, PostCreateView, PostDeleteView, UserPostListView, PostUpdateView, about
from users.views import register, profile
from django.contrib.auth import views as auth_views
from django.test import TestCase


class BlogUrlsTest(TestCase):
    def test_post_list_url_resolved(self):
        url = reverse('home-blog')
        print('url ---- ',url)
        self.assertEquals(resolve(url).func.view_class, PostListView)
    
    def test_post_detail_url_resolved(self):
        url = reverse('post-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
    
    def test_post_create_url_resolved(self):
        url = reverse('post-create')
        print('url ---- ',url)
        self.assertEquals(resolve(url).func.view_class, PostCreateView)
    
    def test_post_update_url_resolved(self):
        url = reverse('post-update', args=[27])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_url_resolved(self):
        url = reverse('post-delete', args=[27])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)

    def test_user_posts_url_resolved(self):
        url = reverse('user-posts', args=['pradnyoday'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_about_url_resolved(self):
        url = reverse('about-blog')
        self.assertEquals(resolve(url).func, about)

class UsersUrlsTest(TestCase):
    def test_user_register_url_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
    def test_user_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)
    def test_user_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)
    def test_user_profile_url_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)