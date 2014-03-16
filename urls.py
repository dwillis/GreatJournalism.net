from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based, create_update
from car.models import Byline, Datatype, Nation, Source, State, Story, Topic, Type, Database, Application
from projects.models import Language, Project, Update, Presentation, Topic
from feeds import LatestEntries, LatestBylines, LatestSources, TopicFeed, SourceFeed, BylineFeed
from django.contrib import admin
admin.autodiscover()

info_dict = {
    'queryset': Story.objects.all().order_by('-pubdate'),
    'date_field':'pubdate',
}

byline_list_info = {
	'queryset': Byline.objects.all().order_by('lastname'),
	'allow_empty': True,
	'paginate_by': 50,
	'template_name': 'byline_list.html',
}

feeds = {
    'latest': LatestEntries,
    'bylines': LatestBylines,
    'sources': LatestSources,
    'topic': TopicFeed,
    'source': SourceFeed,
    'byline': BylineFeed,
}


urlpatterns = patterns('',
    # Redirects to deal with blog.thescoop.org subdomain:
    (r'^feed/$', 'car.views.blog_feed'),
    (r'^$', 'car.views.main'),
    (r'^story/(.*)/$', 'car.views.story_detail'),
    (r'^withdb/$', 'car.views.with_db'),
    (r'^type/$', 'car.views.type_all'),
    (r'^type/(.*)/$', 'car.views.type_detail'),
    (r'^datatype/$', 'car.views.datatype_all'),
    (r'^datatype/(.*)/$', 'car.views.datatype_detail'),
    (r'^topic/$', 'car.views.topic_all'),
    (r'^topic/(.*)/$', 'car.views.topic_detail'),
    (r'^byline/$', list_detail.object_list, byline_list_info),
    (r'^search/$', 'car.views.search'),
    (r'^search/byline/$', 'car.views.byline_search'),
    (r'^search/source/$', 'car.views.source_search'),
    (r'^byline/(.*)/$', 'car.views.byline_detail'),
    (r'^state/$', 'car.views.state'),
    (r'^state/(.*)/$', 'car.views.state_detail'),
    (r'^nation/$', 'car.views.nation'),
    (r'^nation/(.*)/$', 'car.views.nation_detail'),
    (r'^source/$', 'car.views.source_main'),
    (r'^source/(.*)/all/$', 'car.views.source_all'),
    (r'^source/(.*)/(\d+)/$', 'car.views.source_by_year'),
    (r'^source/(.*)/$', 'car.views.source'),
    (r'^dbs/$', 'car.views.db_index'),
    (r'^dbs/app/(?P<appslug>.*)/$', 'car.views.db_app'),
    (r'^dbs/(.*)/$', 'car.views.db_detail'),
    (r'^code/$', 'projects.views.index'),
    (r'^code/language/(?P<lang>[-a-z]+)/$', 'projects.views.language_list'),
    (r'^code/(?P<project>[-a-z]+)/$', 'projects.views.project_detail'),
    (r'^presentations/$', 'projects.views.presentations'),



    (r'^date/$', 'django.views.generic.date_based.archive_index', dict(info_dict, template_name='story_archive_index.html')),
    (r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', dict(info_dict, template_name='story_archive_year.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'django.views.generic.date_based.archive_month', dict(info_dict, template_name='story_archive_month.html')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'django.views.generic.date_based.archive_day', dict(info_dict, template_name='story_archive_day.html')),

    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    # Uncomment this for admin:
    (r'^admin/', include(admin.site.urls)),
)
