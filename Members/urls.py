from django.urls import path
from . import views

urlpatterns = [
    path('',views.member_index,name='member-index'),
    path('member-login/',views.member_login,name='member-login'),
    path('member-logout/',views.member_logout,name='member-logout'),
    path('create-complain/',views.create_complain,name='create-complain'),
    path('my-complains/',views.my_complains,name='my-complains'),
    path('my-notice/',views.my_notice,name='my-notice'),
    path('view-my-notice/<int:pk>/',views.view_my_notice,name='view-my-notice'),
    path('pay-main/',views.pay_main,name='pay-main'),
    path('change-member-detail/',views.change_member_detail,name='change-member-detail'),
    
    
]