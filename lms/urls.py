from django.conf.urls.defaults import patterns, include, url
handler404 = 'lms.views.server_error'
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     ###################for cvtracking################################
     url(r'^CV_Helptextdetail/','lms.views.CV_Helptextdetail'),
     url(r'^CV_Helptext_display/','lms.views.CV_Helptext_display'),
     url(r'^CV_Helptext_edit/id=(?P<helptext_id>[\w\.]+)/$','lms.views.CV_Helptext_edit'),
     url(r'^exportexcelforHelptextadmin/$','lms.views.exportexcelforHelptextadmin'),
     url(r'^exportexcelforHelptextforall/$','lms.views.exportexcelforHelptextforall'),
     
     url(r'^get_collegefordepartmenttable/(?P<uid_id>\d+)','lms.views.get_collegefordepartmenttable'),	
     url(r'^CV_clientsendtoparsing_display/$','lms.views.CV_clientsendtoparsing_display'),
     url(r'^CV_clientsendtoparsing_detail/$','lms.views.CV_clientsendtoparsing_detail'),
     url(r'^CV_clientsendtoparsing_edit/id=(?P<Parsingclient_id>\w+)/$','lms.views.CV_clientsendtoparsing_edit'),
     url(r'^CV_clientsendtoparsing_delete/id=(?P<Parsingclient_id>\w+)/$','lms.views.CV_clientsendtoparsing_delete'),
          

     url(r'^get_college/(?P<cv_uid_id>\d+)','lms.views.get_college'),
     url(r'^get_department/(?P<cv_cid_id>\w+)','lms.views.get_department'),
     url(r'^exportexcel/id=(?P<id>\w+)/id1=(?P<id1>\w+)/id2=(?P<id2>\w+)/$','lms.views.exportexcel'),
     url(r'^exportexcelwithnumber/id=(?P<id>\w+)/id1=(?P<id1>\w+)/id2=(?P<id2>\w+)/$','lms.views.exportexcelwithnumber'),
     url(r'^exportexcelforALLcount/$','lms.views.exportexcelforALLcount'),   
     url(r'^exportexcel/$','lms.views.exportexcel'),
     url(r'^CV_searchmorespecific_detail/$','lms.views.CV_searchmorespecific_detail'), 
     url(r'^CV_searchmorespecific/$','lms.views.CV_searchmorespecific'), 
     url(r'^ChoseSystem/$','lms.views.chosesystem'),
     url(r'^CV_adduniversity/$','lms.views.CV_university_detail'),
     url(r'^CV_university_display/$','lms.views.CV_university_display'),
     url(r'^CV_university_detail/$','lms.views.CV_university_detail'),
     url(r'^CV_university_edit/id=(?P<uid>\w+)/$','lms.views.CV_university_edit'),
     url(r'^CV_university_delete/id=(?P<uid>\w+)/$','lms.views.CV_university_delete'),
     
     url(r'^CV_Cventry_detail/$','lms.views.CV_Cventry_detail'),
     url(r'^CV_Cventry_display/$','lms.views.CV_Cventry_display'),
     url(r'^CV_Cventry_edit/id=(?P<cvid>[\w\.]+)/$','lms.views.CV_Cventry_edit'),
     url(r'^CV_Allcount/$','lms.views.CV_Allcount'),
     url(r'^CV_Calculatecvcount_detail/$','lms.views.CV_Calculatecvcount_detail'),
     url(r'^CV_Calculatecvcount_Display/$','lms.views.CV_Calculatecvcount_Display'),
     url(r'^CV_signin/$','lms.views.CV_access_userbasic_detail1'),
     
     url(r'^CV_captcha/',include('captcha.urls')),
     
     url(r'CV_captcha2/$','lms.views.CV_captcha'),
     url(r'^CV_SignUp', 'lms.views.CV_SignUp'),
     url(r'^CV_access_userbasic_detail1','lms.views.CV_access_userbasic_detail1'),
     url(r'^CV_login/$', 'lms.views.CV_login'),
     url(r'^CV_logout/$','lms.views.CV_stupidsessiondeleteit'),
     url(r'^CV_log2in/$','lms.views.CV_log2in'),
     url(r'^CV_insertupdateexcelsheet/$','lms.views.CV_insertupdateexcelsheet'),
     url(r'^CV_insertupdateexcelsheet_detail/$','lms.views.CV_insertupdateexcelsheet_detail'),
     url(r'^CV_searchdisplay/$','lms.views.CV_searchdisplay'),
     url(r'^CV_searchdisplay/search2=(?P<search2>[\w\*]+)/$','lms.views.CV_searchdisplay'),
     url(r'^CV_College_detail/$','lms.views.CV_College_detail'),
     url(r'^CV_College_display/$','lms.views.CV_College_display'),
     url(r'^CV_College_edit/id=(?P<cid>\w+)/$','lms.views.CV_College_edit'),
     url(r'^CV_College_delete/id=(?P<cid>\w+)/$','lms.views.CV_College_delete'),
     
     url(r'^CV_Department_detail/$','lms.views.CV_Department_detail'),
     url(r'^CV_Department_display/$','lms.views.CV_Department_display'),
     url(r'^CV_Department_edit/id=(?P<did>\w+)/$','lms.views.CV_Department_edit'),
     url(r'^CV_Department_delete/id=(?P<did>\w+)/$','lms.views.CV_Department_delete'),
     url(r'^CV_changepassword/$','lms.views.CV_changepassword'),
     url(r'^CV_Showpasswordchange/$','lms.views.CV_Showpasswordchange'),
     url(r'^CV_passwordrecovery/$','lms.views.CV_passwordrecovery'),
     url(r'^CV_showrecovery/$','lms.views.CV_showrecovery'),
     
     #url(r'^company/autocomplete/$','cvtracking1.views.autocomplete_company'),#q<channel>[a-z]+)$'
     #url(r'^brand/(?P<brand>[-\w]+)/all_json_models/$', 'cvtracking1.views.all_json_models'),  
     url(r'^CV_upload_file/$','lms.views.CV_upload_file') ,
     url(r'^CV_handle_uploaded_file/$','lms.views.CV_handle_uploaded_file') ,
	#url(r'^handle_uploaded_file/$','lms.views.handle_uploaded_file'),
     #url(r'^insertupdateexcelsheet/$','lms.views.insertupdateexcelsheet'),
    # url(r'^insertupdateexcelsheet_detail/$','lms.views.insertupdateexcelsheet_detail'), 
    ###########################################################################

     url(r'^admin/$','lms.views.basic_detail'),
     url(r'^changepassword/$','lms.views.changepassword'),
     url(r'^Showpasswordchange/$','lms.views.Showpasswordchange'),
     url(r'^passwordrecovery/$','lms.views.passwordrecovery'),
     url(r'^showrecovery/$','lms.views.showrecovery'),
     url(r'^admin1/$','lms.views.Adminbasic_detail'),
     url(r'^Adminbasic_detail/$','lms.views.Adminbasic_detail'),
     url(r'^admindisplay_detail/$', 'lms.views.admindisplay_detail'),
     
     url(r'^holidaytypetable_detail/$','lms.views.holidaytypetable_detail'),
     url(r'^holidaytype_tabledisplay/$','lms.views.holidaytype_tabledisplay'),
     url(r'^Holidaytype_editfunction/id=(?P<type_id>\d+)/$','lms.views.Holidaytype_editfunction'),
     
     url(r'^team_detail/$','lms.views.team_detail'),
     url(r'^teamtabledisplay/$','lms.views.teamtabledisplay'),
     url(r'^Team_editfunction/id=(?P<emp_team_id>\d+)/$','lms.views.Team_editfunction'),
     url(r'^position_detail/$','lms.views.position_detail'),
     url(r'^Position_tabledisplay/$','lms.views.Position_tabledisplay'),
     url(r'^Position12_editfunction/id=(?P<emp_position_id>\d+)/$','lms.views.Position12_editfunction'),
     
     url(r'^Gendertabledisplay/$','lms.views.Gendertabledisplay'),
     url(r'^gender/$','lms.views.gender_detail'),
     url(r'^gender_detail/$','lms.views.gender_detail'),
     url(r'^Gender_editfunction/id=(?P<gender_id>\d+)/$','lms.views.Gender_editfunction'),
     url(r'^gender_delete/id=(?P<gender_id>\d+)/$','lms.views.gender_delete'),
     url(r'^supervisordetail/$', 'lms.views.supervisordetail'),
     url(r'^xsuperdisplay22/$', 'lms.views.xsuperdisplay22'),
     url(r'^display_detail/$', 'lms.views.display_detail'),
     url(r'^display_detail/name=(?P<name>\w+)/$', 'lms.views.display_detail'),
     url(r'^logout/$','lms.views.stupidsessiondeleteit'),
     
     ########for leave details fillign form#####
     url(r'^Leavesummaryfill/$','lms.views.fill_the_summaryformbyhr'),
     url(r'^setthesummaryleaves/$','lms.views.setthesummaryleaves'),
     url(r'^summaryleaves/$','lms.views.listof_leavessummary'),####today added
     url(r'^views/delete_new/id=(?P<emp_id>\d+)/$','lms.views.delete_new'),
     url(r'^views/admindelete/id=(?P<emp_id>\d+)/$','lms.views.admindelete'),
     url(r'^killdelete_new/id=(?P<supervisor_hierarchy_id>\d+)/$','lms.views.killdelete_new'),
     
     url(r'^views/delete_new/id=(?P<emp_id>\d+)/name=(?P<name>\w+)/$','lms.views.delete_new'),
     url(r'^views/edit/id=(?P<emp_id>\d+)/$','lms.views.edit'),
     url(r'^doedit/id=(?P<supervisor_hierarchy_id>\d+)/$','lms.views.doedit'),
     
     url(r'^views/adminedit/id=(?P<emp_id>\d+)/$','lms.views.adminedit'),
     url(r'^views/edit/id=(?P<emp_id>\d+)/name=(?P<name>\w+)/$','lms.views.edit'),
   
     url(r'^basic_detail/$','lms.views.basic_detail'),
     url(r'^views/delete_all','lms.views.delete_all'),
     url(r'^views/basic_detail/$','lms.views.basic_detail'),
     url(r'^views/basic_detail/name=(?P<name>\w+)/$','lms.views.basic_detail'),
     ##TO MANAGE HERACHY
     url(r'^mh/$','lms.views.manage_hirarchy'),
     #url(r'^mh/name=(?P<name>\w+)/$','b.views.manage_hirarchy'),
     
     ###to show notification
     url(r'^notification1/name=(?P<name>\w+)/$','lms.views.notice'),
     url(r'^notification1/$','lms.views.notice'),
     url(r'^signin/$','lms.views.access_userbasic_detail1'),
     #for automatic login pagin show up using lightbox#####################
     url(r'^magicsignin/id=(?P<leave_id>\w+)/$','lms.views.magicsignin'),
     url(r'^lmagicmatch/id=(?P<leave_id>\w+)/$', 'lms.views.lmagicmatch'),
