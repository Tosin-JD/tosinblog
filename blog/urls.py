from django.urls import path
from .views import (BlogList,
                    BlogDetail,
                    CreateBlog,
                    UpdateBlog,
                    DeleteBlog,
)


app_name = 'blog'


urlpatterns = [
    path('', BlogList.as_view(), 'list'),
    path('<slugs>', BlogDetail.as_view(), 'detail'),
    path('<slugs>/delete/', CreateBlog.as_view(), 'detail'),
    path('<slugs>/update/', UpdateBlog.as_view(), 'detail'),
    path('create/', DeleteBlog.as_view(), 'detail'),
]

