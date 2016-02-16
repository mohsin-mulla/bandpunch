from django.conf.urls import patterns, url
# Import all the views from the products app
from ticket import views

# $ sign indicates that nothing can be entered after the URL with the current view
urlpatterns = patterns('',
        url(r'^$', views.index, name='Index'),
		url(r'^artists/$', views.browse_artists, name='Browse Artists'),
		url(r'^events/$', views.browse_events, name='Browse Events'),
        url(r'^events/(?P<event_name_url>[-\w]+)/$', views.event_view, name='View Event Details'),
		url(r'^venues/$', views.browse_venues, name='Browse Venues'),
		url(r'^cart/$', views.show_cart, name='Show Cart'),
		url(r'^cart/add/$', views.add, name='Add to Cart'),
		url(r'^cart/remove/$', views.remove, name='Remove from Cart'),
		url(r'^cart/checkout/$', views.checkout, name='Checkout'),
        url(r'^accounts/register/$', views.register, name='Register'),
		url(r'^about/', views.about, name='About'),
		url(r'^terms/', views.terms, name='Terms'),
)