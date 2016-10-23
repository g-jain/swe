from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from lawyered import views
from lawyered.models import Question, Tag
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

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

urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    url(r'^', include('lawyered.urls')),
#    url(r'^ath/', include('laath.urls')),
	url(r'^login/$', views.forumlogin, name='forumlogin'),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^forum/', include('pybb.urls', namespace='pybb')),
	url(r'^forum$', views.forum, name='forum'),
	url(r'^q/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^answer/(?P<question_id>\d+)/$', views.answer, name='answer'),
    url(r'^add/$', views.add, name='add'),
    url(r'^answer/$', views.add_answer, name='add_answer'),
    url(r'^vote/(?P<user_id>\d+)/(?P<answer_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$', views.vote, name='vote'),
    url(r'^comment/(?P<answer_id>\d+)/$', views.comment, name='comment'),
    url(r'^search/$', views.search_question, name='search_question'),
    url(r'^tag/(?P<tag>\w+)/$', views.tag, name='tag'),
    url(r'^thumb/(?P<user_id>\d+)/(?P<question_id>\d+)/(?P<op_code>\d+)/$', views.thumb, name='thumb'),

    url(r'^profile/(?P<user_id>\d+)/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    
    url('^markdown/', include( 'django_markdown.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #url('^forgot/', include('password_reset.urls')),

]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
