from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


# import pdb
# pdb.set_trace()
urlpatterns = [
   

    #### Update
    url('^add_user/$', views.add_user_details,name='add_user'),
    url('^user_validation/$', views.user_validation,name='user_validation'),
    url('^monthly_expense_userwise/$', views.monthly_expense_userwise, name='monthly_expense_userwise'),
    url('^add_expense_details/$', views.add_expense_details,name='add_expense_details'),
    url('^add_income_details/$', views.add_income_details,name='add_income_details'),
    url('^send_otp_to_email/$', views.send_otp_to_email, name='send_otp_to_email'),
    url('^my_otp_match/$', views.my_otp_match, name='my_otp_match'),
    url('^display_table_data/$', views.display_table_data, name='display_table_data'),
    url('^total_exp_vs_income_graph/$', views.total_exp_vs_income_graph, name='total_exp_vs_income_graph'),
    url('^total_exp_vs_income_conclusion/$', views.total_exp_vs_income_conclusion, name='total_exp_vs_income_conclusion'),

    
    #Forgot Password
    url('^verify_email_for_forgot_pass/$', views.verify_email_for_forgot_pass, name='verify_email_for_forgot_pass'),
    url('^verify_otp_forgot_password/$', views.verify_otp_forgot_password, name='verify_otp_forgot_password'),
    url('^update_password/$', views.update_password, name='update_password'),
    url('^display_budget_table/$', views.display_budget_table, name='display_budget_table'),
    url('^send_report_to_email_updated/$', views.send_report_to_email_updated, name='send_report_to_email_updated'),


    

]

urlpatterns = format_suffix_patterns(urlpatterns)
