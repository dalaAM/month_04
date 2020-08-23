from django.urls import path
from . import views
urlpatterns = [
    #127.0.0.1:8000/ajax_js/ajax_xhr
    path('ajax_xhr',views.ajax_xhr),
    #127.0.0.1:8000/ajax_js/test_get
    path('test_get',views.test_get),
    #127.0.0.1:8000/ajax_js/test_jq_get
    path('test_jq_get',views.test_jq_get),
    #127.0.0.1:8000/ajax_js/test_json
    path('test_json',views.test_json),

    path('xhr_get_server',views.xhr_get_server),

]