from django.conf.urls import url, include
# from rest_framework import routers
# import api
import gazovik.webapp.views as views

# router = routers.DefaultRouter()
# router.register(r'tovar', api.TovarViewSet)
# router.register(r'category', api.CategoryViewSet)


# urlpatterns = (
#     # urls for Django Rest Framework API
#     url(r'^api/v1/', include(router.urls)),
# )

urlpatterns = [
    # urls for Tovar
    url(r'^tovar/$', views.TovarListView.as_view(), name='list'),
    url(r'^tovar/(?P<slug>\S+)/$', views.TovarDetailView.as_view(), name='detail'),
    # url(r'^webapp/tovar/update/(?P<slug>\S+)/$', views.TovarUpdateView.as_view(), name='webapp_tovar_update'),

    # urls for Category
    url(r'^category/$', views.CategoryListView.as_view(), name='category_list'),
    # url(r'^webapp/category/create/$', views.CategoryCreateView.as_view(), name='webapp_category_create'),
    url(r'^category/(?P<slug>\S+)/$', views.CategoryDetailView.as_view(), name='webapp_category_detail'),
    # url(r'^webapp/category/update/(?P<slug>\S+)/$', views.CategoryUpdateView.as_view(), name='webapp_category_update'),
]
