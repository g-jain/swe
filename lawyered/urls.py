
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth.views import logout
from django.conf.urls import  include, url
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Question, Tag
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
     )
    class Meta:
        model = Question
        fields = ('id', 'pub_date', 'question_text', 'tags', 'views')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/questions', QuestionViewSet)

app_name = 'lawyered'
urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^login/$', views.login, {'template_name' : 'login.html'}),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^login/$',login, name = 'login'),
	url(r'^logout/$',logout, {'next_page': '/'}, name='logout'),
    url(r'^choose/$',views.choose, name='choose'),
	url(r'^register/$', views.register, name='register'),
	url(r'^profileuser/(?P<user_id>\d+)/$', views.up, name='profileuser'),
    url(r'^registerlawyer/$', views.registerlawyer, name='registerlawyer'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
	url(r'^search/$', views.person_list, name='search'),
	url(r'^add_cases/$', views.form_list, name='add_cases'),
	url(r'^divorce/$', views.divorce, name='divorce'),
	url(r'^dui/$', views.dui, name='dui'),
	url(r'^prenup/$', views.prenup, name='prenup'),
	url(r'^merger/$', views.merger, name='merger'),
	url(r'^criminal/$', views.criminal, name='criminal'),
	url(r'^estate/$', views.estate, name='estate'),
	url(r'^forum/$', views.forum, name='forum'),
	url(r'^forum/logout$', views.forumlogout, name='forumlogout'),
	url(r'^forum/login$', views.forumlogin, name='forumlogin'),
	url(r'^forum/q/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^forum/answer/(?P<question_id>\d+)/$', views.answer, name='answer'),
    url(r'^forum/add/$', views.add, name='add'),
    url(r'^forum/answer/$', views.add_answer, name='add_answer'),
    url(r'^forum/vote/(?P<user_id>\d+)/(?P<answer_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$', views.vote, name='vote'),
    url(r'^forum/comment/(?P<answer_id>\d+)/$', views.comment, name='comment'),
    url(r'^forum/search_question/$', views.search_question, name='search_question'),
    url(r'^forum/tag/(?P<tag>\w+)/$', views.tag, name='tag'),
    url(r'^forum/thumb/(?P<user_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$', views.thumb, name='thumb'),
    url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^divorce/(?P<divorceForm_id>\d+)/$', views.divcasedetail, name='divcasedetail'),
    url(r'^prenup/(?P<prenupForm_id>\d+)/$', views.prenup_update, name='prenup_update'),
    url(r'^criminal/(?P<criminalForm_id>\d+)/$', views.cricasedetail, name='cricasedetail'),
    url(r'^merger/(?P<mergerForm_id>\d+)/$', views.mercasedetail, name='mercasedetail'),
    url(r'^estate/(?P<estateForm_id>\d+)/$', views.estcasedetail, name='estcasedetail'),
    url(r'^dui/(?P<duiForm_id>\d+)/$', views.duicasedetail, name='duicasedetail'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^lawyercases/$', views.lawyercases, name='lawyercases'),
    url(r'^lawyerdashboard/$', views.lawyerdashboard, name='lawyerdashboard'),

]
#url(r'^$', views.dashboard, name='dashboard'),url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),url(r'^login/$', views.user_login,name='login'),
	
