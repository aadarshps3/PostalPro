from django.urls import path

from PostelApp import views, adminviews, staffviews, customerviews

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('staffregister',views.staffregister,name='staffregister'),
    path('customerregister',views.customerregister,name='customerregister'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('staffpage',views.staffpage,name='staffpage'),
    path('customerpage',views.customerpage,name='customerpage'),
    path('logout_view',views.logout_view,name='logout_view'),

    path('view_customers',adminviews.view_customers,name='view_customers'),
    path('view_staffs',adminviews.view_staffs,name='view_staffs'),
    path('approve_staffs/<int:id>/',adminviews.approve_staffs,name='approve_staffs'),
    path('approve_user/<int:id>/',adminviews.approve_user,name='approve_user'),
    path('view_parcel_admin',adminviews.view_parcel_admin,name='view_parcel_admin'),
    path('add_shift',adminviews.add_shift,name='add_shift'),
    path('manage_shifts',adminviews.manage_shifts,name='manage_shifts'),
    path('manage_staff',adminviews.manage_staff,name='manage_staff'),
    path('AddPO',adminviews.AddPO,name='AddPO'),
    path('View_PO',adminviews.View_PO,name='View_PO'),
    path('AddSurvey',adminviews.AddSurvey,name='AddSurvey'),
    path('viewSurvey',adminviews.viewSurvey,name='viewSurvey'),
    # path('add_parcel',adminviews.add_parcel,name='add_parcel'),


    path('view_cust',staffviews.view_cust,name='view_cust'),
    path('viewparcel',staffviews.viewparcel,name='viewparcel'),
    path('approve_parcel/<int:id>/',staffviews.approve_parcel,name='approve_parcel'),
    path('View_Time',staffviews.View_Time,name='View_Time'),
    path('view_feedback',staffviews.view_feedback,name='view_feedback'),
    path('reply_Feedback/<int:id>/',staffviews.reply_Feedback,name='reply_Feedback'),



    path('track-parcel/', customerviews.track_parcel, name='track_parcel'),
    path('add-parcel/', customerviews.add_parcel, name='add_parcel'),
    path('parcel-detail/<int:parcel_id>/', customerviews.parcel_detail, name='parcel_detail'),
    path('view_parcel', customerviews.view_parcel, name='view_parcel'),
    path('add_feedback', customerviews.add_feedback, name='add_feedback'),
    path('Feedback_view_user', customerviews.Feedback_view_user, name='Feedback_view_user'),
    path('take_survey', customerviews.take_survey, name='take_survey'),
]