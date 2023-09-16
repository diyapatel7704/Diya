from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout ,name='logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('pricing/',views.pricing,name='pricing'),
    path('services/',views.services,name='services'),
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('change_password/',views.change_password,name='change_password'),
    path('member_detail/',views.member_detail,name='member_detail'),
    path('edit_member/<int:pk>/',views.edit_member,name='edit_member'),
    path('manage_events/',views.manage_events,name='manage_events'),
    path('view_event/<int:pk>/',views.view_event,name='view_event'),
    path('delet-event/<int:pk>',views.delete_event,name='delete-event'),
    path('add-event/',views.add_event,name='add-event'),
    path('manage_notice/',views.manage_notice,name='manage_notice'),
    path('new-notice/',views.new_notice,name='new-notice'),
    path('manage-complain/',views.manage_complain,name='manage-complain'),
    path('view-complain/<int:pk>/',views.view_complain,name='view-complain'),
    path('solve-complain/<int:pk>/',views.solve_complain,name='solve-complain'),
    path('view-notice/<int:pk>/',views.view_notice,name='view-notice'),
]
