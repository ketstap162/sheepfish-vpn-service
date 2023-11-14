from django.urls import path, re_path   

from .views import home_page_view, vpn_view, site_create_view, site_delete_view

app_name = "VPN"

urlpatterns = [
    path("", home_page_view, name="home"),
    path("site/create", site_create_view, name="site-create"),
    path("site/<int:pk>/delete", site_delete_view, name="site-delete"),
    re_path(r"^vpn/(?P<site_url>[\w-]+)/(?P<path>.*)$", vpn_view, name="vpn"),
]