#######################################################################################     
     url(r'^login/$', 'lms.views.login'),
     url(r'^login/name=(?P<name>\w+)/$','lms.views.login'),
     url(r'^log2in/$','lms.views.log2in'),
     url(r'^access_userbasic_detail1','lms.views.access_userbasic_detail1'),
     url(r'^abcofcasual/id=(?P<leave_id>\d+)/$','lms.views.abcofcasual'),###for excedding casual leave and grant or rejet
     
     url(r'^Holiday_detail/$','lms.views.Holiday_detail'),
     url(r'^adminHoliday_detail/$','lms.views.adminHoliday_detail'),
     url(r'^Holiday_display/$','lms.views.Holiday_display'),
     
     
     #url(r'^views/change/id=(?P<holiday_id>\d+)/name=(?P<name>\w+)/$','b.views.change'),
     url(r'^views/change/id=(?P<holiday_id>\d+)/$','lms.views.change'),
     #url(r'^views/eliminate/id=(?P<holiday_id>\d+)/name=(?P<name>\w+)/$','b.views.eliminate'),
     url(r'^views/eliminate/id=(?P<holiday_id>\d+)/$','lms.views.eliminate'),
     #url(r'^views/waste_function/name=(?P<name>\w+)/$','b.views.waste_function'),
     url(r'^views/waste_function/$','lms.views.waste_function'),
     #url(r'^views/all_delete/name=(?P<name>\w+)/$','b.views.all_delete'),
     url(r'^views/all_delete/$','lms.views.all_delete'),

     url(r'^views/Holiday_detail/$','lms.views.Holiday_detail'),
     url(r'^views/Holiday_detail/name=(?P<name>\w+)/$','lms.views.Holiday_detail'),
     #url(r'^Holiday_display/name=(?P<name>\w+)$','b.views.Holiday_display'),
     #url(r'^capcha/$','b.views.captcha'),
     url(r'^captcha/',include('captcha.urls')),
     url(r'captcha2/$','lms.views.captcha'),
     url(r'^SignUp', 'lms.views.SignUp'),
     
     url(r'^news','lms.views.news_detail'),
     url(r'^express_news','lms.views.express_news'),
     url(r'^views/entigence_newsedit/id=(?P<news_id>\d+)/$','lms.views.entigence_newsedit'),
     url(r'^views/nowdelete_new/(\d+)/$','lms.views.nowdelete_new'),
     url(r'^views/complete_delete_all','lms.views.complete_delete_all'),
     url(r'^views/news_detail','lms.views.news_detail'),
     
     url(r'^send_email','lms.views.send_email'),
     #(r'^openid/', include('django_openid_auth.urls')),
     ###for gmailauthentication
