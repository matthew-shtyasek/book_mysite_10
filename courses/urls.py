from django.urls import path

from courses import views

app_name = 'courses'

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='delete'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='module_update'),
    path('module/<int:module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
]
