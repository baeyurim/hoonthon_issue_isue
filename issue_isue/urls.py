
from django.contrib import admin
from django.urls import path
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name='index'),
    path('maker', app.views.maker, name='maker'),
    path('new', app.views.new, name="new"),
    path('<int:issue_id>', app.views.detail, name="detail"),
    path('app/<int:issue_id>/edit', app.views.edit, name="edit"),
    path('app/<int:issue_id>/delete', app.views.delete, name="delete"),
    path('signup/', app.views.signup, name="signup"),
    path('login/', app.views.login, name="login"),
    path('logout/', app.views.logout, name="logout"),
    path('search', app.views.search, name='search'),
    path('filtering/<int:filter_id>', app.views.filtering, name='filtering'),
    path('<int:issue_id>/comment/create', app.views.comment_create, name="comment_create"),
    path('<int:issue_id>/comment/delete/<int:comment_id>', app.views.comment_delete, name="comment_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 