#     url(r'^google/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
     #url(r'^google/login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
     #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
     url(r'^applyleave/$','lms.views.Leaveapplyforemployee'),
     #url(r'^accepttoshowpage/name=(?P<name>\w+)', 'b.views.accepttoshowpage'),
     
     url(r'^checkleave/id=(?P<leave_id>\w+)/$', 'lms.views.checkleave'),
     url(r'^accepttoshowpage/id=(?P<leave_id>\w+)/$', 'lms.views.accepttoshowpage'),
     url(r'^leaveacceptorreject/id=(?P<leave_id>\w+)/$', 'lms.views.leaveacceptorreject'),
     url(r'^Rject_linkleaveacceptorreject/id=(?P<leave_id>\w+)/$', 'lms.views.Rject_linkleaveacceptorreject'),#this is for the reject link in the notification option
     url(r'^databasematch/id=(?P<leave_id>\w+)/Accept/$', 'lms.views.databasematch'),#for login to accept leave 
     url(r'^zrejectsignin/id=(?P<leave_id>\w+)/Reject/$', 'lms.views.zrejectsignin'),# login to reject leave
     url(r'^finalmailsend/id=(?P<leave_id>\w+)/$','lms.views.finalmailsend'),
     url(r'^finalmailsend/id=(?P<leave_id>\w+)/eid=(?P<e>\w+)/$','lms.views.finalmailsend'),
     url(r'^Rejectfinalmailsend/id=(?P<leave_id>\w+)/$','lms.views.Rejectfinalmailsend'),
     url(r'^Rejectfinalmailsend/id=(?P<leave_id>\w+)/eid=(?P<e>\w+)/$','lms.views.Rejectfinalmailsend'),
     #url(r'^finalmailsend','b.views.finalmailsend'),
     url(r'^accepttoshowpage/', 'lms.views.accepttoshowpage'),
     url(r'^leaveacceptorreject/', 'lms.views.leaveacceptorreject'),
     url(r'^showleaveapplied/name=(?P<name>\w+)', 'lms.views.showleaveapplied'),
     url(r'^showleaveapplied/$', 'lms.views.showleaveapplied'),
     #url(r'^applyleave/name','b.views.Leaveapplyforemployee'),
     url(r'^applyleave/name=(?P<name>\w+)','lms.views.Leaveapplyforemployee'),
     url(r'^Holiday_display/name=(?P<name>\w+)/$','lms.views.Holiday_display'),#to show holiday list with name of user
     #url(r'^reorder/curr=(?P<f_id>\w+)/swap=(?P<s_id>\w+)/$', 'clrt_dajax.views.reorder'),
     #url(r'^ajax/tag/autocomplete/$','b.views.ajax_tag_autocomplete'),
     url(r'^company/autocomplete/$','lms.views.autocomplete_company'),#q<channel>[a-z]+)$'
     #url(r'^company/autocomplete/?q=(?P<q>\w+)/$','b.views.autocomplete_company'),
     
)
