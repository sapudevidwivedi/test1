from django.shortcuts import render_to_response

from django.core.urlresolvers import reverse
#from Sapu.employee.form import *
from lms.form import Signinform,Employeeform, Holidaylistform,CaptchaTestForm,Newsform,Leaveapplyform,Summaryleavefillform,Supervisorform,\
    Genderform, Positionform, Teamform, Holidaytypeform, Passwordrecoveryform,\
    ChangePasswordform,CV_UNIVERSITYform, CV_form, CV_CalculateCvcountform,\
    CV_Signinform, CV_CaptchaTestForm, CV_insertupdatefile, CV_searchform, CV_COLLEGEform,\
    CV_Departmentform, CV_Passwordrecoveryform, CV_ChangePasswordform, CV_UploadFileForm,CV_searchmorespecificForm,CV_CLIENTFOFPARSINGCVform,CV_Helptext
from django.views.decorators.csrf import csrf_exempt
from models import LMS_EMPLOYEE_TABLE, LMS_SIGNIN, LMS_HOLIDAY_LIST,LMS_SIGNUP,LMS_LEAVES_summary_TABLE,LMS_LEAVE_INFO_TABLE,LMS_SUPERVISORHIERACHY,CV_UNIVERSITY, CV_VEIFYWITHDENOGFILE, CV_SIGNUP,\
    CV_POSITION, CV_College, CV_Department,CV_CV,CV_CLIENTFOFPARSINGCV, CV_HELPTEXT
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
import math,PIL
import lms.settings
from lms.models import LMS_NEWS, LMS_TEAM, LMS_POSITION, LMS_GENDER,\
    LMS_HOLIDAY_TYPE
from django.db.models import Q
import datetime
from datetime import date
from django.core.mail import send_mail, BadHeaderError
from PIL import Image, ImageDraw, ImageFont
import sha
import json

from lms import settings
from django.conf import Settings
import smtplib
import email
from django.contrib import contenttypes
from django.core.mail.message import EmailMessage
print 'nishaaaa'
import MySQLdb
import xlrd
from xlrd import open_workbook
import csv
from random import choice
from django.shortcuts import render_to_response
from os import remove
from urlparse import urlparse
from django.core import mail
from django.core.exceptions import ObjectDoesNotExist
from django.utils import simplejson
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from excel_response import ExcelResponse
print 'xxxxxxxxxxxxxxxxxxxxx'

#######################help text ###############################################################
def exportexcelforHelptextforall(request):
    import xlwt
    from xlwt import Workbook
    objs=ABC1cv_daterecieved_test=CV_HELPTEXT.objects.all()
    print 'objs length:'+str(len(objs))
    ###############testing only
    data=[]
    data1=['Help Text Id','Customer Name','Faculty Name','Faculty Id','Date Requested','Nature Of Request','Resolution','Date Responded','Responders Name','Closed Y/N']
    j=2
    data.append(data1)
    for i in objs:
        dataj='data'+str(j)
        dataj=[]
        if len(dataj)<4:
            helptext_id=str(i.helptext_id)
            helpCustomer_Name=str(i.helpCustomer_Name)
            Faculty_Name=str(i.Faculty_Name)
            Faculty_id=str(i.Faculty_id)
            Date_Requested=str(i.Date_Requested)
            Nature_of_the_Request=str(i.Nature_of_the_Request)
            Resolution_of_problem=str(i.Resolution_of_problem)
            Date_Responded=str(i.Date_Responded)
            Responders_Name=str(i.Responders_Name)
            Closed_Y_N=str(i.Closed_Y_N)
            #print 'i:'+str(i)    
            dataj.append(helptext_id)
            dataj.append(helpCustomer_Name)
            dataj.append(Faculty_Name)
            dataj.append(Faculty_id)
            dataj.append(Date_Requested)
            dataj.append(Nature_of_the_Request)
            dataj.append(Resolution_of_problem)
            dataj.append(Date_Responded)#new entry for email id
            dataj.append(Responders_Name)
            dataj.append(Closed_Y_N) 
            data.append(dataj)
            j=j+1
    return ExcelResponse(data,'HelpTextData')



def exportexcelforHelptextadmin(request):
    import xlwt
    from xlwt import Workbook
    objs=ABC1cv_daterecieved_test=CV_HELPTEXT.objects.all()
    print 'objs length:'+str(len(objs))
    ###############testing only
    data=[]
    data1=['Help Text Id','Customer Name','Faculty Name','Faculty Id','Date Requested','Nature Of Request','Resolution','Date Responded','Responders Name','Closed Y/N']
    j=2
    data.append(data1)
    for i in objs:
        dataj='data'+str(j)
        dataj=[]
        if len(dataj)<4:
            helptext_id=str(i.helptext_id)
            helpCustomer_Name=str(i.helpCustomer_Name)
            Faculty_Name=str(i.Faculty_Name)
            Faculty_id=str(i.Faculty_id)
            Date_Requested=str(i.Date_Requested)
            Nature_of_the_Request=str(i.Nature_of_the_Request)
            Resolution_of_problem=str(i.Resolution_of_problem)
            Date_Responded=str(i.Date_Responded)
            Responders_Name=str(i.Responders_Name)
            Closed_Y_N=str(i.Closed_Y_N)
            #print 'i:'+str(i)    
            dataj.append(helptext_id)
            dataj.append(helpCustomer_Name)
            dataj.append(Faculty_Name)
            dataj.append(Faculty_id)
            dataj.append(Date_Requested)
            dataj.append(Nature_of_the_Request)
            dataj.append(Resolution_of_problem)
            dataj.append(Date_Responded)#new entry for email id
            dataj.append(Responders_Name)
            dataj.append(Closed_Y_N) 
            data.append(dataj)
            j=j+1
    return ExcelResponse(data,'HelpTextData')


def CV_Helptextdetail(request):
    newsession1=request.session['username']
    #print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    helptest_myobject1=CV_Helptext()
    #print 'nisha'
    return render_to_response('CV_basic_form.html',{'helptest_myobject1':helptest_myobject1,'extra_object':extra_object},RequestContext(request))

def CV_Helptext_display(request):
    print 'hi'
    newsession1=request.session['username']
    #print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    if request.method =='POST':
        print request.POST
        helptest_myobject_display1=CV_Helptext(request.POST)     
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            #print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        #print 'cvvvvv++++++++++++++++++++'
        if helptest_myobject_display1.is_valid():
            print 'valid'
            helptest_myobject_display1.save()
            print 'save'
            return HttpResponseRedirect('/CV_Helptext_display/')
        #print "ggoooooooooooooo"
        print 'error'
        return render_to_response('CV_basic_form.html',{'helptest_myobject_display1':helptest_myobject_display1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        print 'in else'
        helptest_myobject_display2 = CV_HELPTEXT.objects.all()
        allhelptest_myobject_display2 = CV_HELPTEXT.objects.all()# for fetching all data from database
        search1=CV_searchform()
        allsearch1=CV_searchform()
        downloadHelp1='d'
        downloadHelp2='e'
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            #print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                # for fetching all data from database
                if len(helptest_myobject_display2)==0:
                    #print 'length 0'
                    noentryCV_Helptext1_display1='n'
                    return render_to_response('CV_basic_form.html',{'noentryCV_Helptext1_display1':noentryCV_Helptext1_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
                return render_to_response('CV_basic_form.html',{'helptest_myobject_display2':helptest_myobject_display2,'downloadHelp1':downloadHelp1,'extra_object':extra_object,'search1':search1},
                                  RequestContext(request))
        
        if len(allhelptest_myobject_display2)==0: 
                #print 'len of if len(noticeforteamlead)==0: '
                all_noentryCV_Helptext1_display1='nonewnotification'
                return render_to_response('CV_basic_form.html',{'all_noentryCV_Helptext1_display1':all_noentryCV_Helptext1_display1,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('CV_basic_form.html',{'allhelptest_myobject_display2':allhelptest_myobject_display2,'downloadHelp2':downloadHelp2,'extra_object':extra_object,'allsearch1':allsearch1},
                                  RequestContext(request))
        

def CV_Helptext_edit(request,helptext_id):
    print 'hi check'
    newsession1=request.session['username']
    print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    print "sapu"
#    productget=CV_HELPTEXT.objects.filter(helptext_id=helptext_id)
#    for i in productget:
#        cv_id=i.cv_id
#    cv_id=str(cv_id)    
    product = CV_HELPTEXT.objects.get(pk=helptext_id)
    if request.method == 'POST':
        Myhelptext_myobject10 = CV_Helptext(request.POST, instance=product)
        if Myhelptext_myobject10.is_valid():
            product1 = Myhelptext_myobject10.save( commit=False )
            product1.save()       
            #print 'clicking on editttttttt'     
            return HttpResponseRedirect('/CV_Helptext_display/')
        return render_to_response('CV_basic_form.html',{'Myhelptext_myobject10':Myhelptext_myobject10,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            Myhelptext_myobject11=CV_Helptext(instance=product)
            #print 'clicking on edit'
            return render_to_response('CV_basic_form.html',{'Myhelptext_myobject11':Myhelptext_myobject11,'extra_object':extra_object},RequestContext(request))
 

################################################################end############################


def CV_clientsendtoparsing_detail(request):
    newsession1=request.session['username']
    #print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    #print 'forgot password'
    clientsendtoparsing_detailmyobject1=CV_CLIENTFOFPARSINGCVform()
    return render_to_response('CV_basic_form.html',{'clientsendtoparsing_detailmyobject1':clientsendtoparsing_detailmyobject1,'extra_object':extra_object},RequestContext(request))
    #return render_to_response('passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))

def CV_clientsendtoparsing_display(request):
    newsession1=request.session['username']
    #print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    #print 'emp_position_id:'+str(emp_position_id)
    if request.method =='POST':
        #print 'HERE I am'
        clientsendtoparsing_displaymyobject2=CV_CLIENTFOFPARSINGCVform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            #print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        #print 'university'
        if clientsendtoparsing_displaymyobject2.is_valid():
            #print 'i m insid'
            clientsendtoparsing_displaymyobject2.save()
            #print 'i m here'   
            #print 'sendddddddddd'
           
            #print "why"
            return HttpResponseRedirect('/CV_clientsendtoparsing_display/')
        #print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'clientsendtoparsing_displaymyobject2':clientsendtoparsing_displaymyobject2,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        clientsendtoparsing_display_myobject3 = CV_CLIENTFOFPARSINGCV.objects.all()# for fetching all data from database
        clientsendtoparsing_display_allmyobject3 = CV_CLIENTFOFPARSINGCV.objects.all()
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            #print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                # for fetching all data from database
                if len(clientsendtoparsing_display_myobject3)==0:
                    #print 'length 0'
                    noentryclienttoparsing_display1='n'
                    return render_to_response('CV_basic_form.html',{'noentryclienttoparsing_display1':noentryclienttoparsing_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
                return render_to_response('CV_basic_form.html',{'clientsendtoparsing_display_myobject3':clientsendtoparsing_display_myobject3,'extra_object':extra_object},
                                  RequestContext(request))
        
        if len(clientsendtoparsing_display_allmyobject3)==0: 
                #print 'len of if len(noticeforteamlead)==0: '
                all_noentryclientsendtoparsing_display='nonewnotification'
                return render_to_response('CV_basic_form.html',{'all_noentryclientsendtoparsing_display':all_noentryclientsendtoparsing_display,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('CV_basic_form.html',{'clientsendtoparsing_display_allmyobject3':clientsendtoparsing_display_allmyobject3,'extra_object':extra_object},
                                  RequestContext(request))
        
        
def CV_clientsendtoparsing_edit(request,Parsingclient_id):
    newsession1=request.session['username']
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)   
    product = CV_CLIENTFOFPARSINGCV.objects.get(pk=Parsingclient_id)
    if request.method == 'POST':
        clientsendtoparsing_edit_myobject4 = CV_CLIENTFOFPARSINGCVform(request.POST, instance=product)
        if clientsendtoparsing_edit_myobject4.is_valid():
            product1 = clientsendtoparsing_edit_myobject4.save( commit=False )
            product1.save()       
    
            return HttpResponseRedirect('/CV_clientsendtoparsing_display/')
        return render_to_response('CV_basic_form.html',{'clientsendtoparsing_edit_myobject4':clientsendtoparsing_edit_myobject4,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            clientsendtoparsing_edit_myobject5=CV_CLIENTFOFPARSINGCVform(instance=product)
            #print 'clicking on edit'
            return render_to_response('CV_basic_form.html',{'clientsendtoparsing_edit_myobject5':clientsendtoparsing_edit_myobject5,'extra_object':extra_object},RequestContext(request)) 

def CV_clientsendtoparsing_delete(request,Parsingclient_id):
    newsession1=request.session['username']
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    clientsendtoparsing_delete_myobject6 = CV_CLIENTFOFPARSINGCV.objects.get(pk=Parsingclient_id)
    clientsendtoparsing_delete_myobject6.delete()
    return HttpResponseRedirect('/CV_clientsendtoparsing_display/')

#####get college for department table form ############
def get_collegefordepartmenttable(request,uid_id):#=None):
    import json
    ##print 'hi in ajax fuction '
    uid_id=str(uid_id)
    ##print 'uid_id:'+str(uid_id)
    result1=CV_College.objects.filter(uid=uid_id)
    ##print 'result1:'+ str(result1)
    d={}
    lst=[]
    dict2={}
    for i in result1:
        country_id=i.cid
        country=i.cname
        lst.append({'country_id':country_id,'country':country})
       
    ##print 'lst:'+ str(lst)    
    ##print d    
    dict2={'Table':lst}
    ##print 'dict2:'+ str(dict2)
    data_country= simplejson.dumps(dict2)    
        
    #data_country = serializers.serialize('json', Country.objects.filter(continent=continent_id))
    ##print 'data_country:'+str(data_country)
    #data_country= simplejson.dumps( [ tag.country for tag in result1 ] )
    #return HttpResponse( simplejson.dumps( [ tag.country for tag in result1 ] ) )
    return HttpResponse(data_country)#,content_type = 'application/javascript; charset=utf8')
   

#################################

def get_college(request,cv_uid_id):#=None):
    import json
    ##print 'hi in ajax fuction '
    cv_uid_id=str(cv_uid_id)
    ##print 'cv_uid_id:'+str(cv_uid_id)
    result1=CV_College.objects.filter(uid=cv_uid_id)
    ##print 'result1:'+ str(result1)
    d={}
    lst=[]
    dict2={}
    for i in result1:
        country_id=i.cid
        country=i.cname
        lst.append({'country_id':country_id,'country':country})
       
    ##print 'lst:'+ str(lst)    
    ##print d    
    dict2={'Table':lst}
    ##print 'dict2:'+ str(dict2)
    data_country= simplejson.dumps(dict2)    
        
    #data_country = serializers.serialize('json', Country.objects.filter(continent=continent_id))
    #21#ubuntu   10733     1  0 08:35 ?        00:00:00 python manage.py runserver 0.0.0print 'data_country:'+str(data_country)
    #data_country= simplejson.dumps( [ tag.country for tag in result1 ] )
    #return HttpResponse( simplejson.dumps( [ tag.country for tag in result1 ] ) )
    return HttpResponse(data_country)#,content_type = 'application/javascript; charset=utf8')
   
def get_department(request,cv_cid_id):#=None):
    ##print 'getdepartment'
    import json
    ##print 'hi in ajax fuction '
    cv_cid_id=str(cv_cid_id)
    ##print 'cv_cid_id:'+str(cv_cid_id)
    resultofcollege=CV_College.objects.filter(cid=cv_cid_id)
    for item1 in resultofcollege:
         normalCollege_id=item1.normalCollege_id
    normalCollege_id=str(normalCollege_id)     
    result1=CV_Department.objects.filter(cid=normalCollege_id)
    ##print 'result1:'+ str(result1)
    d={}
    lst=[]
    dict2={}
    for i in result1:
        country_id=i.did
        country=i.dname
        lst.append({'country_id':country_id,'country':country})
       
    ##print 'lst:'+ str(lst)    
    ##print d    
    dict2={'Table':lst}
    ##print 'dict2:'+ str(dict2)
    data_country= simplejson.dumps(dict2)    
        
    #data_country = serializers.serialize('json', Country.objects.filter(continent=continent_id))
    #print 'data_country:'+str(data_country)
    #data_country= simplejson.dumps( [ tag.country for tag in result1 ] )
    #return HttpResponse( simplejson.dumps( [ tag.country for tag in result1 ] ) )
    return HttpResponse(data_country)#,content_type = 'application/javascript; charset=utf8')
   


#########################################
def exportexcelforALLcount(request):
    import xlwt
    from xlwt import Workbook
    objs=ABC1cv_daterecieved_test=CV_CV.objects.exclude(Q(cv_datereceived=''))
    ##print 'objs length:'+str(len(objs))
    ###############testing only
    data=[]
    data1=['Serial Number','Faculty Id','Last Name','First Name','University','College','Department','Email Id','CV Received Date','Verified With HR File','CV Parsing Client Name','Date Sent For Parsing','Date Expected From Aspiration','Date Recived From Aspiration','Date CV Send Back To university','Date CV Received From University','Total Times CV Send To University','Date CV Send For Rework','Date CV Received After Rework','Count Of Rework','Date Validation Completed','Date CV Loaded In Test','Date CV Loaded In Production','User Id','Additional Detail']
    j=2
    data.append(data1)
    for i in objs:
        ##print 'hi2'
        ##print 'j:==='+str(j)
        dataj='data'+str(j)
        dataj=[]
        ##print 'dataj:'+str(dataj)
        ##print 'len dataj:'+str(len(dataj))
        if len(dataj)<4:
            ##print 'hi'
            cv_id=str(i.cv_id)
            cvid=str(i.cvid)
            cvlast_name=str(i.cvlast_name)
            cvemp_name=str(i.cvemp_name)
            cv_uid=str(i.cv_uid)#
            cv_cid=str(i.cv_cid)#
            cv_did= str(i.cv_did)#
            cv_email_id=str(i.cv_email_id)#new entry for email id
            cv_datereceived=str(i.cv_datereceived)
            verify_demog=str(i.verify_demog)#
            Parsingclientoption=str(i.Parsingclientoption_id)
            testofparsingclient_test=CV_CLIENTFOFPARSINGCV.objects.filter(Parsingclient_id=Parsingclientoption)
            for test123 in testofparsingclient_test:
                Parsingclientoption=str(test123.Parsingclient_name)####to check for parsing client option as name not as id
            cv_date_sendtoaspiration=str(i.cv_date_sendtoaspiration)
            cv_date_expectedfromaspiration=str(i.cv_date_expectedfromaspiration)
            cv_date_recivedfromaspiration=str(i.cv_date_recivedfromaspiration)
            cv_date_sendtouniversity=str(i.cv_date_sendtouniversity)
            cv_date_receivedfromuniversity=str(i.cv_date_receivedfromuniversity)
            no_oftimesendtouniversity=str(i.no_oftimesendtouniversity)
            cv_date_sendforrework=str(i.cv_date_sendforrework)
            cv_date_receivedfromrework=str(i.cv_date_receivedfromrework)
            nooftime_sendforrework=str(i.nooftime_sendforrework)
            cv_date_validationcompleted=str(i.cv_date_validationcompleted)
            cv_date_cvloadedintest=str(i.cv_date_cvloadedintest)
            cv_date_cvloadedinproduction=str(i.cv_date_cvloadedinproduction)
            CV_UserId=str(i.CV_UserId)
            CV_additionaldetails=str(i.CV_additionaldetails)
            #print 'i:'+str(i)    
            dataj.append(cv_id)
            dataj.append(cvid)
            dataj.append(cvlast_name)
            dataj.append(cvemp_name)
            dataj.append(cv_uid)
            dataj.append(cv_cid)
            dataj.append(cv_did)
            dataj.append(cv_email_id)#new entry for email id
            dataj.append(cv_datereceived)
            dataj.append(verify_demog)            
            dataj.append(Parsingclientoption)
            dataj.append(cv_date_sendtoaspiration)
            dataj.append(cv_date_expectedfromaspiration)
            dataj.append(cv_date_recivedfromaspiration)
            dataj.append(cv_date_sendtouniversity)
            dataj.append(cv_date_receivedfromuniversity)
            dataj.append(no_oftimesendtouniversity)
            dataj.append(cv_date_sendforrework)
            dataj.append(cv_date_receivedfromrework)
            dataj.append(nooftime_sendforrework)
 		    
            dataj.append(cv_date_validationcompleted)
            dataj.append(cv_date_cvloadedintest)
            dataj.append(cv_date_cvloadedinproduction)
            dataj.append(CV_UserId) 
            dataj.append(CV_additionaldetails)
            data.append(dataj)
            j=j+1
    return ExcelResponse(data,'CV_RecievedStatus')



def exportexcelwithnumber(request,id=None,id1=None,id2=None):
    #print 'export for excelllll'
    #print 'id:'+str(id)
    #print 'id1:'+str(id1)
    normal_id=str(id)
    normalCollege_id=str(id1)
    normalDepartment_id=str(id2)
    import xlwt
    from xlwt import Workbook
    objs=CV_CV.objects.filter(cv_uid=normal_id,cv_cid=normalCollege_id,cv_did=normalDepartment_id)
    ##print 'objs length:'+str(len(objs))
    ################################for getting value and checking if college,university and department are none or all
    check1=CV_UNIVERSITY.objects.filter(normal_id=normal_id)
    for item1 in check1:
        uname=item1.uname
    uname=str(uname) 
    #print 'uname:'+str(uname)
    check2=CV_College.objects.filter(normalCollege_id=normalCollege_id,uid=normal_id)
    for item2 in check2:
        cname=item2.cname
    cname=str(cname)
    #print 'cname:'+str(cname)
            
    check3=CV_Department.objects.filter(normalDepartment_id=normalDepartment_id,cid=normalCollege_id)
    for item3 in check3:
        dname=item3.dname
    dname=str(dname)             
    #print 'dname:'+str(dname)
    ####for none entry in department ,college and university
            
    if dname=='None':
        #print 'cv_did is none'
        objs=CV_CV.objects.filter(cv_uid=normal_id,cv_cid=normalCollege_id)
                
                
    if cname=='None':
        #print 'cv_cid is none'
        objs=CV_CV.objects.filter(cv_uid=normal_id)#,cv_cid=normalCollege_id)
                
    if uname=='All':
        #print 'cv_uid is all'
        objs=CV_CV.objects.all()
            
            
           
    ###############################################################
    ###############testing only
    data=[]
    data1=['Serial Number','Faculty Id','Last Name','First Name','University','College','Department','Email Id','CV Received Date','Verified With HR File','CV Parsing Client Name','Date Sent For Parsing','Date Expected From Aspiration','Date Recived From Aspiration','Date CV Send Back To university','Date CV Received From University','Total Times CV Send To University','Date CV Send For Rework','Date CV Received After Rework','Count Of Rework','Date Validation Completed','Date CV Loaded In Test','Date CV Loaded In Production','User Id','Additional Details']
    j=2
    data.append(data1)
    for i in objs:
        ##print 'hi2'
        ##print 'j:==='+str(j)
        dataj='data'+str(j)
        dataj=[]
        ##print 'dataj:'+str(dataj)
        ##print 'len dataj:'+str(len(dataj))
        if len(dataj)<4:
            ##print 'hi'
            cv_id=str(i.cv_id)
            cvid=str(i.cvid)
            cvlast_name=str(i.cvlast_name)
            cvemp_name=str(i.cvemp_name)
            cv_uid=str(i.cv_uid)#
            cv_cid=str(i.cv_cid)#
            cv_did= str(i.cv_did)#
            cv_email_id=str(i.cv_email_id)#new entry
            cv_datereceived=str(i.cv_datereceived)
            verify_demog=str(i.verify_demog)#
            Parsingclientoption=str(i.Parsingclientoption_id)
            cv_date_sendtoaspiration=str(i.cv_date_sendtoaspiration)
            cv_date_expectedfromaspiration=str(i.cv_date_expectedfromaspiration)
            cv_date_recivedfromaspiration=str(i.cv_date_recivedfromaspiration)
            cv_date_sendtouniversity=str(i.cv_date_sendtouniversity)
            cv_date_receivedfromuniversity=str(i.cv_date_receivedfromuniversity)
            no_oftimesendtouniversity=str(i.no_oftimesendtouniversity)
            cv_date_sendforrework=str(i.cv_date_sendforrework)
            cv_date_receivedfromrework=str(i.cv_date_receivedfromrework)
            nooftime_sendforrework=str(i.nooftime_sendforrework)
            cv_date_validationcompleted=str(i.cv_date_validationcompleted)
            cv_date_cvloadedintest=str(i.cv_date_cvloadedintest)
            cv_date_cvloadedinproduction=str(i.cv_date_cvloadedinproduction)
            CV_UserId=str(i.CV_UserId)
            CV_additionaldetails=str(i.CV_additionaldetails)
            #####################conver to university id(primary key) number 
            universitynumber=CV_UNIVERSITY.objects.filter(uname=cv_uid)
            for item1 in universitynumber:
                normal_id=str(item1.normal_id)   
            ###########################################################################
            #####################conver to college id number 
            collegenumber=CV_College.objects.filter(cname=cv_cid,uid=normal_id)
            for item2 in collegenumber:
                normalCollege_id=str(item2.normalCollege_id)   
            ###########################################################################
            #####################conver to department id number 
            departmentnumber=CV_Department.objects.filter(dname=cv_did,cid=normalCollege_id)
            for item3 in departmentnumber:
                normalDepartment_id=str(item3.normalDepartment_id)   
            ###########################################################################
            #####################conver to demog id number 
            demognumber=CV_VEIFYWITHDENOGFILE.objects.filter(demogfileoption=verify_demog)
            for item4 in demognumber:
                demogfile_id=str(item4.demogfile_id)   
            ###########################################################################
            #print 'i:'+str(i)    
            dataj.append(cv_id)
            dataj.append(cvid)
            dataj.append(cvlast_name)
            dataj.append(cvemp_name)
            dataj.append(normal_id)
            dataj.append(normalCollege_id)
            dataj.append(normalDepartment_id)
            dataj.append(cv_email_id)
            dataj.append(cv_datereceived)
            dataj.append(demogfile_id)
            dataj.append(Parsingclientoption)
            dataj.append(cv_date_sendtoaspiration)
            dataj.append(cv_date_expectedfromaspiration)
            dataj.append(cv_date_recivedfromaspiration)
            dataj.append(cv_date_sendtouniversity)
            dataj.append(cv_date_receivedfromuniversity)
            dataj.append(no_oftimesendtouniversity)
            dataj.append(cv_date_sendforrework)
            dataj.append(cv_date_receivedfromrework)
            dataj.append(nooftime_sendforrework)
            dataj.append(cv_date_validationcompleted)
            dataj.append(cv_date_cvloadedintest)
            dataj.append(cv_date_cvloadedinproduction)
            dataj.append(CV_UserId)
            dataj.append(CV_additionaldetails)
            ##print 'dataj:'+str(dataj)
            #print 'data2 length:'+str(len(data+str(j))) 
            #print 'data2:'+str(data+str(j)) 
            data.append(dataj)
            ##print 'dataj:'+str(dataj)
            j=j+1
            ##print 'j:++++++'+str(j)
       
    #print 'data:'+str(data) 
    ################################    
    ##print 'export 1'
    return ExcelResponse(data,'my_excelwithnumber')
    #return ExcelResponse(objs)
#####################################################


def exportexcel(request,id=None,id1=None,id2=None):
    ##print 'export for excelllll'
    ##print 'id:'+str(id)
    ##print 'id1:'+str(id1)
    normal_id=str(id)
    normalCollege_id=str(id1)
    normalDepartment_id=str(id2)
    import xlwt
    from xlwt import Workbook
    objs=CV_CV.objects.filter(cv_uid=normal_id,cv_cid=normalCollege_id,cv_did=normalDepartment_id)
    ################################for getting value and checking if college,university and department are none or all
    check1=CV_UNIVERSITY.objects.filter(normal_id=normal_id)
    for item1 in check1:
        uname=item1.uname
    uname=str(uname) 
    #print 'uname:'+str(uname)
    check2=CV_College.objects.filter(normalCollege_id=normalCollege_id,uid=normal_id)
    for item2 in check2:
        cname=item2.cname
    cname=str(cname)
    #print 'cname:'+str(cname)
            
    check3=CV_Department.objects.filter(normalDepartment_id=normalDepartment_id,cid=normalCollege_id)
    for item3 in check3:
        dname=item3.dname
    dname=str(dname)             
    #print 'dname:'+str(dname)
    ####for none entry in department ,college and university
            
    if dname=='None':
        #print 'cv_did is none'
        objs=CV_CV.objects.filter(cv_uid=normal_id,cv_cid=normalCollege_id)
                
                
    if cname=='None':
        #print 'cv_cid is none'
        objs=CV_CV.objects.filter(cv_uid=normal_id)#,cv_cid=normalCollege_id)
                
    if uname=='All':
        #print 'cv_uid is all'
        objs=CV_CV.objects.all()
            
            
           
    ###############################################################
    ###############testing only
    data=[]
    data1=['Serial Number','Faculty Id','Last Name','First Name','University','College','Department','Email Id' ,'CV Received Date','Verified With HR File','CV Parsing Client Name','Date Sent For Parsing','Date Expected From Aspiration','Date Recived From Aspiration','Date CV Send Back To university','Date CV Received From University','Total Times CV Send To University','Date CV Send For Rework','Date CV Received After Rework','Count Of Rework','Date Validation Completed','Date CV Loaded In Test','Date CV Loaded In Production','User Id','Additional Details']
    j=2
    data.append(data1)
    for i in objs:
        ##print 'hi2'
        ##print 'j:==='+str(j)
        dataj='data'+str(j)
        dataj=[]
        ##print 'dataj:'+str(dataj)
        ##print 'len dataj:'+str(len(dataj))
        if len(dataj)<4:
            ##print 'hi'
            cv_id=str(i.cv_id)
            cvid=str(i.cvid)
            cvlast_name=str(i.cvlast_name)
            cvemp_name=str(i.cvemp_name)
            cv_uid=str(i.cv_uid)
            cv_cid=str(i.cv_cid)
            cv_did= str(i.cv_did)
            cv_email_id=str(i.cv_email_id)
            cv_datereceived=str(i.cv_datereceived)
            verify_demog=str(i.verify_demog)
            Parsingclientoption=str(i.Parsingclientoption_id)
            testofparsingclient_test=CV_CLIENTFOFPARSINGCV.objects.filter(Parsingclient_id=Parsingclientoption)
            for test123 in testofparsingclient_test:
            	Parsingclientoption=str(test123.Parsingclient_name)####to check for parsing client option as name not as id
            cv_date_sendtoaspiration=str(i.cv_date_sendtoaspiration)
            cv_date_expectedfromaspiration=str(i.cv_date_expectedfromaspiration)
            cv_date_recivedfromaspiration=str(i.cv_date_recivedfromaspiration)
            cv_date_sendtouniversity=str(i.cv_date_sendtouniversity)
            cv_date_receivedfromuniversity=str(i.cv_date_receivedfromuniversity)
            no_oftimesendtouniversity=str(i.no_oftimesendtouniversity)
            cv_date_sendforrework=str(i.cv_date_sendforrework)
            cv_date_receivedfromrework=str(i.cv_date_receivedfromrework)
            nooftime_sendforrework=str(i.nooftime_sendforrework)
            cv_date_validationcompleted=str(i.cv_date_validationcompleted)
            cv_date_cvloadedintest=str(i.cv_date_cvloadedintest)
            cv_date_cvloadedinproduction=str(i.cv_date_cvloadedinproduction)
            CV_UserId=str(i.CV_UserId)
            CV_additionaldetails=str(i.CV_additionaldetails)
            #print 'i:'+str(i)    
            dataj.append(cv_id)
            dataj.append(cvid)
            dataj.append(cvlast_name)
            dataj.append(cvemp_name)
            dataj.append(cv_uid)
            dataj.append(cv_cid)
            dataj.append(cv_did)
            dataj.append(cv_email_id)
            dataj.append(cv_datereceived)
            dataj.append(verify_demog)
            dataj.append(Parsingclientoption)
            dataj.append(cv_date_sendtoaspiration)
            dataj.append(cv_date_expectedfromaspiration)
            dataj.append(cv_date_recivedfromaspiration)
            dataj.append(cv_date_sendtouniversity)
            dataj.append(cv_date_receivedfromuniversity)
            dataj.append(no_oftimesendtouniversity)
            dataj.append(cv_date_sendforrework)
            dataj.append(cv_date_receivedfromrework)
            dataj.append(nooftime_sendforrework)
            dataj.append(cv_date_validationcompleted)
            dataj.append(cv_date_cvloadedintest)
            dataj.append(cv_date_cvloadedinproduction)
            dataj.append(CV_UserId)
            dataj.append(CV_additionaldetails)
            ##print 'dataj:'+str(dataj)
            #print 'data2 length:'+str(len(data+str(j))) 
            #print 'data2:'+str(data+str(j)) 
            data.append(dataj)
            ##print 'dataj:'+str(dataj)
            j=j+1
            ##print 'j:++++++'+str(j)
       
    ##print 'data:'+str(data) 
    ################################    
    ##print 'export 1'
    return ExcelResponse(data,'CV_Tracking')
    #objs = CV_CV.objects.all()
    ##print 'export 1'
    #return ExcelResponse(objs)
#######################select yr system################################
def chosesystem(request):
    ##print 'hiiiisystem chose'
    chosesystem_object1='a'
    return render_to_response('CV_basic_form.html',{'chosesystem_object1':chosesystem_object1,},RequestContext(request))

##################################code for cvtracking###############################

def CV_searchmorespecific_detail(request):
    ##print 'calculate count of cv'
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    #############
    searchmorespecific_detailobject1=CV_searchmorespecificForm()
    allsearchmorespecific_detailobject2=CV_searchmorespecificForm()
    new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.username 
        xemail_id=str(xemail_id)
        ##print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            return render_to_response('CV_basic_form.html',{'searchmorespecific_detailobject1':searchmorespecific_detailobject1,'extra_object':extra_object},RequestContext(request))        
    return render_to_response('CV_basic_form.html',{'allsearchmorespecific_detailobject2':allsearchmorespecific_detailobject2,'extra_object':extra_object},RequestContext(request))        
  
def CV_searchmorespecific(request):
    ##print 'search more specific'
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    #############
    if 'submit' in request.POST:
        ##print "inside login"
        
        myrequestpost=request.POST.copy()
        #print 'myrequestpost:'
        #print myrequestpost
        uid=myrequestpost['cv_uid']
        cid=myrequestpost['cv_cid']
        did=myrequestpost['cv_did']
        #print 'uid:'+str(uid)
        #print 'cid:'+str(cid)
        #print 'did:'+str(did)
        uid=str(uid)
        cid=str(cid)
        did=str(did)
        
        resultofcollege=CV_College.objects.filter(cid=cid)
        for item1 in resultofcollege:
            normalCollege_id=item1.normalCollege_id
        normalCollege_id=str(normalCollege_id) 
        
        resultofdepartment=CV_Department.objects.filter(did=did)
        for item2 in resultofdepartment:
            normalDepartment_id=item2.normalDepartment_id
        normalDepartment_id=str(normalDepartment_id)
        
        myrequestpost['cv_cid']=normalCollege_id
        myrequestpost['cv_did']=normalDepartment_id
        #print 'HERE I am'
        searchmorespecificobject1=CV_searchmorespecificForm(myrequestpost)     
        #############
        #searchmorespecificobject1=CV_searchmorespecificForm(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'cvvvvv'
        if searchmorespecificobject1.is_valid():
            cv_uid=searchmorespecificobject1.cleaned_data['cv_uid']
            cv_cid=searchmorespecificobject1.cleaned_data['cv_cid']
            cv_did=searchmorespecificobject1.cleaned_data['cv_did']
            cv_uid=str(cv_uid)
            cv_cid=str(cv_cid)
            cv_did=str(cv_did)
            ##print 'cv_uid:'+str(cv_uid)
            ##print 'cv_cid:'+str(cv_cid)
            ##print 'cv_did:'+str(cv_did)  
            check1=CV_UNIVERSITY.objects.filter(uname=cv_uid)
            for item1 in check1:
                normal_id=item1.normal_id
            normal_id=str(normal_id) 
            
            check2=CV_College.objects.filter(cname=cv_cid,uid=normal_id)
            for item2 in check2:
                normalCollege_id=item2.normalCollege_id
            normalCollege_id=str(normalCollege_id)
            
            check3=CV_Department.objects.filter(dname=cv_did,cid=normalCollege_id)
            for item3 in check3:
                normalDepartment_id=item3.normalDepartment_id
            normalDepartment_id=str(normalDepartment_id)             
            #return HttpResponseRedirect(sta_url)
            ABC=CV_CV.objects.filter(cv_uid=normal_id,cv_cid=normalCollege_id,cv_did=normalDepartment_id)
            ####for none entry in department ,college and university
            
            if cv_did=='None':
                #print 'cv_did is none'
                ABC=CV_CV.objects.filter(cv_uid=normal_id,cv_cid=normalCollege_id)
                
                
            if cv_cid=='None':
                #print 'cv_cid is none'
                ABC=CV_CV.objects.filter(cv_uid=normal_id)#,cv_cid=normalCollege_id)
                
            if cv_uid=='All':
                #print 'cv_uid is all'
                ABC=CV_CV.objects.all()
            
            
            #####################################
            download1='e'
            download2='g'
            new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
            for x in new_object1111:
                xemail_id=x.username 
                xemail_id=str(xemail_id)
                ##print 'xemail_id:'+str(xemail_id)
                if newsession1==xemail_id:
                    if len(ABC)==0:
                        ##print 'valid entry please'
                        invalidsearch='invalid'
                        return render_to_response('CV_basic_form.html',{'invalidsearch':invalidsearch,'extra_object':extra_object},RequestContext(request))
                    searchmorespecificobject2=ABC
                    return render_to_response('CV_basic_form.html',{'searchmorespecificobject2':searchmorespecificobject2,'extra_object':extra_object,'download1':download1,'download2':download2,'normal_id':normal_id,'normalCollege_id':normalCollege_id,'normalDepartment_id':normalDepartment_id},RequestContext(request))
            if len(ABC)==0:
                ##print 'all please valid entry'
                allinvalidsearch='invalid'
                return render_to_response('CV_basic_form.html',{'allinvalidsearch':allinvalidsearch,'extra_object':extra_object},RequestContext(request))
            Allsearchmorespecificobject2=ABC
            return render_to_response('CV_basic_form.html',{'Allsearchmorespecificobject2':Allsearchmorespecificobject2,'extra_object':extra_object,'download1':download1,'normal_id':normal_id,'normalCollege_id':normalCollege_id,'normalDepartment_id':normalDepartment_id},RequestContext(request))
       #print 'form is not valid'
        return render_to_response('CV_basic_form.html',{'searchmorespecificobject1':searchmorespecificobject1,'extra_object':extra_object},
                                  RequestContext(request)) 

 


##############






def deletlaterinsertupdateexcelsheet(request):
    newsession1=request.session['username']
    ##print newsession1 
    extra_object='abc'
    #extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    if request.method =='POST':
        ##print 'HERE I am'
        ##############
        form = UploadFileForm(request.POST, request.FILES)
        insertupdateexcelsheet1=form
        ##print 'hello'
        ##print form
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/insertupdateexcelsheet_detail/'
            return HttpResponseRedirect(sta_url)
        if form.is_valid():
            ##print 'valid'
            ##print request.FILES['file']
	    input_excel=request.FILES['file']
	    book = xlrd.open_workbook(file_contents=input_excel.read())
            handle_uploaded_file(request.FILES['file'])
	    sheet=book.sheet_by_index(0)
            
	    ##print sheet
            ##print (sheet.nrows,sheet.ncols)
	    ##print sheet.cell(1,4).value
         ##########################################      
#        insertupdateexcelsheet1=insertupdatefile(request.POST)
#            return HttpResponseRedirect('/insertupdateexcelsheet/')
 #       print "ggoooooooooooooo"
  #      return render_to_response('basic_form.html',{'insertupdateexcelsheet1':insertupdateexcelsheet1,'extra_object':extra_object},
   #                               RequestContext(request))
  
#        ##############################################################
#        print 'university'
#        if insertupdateexcelsheet1.is_valid():
#            print 'i m insid'
#            path11=insertupdateexcelsheet1.cleaned_data['Path']
#            path11=str(path11)
#            ff=path11.split('.')
#            ffdot1=ff[0]
#            ffdot2=ff[1]
#            print 'ffdot2:'+str(ffdot2)
#            if ffdot2!='xls':
#                print 'not .xls format '
#                notxlsformat='n' 
#                return render_to_response('basic_form.html',{'notxlsformat':notxlsformat,'extra_object':extra_object},
#                                  RequestContext(request))
#            path11=''+str(path11)+'' 
#            print 'path11999:'+str(path11)
            ##############
            ##print 'hii--insert update excel file'
            import MySQLdb
            #path1=path11
            #print 'hello1----'
            #book = xlrd.open_workbook(path1)
            #print 'hello2----'
            #sheet=book.sheet_by_index(0)
            ##print 'hello3----'
            ##print (sheet.nrows,sheet.ncols)
            # Establish a MySQL connection
            database = MySQLdb.connect(host="lms.cqdyij3rpxcb.us-east-1.rds.amazonaws.com", user = "lms", passwd = "$Carlito$90", db = "lms")
            ##print 'hello4----'
            # Get the cursor, which is used to traverse the database, line by line
            cursor = database.cursor()
            # Create the INSERT INTO sql query
            query = """INSERT INTO lms_cv_cv (cv_id,cvid,cvlast_name, cvemp_name, cv_uid, cv_cid, cv_did, cv_datereceived, verify_demog, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                 ON DUPLICATE KEY UPDATE cv_id=values(cv_id),cvid=values(cvid),
                 cvlast_name=values(cvlast_name),cvemp_name=values(cvemp_name), 
                 cv_uid=values(cv_uid),cv_cid=values(cv_cid),cv_did=values(cv_did), 
                 cv_datereceived=values(cv_datereceived),
                  verify_demog=values(verify_demog),
                  cv_date_sendtoaspiration=values(cv_date_sendtoaspiration), 
                  cv_date_expectedfromaspiration=values(cv_date_expectedfromaspiration),
                   cv_date_recivedfromaspiration=values(cv_date_recivedfromaspiration), 
                   cv_date_validationcompleted=values(cv_date_validationcompleted),
                cv_date_cvloadedintest=values(cv_date_cvloadedintest),
                 cv_date_cvloadedinproduction=values(cv_date_cvloadedinproduction) """
            # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
            for r in range(1, sheet.nrows):
                cv_id=int(sheet.cell(r,0).value)
                cvid     = sheet.cell(r,1).value
                cvlast_name    = sheet.cell(r,2).value
                cvemp_name         = sheet.cell(r,3).value
                cv_uid        = sheet.cell(r,4).value
                cv_cid        = sheet.cell(r,5).value
                cv_did        = sheet.cell(r,6).value
                cv_datereceived      = sheet.cell(r,7).value
                verify_demog    = sheet.cell(r,8).value
                cv_date_sendtoaspiration        = sheet.cell(r,9).value
                cv_date_expectedfromaspiration      = sheet.cell(r,10).value
                cv_date_recivedfromaspiration        = sheet.cell(r,11).value
                cv_date_validationcompleted       = sheet.cell(r,12).value
                cv_date_cvloadedintest         = sheet.cell(r,13).value
                cv_date_cvloadedinproduction         = sheet.cell(r,14).value
                ##print 'HERE I AM'
                ##print (cv_id,cvid,cvlast_name, cvemp_name, cv_uid,cv_cid,cv_did, cv_datereceived, verify_demog, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction)
                # Assign values from each row
                ##print 'hello5----'
                values = (cv_id,cvid,cvlast_name, cvemp_name, cv_uid,cv_cid,cv_did, cv_datereceived, verify_demog, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction)
                ##print 'hello6----'
                # Execute sql Query
                cursor.execute(query,values)
                ##print 'hello7----'
            # Close the cursor
            cursor.close()
            ##print 'hello8----'
            # Commit the transaction
            database.commit()
            ##print 'hello9----'
            # Close the database connection
            database.close()
            ##print 'hello10----'
            # Print results
            print ""
            print "All Done! Bye, for now."
            print ""
            columns = str(sheet.ncols)
            rows = str(sheet.nrows)
           
            return HttpResponseRedirect('/insertupdateexcelsheet/')
        ##print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'insertupdateexcelsheet1':insertupdateexcelsheet1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        ##print 'else'
        myobject9 = CV_CV.objects.all()
        return render_to_response('basic_form.html',{'myobject9':myobject9,'extra_object':extra_object},
                                  RequestContext(request))
    
    




#############################delete this above code#################below is correct code of cvtracking########################################

###########forgot password form
def CV_passwordrecovery(request):
    ##print 'forgot password'
    recoverypassword=CV_Passwordrecoveryform()
    #return render_to_response('basic_form.html',{'recoverypassword':recoverypassword,},RequestContext(request))
    return render_to_response('CV_passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))


def CV_showrecovery(request):
    if request.method =='POST':
        ##print 'HERE I am'
        recoverypassword1=CV_Passwordrecoveryform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/CV_access_userbasic_detail1/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'forgot password'
        if recoverypassword1.is_valid():
            ##print 'i m insiderrrrrrrrrrrrrrrr'
            username=recoverypassword1.cleaned_data['username']
            #recoverypassword1.save()
            username=str(username)
            object_password=CV_SIGNUP.objects.filter(username=username)
            ##print 'object_password:'+str(object_password)
            ##print 'match'
            for i in object_password:
               sendingpassword =i.password
               #summary_id=i.summary_id
            sendingpassword=str(sendingpassword) 
            ##print 'sendingpassword:'+str(sendingpassword) 
            from_email='victory.nisha@gmail.com' ###change it to team lead id
            passwd='nishadwivedinishadwivedi'
            subject='Password Recovery'
            message='Your Password :'+str(sendingpassword)
            connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
            connection.open()
            email1 = mail.EmailMessage(subject,message,from_email, [username], connection=connection)
            email1.send()
                                
            ##print 'i m here'   
            print 'sendddddddddd'
            connection.close()
            ##print "why"
            return HttpResponseRedirect('/CV_showrecovery/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_passwordrelated.html',{'recoverypassword1':recoverypassword1},
                                  RequestContext(request))
    else:
        passwordrecovery3 = 'mail send'# for fetching all data from database
        
        return render_to_response('CV_passwordrelated.html',{'passwordrecovery3':passwordrecovery3},
                                  RequestContext(request))


###############
#######change password####
def CV_changepassword(request):

    ##print 'forgot password'
    changepassword_obj=CV_ChangePasswordform()
    return render_to_response('CV_passwordrelated.html',{'changepassword_obj':changepassword_obj,},RequestContext(request))

def CV_Showpasswordchange(request):
    if request.method =='POST':
        ##print 'HERE I am'
        changepassword1=CV_ChangePasswordform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/CV_access_userbasic_detail1/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'changepassword1'
        if changepassword1.is_valid():
            ##print 'i m insiderrrrrrrrrrrrrrrr'
            username = changepassword1.cleaned_data['username']
            oldpassword = changepassword1.cleaned_data['oldpassword']
            newpassword = changepassword1.cleaned_data['newpassword']
            confirmpassword = changepassword1.cleaned_data['confirmpassword']
            #recoverypassword1.save()
            username=str(username)
            oldpassword=str(oldpassword)
            newpassword=str(newpassword)
            confirmpassword=str(confirmpassword)
            object_passwordchange=CV_SIGNUP.objects.filter(username=username,password=oldpassword)
            ##print 'object_passwordchange:'+str(object_passwordchange)
            ##print 'match'
            for i in object_passwordchange:
               signup_id =i.signup_id
            abc=CV_SIGNUP.objects.get(pk=signup_id)
            ##print 'abc:'+str(abc)
            abc.password=newpassword
            abc.confirm_password=confirmpassword
            abc.save()
            #sendingpassword=str(sendingpassword)  
            from_email='victory.nisha@gmail.com' ###change it to team lead id
            passwd='nishadwivedinishadwivedi'
            subject='Password Recovery'
            message='Your New Password :'+str(newpassword)
            connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
            connection.open()
            email1 = mail.EmailMessage(subject,message,from_email, [username], connection=connection)
            email1.send()
                                
            ##print 'i m here'   
            print 'sendddddddddd'
            connection.close()
            ##print "why"
            return HttpResponseRedirect('/CV_Showpasswordchange/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_passwordrelated.html',{'changepassword1':changepassword1},
                                  RequestContext(request))
    else:
        passwordrecovery3 = 'mail send'# for fetching all data from database
        
        return render_to_response('CV_passwordrelated.html',{'passwordrecovery3':passwordrecovery3},
                                  RequestContext(request))



###########collegeentryform
def CV_Department_detail(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print 'forgot password'
    department_detailobject1=CV_Departmentform()
    return render_to_response('CV_basic_form.html',{'department_detailobject1':department_detailobject1,'extra_object':extra_object},RequestContext(request))
    #return render_to_response('passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))

def CV_Department_display(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.username 
        xemail_id=str(xemail_id)
    ##print 'xemail_id:'+str(xemail_id)
    if request.method =='POST':
        ##print 'HERE I am'
        myrequestpost=request.POST.copy()
        #print 'myrequestpost:'
        cid=myrequestpost['cid']
        #print 'cid:'+str(cid)
        cid=str(cid)
        resultofcollege=CV_College.objects.filter(cid=cid)
        for item1 in resultofcollege:
            normalCollege_id=item1.normalCollege_id
        normalCollege_id=str(normalCollege_id) 
        myrequestpost['cid']=normalCollege_id
        department_displayobject1=CV_Departmentform(myrequestpost)
        #department_displayobject1=CV_Departmentform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'university'
        if department_displayobject1.is_valid():
            ##print 'i m insid'
            department_displayobject1.save()
            ##print 'i m here'   
            print 'sendddddddddd'
           
            ##print "why"
            return HttpResponseRedirect('/CV_Department_display/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'department_displayobject1':department_displayobject1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        department_displayobject2 = CV_Department.objects.all()
        alldepartment_displayobject2 = CV_Department.objects.all()
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            ##print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                # for fetching all data from database
                if len(department_displayobject2)==0:
                    ##print 'length 0'
                    noentrydepartment_display1='n'
                    return render_to_response('CV_basic_form.html',{'noentrydepartment_display1':noentrydepartment_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
                return render_to_response('CV_basic_form.html',{'department_displayobject2':department_displayobject2,'extra_object':extra_object},
                                  RequestContext(request))
        if len(alldepartment_displayobject2)==0: 
                ##print 'len of if len(noticeforteamlead)==0: '
                all_noentrydepartment_display1='nonewnotification'
                return render_to_response('CV_basic_form.html',{'all_noentrydepartment_display1':all_noentrydepartment_display1,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('CV_basic_form.html',{'alldepartment_displayobject2':alldepartment_displayobject2,'extra_object':extra_object},
                                  RequestContext(request))
        
        
def CV_Department_edit(request,did):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "sapu"
    productget=CV_Department.objects.filter(did=did)
    for i in productget:
        normalDepartment_id=i.normalDepartment_id
    normalDepartment_id=str(normalDepartment_id)    
    product = CV_Department.objects.get(pk=normalDepartment_id)
    if request.method == 'POST':
        department_edit1 = CV_Departmentform(request.POST, instance=product)

        ##print "PRODUCTchecking POST"

        if department_edit1.is_valid():
            ##print "Display Form"

            product1 = department_edit1.save( commit=False )
            product1.save()       
            ##print 'clicking on editttttttt'     
            return HttpResponseRedirect('/CV_Department_display/')
        return render_to_response('CV_basic_form.html',{'department_edit1':department_edit1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            department_edit2=CV_Departmentform(instance=product)
            ##print 'clicking on edit'
            return render_to_response('CV_basic_form.html',{'department_edit2':department_edit2,'extra_object':extra_object},RequestContext(request)) 

def CV_Department_delete(request,did):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "delete"
    productget=CV_Department.objects.filter(did=did)
    for i in productget:
        normalDepartment_id=i.normalDepartment_id
    departmentdelete1 = CV_Department.objects.get(pk=normalDepartment_id)
    departmentdelete1.delete()
    return HttpResponseRedirect('/CV_Department_display/')


###########collegeentryform
def CV_College_detail(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print 'forgot password'
    college_detailobject1=CV_COLLEGEform()
    return render_to_response('CV_basic_form.html',{'college_detailobject1':college_detailobject1,'extra_object':extra_object},RequestContext(request))
    #return render_to_response('passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))

def CV_College_display(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    if request.method =='POST':
        ##print 'HERE I am'
        college_displayobject1=CV_COLLEGEform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'university'
        if college_displayobject1.is_valid():
            print 'i m insid'
            college_displayobject1.save()
            ##print 'i m here'   
            ##print 'sendddddddddd'
           
            ##print "why"
            return HttpResponseRedirect('/CV_College_display/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'college_displayobject1':college_displayobject1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        college_displayobject2 = CV_College.objects.all()# for fetching all data from database
        allcollege_displayobject2 = CV_College.objects.all()
        ##print 'extra_object'+str(extra_object)
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            ##print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                # for fetching all data from database
                if len(college_displayobject2)==0:
                    ##print 'length 0'
                    noentryCollege_display1='n'
                    return render_to_response('CV_basic_form.html',{'noentryCollege_display1':noentryCollege_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
                return render_to_response('CV_basic_form.html',{'college_displayobject2':college_displayobject2,'extra_object':extra_object},
                                  RequestContext(request))
        
        if len(allcollege_displayobject2)==0: 
                ##print 'len of if len(noticeforteamlead)==0: '
                all_noentryCollege_display1='nonewnotification'
                return render_to_response('CV_basic_form.html',{'all_noentryCollege_display1':all_noentryCollege_display1,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('CV_basic_form.html',{'allcollege_displayobject2':allcollege_displayobject2,'extra_object':extra_object},
                                  RequestContext(request))
        
        
def CV_College_edit(request,cid):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "sapu"
    productget=CV_College.objects.filter(cid=cid)
    for i in productget:
        normalCollege_id=i.normalCollege_id
    normalCollege_id=str(normalCollege_id)    
    product = CV_College.objects.get(pk=normalCollege_id)
    if request.method == 'POST':
        college_edit1 = CV_COLLEGEform(request.POST, instance=product)

        ##print "PRODUCTchecking POST"

        if college_edit1.is_valid():
            ##print "Display Form"

            product1 = college_edit1.save( commit=False )
            product1.save()       
            ##print 'clicking on editttttttt'     
            return HttpResponseRedirect('/CV_College_display/')
        return render_to_response('CV_basic_form.html',{'college_edit1':college_edit1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            college_edit2=CV_COLLEGEform(instance=product)
            ##print 'clicking on edit'
            return render_to_response('CV_basic_form.html',{'college_edit2':college_edit2,'extra_object':extra_object},RequestContext(request)) 

def CV_College_delete(request,cid):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "delete"
    productget=CV_College.objects.filter(cid=cid)
    for i in productget:
        normalCollege_id=i.normalCollege_id
    collegedelete1 = CV_College.objects.get(pk=normalCollege_id)
    collegedelete1.delete()
    return HttpResponseRedirect('/CV_College_display/')


def CV_searchdisplay(request,search2=None):
    ##print 'search result display'
    search3=str(search2)
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    if request.method =='POST':
        ##print 'HERE I am'
        searchdisplay1=CV_searchform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'cvvvvv'
        if searchdisplay1.is_valid():
            search2=searchdisplay1.cleaned_data['search']
            search2=str(search2)
            ##print 'search2:'+str(search2)
            aa=CV_UNIVERSITY.objects.filter(uname=search2)
            if len(aa)==0:
                ##print '---'
                ff=search2.split()
                if len(ff)>1:
                    ff1='_'.join(ff)
                    search2=str(ff1)
                    ##print 'ff1:+++'+str(ff1)
                    sta_url='/CV_searchdisplay/search2='+str(search2)+'/'
                    return HttpResponseRedirect(sta_url)
                ##print 'len(ff):'+str(len(ff))
                ##print 'search2++++++:'+str(search2)
                ##print 'ff+++++:'+str(ff)
                search2=str(search2)
                sta_url='/CV_searchdisplay/search2='+str(search2)+'/'
                return HttpResponseRedirect(sta_url)
            else:
                #for itemsearch in aa:
                    #normal_id=itemsearch.normal_id
                #normal_id=str(normal_id)
                ff=search2.split()
                flength=len(ff)+1
                ff1='_'.join(ff)
                search2=ff1
                ##print 'search2:'+str(search2)
                ##print 'ff1:'+str(ff1)    
                ##print 'flength:'+str(flength)
                ##print 'ff:'+str(ff)
                ##print 'i m insid'
                sta_url='/CV_searchdisplay/search2='+str(search2)+'/'
                return HttpResponseRedirect(sta_url)
        ##print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'searchdisplay1':searchdisplay1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        ##print 'page refreshed'
        search2=search3
        if len(search2)==0:
            search2=str(search2)
        else:
            fff=search2.split('_')
            fff1=' '.join(fff)
            ##print 'fff1:'+str(fff1)
            search2=str(fff1)    
        aa=CV_UNIVERSITY.objects.filter(uname=search2)
        if len(aa)==0:
            ##print 'ignore'
            search3=CV_CV.objects.filter(Q(cvid=search2) | Q(cvlast_name=search2) | Q(cvemp_name=search2))
            if len(search3)==0:
                ##print 'noentry'
                invalidsearch='invalid'
                allinvalidsearch='invalid'
                new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
                for x in new_object1111:
                    xemail_id=x.username 
                    xemail_id=str(xemail_id)
                    ##print 'xemail_id:'+str(xemail_id)
                    if newsession1==xemail_id:
                        return render_to_response('CV_basic_form.html',{'invalidsearch':invalidsearch,'extra_object':extra_object},RequestContext(request))
                return render_to_response('CV_basic_form.html',{'allinvalidsearch':allinvalidsearch,'extra_object':extra_object},RequestContext(request))
               
            else:
                allsearch3=search3
                search3=search3 
                new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
                for x in new_object1111:
                    xemail_id=x.username 
                    xemail_id=str(xemail_id)
                    ##print 'xemail_id:'+str(xemail_id)
                    if newsession1==xemail_id:
                        return render_to_response('CV_basic_form.html',{'search3':search3,'extra_object':extra_object},
                                  RequestContext(request))
                return render_to_response('CV_basic_form.html',{'allsearch3':allsearch3,'extra_object':extra_object},
                                  RequestContext(request))        
        else:
            for itemsearch in aa:
                normal_id=itemsearch.normal_id
            normal_id=str(normal_id) 
            search4=CV_CV.objects.filter(cv_uid=normal_id) 
            allsearch3=search4
            search3=search4 
            new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
            for x in new_object1111:
                xemail_id=x.username 
                xemail_id=str(xemail_id)
                ##print 'xemail_id:'+str(xemail_id)
                if newsession1==xemail_id:
                    return render_to_response('CV_basic_form.html',{'search3':search3,'extra_object':extra_object},
                                  RequestContext(request))
            return render_to_response('CV_basic_form.html',{'allsearch3':allsearch3,'extra_object':extra_object},
                                  RequestContext(request))

#def CV_upload_file(request):
#    if request.method == 'POST':
#        print 'hi'
#        form = CV_UploadFileForm(request.POST, request.FILES)
#        print 'hello'
#        if form.is_valid():
#            print 'valid'
#            CV_handle_uploaded_file(request.FILES['file'])
#            return HttpResponseRedirect('/success/url/')
#    else:
#        form = CV_UploadFileForm()
#    return render_to_response('article.html', {'form': form})

def CV_handle_uploaded_file(f):
    ##print 'welcome'      
    from mmap import mmap,ACCESS_READ
    from xlrd import open_workbook ,cellname
    with open('C:/Documents and Settings/Pradeep Choudhary/Desktop/testexcell.xls', 'wb+') as destination:
        for chunk in f.chunks():
            ##print ';hialla'
            #chunk= '='""+chunk+""
            ##print 'chunk:'+str(chunk)
            destination.write(chunk)
    ##print '----------'
    path1='C:/Documents and Settings/Pradeep Choudhary/Desktop/testexcell.xls'
    ##print 'hello1----'
    import xlrd
    import MySQLdb
    book = xlrd.open_workbook(path1)
    ##print 'hello2----'
    sheet=book.sheet_by_index(0)
    ##print 'hello3----'
    ##print (sheet.nrows,sheet.ncols)
    # Establish a MySQL connection
    database = MySQLdb.connect(host="localhost", user = "cvtracking1", passwd = "cvtracking1", db = "cvtracking1")
    ##print 'hello4----'
# Get the cursor, which is used to traverse the database, line by line
    cursor = database.cursor()
# Create the INSERT INTO sql query
    query = """INSERT INTO cvtracking1_CV_CV (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id, cv_cid_id, cv_did_id, cv_datereceived, verify_demog_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                ON DUPLICATE KEY UPDATE cv_id=values(cv_id),cvid=values(cvid),
                 cvlast_name=values(cvlast_name),cvemp_name=values(cvemp_name), 
                 cv_uid_id=values(cv_uid_id),cv_cid_id=values(cv_cid_id),cv_did_id=values(cv_did_id), 
                 cv_datereceived=values(cv_datereceived),
                  verify_demog_id=values(verify_demog_id),
                  cv_date_sendtoaspiration=values(cv_date_sendtoaspiration), 
                  cv_date_expectedfromaspiration=values(cv_date_expectedfromaspiration),
                   cv_date_recivedfromaspiration=values(cv_date_recivedfromaspiration), 
                   cv_date_validationcompleted=values(cv_date_validationcompleted),
                cv_date_cvloadedintest=values(cv_date_cvloadedintest),
                 cv_date_cvloadedinproduction=values(cv_date_cvloadedinproduction) """
#query = """INSERT INTO cvtracking1.CV_CV (cv_id,cvid,cvlast_name, cvemp_name, cv_uid, cv_datereceived, verify_demog, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
    for r in range(1, sheet.nrows):
        cv_id=int(sheet.cell(r,0).value)
        cvid     = sheet.cell(r,1).value
        cvlast_name    = sheet.cell(r,2).value
        cvemp_name         = sheet.cell(r,3).value
        cv_uid_id        = sheet.cell(r,4).value
        cv_cid_id        = sheet.cell(r,5).value
        cv_did_id        = sheet.cell(r,6).value
        cv_datereceived      = sheet.cell(r,7).value
        verify_demog_id    = sheet.cell(r,8).value
        cv_date_sendtoaspiration        = sheet.cell(r,9).value
        cv_date_expectedfromaspiration      = sheet.cell(r,10).value
        cv_date_recivedfromaspiration        = sheet.cell(r,11).value
        cv_date_validationcompleted       = sheet.cell(r,12).value
        cv_date_cvloadedintest         = sheet.cell(r,13).value
        cv_date_cvloadedinproduction         = sheet.cell(r,14).value
        ##print 'HERE I AM'
        ##print (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id,cv_cid_id,cv_did_id, cv_datereceived, verify_demog_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction)
        # Assign values from each row
        ##print 'hello5----'
        values = (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id,cv_cid_id,cv_did_id, cv_datereceived, verify_demog_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction)
        ##print 'hello6----'
        # Execute sql Query
        cursor.execute(query,values)
        ##print 'hello7----'
    # Close the cursor
    cursor.close()
    ##print 'hello8----'
    # Commit the transaction
    database.commit()
    ##print 'hello9----'
    # Close the database connection
    database.close()
    ##print 'hello10----'
    # Print results
    ##print ""
    ##print "All Done! Bye, for now."
    ##print ""
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    
    
#print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"

    
########################################################################################################################    
#    print open_workbook('C:/Documents and Settings/Pradeep Choudhary/Desktop/pytest.xls')
#    with open('C:/Documents and Settings/Pradeep Choudhary/Desktop/pytest.xls','rb') as f:
#        print open_workbook(
#                            file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
#                            )
#    aString = open('C:/Documents and Settings/Pradeep Choudhary/Desktop/pytest.xls','rb').read()
#    print 'testing reading xls'
#    print open_workbook(file_contents=aString) 
#    
#    book = open_workbook('C:/Documents and Settings/Pradeep Choudhary/Desktop/pytest.xls')
#    sheet = book.sheet_by_index(0)
#    print 'sheet.name:='+str(sheet.name)
#    print 'sheet.nrows:='+str(sheet.nrows),'sheet.ncols:='+str(sheet.ncols)
#    for row_index in range(sheet.nrows):
#        for col_index in range(sheet.ncols):
#            print cellname(row_index,col_index),'-',sheet.cell(row_index,col_index).value
#            
#            #print sheet.cell(row_index,col_index).value
    ##print 'hiii'
    ##
#    book = open_workbook('C:/Documents and Settings/Pradeep Choudhary/Desktop/pytesy3.xls')
#    sheet = book.sheet_by_index(0)
#    for r in range(1, sheet.nrows):
#        cv_id=int(sheet.cell(r,0).value)
#        cvid     = sheet.cell(r,1).value
#        cvlast_name    = sheet.cell(r,2).value
#        cvemp_name         = sheet.cell(r,3).value
#        cv_uid_id        = sheet.cell(r,4).value
#        cv_cid_id        = sheet.cell(r,5).value
#        cv_did_id        = sheet.cell(r,6).value
#        cv_datereceived      = sheet.cell(r,7).value
#        verify_demog_id    = sheet.cell(r,8).value
#        cv_date_sendtoaspiration        = sheet.cell(r,9).value
#        cv_date_expectedfromaspiration      = sheet.cell(r,10).value
#        cv_date_recivedfromaspiration        = sheet.cell(r,11).value
#        cv_date_validationcompleted       = sheet.cell(r,12).value
#        cv_date_cvloadedintest         = sheet.cell(r,13).value
#        cv_date_cvloadedinproduction         = sheet.cell(r,14).value
#        print 'HERE I AM'
#        print (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id,cv_cid_id,cv_did_id, cv_datereceived, verify_demog_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction)
#        # Assign values from each row
#        print 'hello5----'
    ##############
    
     
#    with open('C:/Documents and Settings/Pradeep Choudhary/Desktop/pytest4.csv', 'wb+') as destination:
#        for chunk in f.chunks():
#            print ';hialla'
#            #chunk= '='""+chunk+""
#            print 'chunk:'+str(chunk)
#            destination.write(chunk)
#    import xlrd
#    import csv
#    import MySQLdb
#    path1='C:/Documents and Settings/Pradeep Choudhary/Desktop/pytest4.csv'
#    print 'hello1----'
###    csv_data = csv.reader(path1)
#    database = MySQLdb.connect(host="localhost", user = "cvtracking1", passwd = "cvtracking1", db = "cvtracking1")
#    print 'hello3----'
## Get the cursor, which is used to traverse the database, line by line
#    cursor = database.cursor()
#    print 'hello4'
#    csv_data = csv.reader(file(path1))
#    print 'hello5'
#    for row in csv_data:
#        cursor.execute('''INSERT INTO cvtracking1_CV_CV (cv_id,cvid,cvlast_name, cvemp_name, 
#        cv_uid_id, cv_cid_id, cv_did_id, cv_datereceived, verify_demog_id, 
#        cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, 
#        cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction) 
#        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
#        ON DUPLICATE KEY UPDATE cv_id=values(cv_id),cvid=values(cvid),
#                 cvlast_name=values(cvlast_name),cvemp_name=values(cvemp_name), 
#                 cv_uid_id=values(cv_uid_id),cv_cid_id=values(cv_cid_id),cv_did_id=values(cv_did_id), 
#                 cv_datereceived=values(cv_datereceived),
#                  verify_demog_id=values(verify_demog_id),
#                  cv_date_sendtoaspiration=values(cv_date_sendtoaspiration), 
#                  cv_date_expectedfromaspiration=values(cv_date_expectedfromaspiration),
#                   cv_date_recivedfromaspiration=values(cv_date_recivedfromaspiration), 
#                   cv_date_validationcompleted=values(cv_date_validationcompleted),
#                cv_date_cvloadedintest=values(cv_date_cvloadedintest),
#                 cv_date_cvloadedinproduction=values(cv_date_cvloadedinproduction)''',row) 
#             
#        print 'hello7----'
#    cursor.close()
#    print 'hello8----'
#    database.commit()
#    print 'hello9----'
#    database.close()
#    print 'hello10----'
    
    
def CV_insertupdateexcelsheet_detail(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    insertupdateexcelsheet_detail_1=CV_insertupdatefile()
    ######
    form = CV_UploadFileForm()
    ##print 'nisha'
    return render_to_response('CV_basic_form.html',{'insertupdateexcelsheet_detail_1':insertupdateexcelsheet_detail_1,'form': form,'extra_object':extra_object},RequestContext(request))

def CV_insertupdateexcelsheet(request):
    newsession1=request.session['username']
    ##print newsession1 
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    if request.method =='POST':
        ##print 'HERE I am'
        ##############
        form = CV_UploadFileForm(request.POST, request.FILES)
        insertupdateexcelsheet1=form
        ##print 'hello'
        ##print form
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/CV_insertupdateexcelsheet_detail/'
            return HttpResponseRedirect(sta_url)
        if form.is_valid():
            ##print 'valid'
            ##print request.FILES['file']
            input_excel=request.FILES['file']
            book=xlrd.open_workbook(file_contents=input_excel.read())
            sheet=book.sheet_by_index(0)
            #handle_uploaded_file(request.FILES['file'])
         ##########################################      
#        insertupdateexcelsheet1=insertupdatefile(request.POST)
            #return HttpResponseRedirect('/insertupdateexcelsheet/')
        #print "ggoooooooooooooo"
        #return render_to_response('basic_form.html',{'insertupdateexcelsheet1':insertupdateexcelsheet1,'extra_object':extra_object},
#                                  RequestContext(request))
  
#        ##############################################################
#        print 'university'
#        if insertupdateexcelsheet1.is_valid():
#            print 'i m insid'
#            path11=insertupdateexcelsheet1.cleaned_data['Path']
#            path11=str(path11)
#            ff=path11.split('.')
#            ffdot1=ff[0]
#            ffdot2=ff[1]
#            print 'ffdot2:'+str(ffdot2)
#            if ffdot2!='xls':
#                print 'not .xls format '
#                notxlsformat='n' 
#                return render_to_response('basic_form.html',{'notxlsformat':notxlsformat,'extra_object':extra_object},
#                                  RequestContext(request))
#            path11=''+str(path11)+'' 
#            print 'path11999:'+str(path11)
#            ##############
#            print 'hii--insert update excel file'
#            import xlrd
#            import MySQLdb
#            path1=path11
#            print 'hello1----'
#            book = xlrd.open_workbook(path1)
#            print 'hello2----'
#            sheet=book.sheet_by_index(0)
#            print 'hello3----'
            ##print (sheet.nrows,sheet.ncols)
            # Establish a MySQL connection
            database = MySQLdb.connect(host="lms.cqdyij3rpxcb.us-east-1.rds.amazonaws.com", user = "lms", passwd = "$Carlito$90", db = "lms")
            ##print 'hello4----'
            # Get the cursor, which is used to traverse the database, line by line
            cursor = database.cursor()
            # Create the INSERT INTO sql query
            query = """INSERT INTO lms_cv_cv (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id, cv_cid_id, cv_did_id,cv_email_id, cv_datereceived, verify_demog_id,Parsingclientoption_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration,cv_date_sendtouniversity,cv_date_receivedfromuniversity,no_oftimesendtouniversity, cv_date_sendforrework,cv_date_receivedfromrework,nooftime_sendforrework, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction,CV_UserId,CV_additionaldetails) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
                 ON DUPLICATE KEY UPDATE cv_id=values(cv_id),cvid=values(cvid),
                 cvlast_name=values(cvlast_name),cvemp_name=values(cvemp_name), 
                 cv_uid_id=values(cv_uid_id),cv_cid_id=values(cv_cid_id),cv_did_id=values(cv_did_id),cv_email_id=values(cv_email_id), 
                 cv_datereceived=values(cv_datereceived),
                  verify_demog_id=values(verify_demog_id),
                  Parsingclientoption_id=values(Parsingclientoption_id),
                  cv_date_sendtoaspiration=values(cv_date_sendtoaspiration), 
                  cv_date_expectedfromaspiration=values(cv_date_expectedfromaspiration),
                   cv_date_recivedfromaspiration=values(cv_date_recivedfromaspiration), 
                  cv_date_sendtouniversity=values(cv_date_sendtouniversity),
                   cv_date_receivedfromuniversity=values(cv_date_receivedfromuniversity),
                   no_oftimesendtouniversity=values(no_oftimesendtouniversity),
                   cv_date_sendforrework=values(cv_date_sendforrework),
                   cv_date_receivedfromrework=values(cv_date_receivedfromrework),
                   nooftime_sendforrework=values(nooftime_sendforrework),           
                   cv_date_validationcompleted=values(cv_date_validationcompleted),
                cv_date_cvloadedintest=values(cv_date_cvloadedintest),
                 cv_date_cvloadedinproduction=values(cv_date_cvloadedinproduction), 
                 CV_UserId=values(CV_UserId),
                 CV_additionaldetails=values(CV_additionaldetails) """
            # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
            for r in range(1, sheet.nrows):
                cv_id=int(sheet.cell(r,0).value)
                cvid     = sheet.cell(r,1).value
                cvlast_name    = sheet.cell(r,2).value
                cvemp_name         = sheet.cell(r,3).value
                cv_uid_id        =str( sheet.cell(r,4).value)
                cv_cid_id        = str(sheet.cell(r,5).value)
                cv_did_id        = str(sheet.cell(r,6).value)
                cv_email_id      = sheet.cell(r,7).value
                cv_datereceived      = sheet.cell(r,8).value
                verify_demog_id    = str(sheet.cell(r,9).value)
                Parsingclientoption_id   =str(sheet.cell(r,10).value)
                cv_date_sendtoaspiration        = sheet.cell(r,11).value
                cv_date_expectedfromaspiration      = sheet.cell(r,12).value
                cv_date_recivedfromaspiration        = sheet.cell(r,13).value
                cv_date_sendtouniversity=     sheet.cell(r,14).value
                cv_date_receivedfromuniversity=sheet.cell(r,15).value
                no_oftimesendtouniversity=    sheet.cell(r,16).value
                cv_date_sendforrework              = sheet.cell(r,17).value
                cv_date_receivedfromrework= sheet.cell(r,18).value
                nooftime_sendforrework= sheet.cell(r,19).value
                cv_date_validationcompleted       = sheet.cell(r,20).value
                cv_date_cvloadedintest         = sheet.cell(r,21).value
                cv_date_cvloadedinproduction         = sheet.cell(r,22).value
                CV_UserId                         =sheet.cell(r,23).value
                CV_additionaldetails             =sheet.cell(r,24).value
                ##print 'HERE I AM'
                #####################conver to university id(primary key) number 
                universitynumber=CV_UNIVERSITY.objects.filter(uname=cv_uid_id)
                for item1 in universitynumber:
                    normal_id=str(item1.normal_id)   
                ###########################################################################
                #####################conver to college id number 
                collegenumber=CV_College.objects.filter(cname=cv_cid_id,uid=normal_id)
                for item2 in collegenumber:
                    normalCollege_id=str(item2.normalCollege_id)   
                ###########################################################################
                #####################conver to department id number 
                departmentnumber=CV_Department.objects.filter(dname=cv_did_id,cid=normalCollege_id)
                for item3 in departmentnumber:
                    normalDepartment_id=str(item3.normalDepartment_id) 
                verifynumberconvert=CV_VEIFYWITHDENOGFILE.objects.filter(demogfileoption=verify_demog_id)      
                for item3 in verifynumberconvert:
                    demogfile_id=str(item3.demogfile_id)         
                clientnameconvert=CV_CLIENTFOFPARSINGCV.objects.filter(Parsingclient_name=Parsingclientoption_id)
                for item4 in clientnameconvert:
                    Parsingclient_id=str(item4.Parsingclient_id) 
            ###########################################################################
                # Assign values from each row
                ##print 'hellov----'
                cv_uid_id=normal_id
                cv_cid_id=normalCollege_id
                cv_did_id=normalDepartment_id
                verify_demog_id=demogfile_id
                Parsingclientoption_id=Parsingclient_id
                #print (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id,cv_cid_id,cv_did_id, cv_datereceived, verify_demog_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction)
                # Assign values from each row
                ##print 'hello5----'
                values = (cv_id,cvid,cvlast_name, cvemp_name, cv_uid_id,cv_cid_id,cv_did_id,cv_email_id, cv_datereceived, verify_demog_id,Parsingclientoption_id, cv_date_sendtoaspiration, cv_date_expectedfromaspiration, cv_date_recivedfromaspiration,cv_date_sendtouniversity,cv_date_receivedfromuniversity,no_oftimesendtouniversity, cv_date_sendforrework,cv_date_receivedfromrework,nooftime_sendforrework, cv_date_validationcompleted, cv_date_cvloadedintest, cv_date_cvloadedinproduction,CV_UserId,CV_additionaldetails)
                ##print 'hello6----'
                # Execute sql Query
                cursor.execute(query,values)
                ##print 'hello7----'
            # Close the cursor
            cursor.close()
            ##print 'hello8----'
            # Commit the transaction
            database.commit()
            ##print 'hello9----'
            # Close the database connection
            database.close()
            ##print 'hello10----'
            # Print results
            ##print ""
            ##print "All Done! Bye, for now."
            ##print ""
            columns = str(sheet.ncols)
            rows = str(sheet.nrows)
            
            return HttpResponseRedirect('/CV_insertupdateexcelsheet/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'insertupdateexcelsheet1':insertupdateexcelsheet1,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        ##print 'else'
        myobject9 = CV_CV.objects.all()
        return render_to_response('CV_basic_form.html',{'myobject9':myobject9,'extra_object':extra_object},
                                  RequestContext(request))    
def CV_captcha(request):
    if request.POST:
        ob1 = CV_CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if ob1.is_valid():
            human = True
    else:
        ob1 = CV_CaptchaTestForm()

    #return render_to_response('template.html',locals())
    return render_to_response('CV_basic_form.html',{'ob1':ob1},RequestContext(request))

def CV_SignUp(request):
    ##print "signup "
    
    if request.method =='POST':
        ##print request.POST
        myrequestpost=request.POST.copy()
        ##print 'myrequestpost:'
        ##print myrequestpost
        ##print myrequestpost['name']
        myrequestpost['name']=myrequestpost['name'].title()
        myrequestpost['middlename']=myrequestpost['middlename'].title()
        myrequestpost['lastname']=myrequestpost['lastname'].title()
        ##print 'HERE I am'
        #ob2=CaptchaTestForm(request.POST)
        ob2=CV_CaptchaTestForm(myrequestpost)
        ##print "ggoooooooooooooo"
        #this code is for the login button button######################
        if 'cancel1' in request.POST:
            ##print "inside login"
            strUrl = '/CV_access_userbasic_detail1'
            ##print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ##############################################################
        
        if ob2.is_valid():
            ##print 'i m inside'
            ##print ob2
            ob2.save()
            ##print "why"
            return HttpResponseRedirect('/CV_SignUp/')
        
        return render_to_response('CV_basic_form.html',{'ob2':ob2},
                                  RequestContext(request))
    else:
        ob3 = CV_SIGNUP.objects.all()# for fetching all data from database
        return render_to_response('CV_basic_form.html',{'ob3':ob3},
                                  RequestContext(request))

###signin form
def CV_access_userbasic_detail1(request):
    my_object6=CV_Signinform()
    ##print 'nisha'
    return render_to_response('CV_new_form1.html',{'my_object6':my_object6},RequestContext(request))


def CV_login(request): 
    #if the submitt button selected is login
    ##print request.POST
    if 'LOGIN' in request.POST:
        ##print "inside login"
        u_name=request.POST['username']
        u_pass=request.POST['password']
        ##print 'u_name:'+u_name,'u_pass:'+u_pass
        if u_name=='' and u_pass=='':
            ##print 'the username and password are empty'
            sblank=CV_Signinform()
            return render_to_response('CV_new_form1.html',{'sblank':sblank},RequestContext(request))
        try:
            ##print 'username:' 
            if CV_SIGNUP.objects.get(username=u_name) and CV_SIGNUP.objects.get(password=u_pass): 
                ##print "username and password matches to database"
               ##########this code is for session  #################
                request.session['username']=CV_SIGNUP.objects.get(username=u_name).username
                ##print 'we are using session ie database session'
                ##print request.session['username']
               ############################################               
                my_object17=CV_SIGNUP.objects.filter(username=u_name) 
                extra_object=my_object17   
                a=datetime.date.today()
                ##print a
                
# $$$$$$$$$$$$$$$this part is admin(hr)####################################################3
                testposition=CV_POSITION.objects.filter(emp_position='Admin')
                for k in testposition:
                    emp_position_id=k.emp_position_id
                ##print 'emp_position_id:'+str(emp_position_id)         
                new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
                for x in new_object1111:
                    xemail_id=x.username 
                    xemail_id=str(xemail_id)
                    ##print 'xemail_id:'+str(xemail_id)  
                    if u_name==xemail_id:
                        HR=CV_SIGNUP.objects.filter(username=u_name)
                        extra_object=HR
                        return render_to_response('CV_basic_form.html',{'HR':HR,'a':a,'extra_object':extra_object},RequestContext(request))
                        
                 ##################################################################3        
                my_object17=CV_SIGNUP.objects.filter(username=u_name) 
                extra_object=my_object17
                return render_to_response('CV_basic_form.html',{'my_object17':my_object17,'a':a,'extra_object':extra_object},RequestContext(request))

                
        except:
            ##print "not in database" ###when password or username does not match database       
            sblank=CV_Signinform()
            return render_to_response('CV_new_form1.html',{'sblank':sblank},RequestContext(request))
            #return HttpResponseRedirect('/access_userbasic_detail1/')    
        
    #if the submitt button selected  is forgot password
    if 'FORGOT' in request.POST:
        ##print request.POST
        print 'forgot password' 
    ##this is addition to slove the login link problem which is not working due to htttp response problem
    #this code is for the login button button######################
    if 'cancel1' in request.POST:
        ##print "inside signup"
        strUrl = '/CV_captcha2/'
        ##print 'url:'+str(strUrl)
        return HttpResponseRedirect(strUrl)
    ##############################################################
    ##print request.session['username']
    newsession1=request.session['username']
    ##print newsession1
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
        ##print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.username 
        xemail_id=str(xemail_id)
        ##print 'xemail_id:'+str(xemail_id)
        ##print 'outside try and catch and if'
        if newsession1==xemail_id:
            ##print 'hr'
            HR=CV_SIGNUP.objects.filter(username=newsession1) 
            extra_object=HR  
            return render_to_response('CV_basic_form.html',{'HR':HR,'extra_object':extra_object},RequestContext(request))
    ##print 'other user'
    my_object17=CV_SIGNUP.objects.filter(username=newsession1)
    extra_object=my_object17
    return render_to_response('CV_basic_form.html',{'my_object17':my_object17,'extra_object':extra_object},RequestContext(request))
#################################################################

def CV_log2in(request):
    ##print 'request.signup_id-------------------------------'
    ##print request.session['username']
    newsession1=request.session['username']
    ##print newsession1
    my_object17=CV_SIGNUP.objects.filter(username=newsession1)
    ##print 'code here for hr' 
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.username 
        xemail_id=str(xemail_id)
        ##print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            HR=CV_SIGNUP.objects.filter(username=newsession1) 
            extra_object=HR          
            return render_to_response('CV_basic_form.html',{'HR':HR,'extra_object':extra_object},RequestContext(request))
    my_object17=CV_SIGNUP.objects.filter(username=newsession1)
    extra_object=my_object17
    return render_to_response('CV_basic_form.html',{'my_object17':my_object17,'extra_object':extra_object},RequestContext(request))




def CV_stupidsessiondeleteit(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:    
        ##print 'username length less equal to zero which means user is logout.and session is deleted '
        my_object6=CV_Signinform()
        ##print 'nisha'
        return render_to_response('CV_new_form1.html',{'my_object6':my_object6},RequestContext(request))
##################################################################################################
   
   
    stupidsession=CV_Signinform()
    ##print 'nisha'
    ##print request.session['username']
    newsession1=request.session['username']
    ##print newsession1
    ####this is for session code#########
    try:
        ##print 'we are to delete the session'
        #print request.session['signup_id']
        ##print request.session['username']
        #del request.session['signup_id']
        del request.session['username']
        ##print 'we deleted the session'
    except KeyError:
        pass
#   ############################################# 
    #return render_to_response('basic_form.html',{'my_object6':my_object6},RequestContext(request))
    return render_to_response('CV_new_form1.html',{'stupidsession':stupidsession},RequestContext(request))



###########universityentryform
def CV_university_detail(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print 'forgot password'
    myobject1=CV_UNIVERSITYform()
    return render_to_response('CV_basic_form.html',{'myobject1':myobject1,'extra_object':extra_object},RequestContext(request))
    #return render_to_response('passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))

def CV_university_display(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    if request.method =='POST':
        ##print 'HERE I am'
        myobject2=CV_UNIVERSITYform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'university'
        if myobject2.is_valid():
            ##print 'i m insid'
            myobject2.save()
            ##print 'i m here'   
            ##print 'sendddddddddd'
           
            ##print "why"
            return HttpResponseRedirect('/CV_university_display/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'myobject2':myobject2,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        myobject3 = CV_UNIVERSITY.objects.all()# for fetching all data from database
        allmyobject3 = CV_UNIVERSITY.objects.all()
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            ##print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                # for fetching all data from database
                if len(myobject3)==0:
                    ##print 'length 0'
                    noentryUniversity_display1='n'
                    return render_to_response('CV_basic_form.html',{'noentryUniversity_display1':noentryUniversity_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
                return render_to_response('CV_basic_form.html',{'myobject3':myobject3,'extra_object':extra_object},
                                  RequestContext(request))
        
        if len(allmyobject3)==0: 
                ##print 'len of if len(noticeforteamlead)==0: '
                all_noentryUniversity_display1='nonewnotification'
                return render_to_response('CV_basic_form.html',{'all_noentryUniversity_display1':all_noentryUniversity_display1,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('CV_basic_form.html',{'allmyobject3':allmyobject3,'extra_object':extra_object},
                                  RequestContext(request))
        
        
def CV_university_edit(request,uid):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "sapu"
    productget=CV_UNIVERSITY.objects.filter(uid=uid)
    for i in productget:
        normal_id=i.normal_id
    normal_id=str(normal_id)    
    product = CV_UNIVERSITY.objects.get(pk=normal_id)
    if request.method == 'POST':
        myobject4 = CV_UNIVERSITYform(request.POST, instance=product)

        ##print "PRODUCTchecking POST"

        if myobject4.is_valid():
            ##print "Display Form"

            product1 = myobject4.save( commit=False )
            product1.save()       
            ##print 'clicking on editttttttt'     
            return HttpResponseRedirect('/CV_university_display/')
        return render_to_response('CV_basic_form.html',{'myobject4':myobject4,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            myobject5=CV_UNIVERSITYform(instance=product)
            ##print 'clicking on edit'
            return render_to_response('CV_basic_form.html',{'myobject5':myobject5,'extra_object':extra_object},RequestContext(request)) 

def CV_university_delete(request,uid):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "delete"
    productget=CV_UNIVERSITY.objects.filter(uid=uid)
    for i in productget:
        normal_id=i.normal_id
    myobject6 = CV_UNIVERSITY.objects.get(pk=normal_id)
    myobject6.delete()
    return HttpResponseRedirect('/CV_university_display/')



#####for cvrecieved entry form
def CV_Cventry_detail(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print 'cventryformafterrecivingfrom uiversity for excell'
    myobject7=CV_form()
    return render_to_response('CV_basic_form.html',{'myobject7':myobject7,'extra_object':extra_object},RequestContext(request))
    #return render_to_response('passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))

def CV_Cventry_display(request):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    if request.method =='POST':
        ##print 'HERE I am'
        myrequestpost=request.POST.copy()
        #print 'myrequestpost:'
        #print myrequestpost
        cid=myrequestpost['cv_cid']###this fuction is for converting the 1st letter of every word to capital
        did=myrequestpost['cv_did']
        ##print 'cid:'+str(cid)
        ##print 'did:'+str(did)
        cid=str(cid)
        did=str(did)
        
        resultofcollege=CV_College.objects.filter(cid=cid)
        for item1 in resultofcollege:
            normalCollege_id=item1.normalCollege_id
        normalCollege_id=str(normalCollege_id) 
        
        resultofdepartment=CV_Department.objects.filter(did=did)
        ##print 'department'
        ##print resultofdepartment
        for item2 in resultofdepartment:
            normalDepartment_id=item2.normalDepartment_id
        normalDepartment_id=str(normalDepartment_id)
        ##print 'normalDepartment_id:'+str(normalDepartment_id)
        myrequestpost['cv_cid']=normalCollege_id
        myrequestpost['cv_did']=normalDepartment_id
        #print 'HERE I am'
        myobject8=CV_form(myrequestpost)
        #myobject8=CV_form(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            ##print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='//'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        ##print 'cvvvvv'
        if myobject8.is_valid():
            ##print 'i m insid'
            myobject8.save()
            ##print 'i m here'   
            ##print 'sendddddddddd'
           
            ##print "why"
            return HttpResponseRedirect('/CV_Cventry_display/')
        ##print "ggoooooooooooooo"
        return render_to_response('CV_basic_form.html',{'myobject8':myobject8,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        myobject9 = CV_CV.objects.all()
        allmyobject9 = CV_CV.objects.all()# for fetching all data from database
        search1=CV_searchform()
        allsearch1=CV_searchform()
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            ##print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                # for fetching all data from database
                if len(myobject9)==0:
                    ##print 'length 0'
                    noentryCVentry_display1='n'
                    return render_to_response('CV_basic_form.html',{'noentryCVentry_display1':noentryCVentry_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
                return render_to_response('CV_basic_form.html',{'myobject9':myobject9,'extra_object':extra_object,'search1':search1},
                                  RequestContext(request))
        
        if len(allmyobject9)==0: 
                ##print 'len of if len(noticeforteamlead)==0: '
                all_noentryCVentry_display1='nonewnotification'
                return render_to_response('CV_basic_form.html',{'all_noentryCVentry_display1':all_noentryCVentry_display1,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('CV_basic_form.html',{'allmyobject9':allmyobject9,'extra_object':extra_object,'allsearch1':allsearch1},
                                  RequestContext(request))
        
        
def CV_Cventry_edit(request,cvid):
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    ##print "sapu"
    productget=CV_CV.objects.filter(cvid=cvid)
    for i in productget:
        cv_id=i.cv_id
    cv_id=str(cv_id)    
    product = CV_CV.objects.get(pk=cv_id)
    if request.method == 'POST':
        myobject10 = CV_form(request.POST, instance=product)

        ##print "PRODUCTchecking POST"

        if myobject10.is_valid():
            ##print "Display Form"

            product1 = myobject10.save( commit=False )
            product1.save()       
            ##print 'clicking on editttttttt'     
            return HttpResponseRedirect('/CV_Cventry_display/')
        return render_to_response('CV_basic_form.html',{'myobject10':myobject10,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            myobject11=CV_form(instance=product)
            ##print 'clicking on edit'
            return render_to_response('CV_basic_form.html',{'myobject11':myobject11,'extra_object':extra_object},RequestContext(request))
 
 
def CV_Allcount(request):
        newsession1=request.session['username']
        ##print newsession1
        extra_object=CV_SIGNUP.objects.filter(username=newsession1)
        testposition=CV_POSITION.objects.filter(emp_position='Admin')
        for k in testposition:
            emp_position_id=k.emp_position_id
        ##print 'emp_position_id:'+str(emp_position_id)
    #############
        a=datetime.date.today()
        current_year=datetime.date.today().year
        current_month=datetime.date.today().month
        current_day=datetime.date.today().day
        sumsquares=0
        sumsquares2=0
        sumsquares3=0
        sumsquares4=0
        sumsquares5=0
        sumsquares6=0
        sumsquares7=0
        
        ABC=CV_CV.objects.all()
        empty_list=[]
        myempty_list2=[]
        myempty_list3=[]
        myempty_list4=[]
        myempty_list5=[]
        myempty_list6=[]
        myempty_list7=[]
        
        for i in ABC:
            empty_list1=i.cv_date_sendtoaspiration
            empty_list2=i.cv_datereceived
            empty_list3=i.cv_date_expectedfromaspiration
            empty_list4=i.cv_date_recivedfromaspiration
            empty_list5=i.cv_date_validationcompleted
            empty_list6=i.cv_date_cvloadedintest
            empty_list7=i.cv_date_cvloadedinproduction
            empty_list1=str(empty_list1)
            empty_list2=str(empty_list2)
            empty_list3=str(empty_list3)
            empty_list4=str(empty_list4)
            empty_list5=str(empty_list5)
            empty_list6=str(empty_list6)
            empty_list7=str(empty_list7)
            ##print 'cv_date_sendtoaspiration'+str(empty_list1)
            ##print 'empty_list1:'+str(empty_list1)
            ##print 'empty_list2:'+str(empty_list2)
            ##print 'empty_list3:'+str(empty_list3)
            ##print 'empty_list4:'+str(empty_list4)
            ##print 'empty_list5:'+str(empty_list5)
            ##print 'empty_list6:'+str(empty_list6)
            ##print 'empty_list7:'+str(empty_list7)
            
            if empty_list1=='':
                onlychech=0
                #@print 'empty_list for blank ::'+str(empty_list)
            else:
                empty_list.append(empty_list1)     
            if empty_list2=='':
                onlycheck2=0
                #@print 'empty list for blank myempty_list2::'+str(myempty_list2) 
            else:
                myempty_list2.append(empty_list2)
                
            if empty_list3=='':
                onlychech3=0
                #@print 'empty list for blank myempty_list2::'+str(myempty_list3) 
            else:
                myempty_list3.append(empty_list3)    
            if empty_list4=='':
                onlychech4=0 
                #print 'empty list for blank myempty_list2::'+str(myempty_list4)
            else:
                myempty_list4.append(empty_list4)
            if empty_list5=='':
                onlychech5=0 
                #@print 'empty list for blank myempty_list2::'+str(myempty_list5)
            else:
                myempty_list5.append(empty_list5)    
            if empty_list6=='':
                onlycheck6=0 
                #@print 'empty list for blank myempty_list2::'+str(myempty_list6)
            else:
                myempty_list6.append(empty_list6)    
            if empty_list7=='':
                onlycheck7=0
                #@print 'empty_list for blank ::'+str(myempty_list7)
            else:
                myempty_list7.append(empty_list7)
                #empty_list.append(empty_list1)
                #myempty_list2.append(empty_list2)
#                myempty_list3.append(empty_list3)
#                myempty_list4.append(empty_list4)
#                myempty_list5.append(empty_list5)
#                myempty_list6.append(empty_list6)
#                myempty_list7.append(empty_list7)   
        ##print 'empty_list:'+str(empty_list)
        if len(empty_list)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min1=str(a)  
        else:      
            min1=min(empty_list) 
        if len(myempty_list2)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min2=str(a)
        else:    
            min2=min(myempty_list2)
        if len(myempty_list3)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min3=str(a)
        else:    
            min3=min(myempty_list3)
        if len(myempty_list4)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min4=str(a)  
        else:      
            min4=min(myempty_list4)
        if len(myempty_list5)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min5=str(a)
        else:    
            min5=min(myempty_list5)
        if len(myempty_list6)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min6=str(a) 
        else:       
            min6=min(myempty_list6)
        if len(myempty_list7)==0:
            a=datetime.date.today()
            ##print 'a:'+str(a)
            min7=str(a)   
        else:     
            min7=min(myempty_list7)   
        #print  'min:=='+str(min(empty_list))    
        #b='2013-01-01'
        b=min1
        b2=min2
        b3=min3
        b4=min4
        b5=min5
        b6=min6
        b7=min7
        ##print 'b:'+str(b)
        ##print 'b2:'+str(b2)
        ##print 'b3:'+str(b3)
        ##print 'b4:'+str(b4)
        ##print 'b5:'+str(b5)
        ##print 'b6:'+str(b6)
        ##print 'b7:'+str(b7)
        ##print 'a:'+str(a)
        a=str(a)
        if b>a:
            ##print 'b>a'
            ##print 'b:'+str(b)
            ##print 'a:'+str(a)
            b=a
        if b2>a:
            ##print 'b2>a'
            ##print 'b2:'+str(b2)
            ##print 'a:'+str(a)
            b2=a
        if b3>a:
            ##print 'b3>a'
            ##print 'b3:'+str(b3)
            ##print 'a:'+str(a)
            b3=a 
        if b4>a:
            ##print 'b4>a'
            ##print 'b4:'+str(b4)
            ##print 'a:'+str(a)
            b4=a
        if b5>a:
            ##print 'b5>a'
            ##print 'b5:'+str(b5)
            ##print 'a:'+str(a)
            b5=a
        if b6>a:
            ##print 'b6>a'
            ##print 'b6:'+str(b6)
            ##print 'a:'+str(a)
            b6=a
        if b7>a:
            ##print 'b7>a'
            ##print 'b7:'+str(b7)
            ##print 'a:'+str(a)
            b7=a                       
        s=b.split('-')
        s2=b2.split('-')
        s3=b3.split('-')
        s4=b4.split('-')
        s5=b5.split('-')
        s6=b6.split('-')
        s7=b7.split('-')
        
        tillyear=s[0]
        tillmonth=s[1]
        tillday=s[2]
        tillyear2=s2[0]
        tillmonth2=s2[1]
        tillday2=s2[2]
        tillyear3=s3[0]
        tillmonth3=s3[1]
        tillday3=s3[2]
        tillyear4=s4[0]
        tillmonth4=s4[1]
        tillday4=s4[2]
        tillyear5=s5[0]
        tillmonth5=s5[1]
        tillday5=s5[2]
        tillyear6=s6[0]
        tillmonth6=s6[1]
        tillday6=s6[2]
        tillyear7=s7[0]
        tillmonth7=s7[1]
        tillday7=s7[2]
        
        ##print 'a:---'+str(a)
        ##print 'b:'+str(b)
        d1=date(int(current_year),current_month,current_day)
        d2=date(int(tillyear),int(tillmonth),int(tillday))
        d22=date(int(tillyear2),int(tillmonth2),int(tillday2))
        d3=date(int(tillyear3),int(tillmonth3),int(tillday3))
        d4=date(int(tillyear4),int(tillmonth4),int(tillday4))
        d5=date(int(tillyear5),int(tillmonth5),int(tillday5))
        d6=date(int(tillyear6),int(tillmonth6),int(tillday6))
        d7=date(int(tillyear7),int(tillmonth7),int(tillday7))
        days_left=(d1-d2).days
        days_left=abs(days_left)
        days_left=int(days_left)+1
        ##print 'days:---'+str(days_left)
        days_left2=(d1-d22).days
        days_left2=int(days_left2)+1
        ##print 'days2:---'+str(days_left2)
        days_left3=(d1-d3).days
        days_left3=abs(days_left3)
        days_left3=int(days_left3)+1
        ##print 'days3:---'+str(days_left3)
        days_left4=(d1-d4).days
        days_left4=abs(days_left4)
        days_left4=int(days_left4)+1
        ##print 'days4:---'+str(days_left4)
        days_left5=(d1-d5).days
        days_left5=abs(days_left5)
        days_left5=int(days_left5)+1
        ##print 'days5:---'+str(days_left5)
        days_left6=(d1-d6).days
        days_left6=abs(days_left6)
        days_left6=int(days_left6)+1
        ##print 'days6:---'+str(days_left6)
        days_left7=(d1-d7).days
        days_left7=abs(days_left7)
        days_left7=int(days_left7)+1
        ##print 'days7:---'+str(days_left7)

        datee = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        ##print 'datee--'+str(datee)
        datee2 = datetime.datetime(int(tillyear2),int(tillmonth2),int(tillday2),00,00,00)
        ##print 'datee2--'+str(datee2)
        datee3 = datetime.datetime(int(tillyear3),int(tillmonth3),int(tillday3),00,00,00)
        ##print 'datee3--'+str(datee3)
        datee4 = datetime.datetime(int(tillyear4),int(tillmonth4),int(tillday4),00,00,00)
        ##print 'datee4--'+str(datee4)
        datee5 = datetime.datetime(int(tillyear5),int(tillmonth5),int(tillday5),00,00,00)
        ##print 'datee5--'+str(datee5)
        datee6 = datetime.datetime(int(tillyear6),int(tillmonth6),int(tillday6),00,00,00)
        ##print 'datee--6'+str(datee6)
        datee7 = datetime.datetime(int(tillyear7),int(tillmonth7),int(tillday7),00,00,00)
        ##print 'datee7--'+str(datee7)
        
        for itemx in range(days_left):
            #print 'abc'
            ABC=CV_CV.objects.filter(cv_date_sendtoaspiration=b)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares = sumsquares + entrylength
            #print 'sumsquares:'+str(sumsquares)
            datee += datetime.timedelta(days=1)
            #print(datee)
            b=datee.strftime('%Y-%m-%d')
            #print 'new d--'+str(b)
            #print 'itemx---'+str(itemx)
        print 'sumsquares++++++'+str(sumsquares)     
        ###############
        for itemx2 in range(days_left2):
            #print 'abc2'
            ABC=CV_CV.objects.filter(cv_datereceived=b2)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares2 = sumsquares2 + entrylength
            #print 'sumsquares2:'+str(sumsquares2)
            datee2 += datetime.timedelta(days=1)
            #print(datee2)
            b2=datee2.strftime('%Y-%m-%d')
            #print 'new d--'+str(b2)
            #print 'itemx2---'+str(itemx2)
        print 'sumsquares2++++++'+str(sumsquares2)     
        ###############
        for itemx3 in range(days_left3):
            #print 'abc3'
            ABC=CV_CV.objects.filter(cv_date_expectedfromaspiration=b3)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares3 = sumsquares3 + entrylength
            #print 'sumsquares3:'+str(sumsquares3)
            datee3 += datetime.timedelta(days=1)
            #print(datee3)
            b3=datee3.strftime('%Y-%m-%d')
            #print 'new d--'+str(b3)
            #print 'itemx3---'+str(itemx3)
        print 'sumsquares3++++++'+str(sumsquares3)     
        ###############
        for itemx4 in range(days_left4):
            #print 'abc4'
            ABC=CV_CV.objects.filter(cv_date_recivedfromaspiration=b4)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares4 = sumsquares4 + entrylength
            #print 'sumsquares4:'+str(sumsquares4)
            datee4 += datetime.timedelta(days=1)
            #print(datee4)
            b4=datee4.strftime('%Y-%m-%d')
            #print 'new d--'+str(b4)
            #print 'itemx4---'+str(itemx4)
        print 'sumsquares4++++++'+str(sumsquares4)     
        ###############
        for itemx5 in range(days_left5):
            #print 'abc5'
            ABC=CV_CV.objects.filter(cv_date_validationcompleted=b5)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares5 = sumsquares5 + entrylength
            #print 'sumsquares5:'+str(sumsquares5)
            datee5 += datetime.timedelta(days=1)
            #print(datee5)
            b5=datee5.strftime('%Y-%m-%d')
            #print 'new d--'+str(b5)
            #print 'itemx5---'+str(itemx5)
        print 'sumsquares5++++++'+str(sumsquares5)     
        ###############
        for itemx6 in range(days_left6):
            #print 'abc6'
            ABC=CV_CV.objects.filter(cv_date_cvloadedintest=b6)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares6 = sumsquares6 + entrylength
            #print 'sumsquares6:'+str(sumsquares6)
            datee6 += datetime.timedelta(days=1)
            #print(datee6)
            b6=datee6.strftime('%Y-%m-%d')
            #print 'new d--'+str(b6)
            #print 'itemx6---'+str(itemx6)
        print 'sumsquares6++++++'+str(sumsquares6)     
        ###############
        for itemx7 in range(days_left7):
            #print 'abc7'
            ABC=CV_CV.objects.filter(cv_date_cvloadedinproduction=b7)
            entrylength=len(ABC)
            #print 'len(abc);;;;'+str(len(ABC))
            sumsquares7 = sumsquares7 + entrylength
            #print 'sumsquares7:'+str(sumsquares7)
            datee7 += datetime.timedelta(days=1)
            #print(datee7)
            b7=datee7.strftime('%Y-%m-%d')
            #print 'new d--'+str(b7)
            #print 'itemx7---'+str(itemx7)
        print 'sumsquares7++++++'+str(sumsquares7)     
        
        abc11=CV_VEIFYWITHDENOGFILE.objects.filter(demogfileoption='Yes')
        for i in abc11:
            demogfile_id=i.demogfile_id
        demogfile_id=str(demogfile_id)    
        ABC=CV_CV.objects.filter(verify_demog=demogfile_id)
        demoglength_yes=len(ABC)
        ##print 'demoglength_yes:'+str(demoglength_yes)
        
        abc11=CV_VEIFYWITHDENOGFILE.objects.filter(demogfileoption='No')
        for i in abc11:
            demogfile_id=i.demogfile_id
        demogfile_id=str(demogfile_id)
        ABC=CV_CV.objects.filter(verify_demog=demogfile_id)
        demoglength_no=len(ABC)
        ##print 'demoglength_yes:'+str(demoglength_no)
        abcnew1=CV_CV.objects.all()
        abcnew1length=len(abcnew1)
        ##print 'abcnew1length:'+str(abcnew1length)
	ABC1cv_daterecieved_test=CV_CV.objects.exclude(Q(cv_datereceived=''))
        ###############
        myobject12='h'
        allmyobject12='h'
        myobject12_len='h'
        allmyobject12_len='h'
        download12='h'
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            ##print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                if len(ABC1cv_daterecieved_test)==0:
                    ##print 'ABC1cv_daterecieved_test len is zero'
                    return render_to_response('CV_basic_form.html',{'myobject12_len':myobject12_len,'abcnew1length':abcnew1length,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
    
                return render_to_response('CV_basic_form.html',{'myobject12':myobject12,'abcnew1length':abcnew1length,'ABC1cv_daterecieved_test':ABC1cv_daterecieved_test,'download12':download12,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
        if len(ABC1cv_daterecieved_test)==0:
                    ##print 'ABC1cv_daterecieved_test len is zero'
                    return render_to_response('CV_basic_form.html',{'allmyobject12_len':allmyobject12_len,'abcnew1length':abcnew1length,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
 
        return render_to_response('CV_basic_form.html',{'allmyobject12':allmyobject12,'abcnew1length':abcnew1length,'ABC1cv_daterecieved_test':ABC1cv_daterecieved_test,'download12':download12,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
 
                   
def CV_Calculatecvcount_detail(request):
    ##print 'calculate count of cv'
    newsession1=request.session['username']
    print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    #############
    myobject13=CV_CalculateCvcountform()
    allmyobject13=CV_CalculateCvcountform()
    new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.username 
        xemail_id=str(xemail_id)
        ##print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            return render_to_response('CV_basic_form.html',{'myobject13':myobject13,'extra_object':extra_object},RequestContext(request))        
    return render_to_response('CV_basic_form.html',{'allmyobject13':allmyobject13,'extra_object':extra_object},RequestContext(request))        
            
         
def CV_Calculatecvcount_Display(request):##do changes here
    newsession1=request.session['username']
    ##print newsession1
    extra_object=CV_SIGNUP.objects.filter(username=newsession1)
    testposition=CV_POSITION.objects.filter(emp_position='Admin')
    for k in testposition:
        emp_position_id=k.emp_position_id
    ##print 'emp_position_id:'+str(emp_position_id)
    #############
    if 'submit' in request.POST:
        ##print "inside login"
        myrequestpost=request.POST.copy()
        fromdate_year=myrequestpost['fromdate_year']
        fromdate_month=myrequestpost['fromdate_month']
        fromdate_day=myrequestpost['fromdate_day']
        
        todate_year=myrequestpost['todate_year']
        todate_month=myrequestpost['todate_month']
        todate_day=myrequestpost['todate_day']
        cv_uid=myrequestpost['cv_uid']
        ##print 'fromdate_year:'+str(fromdate_year),'fromdate_month:'+str(fromdate_month),'fromdate_day:'+str(fromdate_day)
        ##print 'todate_year:'+str(todate_year),'todate_month:'+str(todate_month),'todate_day:'+str(todate_day)
        ##print 'cv_uid:'+str(cv_uid)
        
        #####
        #############
        a=datetime.date.today()
        sumsquares=0
        sumsquares2=0
        sumsquares3=0
        sumsquares4=0
        sumsquares5=0
        sumsquares6=0
        sumsquares7=0
        ##print 'a:---'+str(a)
        
        d1=date(int(fromdate_year),int(fromdate_month),int(fromdate_day))
        d2=date(int(todate_year),int(todate_month),int(todate_day))
        days_left=(d1-d2).days
        days_left=abs(days_left)
        days_left=int(days_left)+1
        days_left=days_left
        days_left2=days_left
        days_left3=days_left
        days_left4=days_left
        days_left5=days_left
        days_left6=days_left
        days_left7=days_left
        ##print 'days:---'+str(days_left)
        #empty_list.append(empty_list1)
        d1=str(d1)
        d2=str(d2)
        empty_list=[d1,d2]
        b=min(empty_list)
        b2=min(empty_list)
        b3=min(empty_list)
        b4=min(empty_list)
        b5=min(empty_list)
        b6=min(empty_list)
        b7=min(empty_list)
        ##print 'b:'+str(b)
        s=b.split('-')
        tillyear=s[0]
        tillmonth=s[1]
        tillday=s[2]
        
        datee = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        datee2 = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        datee3 = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        datee4 = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        datee5 = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        datee6 = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        datee7 = datetime.datetime(int(tillyear),int(tillmonth),int(tillday),00,00,00)
        ##print 'datee--'+str(datee) 
        universityfindname1=CV_UNIVERSITY.objects.filter(normal_id=cv_uid)  #      
        for unitem1nb in universityfindname1:
            uname=unitem1nb.uname       
        for itemx in range(days_left):
            ##print 'abc'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_date_sendtoaspiration=b)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_date_sendtoaspiration=b,cv_uid=cv_uid)
            #ABC=CV_CV.objects.filter(cv_date_sendtoaspiration=b,cv_uid=cv_uid)
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares = sumsquares + entrylength
            ##print 'sumsquares:'+str(sumsquares)
            datee += datetime.timedelta(days=1)
            ##print(datee)
            b=datee.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b)
            ##print 'itemx---'+str(itemx)
        print 'sumsquares++++++'+str(sumsquares)     
        ###############
        dateemptylist=[]
        for itemx2 in range(days_left2):
            ##print 'abc2'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_datereceived=b2)#,cv_uid=cv_uid)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_datereceived=b2,cv_uid=cv_uid)
            #ABC=CV_CV.objects.filter(cv_datereceived=b2,cv_uid=cv_uid)
            #test###
            cv_daterecieved_test=ABC###test
            if len(cv_daterecieved_test)>0:
                ##print 'length greater then 0'
                dateemptylist.append(cv_daterecieved_test)
                
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares2 = sumsquares2 + entrylength
            ##print 'sumsquares2:'+str(sumsquares2)
            datee2 += datetime.timedelta(days=1)
            ##print(datee2)
            b2=datee2.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b2)
            ##print 'itemx2---'+str(itemx2)
        print 'sumsquares2++++++'+str(sumsquares2) 
        ##print 'dateemptylist:'+str(dateemptylist)    
        ###############
        for itemx3 in range(days_left3):
            ##print 'abc3'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_date_expectedfromaspiration=b3)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_date_expectedfromaspiration=b3,cv_uid=cv_uid)
            #ABC=CV_CV.objects.filter(cv_date_expectedfromaspiration=b3,cv_uid=cv_uid)
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares3 = sumsquares3 + entrylength
            ##print 'sumsquares3:'+str(sumsquares3)
            datee3 += datetime.timedelta(days=1)
            ##print(datee3)
            b3=datee3.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b3)
            ##print 'itemx3---'+str(itemx3)
        print 'sumsquares3++++++'+str(sumsquares3)     
        ###############
        for itemx4 in range(days_left4):
            ##print 'abc4'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_date_recivedfromaspiration=b4)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_date_recivedfromaspiration=b4,cv_uid=cv_uid)
            
            #ABC=CV_CV.objects.filter(cv_date_recivedfromaspiration=b4,cv_uid=cv_uid)
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares4 = sumsquares4 + entrylength
            ##print 'sumsquares4:'+str(sumsquares4)
            datee4 += datetime.timedelta(days=1)
            ##print(datee4)
            b4=datee4.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b4)
            ##print 'itemx4---'+str(itemx4)
        print 'sumsquares4++++++'+str(sumsquares4)     
        ###############
        for itemx5 in range(days_left5):
            ##print 'abc5'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_date_validationcompleted=b5)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_date_validationcompleted=b5,cv_uid=cv_uid)
            
            #ABC=CV_CV.objects.filter(cv_date_validationcompleted=b5,cv_uid=cv_uid)
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares5 = sumsquares5 + entrylength
            ##print 'sumsquares5:'+str(sumsquares5)
            datee5 += datetime.timedelta(days=1)
            ##print(datee5)
            b5=datee5.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b5)
            ##print 'itemx5---'+str(itemx5)
        print 'sumsquares5++++++'+str(sumsquares5)     
        ###############
        for itemx6 in range(days_left6):
            ##print 'abc6'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_date_cvloadedintest=b6)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_date_cvloadedintest=b6,cv_uid=cv_uid)
            #ABC=CV_CV.objects.filter(cv_date_cvloadedintest=b6,cv_uid=cv_uid)
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares6 = sumsquares6 + entrylength
            ##print 'sumsquares6:'+str(sumsquares6)
            datee6 += datetime.timedelta(days=1)
            ##print(datee6)
            b6=datee6.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b6)
            ##print 'itemx6---'+str(itemx6)
        print 'sumsquares6++++++'+str(sumsquares6)     
        ###############
        for itemx7 in range(days_left7):
            ##print 'abc7'
            if uname=='All':
                ##print 'uname is all'
                ABC=CV_CV.objects.filter(cv_date_cvloadedinproduction=b7)
            else:
                ##print 'some university but not all'
                ABC=CV_CV.objects.filter(cv_date_cvloadedinproduction=b7,cv_uid=cv_uid)
            #ABC=CV_CV.objects.filter(cv_date_cvloadedinproduction=b7,cv_uid=cv_uid)
            entrylength=len(ABC)
            ##print 'len(abc);;;;'+str(len(ABC))
            sumsquares7 = sumsquares7 + entrylength
            ##print 'sumsquares7:'+str(sumsquares7)
            datee7 += datetime.timedelta(days=1)
            ##print(datee7)
            b7=datee7.strftime('%Y-%m-%d')
            ##print 'new d--'+str(b7)
            ##print 'itemx7---'+str(itemx7)
        print 'sumsquares7++++++'+str(sumsquares7)     
        
        abc11=CV_VEIFYWITHDENOGFILE.objects.filter(demogfileoption='Yes')
        for i in abc11:
            demogfile_id=i.demogfile_id
        demogfile_id=str(demogfile_id)    
        ABC=CV_CV.objects.filter(verify_demog=demogfile_id)
        demoglength_yes=len(ABC)
        ##print 'demoglength_yes:'+str(demoglength_yes)
        
        abc11=CV_VEIFYWITHDENOGFILE.objects.filter(demogfileoption='No')
        for i in abc11:
            demogfile_id=i.demogfile_id
        demogfile_id=str(demogfile_id)
        ABC=CV_CV.objects.filter(verify_demog=demogfile_id)
        demoglength_no=len(ABC)
        ##print 'demoglength_yes:'+str(demoglength_no)
        ABCnew1=CV_CV.objects.all()
        abcnew1length=len(ABCnew1)
        ###############
        myobject15='h'
        myobject15_len='h'
        allmyobject15='h'
        allmyobject15_len='h'
        new_object1111=CV_SIGNUP.objects.filter(emp_position=emp_position_id)
        for x in new_object1111:
            xemail_id=x.username 
            xemail_id=str(xemail_id)
            ##print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                if len(dateemptylist)==0:
                    ##print 'dateemptylist len 0'
                    return render_to_response('CV_basic_form.html',{'myobject15_len':myobject15_len,'abcnew1length':abcnew1length,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
      
                return render_to_response('CV_basic_form.html',{'myobject15':myobject15,'abcnew1length':abcnew1length,'dateemptylist':dateemptylist,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
        if len(dateemptylist)==0:
                    ##print 'dateemptylist len 0'
                    return render_to_response('CV_basic_form.html',{'allmyobject15_len':allmyobject15_len,'abcnew1length':abcnew1length,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
       
        return render_to_response('CV_basic_form.html',{'allmyobject15':allmyobject15,'abcnew1length':abcnew1length,'dateemptylist':dateemptylist,'sumsquares':sumsquares,'sumsquares2':sumsquares2,'sumsquares3':sumsquares3,'sumsquares4':sumsquares4,'sumsquares5':sumsquares5,'sumsquares6':sumsquares6,'sumsquares7':sumsquares7,'demoglength_yes':demoglength_yes,'demoglength_no':demoglength_no,'extra_object':extra_object},RequestContext(request))
 
        
        






##################################code of cvtracking ends here ######################
###to raise error ####
def server_error(request):
   template = loader.get_template('404.html')
   context = Context({
        'message': 'All: %s' % request,
        })
   return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

#####################################


def listof_leavessummary(request):
    print 'list of summary '
    #listsummary3209=LMS_LEAVES_summary_TABLE.objects.all()
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='summaryleaves'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1) 
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)  
                    
                    a=datetime.date.today()
                    listsummary3209=LMS_LEAVES_summary_TABLE.objects.all()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            print 'xemail_id:'+str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'listsummary3209':listsummary3209,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='summaryleaves'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='summaryleaves'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1

    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='Hr')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    a=datetime.date.today()
    listsummary3209=LMS_LEAVES_summary_TABLE.objects.all()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            print 'holiday form of hrrrrrrrrrr'
            return render_to_response('basic_form.html',{'listsummary3209':listsummary3209,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))



###########forgot password form
def passwordrecovery(request):
    print 'forgot password'
    recoverypassword=Passwordrecoveryform()
    #return render_to_response('basic_form.html',{'recoverypassword':recoverypassword,},RequestContext(request))
    return render_to_response('passwordrelated.html',{'recoverypassword':recoverypassword,},RequestContext(request))


def showrecovery(request):
    if request.method =='POST':
        print 'HERE I am'
        recoverypassword1=Passwordrecoveryform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/access_userbasic_detail1/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        print 'forgot password'
        if recoverypassword1.is_valid():
            print 'i m insiderrrrrrrrrrrrrrrr'
            username=recoverypassword1.cleaned_data['username']
            #recoverypassword1.save()
            username=str(username)
            object_password=LMS_SIGNUP.objects.filter(username=username)
            print 'object_password:'+str(object_password)
            print 'match'
            for i in object_password:
               sendingpassword =i.password
               #summary_id=i.summary_id
            sendingpassword=str(sendingpassword)  
            from_email='victory.nisha@gmail.com' ###change it to team lead id
            passwd='nishadwivedinishadwivedi'
            subject='Password Recovery'
            message='Your Password :'+str(sendingpassword)
            connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
            connection.open()
            email1 = mail.EmailMessage(subject,message,from_email, [username], connection=connection)
            email1.send()
                                
            print 'i m here'   
            print 'sendddddddddd'
            connection.close()
            print "why"
            return HttpResponseRedirect('/showrecovery/')
        print "ggoooooooooooooo"
        return render_to_response('passwordrelated.html',{'recoverypassword1':recoverypassword1},
                                  RequestContext(request))
    else:
        passwordrecovery3 = 'mail send'# for fetching all data from database
        
        return render_to_response('passwordrelated.html',{'passwordrecovery3':passwordrecovery3},
                                  RequestContext(request))


###############
#######change password####
def changepassword(request):
    print 'forgot password'
    changepassword_obj=ChangePasswordform()
    return render_to_response('passwordrelated.html',{'changepassword_obj':changepassword_obj,},RequestContext(request))

def Showpasswordchange(request):
    if request.method =='POST':
        print 'HERE I am'
        changepassword1=ChangePasswordform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/access_userbasic_detail1/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        print 'changepassword1'
        if changepassword1.is_valid():
            print 'i m insiderrrrrrrrrrrrrrrr'
            username = changepassword1.cleaned_data['username']
            oldpassword = changepassword1.cleaned_data['oldpassword']
            newpassword = changepassword1.cleaned_data['newpassword']
            confirmpassword = changepassword1.cleaned_data['confirmpassword']
            #recoverypassword1.save()
            username=str(username)
            oldpassword=str(oldpassword)
            newpassword=str(newpassword)
            confirmpassword=str(confirmpassword)
            object_passwordchange=LMS_SIGNUP.objects.filter(username=username,password=oldpassword)
            print 'object_passwordchange:'+str(object_passwordchange)
            print 'match'
            for i in object_passwordchange:
               signup_id =i.signup_id
            abc=LMS_SIGNUP.objects.get(pk=signup_id)
            print 'abc:'+str(abc)
            abc.password=newpassword
            abc.confirm_password=confirmpassword
            abc.save()
            #sendingpassword=str(sendingpassword)  
            from_email='victory.nisha@gmail.com' ###change it to team lead id
            passwd='nishadwivedinishadwivedi'
            subject='Password Recovery'
            message='Your New Password :'+str(newpassword)
            connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
            connection.open()
            email1 = mail.EmailMessage(subject,message,from_email, [username], connection=connection)
            email1.send()
                                
            print 'i m here'   
            print 'sendddddddddd'
            connection.close()
            print "why"
            return HttpResponseRedirect('/Showpasswordchange/')
        print "ggoooooooooooooo"
        return render_to_response('passwordrelated.html',{'changepassword1':changepassword1},
                                  RequestContext(request))
    else:
        passwordrecovery3 = 'mail send'# for fetching all data from database
        
        return render_to_response('passwordrelated.html',{'passwordrecovery3':passwordrecovery3},
                                  RequestContext(request))


###################

def fill_the_summaryformbyhr(request):
    print 'Summaryleavefillform'
    summaryobject=Summaryleavefillform()
    return render_to_response('basic_form.html',{'summaryobject':summaryobject,},RequestContext(request))
    
def setthesummaryleaves(request):
    if request.method =='POST':
        print 'HERE I am'
        summaryobject1=Summaryleavefillform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/setthesummaryleaves/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        print 'employeeform'
        if summaryobject1.is_valid():
            print 'i m insiderrrrrrrrrrrrrrrr'
            #emp_id_of_employee=summaryobject1.cleaned_data['leaves_type']
            emp_number_of_employee=summaryobject1.cleaned_data['leaves_type']
            eligiable_avaliable_leave=summaryobject1.cleaned_data['updated_date']
            casual_leaves_used=summaryobject1.cleaned_data['created_by']
            sick_leaves_used=summaryobject1.cleaned_data['created_date']
            leave_comp_off=summaryobject1.cleaned_data['updated_by']
            emp_number_of_employee=str(emp_number_of_employee)
            #emp_id_of_employee=str(emp_id_of_employee)
            summaryobject1.save()
            objectsummary_employee=LMS_EMPLOYEE_TABLE.objects.filter(emp_number=emp_number_of_employee)
            for lms in objectsummary_employee:
                emp_id =lms.emp_id
            emp_id_of_employee=str(emp_id)   
            print 'emp_id_of_employee:'+str(emp_id_of_employee)
            objectsummary=LMS_LEAVES_summary_TABLE.objects.filter(emp_id_of_employee=emp_id_of_employee)
            print 'match'
            for i in objectsummary:
               total_casual_leaves =i.total_casual_leaves
               summary_id=i.summary_id

            eligiable_avaliable_leave=float(eligiable_avaliable_leave)
            casual_leaves_used=float(casual_leaves_used)
            sick_leaves_used=float(sick_leaves_used)
            leave_comp_off=float(leave_comp_off)
            
            xyz=LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)
            print 'xyz:'+str(xyz) 
            xyz.eligiable_avaliable_leave=eligiable_avaliable_leave####new addition
            
            xyz.casual_leaves_used=casual_leaves_used       
            xyz.sick_leaves_used=sick_leaves_used
            xyz.leave_comp_off=leave_comp_off
            print xyz.name_of_employee
            xyz.save() 
         
            print "why"
            return HttpResponseRedirect('/setthesummaryleaves/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'summaryobject1':summaryobject1},
                                  RequestContext(request))
    else:
        summaryobject2 = LMS_LEAVES_summary_TABLE.objects.all()# for fetching all data from database
        
        return render_to_response('basic_form.html',{'summaryobject2':summaryobject2},
                                  RequestContext(request))

#for gender form#######


####leave apply form code
#def Leaveapplyforemployee(request,name):
def Leaveapplyforemployee(request): 
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='applyleave'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    for j in extra_object:
                        team=j.team
                        name=j.name_of_employee
                        team=str(team)
                        name=str(name)
                    new_object=LMS_TEAM.objects.filter(emp_team=team)
                    for i in new_object:
                        mh1=(i.mh1).strip()
                        mh2=(i.mh2).strip()
                        mh3=(i.mh3).strip()
                        mh1=str(mh1)
                        mh2=str(mh2)
                        mh3=str(mh3)
                    print 'mh1:'+str(mh1)
                    print 'mh2:'+str(mh2)
                    print 'mh3:'+str(mh3)   
                    print 'name:'+str(name)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id1=k.emp_position_id
                    print 'emp_position_id1:'+str(emp_position_id1)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)
                    a=datetime.date.today()
                    print 'newsession1'+str(newsession1)
                    my_obj1=Leaveapplyform()
                    my_obj1forhrr=Leaveapplyform()
                    name=name
                    la1 = LMS_HOLIDAY_LIST.objects.all()
                    empty_list=[]
                    for i in la1:
                        #for fetching only the date field of the database of the table
                        empty_list1=i.holiday_date
                        empty_list.append(str(empty_list1))
        
                        #        print i.holiday_date
                    print 'empty_list:'+str(empty_list)
                    #print 'hhhhhhhhhhhhhhhhhhhhhhh'+str(la1)
                    json_list = json.dumps(empty_list)
                    print json_list
		    for x in new_object1111:
        	        xemail_id=x.email_id####email id of hr 
    			xemail_id=str(xemail_id)
    			print 'xemail_id:'+str(xemail_id)
                    	if newsession1==xemail_id:
                            return render_to_response('basic_form.html',{'my_obj1forhrr':my_obj1forhrr,'a':a,'empty_list':empty_list,'json_list':json_list,'name':name,'extra_object':extra_object},RequestContext(request))

                    return render_to_response('basic_form.html',{'my_obj1':my_obj1,'a':a,'empty_list':empty_list,'json_list':json_list,'name':name,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='applyleave'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='applyleave'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
   
    ###################################################################################################
   
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1

    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id1=k.emp_position_id
    print 'emp_position_id1:'+str(emp_position_id1)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)
    for x in new_object1111:
        xemail_id=x.email_id 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    a=datetime.date.today()
    print 'newsession1'+str(newsession1)
    for j in extra_object:
        name=j.name_of_employee
        teamtocheck=j.team
        name=str(name)
    a=datetime.date.today()
    my_obj1=Leaveapplyform()
    my_obj1forhrr=Leaveapplyform()
    name=name
    print 'nisha'
    a=datetime.date.today()
    la1 = LMS_HOLIDAY_LIST.objects.all()
    empty_list=[]
    for i in la1:
        #for fetching only the date field of the database of the table
        empty_list1=i.holiday_date
        empty_list.append(str(empty_list1))
        
#        print i.holiday_date
        print 'empty_list:'+str(empty_list)
    #print 'hhhhhhhhhhhhhhhhhhhhhhh'+str(la1)
    json_list = json.dumps(empty_list)
    print json_list
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            return render_to_response('basic_form.html',{'my_obj1forhrr':my_obj1forhrr,'a':a,'empty_list':empty_list,'json_list':json_list,'name':name,'extra_object':extra_object},RequestContext(request))

    return render_to_response('basic_form.html',{'my_obj1':my_obj1,'a':a,'empty_list':empty_list,'json_list':json_list,'name':name,'extra_object':extra_object},RequestContext(request))

#def showleaveapplied(request, name):
def showleaveapplied(request): 
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='showleaveapplied'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    a=datetime.date.today()
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    detailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_email_id=newsession1)
                    for i in detailsnew_object:
                        emp_number=i.emp_number
                        emp_name=i.emp_name
                        emp_position=i.emp_position
                        emp_team=i.emp_team
                        name=str(emp_name)    
                        emp_team=str(emp_team)    
                        emp_position=str(emp_position)    
                    print 'emp_number:'+str(emp_number)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id####email id of hr 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)
                    a=datetime.date.today()
                    my_object=Employeeform()
                   
                    my_obj3=LMS_LEAVE_INFO_TABLE.objects.filter( Q(name=name),Q(emp_id_ofuser=newsession1),Q(leaves_approved_by=emp_team),Q(leaves_status='Active') | Q(leaves_status='Passive'))
                    for x in new_object1111:
        	        xemail_id=x.email_id####email id of hr 
    			xemail_id=str(xemail_id)
    			print 'xemail_id:'+str(xemail_id)
                    	if newsession1==xemail_id:
                            return render_to_response('noticeforall.html',{'my_obj3':my_obj3,'a':a,'name':name,'extra_object':extra_object},
                                  RequestContext(request))
                    return render_to_response('basic_form.html',{'my_obj3':my_obj3,'a':a,'name':name,'extra_object':extra_object},
                                  RequestContext(request))

##                    #my_obj3 = LMS_LEAVE_INFO_TABLE.objects.filter(name=name_id)# for fetching all data from database
##                    my_obj3=LMS_LEAVE_INFO_TABLE.objects.filter( Q(name=name_id),Q(leaves_approved_by=team),Q(leaves_status='Active') | Q(leaves_status='Passive'))
##                   
##                    return render_to_response('basic_form.html',{'my_obj3':my_obj3,'name_id':name_id,'a':a,'name':name,'extra_object':extra_object},
##                                  RequestContext(request))
##                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='showleaveapplied'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='showleaveapplied'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################

    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    detailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_email_id=newsession1)
    for i in detailsnew_object:
        emp_number=i.emp_number
        emp_name=i.emp_name
        emp_position=i.emp_position
        emp_team=i.emp_team
        name=str(emp_name)    
        emp_team=str(emp_team)    
        emp_position=str(emp_position)    
    print 'emp_number:'+str(emp_number)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    print 'emp_number:'+str(emp_number)
    supervisordetails= LMS_SUPERVISORHIERACHY.objects.filter(emp_number1=emp_number)
    print len(supervisordetails)
    if len(supervisordetails)==0:
        xsuperx='zero'
        xsuperxforhr='zeroforhr'
        for x in new_object1111:
            xemail_id=x.email_id####email id of hr 
    	    xemail_id=str(xemail_id)
    	    print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                return render_to_response('noticeforall.html',{'xsuperxforhr':xsuperxforhr,'extra_object':extra_object,},
                                                              RequestContext(request))
            
        return render_to_response('noticeforall.html',{'xsuperx':xsuperx,'extra_object':extra_object,},
                                                              RequestContext(request))
         
    for j in supervisordetails:
        supervisor_number1=j.supervisor_number1
    supervisor_number1=str(supervisor_number1)        
    supervisor_number1=supervisor_number1.split('-')
        #supervisor_number=supervisor_number[1]
    first_ofsupervisor=supervisor_number1[0]
    middle_ofsupervisor=supervisor_number1[1]
    last_ofsupervisor=supervisor_number1[2]
    print 'supervisor_number1:'+str(supervisor_number1)
    fetchemailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name=first_ofsupervisor) & Q(middle_name=middle_ofsupervisor) & Q(last_name=last_ofsupervisor))
    #fetchemailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_number=supervisor_number1) 
    for k in fetchemailsnew_object:
        emailid_of_supervisor=k.emp_email_id
    emailid_of_supervisor=str(emailid_of_supervisor)    
    print 'emailid_of_supervisor :'+str(emailid_of_supervisor)
 
    if request.method =='POST':
        print 'HERE I am:name====='
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['leaves_applied_reason']
        myrequestpost['leaves_applied_reason']=myrequestpost['leaves_applied_reason'].title()###this fuction is for converting the 1st letter of every word to capital
        print 'HERE I am'
        
        #my_obj2=Leaveapplyform(request.POST)
        my_obj2=Leaveapplyform(myrequestpost)
        ##########this code is for cancel of the form######
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/login/name='+str(name)+'/'
            strUrl = '/log2in/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ########################################################
        if my_obj2.is_valid():
            leaves_from=my_obj2.cleaned_data['leaves_from']
            leaves_to=my_obj2.cleaned_data['leaves_till']
            leaves_count=my_obj2.cleaned_data['actual_totalleavesdifference']
            type_of_leave=my_obj2.cleaned_data['leave_type_id']
            subject='Applying for %s leave from %s to %s'%(type_of_leave,leaves_from,leaves_to)
            message1=my_obj2.cleaned_data['leaves_applied_reason']
            from_email='victory.nisha@gmail.com'
            passwd='nishadwivedinishadwivedi'
            print 'passwd:'+passwd
            connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
            connection.open()
            my_obj2.save()
            print 'HHHHHHHHHHHHHHH<<<>>>>>JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ'
            print my_obj2.instance.pk
            leave_id=my_obj2.instance.pk
            print 'leave_id:'+str(leave_id)
            active_field=LMS_LEAVE_INFO_TABLE()         
            active_field.leaves_from=leaves_from        
            active_field.leaves_till=leaves_to       
            active_field.actual_totalleavesdifference=leaves_count
            active_field.leaves_applied_reason=message1           
            active_field.leaves_status='Active' 
            active_field.leaves_approved_by_manager=emp_position  ###for position of employee     
            active_field.leaves_approved_by=emp_team   #this entry on table is for showing the team of the person applying for leave     
            active_field.leave_type_id=type_of_leave                        
            active_field.name=name
            active_field.emp_id_ofuser=newsession1
            active_field.leaves_approved_by_HR=emailid_of_supervisor ######this email id of the supervisor of the employee
            active_field.save()
            
            ###################################################
            leave_id=leave_id+1
            print 'leave_id:++++++++++++++++++++++++++++++++++++'+str(leave_id)
            link1="http://ec2-174-129-147-22.compute-1.amazonaws.com:8000/accepttoshowpage/id="+str(leave_id)+'/' ####link to be send
            #link1="http://127.0.0.1:8000/signin/"
            #link1="http://accepttoshowpage/id="+str(leave_id)+'/' ####link to be send
            #reverse('foo-direct', kwargs={'page_slug': 'foo'})'/foo-direct/'
            #reverse('foo-direct', kwargs={'page_slug': 'foo'})'/foo-direct/'
            message='%s\n\nDetails:\nDate From :%s\nDate To :%s\nType Of Leave :%s\nTotal Days Leave Applied For :%s\nLink:%s'%(message1,leaves_from,leaves_to,type_of_leave,leaves_count,link1)
            if subject and message and from_email:
                try:
                    print ';inside try box'        
##                    [emailid_of_supervisor,xemail_id], copy and paste its combination of supervisor emailid and hr emailid
                    email1 = mail.EmailMessage(subject,message,from_email,[emailid_of_supervisor], connection=connection)
                    email1.send()
                    print 'mail send'
                    connection.close()      
                except BadHeaderError:
                    print '33333'
                    return HttpResponse('Invalid header found.')
                #strUrl = '/showleaveapplied/name='+str(name_id)
                strUrl = '/showleaveapplied/'
                print 'url:'+str(strUrl)
            #my_obj2.save()
            return HttpResponseRedirect(strUrl)
        print "ggoooooooooooooo"
        ##for hr#########
        for x in new_object1111:
            xemail_id=x.email_id####email id of hr 
            xemail_id=str(xemail_id)
            print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                #my_obj2forhrr='forhrapply leave'
                return render_to_response('noticeforall.html',{'my_obj2':my_obj2,'name':name,'extra_object':extra_object},
                                  RequestContext(request))
        ############
        return render_to_response('basic_form.html',{'my_obj2':my_obj2,'name':name,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        #my_obj3 = LMS_LEAVE_INFO_TABLE.objects.all()
        #my_obj3 = LMS_LEAVE_INFO_TABLE.objects.filter(name=name_id)# for fetching all data from database
        my_obj3=LMS_LEAVE_INFO_TABLE.objects.filter( Q(name=name),Q(emp_id_ofuser=newsession1),Q(leaves_approved_by=emp_team),Q(leaves_status='Active') | Q(leaves_status='Passive'))
        #my_obj3=my_obj3.filter(Q(leaves_status='Active')|Q(leaves_status='Passive')) 
	for x in new_object1111:
            xemail_id=x.email_id####email id of hr 
            xemail_id=str(xemail_id)
    	    print 'xemail_id:'+str(xemail_id)
            if newsession1==xemail_id:
                return render_to_response('noticeforall.html',{'my_obj3':my_obj3,'a':a,'name':name,'extra_object':extra_object},
                                  RequestContext(request))

        return render_to_response('basic_form.html',{'my_obj3':my_obj3,'a':a,'name':name,'extra_object':extra_object},
                                  RequestContext(request))


def accepttoshowpage(request,leave_id):
    #print 'name:'+str(name)
    print request.POST
    print 'leave_id:'+str(leave_id)
    leave_id=leave_id
    x=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    y=LMS_LEAVE_INFO_TABLE.objects.all()
    #return render_to_response('basic_form.html',{'x':x,'leave_id':leave_id},
     #                             RequestContext(request))
    return render_to_response('forloginpage.html',{'x':x,'leave_id':leave_id},
                                  RequestContext(request))
    
def leaveacceptorreject(request,leave_id):
    print request.POST
    leave_id=leave_id
    y=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    for y in y:
        name=y.name
        leaves_from=y.leaves_from
        leaves_till=y.leaves_till 
    Accept='accept'    
    showsign=Signinform()
    print 'nisha'
    if 'REJECT123' in request.POST:
        #print request.POST
        print 'reject BUTTON IS SELECTED'
        Reject='reject'
        decilineshowsign=Signinform()
        return render_to_response('basic_form.html',{'decilineshowsign':decilineshowsign,'leave_id':leave_id,'Reject':Reject},
                                  RequestContext(request)) 
    return render_to_response('basic_form.html',{'showsign':showsign,'leave_id':leave_id,'Accept':Accept},RequestContext(request))     
#    ###CODE FOR ACCEPT BUTTON
#    print 'code for accept'
#    if 'REJECT123' in request.POST:
#        #print request.POST
#        print 'reject BUTTON IS SELECTED'
#        reject='abc'
#        return render_to_response('basic_form.html',{'reject':reject,'leave_id':leave_id,'name':name,'leaves_from':leaves_from,'leaves_till':leaves_till},
#                                  RequestContext(request)) 
#    
#        
#    return render_to_response('basic_form.html',{'y':y,'leave_id':leave_id,'name':name,'leaves_from':leaves_from,'leaves_till':leaves_till},
#                                  RequestContext(request))   

#this is the copy of above function but for reject link in the notification link#############
def Rject_linkleaveacceptorreject(request,leave_id):
    print request.POST
    leave_id=leave_id
    y=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    for y in y:
        name=y.name
        leaves_from=y.leaves_from
        leaves_till=y.leaves_till 
    Accept='accept'    
    showsign=Signinform()
    print 'nisha'
    #if 'REJECT123' in request.POST:
        #print request.POST
    print 'reject BUTTON IS SELECTED'
    Reject='reject'
    decilineshowsign=Signinform()
    return render_to_response('basic_form.html',{'decilineshowsign':decilineshowsign,'leave_id':leave_id,'Reject':Reject},
                                  RequestContext(request)) 
    #return render_to_response('basic_form.html',{'showsign':showsign,'leave_id':leave_id,'Accept':Accept},RequestContext(request))     


#####################################################################################################
##################this code is for showinging the magic login page  after 3 seconds using lightbox########
def magicsignin(request,leave_id):
    print request.POST
    leave_id=leave_id
    y=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    for y in y:
        name=y.name
        leaves_from=y.leaves_from
        leaves_till=y.leaves_till 
    #Accept='accept'    
    magic3sec=Signinform()
    print 'nisha'
    
    
    return render_to_response('differentsigninform.html',{'magic3sec':magic3sec,'leave_id':leave_id,},
                                  RequestContext(request)) 
    #return render_to_response('basic_form.html',{'showsign':showsign,'leave_id':leave_id,'Accept':Accept},RequestContext(request))     

##############################################################################
##################################this code is matching datain database of lightbox#########################################################
def lmagicmatch(request,leave_id):
    # sign in to accept leave
    print request.POST
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id1=k.emp_position_id
    print 'emp_position_id1:'+str(emp_position_id1)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)
    for x in new_object1111:
        xemail_id=x.email_id 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    leave_id=leave_id
    x=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    for y in x:
        name=y.name
        leaves_from=y.leaves_from
        leaves_till=y.leaves_till
        emp_id_ofuser=y.emp_id_ofuser
    print 'emp_id_ofuser:'+str(emp_id_ofuser)
    emp_id_ofuser=str(emp_id_ofuser) 
    nes=LMS_EMPLOYEE_TABLE.objects.filter(emp_email_id=emp_id_ofuser) 
    for nes in nes:
        emp_number=nes.emp_number
    emp_number=str(emp_number)
    print 'emp_number:'+str(emp_number)
    
    supervisordetails= LMS_SUPERVISORHIERACHY.objects.filter(emp_number1=emp_number) 
    for j in supervisordetails:
        supervisor_number1=j.supervisor_number1
    supervisor_number1=str(supervisor_number1)        
    supervisor_number1=supervisor_number1.split('-')
        
    first_ofsupervisor=supervisor_number1[0]
    middle_ofsupervisor=supervisor_number1[1]
    last_ofsupervisor=supervisor_number1[2]
    print 'supervisor_number1:'+str(supervisor_number1)
    fetchemailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name=first_ofsupervisor) & Q(middle_name=middle_ofsupervisor) & Q(last_name=last_ofsupervisor))
    #fetchemailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_number=supervisor_number1) 
    for k in fetchemailsnew_object:
        emailid_of_supervisor=k.emp_email_id
    emailid_of_supervisor=str(emailid_of_supervisor)    
    print 'emailid_of_supervisor :'+str(emailid_of_supervisor)
          
    if 'LOGIN' in request.POST:
        print "inside login"
        u_name=request.POST['username']
        u_pass=request.POST['password']
        print 'u_name:'+u_name,'u_pass:'+u_pass
        if u_name=='' and u_pass=='':
            print 'the username and password are empty'
            Esblank=Signinform()
            #return render_to_response('basic_form.html',{'sblank':sblank},RequestContext(request))
            return render_to_response('new_form1.html',{'Esblank':Esblank,'leave_id':leave_id},RequestContext(request))
#        
        try:
            print 'username:' 

            if LMS_SIGNUP.objects.get(username=u_name) and LMS_SIGNUP.objects.get(password=u_pass): 
                print "username and password matches to database"
                ##########this code is for session  #################
                request.session['username']=LMS_SIGNUP.objects.get(username=u_name).username
                print 'we are using session ie database session'
                print request.session['username']
                newsession1=request.session['username']
               # return HttpResponse("You're logged in.")
               ############################################
                print datetime.date.today()
                a=datetime.date.today()
                extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=u_name)
                extra_obj=extra_object
                for i in extra_object:
                    #for fetching only the date field of the database of the table
                    name=i.name_of_employee
                    
                    print'name'
                    print name
                testemail=u_name.split('@')
                e=testemail[0]
                e=str(e)
		print 'new_object1111:'
		print new_object1111
                if emailid_of_supervisor==newsession1:
                    #status=False
		    for item in new_object1111:
			xemail_id=str(item.email_id)
			if newsession1==xemail_id:
				#print 'status: '+str(status)
				#status=True
                    #print 'stsatus' +str(status)
                    #if status:
		#	return HttpResponseRedirect('')
                            return render_to_response('noticeforall.html',{'x':x,'u_name':u_name,'u_pass':u_pass,'e':e,'leave_id':leave_id,'name':name,'extra_object':extra_object,}, RequestContext(request))
                    #else:
	#		return HttpResponseRedirect('')
		    render_to_response('basic_form.html',{'x':x,'leave_id':leave_id,'name':name,'extra_object':extra_object,'u_name':u_name,'u_pass':u_pass,'e':e,}, RequestContext(request)) 
                invaliduser='invalid'
   
                invaliduserforhrr='for hrrrr'
		for x in new_object1111:
        	    xemail_id=x.email_id 
        	    xemail_id=str(xemail_id)
        	    print 'xemail_id:'+str(xemail_id)
                    if newsession1==xemail_id:
			print 'invalid hr'
                    	return render_to_response('basic_form.html',{'invaliduserforhrr':invaliduserforhrr,'extra_object':extra_object},RequestContext(request))
		print 'invalid user'
                return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                #return render_to_response('basic_form.html',{'y':y,'leave_id':leave_id,'name':name,'leaves_from':leaves_from,'leaves_till':leaves_till,'u_name':u_name,'u_pass':u_pass},
                                  #RequestContext(request)) 
               

                
        except:
            print "not in database" ###when password or username does not match database       
            #return HttpResponseRedirect('/access_userbasic_detail1/')
            Esblank=Signinform()
            return render_to_response('new_form1.html',{'Esblank':Esblank,'leave_id':leave_id},RequestContext(request))
       
        
    #if the submitt button selected  is forgot password
    if 'FORGOT' in request.POST:
        print request.POST
        print 'forgot password'    
    #######delete if doesnotwork----testing -------#####
    newsession1=request.session['username']
    print datetime.date.today()
    a=datetime.date.today()
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    for i in extra_object:
        name=i.name_of_employee
    print'name'
    print name
    #testemail=u_name.split('@')
    #e=testemail[0]
    #e=str(e)
    if emailid_of_supervisor==newsession1:
	for someitem in new_object1111:
	    xemail_id=str(someitem.email_id)
            if newsession1==xemail_id:
                return render_to_response('noticeforall.html',{'x':x,'leave_id':leave_id,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('basic_form.html',{'x':x,'leave_id':leave_id,'extra_object':extra_object,},
                                  RequestContext(request))
                
    invaliduser='invalid'
    invaliduserforhrr='for hrrrr'
    for someitem2 in new_object1111:
        xemail_id=str(someitem2.email_id)
    	if newsession1==xemail_id:
            return render_to_response('basic_form.html',{'invaliduserforhrr':invaliduserforhrr,'extra_object':extra_object},RequestContext(request))

    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
           




#########################################################################################
def databasematch(request,leave_id):
    # sign in to accept leave
    print request.POST
    print request.POST
    leave_id=leave_id
    y=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    for y in y:
        name=y.name
        leaves_from=y.leaves_from
        leaves_till=y.leaves_till
    if 'LOGIN' in request.POST:
        print "inside login"
        u_name=request.POST['username']
        u_pass=request.POST['password']
        print 'u_name:'+u_name,'u_pass:'+u_pass
        if u_name=='' and u_pass=='':
            print 'the username and password are empty'
            sblank='blank'
            return render_to_response('basic_form.html',{'sblank':sblank},RequestContext(request))
#        name1=LMS_SIGNUP.objects.get(username=u_name)
#        
#        print name1
#        print name1
        try:
            print 'username:' 
            #if LMS_SIGNIN.objects.get(username=username):
            if LMS_SIGNUP.objects.get(username=u_name) and LMS_SIGNUP.objects.get(password=u_pass): 
                print "username and password matches to database"
                print datetime.date.today()
                a=datetime.date.today()
                
                
                return render_to_response('basic_form.html',{'y':y,'leave_id':leave_id,'name':name,'leaves_from':leaves_from,'leaves_till':leaves_till,'u_name':u_name,'u_pass':u_pass},
                                  RequestContext(request)) 
               

                
        except:
            print "not in database" ###when password or username does not match database       
            #return HttpResponseRedirect('/access_userbasic_detail1/')
            Accept='accept'  
            showsign=Signinform()
            return render_to_response('basic_form.html',{'showsign':showsign,'leave_id':leave_id,'Accept':Accept},RequestContext(request))         
        
    #if the submitt button selected  is forgot password
    if 'FORGOT' in request.POST:
        print request.POST
        print 'forgot password'    
        
##########sign in to reject the leave
def zrejectsignin(request,leave_id):
   ##########sign in to reject the leave 
    print request.POST
    print request.POST
    leave_id=leave_id
    y=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)
    for y in y:
        name=y.name
        leaves_from=y.leaves_from
        leaves_till=y.leaves_till
    if 'LOGIN' in request.POST:
        print "inside login"
        u_name=request.POST['username']
        u_pass=request.POST['password']
        print 'u_name:'+u_name,'u_pass:'+u_pass
        if u_name=='' and u_pass=='':
            print 'the username and password are empty'
            sblank='blank'
            return render_to_response('basic_form.html',{'sblank':sblank},RequestContext(request))
#        name1=LMS_SIGNUP.objects.get(username=u_name)
#        
#        print name1
#        print name1
        try:
            print 'username:' 
            u_pass=u_pass#####password of the user
            u_name=u_name####emailid of user
            
            #if LMS_SIGNIN.objects.get(username=username):
            if LMS_SIGNUP.objects.get(username=u_name) and LMS_SIGNUP.objects.get(password=u_pass): 
                print "username and password matches to database"
                print datetime.date.today()
                a=datetime.date.today()
                
                
#    if 'REJECT123' in request.POST:
#        #print request.POST
#        print 'reject BUTTON IS SELECTED'
                reject='abc'
                return render_to_response('basic_form.html',

{'reject':reject,'leave_id':leave_id,'name':name,'leaves_from':leaves_from,'leaves_till':leaves_till,'u_name':u_name,'u_pass':u_pass},
                                  RequestContext(request)) 
    
        
               
                
        except:
            print "not in database" ###when password or username does not match database       
            #return HttpResponseRedirect('/access_userbasic_detail1/') 
            Reject='reject'
            decilineshowsign=Signinform()
            return render_to_response('basic_form.html',{'decilineshowsign':decilineshowsign,'leave_id':leave_id,'Reject':Reject},
                                  RequestContext(request))   
        
    #if the submitt button selected  is forgot password
    if 'FORGOT' in request.POST:
        print request.POST
        print 'forgot password'    
    
    


######get the email id from sign in form 
#def Rejectfinalmailsend(request,leave_id,e=None):
def Rejectfinalmailsend(request,leave_id):    
#def Rejectfinalmailsend(request,e=None):    
     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:    
        print 'username length less equal to zero which means user is logout.and session is deleted '
        my_object6=Signinform()
        print 'nisha'
        return render_to_response('new_form1.html',{'my_object6':my_object6},RequestContext(request))
    ###################################################################################################

    print 'hi'
    #leave_id='101'####delete this
    print request.POST
#    a=request.POST.keys()
#    b=a[0]
#    c=str(b)
#    d=c.split('=')
#    e=d[1]
#    f=d[3]
#    e=str(e)
#    f=str(f)
#    print 'a:'+str(a)
#    print 'b:'+str(b)
#    print 'c:'+str(c)
#    print 'd:'+str(d)
#    print 'e:'+str(e)
#    print 'f:'+str(f)
    print 'hi'
    print request.POST
    a=request.POST.keys()
    print 'this causes problem fix here--------------'
#    try:
#        print 'in the try box'
#        b=a[1]
#        c=str(b)
#        d=c.split('=')
#        e=d[1]
#        #f=d[3]
#        e=str(e)
#        #f=str(f)
#    except:
#        print 'in except' 
#        b=a[0]
#        c=str(b)
#        d=c.split('=')
#        e=d[1]
#        #f=d[3]
#        e=str(e)
#        #f=str(f)
#
#    print 'a:'+str(a)
#    print 'b:'+str(b)
#    print 'c:'+str(c)
#    print 'd:'+str(d)
#    print 'e:'+str(e)
#    e=str(e)+'@entigencesolutions.in'
#    print 'e:'+str(e)
    
    #print 'f:'+str(f)
    #for geting the name to set the go back login page ###
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)          
  ####work here for sending mail by team lead to employee
    print 'leave_id:'+str(leave_id)
    z=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)###########################
    print 'zzzzzzzzzzzzzzzzzzzzzz'
    for i in z:
        name=i.name
        actual_totalleavesdifference=i.actual_totalleavesdifference
        leave_type_id=i.leave_type_id
        emp_id_ofuser=i.emp_id_ofuser###emailid of person whose leave is being approved or rejected
        print 'name:'+str(name)
        print 'leave_type_id:'+str(leave_type_id)
        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
        print 'emp_id_ofuser:'+str(emp_id_ofuser)
    emp_id_ofuser=str(emp_id_ofuser)    
    z1=LMS_LEAVES_summary_TABLE.objects.filter(email_id=emp_id_ofuser)       
    for i in z1:
        emp_team=i.team
        email_id=i.email_id
        summary_id=i.summary_id
        total_casual_leaves=i.total_casual_leaves
        total_sick_leaves=i.total_sick_leaves
        eligiable_avaliable_leave=i.eligiable_avaliable_leave
        casual_leaves_used=i.casual_leaves_used
        sick_leaves_used=i.sick_leaves_used
        print 'summary_id:'+str(summary_id)
        print 'total_casual_leaves:'+str(total_casual_leaves)
        print 'total_sick_leaves:'+str(total_sick_leaves)
        print 'eligiable_avaliable_leave:'+str(eligiable_avaliable_leave)
        print 'casual_leaves_used:'+str(casual_leaves_used)
        print 'sick_leaves_used:'+str(sick_leaves_used) 
        print'emp_team:'+str(emp_team)
        print 'email_id:'+str(email_id)####emailid of employeee whose leave is to be approved or reject .
 
    emp_team=str(emp_team)
    email_id=str(email_id)
    from_email='victory.nisha@gmail.com' ###change it to team lead id
    passwd='nishadwivedinishadwivedi'
    print 'from_email:'+str(from_email)
    print 'passwd:'+str(passwd)
    subject='Leave Rejected'
    message='Leave Not Approved'
    connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
    connection.open()
    if subject and message and from_email:
                try:
                    print 'inside try box'
                    print'sening mail '
                    print 'from emaiL: '+str(from_email)
                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
                        #email1.send()
                        #this part is for updating the leave status part of leave table to passive.
                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                    print "this part is for updating the leave status part of leave table to passive."
                    x.leaves_status='Passive'
                    x.leaves_approved_by_tl='Leave Rejected'
                    x.save()
                        ########################################################
                    leave_type_id=str(leave_type_id)
                    print 'leave_type_id:'+str(leave_type_id)
                        
                        #email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser,xemail_id], connection=connection)
                    email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                    email1.send()
                                
                    print 'i m here'   
                    print 'sendddddddddd'
                    connection.close()
#                    if emp_team=='Claret':
#                        print'sening mail for Claret'
#                        #send_mail(subject, message, from_email, ['sapudevidwivedi@gmail.com','sdwivedi@entigencesolutions.in'],)
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Rejected'
#                        x.save()
#                        ########################################################
#                        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                        leave_type_id=str(leave_type_id)
#                        print 'leave_type_id:'+str(leave_type_id)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()
#                        
#                                
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()  
#                    if emp_team=='Lyterati':
#                        print'sening mail for Lyterati'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Rejected'
#                        x.save()
#                        ########################################################
#                        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                        leave_type_id=str(leave_type_id)
#                        print 'leave_type_id:'+str(leave_type_id)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()
#                                
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
                        #send_mail(subject, message, from_email, ['sapudevidwivedi@gmail.com','sdwivedi@entigencesolutions.in'],)   
#                    if emp_team=='Adminstrative':
#                        print'sening mail for Adminstrative'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Rejected'
#                        x.save()
#                        ########################################################
#                        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                        leave_type_id=str(leave_type_id)
#                        print 'leave_type_id:'+str(leave_type_id)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()
#                                
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                    else:
#                        print 'no match'
                except BadHeaderError:
                    print '33333'
                    return HttpResponse('Invalid header found.')
    for x2ws in new_object1111:
        xemail_id=x2ws.email_id####email id of hr 
        xemail_id=str(xemail_id) 
        if newsession1==xemail_id:
            return render_to_response('noticeforall.html',{'z':z,'extra_object':extra_object},
                                  RequestContext(request))              
    return render_to_response('basic_form.html',{'z':z,'extra_object':extra_object},
                                  RequestContext(request)) 


def abcofcasual(request,leave_id):
    leave_id=leave_id
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    print 'leave_id:'+str(leave_id)
    
    z=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)###########################
    print 'zzzzzzzzzzzzzzzzzzzzzz'
    for i in z:
        name=i.name
        actual_totalleavesdifference=i.actual_totalleavesdifference
        leave_type_id=i.leave_type_id
        emp_id_ofuser=i.emp_id_ofuser###emailid of person whose leave is being approved or rejected
        print 'name:'+str(name)
        print 'leave_type_id:'+str(leave_type_id)
        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
        print 'emp_id_ofuser:'+str(emp_id_ofuser)
    emp_id_ofuser=str(emp_id_ofuser)    
    z1=LMS_LEAVES_summary_TABLE.objects.filter(email_id=emp_id_ofuser)       
    for i in z1:
        emp_team=i.team
        email_id=i.email_id
        summary_id=i.summary_id
        total_casual_leaves=i.total_casual_leaves
        total_sick_leaves=i.total_sick_leaves
        eligiable_avaliable_leave=i.eligiable_avaliable_leave
        casual_leaves_used=i.casual_leaves_used
        sick_leaves_used=i.sick_leaves_used
        print 'summary_id:'+str(summary_id)
        print 'total_casual_leaves:'+str(total_casual_leaves)
        print 'total_sick_leaves:'+str(total_sick_leaves)
        print 'eligiable_avaliable_leave:'+str(eligiable_avaliable_leave)
        print 'casual_leaves_used:'+str(casual_leaves_used)
        print 'sick_leaves_used:'+str(sick_leaves_used) 
        print'emp_team:'+str(emp_team)
        print 'email_id:'+str(email_id)####emailid of employeee whose leave is to be approved or reject .
    from_email='victory.nisha@gmail.com' ###change it to team lead id
    passwd='nishadwivedinishadwivedi'
    subject='Approve'
    message='Leave Approved'
    connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
    connection.open()
    if subject and message and from_email: 
        if 'reject33' in request.POST:
            print 'reject side of the form .clicked reject'
            subject='Leave Rejected'
            message='Leave Not Approved'
            try:
                print 'inside try box'
                print'sening mail for rejecting the leaves as insuffient leaves::::::'
                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
                        #email1.send()
                        #this part is for updating the leave status part of leave table to passive.
                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                if leave_type_id=='CL':
                    print 'rejecting casual leave on insuffient leave'
                    print "this part is for updating the leave status part of leave table to passive."
                    x.leaves_status='Passive'
                    x.leaves_approved_by_tl='Not Sufficient Casual Leave'
                    x.save()
                    ########################################################
                    leave_type_id=str(leave_type_id)
                    print 'leave_type_id:'+str(leave_type_id)
                        
                    #email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser,xemail_id], connection=connection)
                    email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                    email1.send()
                                
                    print 'i m here'   
                    print 'sendddddddddd'
                    connection.close()
                if leave_type_id=='SL': 
                    print 'rejected sick  leave on insuffient leave'  
                    print 'siclleave'
                    print "this part is for updating the leave status part of leave table to passive."
                    x.leaves_status='Passive'
                    x.leaves_approved_by_tl='Not Sufficient Sick Leave'
                    x.save()
                            ########################################################
                    leave_type_id=str(leave_type_id)
                    print 'leave_type_id:'+str(leave_type_id)
                        
                            #email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser,xemail_id], connection=connection)
                    email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                    email1.send()
                                
                    print 'i m here'   
                    print 'sendddddddddd'
                    connection.close() 
                #change it to team name#####
#                if emp_team=='Claret':
#                        print'sening mail for etl for rejecting the leaves as insuffient leaves::::::'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        if leave_type_id=='CL':
#                            print 'rejecting casual leave on insuffient leave'
#                            print "this part is for updating the leave status part of leave table to passive."
#                            x.leaves_status='Passive'
#                            x.leaves_approved_by_tl='Not sufficient casual leave'
#                            x.save()
#                            ########################################################
#                            leave_type_id=str(leave_type_id)
#                            print 'leave_type_id:'+str(leave_type_id)
#                        
#                            #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                            email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                            email1.send()
#                                
#                            print 'i m here'   
#                            print 'sendddddddddd'
#                            connection.close()
#                        if leave_type_id=='SL': 
#                            print 'rejected sick  leave on insuffient leave'  
#                            print 'siclleave'
#                            print "this part is for updating the leave status part of leave table to passive."
#                            x.leaves_status='Passive'
#                            x.leaves_approved_by_tl='Not sufficient sick leave'
#                            x.save()
#                            ########################################################
#                            leave_type_id=str(leave_type_id)
#                            print 'leave_type_id:'+str(leave_type_id)
#                        
#                            #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                            email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                            email1.send()
#                                
#                            print 'i m here'   
#                            print 'sendddddddddd'
#                            connection.close()
#                ######################
                
#                if emp_team=='Lyterati':
#                        print'sening mail for etl for rejecting the leaves as insuffient leaves::::::'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        if leave_type_id=='CL':
#                            print 'rejecting casual leave on insuffient leave'
#                            print "this part is for updating the leave status part of leave table to passive."
#                            x.leaves_status='Passive'
#                            x.leaves_approved_by_tl='Not sufficient casual leave'
#                            x.save()
#                            ########################################################
#                            leave_type_id=str(leave_type_id)
#                            print 'leave_type_id:'+str(leave_type_id)
#                        
#                            #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                            email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                            email1.send()
#                                
#                            print 'i m here'   
#                            print 'sendddddddddd'
#                            connection.close()
#                        if leave_type_id=='SL': 
#                            print 'rejected sick  leave on insuffient leave'  
#                            print 'siclleave'
#                            print "this part is for updating the leave status part of leave table to passive."
#                            x.leaves_status='Passive'
#                            x.leaves_approved_by_tl='Not sufficient sick leave'
#                            x.save()
#                            ########################################################
#                            leave_type_id=str(leave_type_id)
#                            print 'leave_type_id:'+str(leave_type_id)
#                        
#                            #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                            email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                            email1.send()
#                                
#                            print 'i m here'   
#                            print 'sendddddddddd'
#                            connection.close()
#                ####################
#                
#                if emp_team=='Adminstrative':
#                        print'sening mail for etl for rejecting the leaves as insuffient leaves::::::'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        if leave_type_id=='CL':
#                            print 'rejecting casual leave on insuffient leave'
#                            print "this part is for updating the leave status part of leave table to passive."
#                            x.leaves_status='Passive'
#                            x.leaves_approved_by_tl='Not sufficient casual leave'
#                            x.save()
#                            ########################################################
#                            leave_type_id=str(leave_type_id)
#                            print 'leave_type_id:'+str(leave_type_id)
#                        
#                            #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                            email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                            email1.send()
#                                
#                            print 'i m here'   
#                            print 'sendddddddddd'
#                            connection.close()
#                        if leave_type_id=='SL': 
#                            print 'rejected sick  leave on insuffient leave'  
#                            print 'siclleave'
#                            print "this part is for updating the leave status part of leave table to passive."
#                            x.leaves_status='Passive'
#                            x.leaves_approved_by_tl='Not sufficient sick leave'
#                            x.save()
#                            ########################################################
#                            leave_type_id=str(leave_type_id)
#                            print 'leave_type_id:'+str(leave_type_id)
#                        
#                            #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                            email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                            email1.send()
#                                
#                            print 'i m here'   
#                            print 'sendddddddddd'
#                            connection.close()
#                ###################
#                
#                
                
                
                 
                else:
                    print 'no match'
            except BadHeaderError:
                    print '33333'
                    return HttpResponse('Invalid header found.')
        else: 
            print 'this is for allowing the leave on insuffient casual leave' 
            try:
                print 'inside try box'
                print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave or sick leave'
                print 'from emaiL: '+str(from_email)
                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
                    #email1.send()
                print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
                leave_type_id=str(leave_type_id)
                print 'leave_type_id:'+str(leave_type_id)
                if leave_type_id=='CL':
                    print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave '
                    print 'leaveid is cl' 
                    b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
                    c=float(casual_leaves_used)+float(actual_totalleavesdifference)
                    print 'b:'+str(b)
                    print 'c:'+str(c)
                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
                        #a.current_casual_leaves=b ####to update the value in database.#######
                    a.eligiable_avaliable_leave=b ####to update the value in database.#######
                    a.casual_leaves_used=c
                    a.save()
                        #this part is for updating the leave status part of leave table to passive.
                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                    print "this part is for updating the leave status part of leave table to passive."
                    x.leaves_status='Passive'
                    x.leaves_approved_by_tl='Leave Approved'
                    x.save()
                        ########################################################
                    print 'a:'+str(a)
                        #email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser,xemail_id], connection=connection)
                    email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                    email1.send()
                    print 'i m here'   
                    print 'sendddddddddd'
                    connection.close()
                   ####work here for sick leave and other team 
                if leave_type_id=='SL':
                    print'sening mail for etl but for casual leave approving inspite of not having suffienent sick leave'
                    print 'leaveid is sl' 
                        #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
                    b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
                    c=float(sick_leaves_used)+float(actual_totalleavesdifference)
                        #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
                    print 'b:'+str(b)
                    print 'c:'+str(c)
                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
                        #a.current_sick_leaves=b
                    a.eligiable_avaliable_leave=b 
                    a.sick_leaves_used=c
                    a.save()
                        #this part is for updating the leave status part of leave table to passive.
                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                    print "this part is for updating the leave status part of leave table to passive."
                    x.leaves_status='Passive'
                    x.leaves_approved_by_tl='Leave Approved'
                    x.save()
                        ########################################################
                    print 'a:'+str(a)
                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
                    email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                    email1.send()    
                    print 'i m here'   
                    print 'sendddddddddd'
                    connection.close()
                        
                 ######################################
#                if emp_team=='Claret':
#                    print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave or sick leave'
#                    print 'from emaiL: '+str(from_email)
#                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                    #email1.send()
#                    print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                    leave_type_id=str(leave_type_id)
#                    print 'leave_type_id:'+str(leave_type_id)
#                    if leave_type_id=='CL':
#                        print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave '
#                    
#                        print 'leaveid is cl' 
#                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                        c=float(casual_leaves_used)+float(actual_totalleavesdifference)
#                        print 'b:'+str(b)
#                        print 'c:'+str(c)
#                        a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
#                        #a.current_casual_leaves=b ####to update the value in database.#######
#                        a.eligiable_avaliable_leave=b ####to update the value in database.#######
#                        a.casual_leaves_used=c
#                        a.save()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Approved'
#                        x.save()
#                        ########################################################
#                        print 'a:'+str(a)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                   ####work here for sick leave and other team 
#                    if leave_type_id=='SL':
#                        print'sening mail for etl but for casual leave approving inspite of not having suffienent sick leave'
#                    
#                        print 'leaveid is sl' 
#                        #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
#                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                        c=float(sick_leaves_used)+float(actual_totalleavesdifference)
#                        #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
#                        print 'b:'+str(b)
#                        print 'c:'+str(c)
#                        a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
#                        #a.current_sick_leaves=b
#                        a.eligiable_avaliable_leave=b 
#                        a.sick_leaves_used=c
#                        a.save()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Approved'
#                        x.save()
#                        ########################################################
#                        print 'a:'+str(a)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()    
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                 #################################
##                 ############################
#                if emp_team=='Lyterati':
#                    print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave or sick leave'
#                    print 'from emaiL: '+str(from_email)
#                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                    #email1.send()
#                    print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                    leave_type_id=str(leave_type_id)
#                    print 'leave_type_id:'+str(leave_type_id)
#                    if leave_type_id=='CL':
#                        print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave '
#                    
#                        print 'leaveid is cl' 
#                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                        c=float(casual_leaves_used)+float(actual_totalleavesdifference)
#                        print 'b:'+str(b)
#                        print 'c:'+str(c)
#                        a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
#                        #a.current_casual_leaves=b ####to update the value in database.#######
#                        a.eligiable_avaliable_leave=b ####to update the value in database.#######
#                        a.casual_leaves_used=c
#                        a.save()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Approved'
#                        x.save()
#                        ########################################################
#                        print 'a:'+str(a)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                   ####work here for sick leave and other team 
#                    if leave_type_id=='SL':
#                        print'sening mail for etl but for casual leave approving inspite of not having suffienent sick leave'
#                    
#                        print 'leaveid is sl' 
#                        #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
#                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                        c=float(sick_leaves_used)+float(actual_totalleavesdifference)
#                        #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
#                        print 'b:'+str(b)
#                        print 'c:'+str(c)
#                        a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
#                        #a.current_sick_leaves=b
#                        a.eligiable_avaliable_leave=b 
#                        a.sick_leaves_used=c
#                        a.save()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Approved'
#                        x.save()
#                        ########################################################
#                        print 'a:'+str(a)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()    
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
                 ################################
#                if emp_team=='Adminstrative':
#                    print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave or sick leave'
#                    print 'from emaiL: '+str(from_email)
#                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                    #email1.send()
#                    print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                    leave_type_id=str(leave_type_id)
#                    print 'leave_type_id:'+str(leave_type_id)
#                    if leave_type_id=='CL':
#                        print'sening mail for etl but for casual leave approving inspite of not having suffienent csaual leave '
#                    
#                        print 'leaveid is cl' 
#                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                        c=float(casual_leaves_used)+float(actual_totalleavesdifference)
#                        print 'b:'+str(b)
#                        print 'c:'+str(c)
#                        a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
#                        #a.current_casual_leaves=b ####to update the value in database.#######
#                        a.eligiable_avaliable_leave=b ####to update the value in database.#######
#                        a.casual_leaves_used=c
#                        a.save()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Approved'
#                        x.save()
#                        ########################################################
#                        print 'a:'+str(a)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                   ####work here for sick leave and other team 
#                    if leave_type_id=='SL':
#                        print'sening mail for etl but for casual leave approving inspite of not having suffienent sick leave'
#                    
#                        print 'leaveid is sl' 
#                        #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
#                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                        c=float(sick_leaves_used)+float(actual_totalleavesdifference)
#                        #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
#                        print 'b:'+str(b)
#                        print 'c:'+str(c)
#                        a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
#                        #a.current_sick_leaves=b
#                        a.eligiable_avaliable_leave=b 
#                        a.sick_leaves_used=c
#                        a.save()
#                        #this part is for updating the leave status part of leave table to passive.
#                        x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                        print "this part is for updating the leave status part of leave table to passive."
#                        x.leaves_status='Passive'
#                        x.leaves_approved_by_tl='Leave Approved'
#                        x.save()
#                        ########################################################
#                        print 'a:'+str(a)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                        email1.send()    
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                 ############################

                      
                
            except BadHeaderError:
                print '33333'
                return HttpResponse('Invalid header found.') 
    for xsd in new_object1111:
        xemail_id=xsd.email_id 
        xemail_id=str(xemail_id)  
    	if newsession1==xemail_id:
            return render_to_response('noticeforall.html',{'z':z,'extra_object':extra_object},
                                  RequestContext(request))             
    return render_to_response('basic_form.html',{'z':z,'extra_object':extra_object},
                                  RequestContext(request))      
        
        
        
        
       
    
    
    
#    Accept='accept'    
#    #showsign=Signinform()
#    print 'nisha'
#    if 'reject33' in request.POST:
#        #print request.POST
#        print 'reject BUTTON IS SELECTED'
#        Reject='reject'
#        #decilineshowsign=Signinform()
#        return render_to_response('basic_form.html',{'decilineshowsign':decilineshowsign,'leave_id':leave_id,'Reject':Reject},
#                                  RequestContext(request)) 
#    return render_to_response('basic_form.html',{'showsign':showsign,'leave_id':leave_id,'Accept':Accept},RequestContext(request))     
#
#    


#below is code for accept leave by the team leave
def finalmailsend(request,leave_id,e=None):
     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:    
        print 'username length less equal to zero which means user is logout.and session is deleted '
        my_object6=Signinform()
        print 'nisha'
        return render_to_response('new_form1.html',{'my_object6':my_object6},RequestContext(request))
    ###################################################################################################

    print 'hi'
    print request.POST
#    a=request.POST.keys()
#    e=str(e)+'@entigencesolutions.in'
#    print 'e:'+str(e)
    print 'this causes problem fix here--------------'
#    try:
#        print 'in the try box'
#        b=a[1]
#        c=str(b)
#        d=c.split('=')
#        e=d[1]
#        #f=d[3]
#        e=str(e)
#        #f=str(f)
#    except:
#        print 'in except' 
#        b=a[0]
#        c=str(b)
#        d=c.split('=')
#        e=d[1]
#        #f=d[3]
#        e=str(e)
#        #f=str(f)   
#        
##    b=a[1]
##    c=str(b)
##    d=c.split('=')
##    e=d[1]
##    #f=d[3]
##    e=str(e)
##    #f=str(f)
#    print 'a:'+str(a)
#    print 'b:'+str(b)
#    print 'c:'+str(c)
#    print 'd:'+str(d)
#    print 'e:'+str(e)
#    #print 'f:'+str(f)
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
 
  ####work here for sending mail by team lead to employee
    print 'leave_id:'+str(leave_id)
    z=LMS_LEAVE_INFO_TABLE.objects.filter(leave_id=leave_id)###########################
    print 'zzzzzzzzzzzzzzzzzzzzzz'
    for i in z:
        name=i.name
        actual_totalleavesdifference=i.actual_totalleavesdifference
        leave_type_id=i.leave_type_id
        emp_id_ofuser=i.emp_id_ofuser###emailid of person whose leave is being approved or rejected
        print 'name:'+str(name)
        print 'leave_type_id:'+str(leave_type_id)
        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
        print 'emp_id_ofuser:'+str(emp_id_ofuser)
    emp_id_ofuser=str(emp_id_ofuser)    
    z1=LMS_LEAVES_summary_TABLE.objects.filter(email_id=emp_id_ofuser)       
    for i in z1:
        emp_team=i.team
        email_id=i.email_id
        summary_id=i.summary_id
        total_casual_leaves=i.total_casual_leaves
        total_sick_leaves=i.total_sick_leaves
        eligiable_avaliable_leave=i.eligiable_avaliable_leave
        casual_leaves_used=i.casual_leaves_used
        sick_leaves_used=i.sick_leaves_used
        print 'summary_id:'+str(summary_id)
        print 'total_casual_leaves:'+str(total_casual_leaves)
        print 'total_sick_leaves:'+str(total_sick_leaves)
        print 'eligiable_avaliable_leave:'+str(eligiable_avaliable_leave)
        print 'casual_leaves_used:'+str(casual_leaves_used)
        print 'sick_leaves_used:'+str(sick_leaves_used) 
        print'emp_team:'+str(emp_team)
        print 'email_id:'+str(email_id)####emailid of employeee whose leave is to be approved or reject .
 
    from_email='victory.nisha@gmail.com' ###change it to team lead id
    passwd='nishadwivedinishadwivedi'
    #passwd=f#fill in before sending mail
    subject='Approve'
    message='Leave Approved'
    connection = mail.get_connection(host ='smtp.gmail.com',  port = '587',  username=from_email,  password=passwd, user_tls=True)
    connection.open()
    if subject and message and from_email:
                try:
                    print 'inside try box'
                    print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
                    leave_type_id=str(leave_type_id)
                    print 'leave_type_id:'+str(leave_type_id)
                    if leave_type_id=='CL':
                        print 'leaveid is Cl' 
                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
                        c=float(casual_leaves_used)+float(actual_totalleavesdifference)
                        print 'b:'+str(b)
                        print 'c:'+str(c)
                        if float(b)<0:
                            print 'not sufficient sick leave'
                            print 'not sufficient sick leave'   
                            #this part is for updating the leave status part of leave table to passive.
                            x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                            print "this part is for updating the leave status part of leave table to passive."
                            #x.leaves_status='Passive'
                            #x.leaves_approved_by_tl='Not sufficient sick leave'
                            #x.save()
                            ########################################################
                            casualnotsendmail='abc'
			    for xsd23 in new_object1111:
                                xemail_id=xsd23.email_id 
                                xemail_id=str(xemail_id)
                                if newsession1==xemail_id:
                                    return render_to_response('noticeforall.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                            return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                                #this part is for updating the leave status part of leave table to passive.
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive."
#                                x.leaves_status='Passive'
#                                x.leaves_approved_by_tl='Not sufficient sick leave'
#                                x.save()
#                                ########################################################
#                                notsendmail='abc'
#                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
#                                  RequestContext(request))
                        else:
                            if float(c)<=float(total_casual_leaves):  
                                print 'checking'
                                print 'this value is less then 12or equal'
                                a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
                                #a.current_casual_leaves=b ####to update the value in database.#######
                                a.eligiable_avaliable_leave=b ####to update the value in database.#######
                                a.casual_leaves_used=c
                                a.save()
                                #this part is for updating the leave status part of leave table to passive.
                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                                print "this part is for updating the leave status part of leave table to passive."
                                x.leaves_status='Passive'
                                x.leaves_approved_by_tl='Leave Approved'
                                x.save()
                                ########################################################
                                print 'a:'+str(a)
                                #email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser,xemail_id], connection=connection)
                                email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                                email1.send()
                            else:
                                print 'not sufficient sick leave'
                                # to work here###########
                                #this part is for updating the leave status part of leave table to passive.
                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                                print "this part is for updating the leave status part of leave table to passive."
                                #x.leaves_status='Passive'
                                #x.leaves_approved_by_tl='Not sufficient sick leave'
                                #x.save()
                                ########################################################
                                casualnotsendmail='abc'
			        for xsd in new_object1111:
        			    xemail_id=xsd.email_id 
        			    xemail_id=str(xemail_id)
                                    if newsession1==xemail_id:
                                        return render_to_response('noticeforall.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object},
                                                              RequestContext(request))
                                        
                    if leave_type_id=='SL':
                        print 'leaveid is sl' 
                        #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
                        b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
                        c=float(sick_leaves_used)+float(actual_totalleavesdifference)
                        #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
                        print 'b:'+str(b)
                        print 'c:'+str(c)
                        #print 'current_sick_leaves:'+str(current_sick_leaves)
                        if int(b)<0:
                            print 'not sufficient sick leave'
                            print 'leave_id:'+str(leave_id)
                            #this part is for updating the leave status part of leave table to passive.
                            x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                            print "this part is for updating the leave status part of leave table to passive." 
                            casualnotsendmail='abc'
			    for xsd in new_object1111:
        		        xemail_id=xsd.email_id 
        		        xemail_id=str(xemail_id)
                                if newsession1==xemail_id:
                                    return render_to_response('noticeforall.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                               
                            return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                               
#                              x.leaves_status='Passive'
#                                x.leaves_approved_by_tl='Not sufficient sick leave'
#                                x.save()
#                                ########################################################
#                                notsendmail='abc'
#                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
#                                  RequestContext(request)) 
                        else :
                            if float(c)<=float(total_sick_leaves):
                                print 'checking'
#                                
                                a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
                                #a.current_sick_leaves=b
                                a.eligiable_avaliable_leave=b 
                                a.sick_leaves_used=c
                                a.save()
                                #this part is for updating the leave status part of leave table to passive.
                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                                print "this part is for updating the leave status part of leave table to passive."
                                x.leaves_status='Passive'
                                x.leaves_approved_by_tl='Leave Approved'
                                x.save()
                                ########################################################
                                print 'a:'+str(a)
                                #email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser,xemail_id], connection=connection)
                                email1 = mail.EmailMessage(subject,message,from_email, [emp_id_ofuser], connection=connection)
                                email1.send()
                            else:
                                print 'not sufficient sick leave'
                                # to work here###########
                                #this part is for updating the leave status part of leave table to passive.
                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                                print "this part is for updating the leave status part of leave table to passive."
                                    #x.leaves_status='Passive'
                                    #x.leaves_approved_by_tl='Not sufficient sick leave'
                                    #x.save()
                                    ########################################################
                                casualnotsendmail='abc'
				for xsd in new_object1111:
                                    xemail_id=xsd.email_id 
                                    xemail_id=str(xemail_id)
                                    if newsession1==xemail_id:
                                        return render_to_response('noticeforall.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'extra_object':extra_object,},
                                                              RequestContext(request))
                                    
                        print 'i m here'   
                        print 'sendddddddddd'
                        connection.close()
#                    if emp_team=='Claret':
#                        print'sening mail for CLARIT'
#                        #send_mail(subject, message, from_email, ['sapudevidwivedi@gmail.com','sdwivedi@entigencesolutions.in'],)
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                        leave_type_id=str(leave_type_id)
#                        print 'leave_type_id:'+str(leave_type_id)
#                        if leave_type_id=='CL':
#                            print 'leaveid is cl' 
#                            #b=int(current_casual_leaves)-int(actual_totalleavesdifference)
#                            b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                            c=int(casual_leaves_used)+int(actual_totalleavesdifference)
#                            print 'b:'+str(b)
#                            print 'c:'+str(c)
#                            if int(b)<0:
#                                print 'not sufficient sick leave'
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive."
#                                casualnotsendmail='abc'
#                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                
##                                #this part is for updating the leave status part of leave table to passive.
##                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
##                                print "this part is for updating the leave status part of leave table to passive."
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Not sufficient sick leave'
##                                x.save()
##                                ########################################################
##                                notsendmail='abc'
##                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
##                                  RequestContext(request))
#                            else:
#                                if float(c)<=float(total_casual_leaves):  
#                                    print 'checking'
#                                    print 'this value is less then 12or equal'
#                                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
#                                    #a.current_casual_leaves=b ####to update the value in database.#######
#                                    a.eligiable_avaliable_leave=b ####to update the value in database.#######
#                                    a.casual_leaves_used=c
#                                    a.save()
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    x.leaves_status='Passive'
#                                    x.leaves_approved_by_tl='Leave Approved'
#                                    x.save()
#                                    ########################################################
#                                    print 'a:'+str(a)
#                                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                                    email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                                    email1.send()
##                                print 'checking'
##                                a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
##                                a.current_casual_leaves=b ####to update the value in database.#######
##                                a.casual_leaves_used=c
##                                a.save()
##                                #this part is for updating the leave status part of leave table to passive.
##                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
##                                print "this part is for updating the leave status part of leave table to passive."
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Leave Approved'
##                                x.save()
##                                ########################################################
##                                print 'a:'+str(a)
##                                #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
##                                email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
##                                email1.send()
#                                else:
#                                    print 'not sufficient sick leave'
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    casualnotsendmail='abc'
#                                    return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                        
#                        if leave_type_id=='SL':
#                            print 'leaveid is sl' 
#                            b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                            c=float(sick_leaves_used)+float(actual_totalleavesdifference)
#                            #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
#                            print 'b:'+str(b)
#                            print 'c:'+str(c)
#                            if int(b)<0:
#                                print 'not sufficient sick leave'
#                                print 'leave_id:'+str(leave_id)
#                                #this part is for updating the leave status part of leave table to passive.
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive." 
#                                casualnotsendmail='abc'
#                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                               
#                            else :
#                                if float(c)<=float(total_sick_leaves):
#                                    print 'checking'
##                                
#                                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
#                                    #a.current_sick_leaves=b
#                                    a.eligiable_avaliable_leave=b 
#                                    a.sick_leaves_used=c
#                                    a.save()
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    x.leaves_status='Passive'
#                                    x.leaves_approved_by_tl='Leave Approved'
#                                    x.save()
#                                    ########################################################
#                                    print 'a:'+str(a)
#                                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                                    email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                                    email1.send()
#                                else:
#                                    print 'not sufficient sick leave'
#                                    # to work here###########
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    #x.leaves_status='Passive'
#                                    #x.leaves_approved_by_tl='Not sufficient sick leave'
#                                    #x.save()
#                                    ########################################################
#                                    casualnotsendmail='abc'
#                                    return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()  
#                    if emp_team=='Lyterati':
#                        print'sening mail for Lyterati'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                        leave_type_id=str(leave_type_id)
#                        print 'leave_type_id:'+str(leave_type_id)
#                        if leave_type_id=='CL':
#                            print 'leaveid is cl' 
#                            #b=int(current_casual_leaves)-int(actual_totalleavesdifference)
#                            b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                            c=int(casual_leaves_used)+int(actual_totalleavesdifference)
#                            print 'b:'+str(b)
#                            print 'c:'+str(c)
#                            if int(b)<0:
#                                print 'not sufficient sick leave'
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive."
#                                casualnotsendmail='abc'
#                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                
##                                #this part is for updating the leave status part of leave table to passive.
##                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
##                                print "this part is for updating the leave status part of leave table to passive."
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Not sufficient sick leave'
##                                x.save()
##                                ########################################################
##                                notsendmail='abc'
##                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
##                                  RequestContext(request))
#                            else:
#                                if float(c)<=float(total_casual_leaves):  
#                                    print 'checking'
#                                    print 'this value is less then 12or equal'
#                                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
#                                    #a.current_casual_leaves=b ####to update the value in database.#######
#                                    a.eligiable_avaliable_leave=b ####to update the value in database.#######
#                                    a.casual_leaves_used=c
#                                    a.save()
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    x.leaves_status='Passive'
#                                    x.leaves_approved_by_tl='Leave Approved'
#                                    x.save()
#                                    ########################################################
#                                    print 'a:'+str(a)
#                                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                                    email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                                    email1.send()
##                                print 'checking'
##                                a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
##                                a.current_casual_leaves=b ####to update the value in database.#######
##                                a.casual_leaves_used=c
##                                a.save()
##                                #this part is for updating the leave status part of leave table to passive.
##                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
##                                print "this part is for updating the leave status part of leave table to passive."
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Leave Approved'
##                                x.save()
##                                ########################################################
##                                print 'a:'+str(a)
##                                #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
##                                email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
##                                email1.send()
#                                else:
#                                    print 'not sufficient sick leave'
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    casualnotsendmail='abc'
#                                    return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#
#                        if leave_type_id=='SL':
#                            print 'leaveid is sl' 
#                            #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
#                            b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                            c=float(sick_leaves_used)+float(actual_totalleavesdifference)
#                            #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
#                            print 'b:'+str(b)
#                            print 'c:'+str(c)
#                            #print 'current_sick_leaves:'+str(current_sick_leaves)
#                            if int(b)<0:
#                                print 'not sufficient sick leave'
#                                print 'leave_id:'+str(leave_id)
#                                #this part is for updating the leave status part of leave table to passive.
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive." 
#                                casualnotsendmail='abc'
#                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                               
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Not sufficient sick leave'
##                                x.save()
##                                ########################################################
##                                notsendmail='abc'
##                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
##                                  RequestContext(request)) 
#                            else :
#                                if float(c)<=float(total_sick_leaves):
#                                    print 'checking'
##                                
#                                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
#                                    #a.current_sick_leaves=b
#                                    a.eligiable_avaliable_leave=b 
#                                    a.sick_leaves_used=c
#                                    a.save()
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    x.leaves_status='Passive'
#                                    x.leaves_approved_by_tl='Leave Approved'
#                                    x.save()
#                                    ########################################################
#                                    print 'a:'+str(a)
#                                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                                    email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                                    email1.send()
#                                else:
#                                    print 'not sufficient sick leave'
#                                    # to work here###########
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    #x.leaves_status='Passive'
#                                    #x.leaves_approved_by_tl='Not sufficient sick leave'
#                                    #x.save()
#                                    ########################################################
#                                    casualnotsendmail='abc'
#                                    return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                    
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
#                        #send_mail(subject, message, from_email, ['sapudevidwivedi@gmail.com','sdwivedi@entigencesolutions.in'],)   
#                    if emp_team=='Adminstrative':
#                        print'sening mail for Adminstrative'
#                        print 'from emaiL: '+str(from_email)
#                        #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                        #email1.send()
#                        print 'actual_totalleavesdifference:'+str(actual_totalleavesdifference)
#                        leave_type_id=str(leave_type_id)
#                        print 'leave_type_id:'+str(leave_type_id)
#                        if leave_type_id=='CL':
#                            print 'leaveid is cl' 
#                            #b=int(current_casual_leaves)-int(actual_totalleavesdifference)
#                            b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                            c=int(casual_leaves_used)+int(actual_totalleavesdifference)
#                            print 'b:'+str(b)
#                            print 'c:'+str(c)
#                            if int(b)<0:
#                                print 'not sufficient sick leave'
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive."
#                                casualnotsendmail='abc'
#                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                
##                                #this part is for updating the leave status part of leave table to passive.
##                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
##                                print "this part is for updating the leave status part of leave table to passive."
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Not sufficient sick leave'
##                                x.save()
##                                ########################################################
##                                notsendmail='abc'
##                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
##                                  RequestContext(request))
#                            else:
#                                if float(c)<=float(total_casual_leaves):  
#                                    print 'checking'
#                                    print 'this value is less then 12or equal'
#                                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
#                                    #a.current_casual_leaves=b ####to update the value in database.#######
#                                    a.eligiable_avaliable_leave=b ####to update the value in database.#######
#                                    a.casual_leaves_used=c
#                                    a.save()
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    x.leaves_status='Passive'
#                                    x.leaves_approved_by_tl='Leave Approved'
#                                    x.save()
#                                    ########################################################
#                                    print 'a:'+str(a)
#                                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                                    email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                                    email1.send()
##                                print 'checking'
##                                a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.#######
##                                a.current_casual_leaves=b ####to update the value in database.#######
##                                a.casual_leaves_used=c
##                                a.save()
##                                #this part is for updating the leave status part of leave table to passive.
##                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
##                                print "this part is for updating the leave status part of leave table to passive."
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Leave Approved'
##                                x.save()
##                                ########################################################
##                                print 'a:'+str(a)
##                                #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
##                                email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
##                                email1.send()
#                                else:
#                                    print 'not sufficient sick leave'
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    casualnotsendmail='abc'
#                                    return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#
#                        if leave_type_id=='SL':
#                            print 'leaveid is sl' 
#                            #b=int(current_sick_leaves)-int(actual_totalleavesdifference)
#                            b=float(eligiable_avaliable_leave)-float(actual_totalleavesdifference)
#                            c=float(sick_leaves_used)+float(actual_totalleavesdifference)
#                            #c=int(sick_leaves_used)+int(actual_totalleavesdifference)
#                            print 'b:'+str(b)
#                            print 'c:'+str(c)
#                            #print 'current_sick_leaves:'+str(current_sick_leaves)
#                            if int(b)<0:
#                                print 'not sufficient sick leave'
#                                print 'leave_id:'+str(leave_id)
#                                #this part is for updating the leave status part of leave table to passive.
#                                x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                print "this part is for updating the leave status part of leave table to passive." 
#                                casualnotsendmail='abc'
#                                return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                               
##                                x.leaves_status='Passive'
##                                x.leaves_approved_by_tl='Not sufficient sick leave'
##                                x.save()
##                                ########################################################
##                                notsendmail='abc'
##                                return render_to_response('basic_form.html',{'notsendmail':notsendmail,},
##                                  RequestContext(request)) 
#                            else :
#                                if float(c)<=float(total_sick_leaves):
#                                    print 'checking'
##                                
#                                    a = LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)####to update the value in database get the unique field.######
#                                    #a.current_sick_leaves=b
#                                    a.eligiable_avaliable_leave=b 
#                                    a.sick_leaves_used=c
#                                    a.save()
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    x.leaves_status='Passive'
#                                    x.leaves_approved_by_tl='Leave Approved'
#                                    x.save()
#                                    ########################################################
#                                    print 'a:'+str(a)
#                                    #email1 = mail.EmailMessage(subject,message,from_email, [to], connection=connection)
#                                    email1 = mail.EmailMessage(subject,message,from_email, ['victory.nisha@gmail.com'], connection=connection)
#                                    email1.send()
#                                else:
#                                    print 'not sufficient sick leave'
#                                    # to work here###########
#                                    #this part is for updating the leave status part of leave table to passive.
#                                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
#                                    print "this part is for updating the leave status part of leave table to passive."
#                                    #x.leaves_status='Passive'
#                                    #x.leaves_approved_by_tl='Not sufficient sick leave'
#                                    #x.save()
#                                    ########################################################
#                                    casualnotsendmail='abc'
#                                    return render_to_response('basic_form.html',{'casualnotsendmail':casualnotsendmail,'leave_id':leave_id,'showname':showname,},
#                                                              RequestContext(request))
#                                    
#                        print 'i m here'   
#                        print 'sendddddddddd'
#                        connection.close()
                    else:
                        print 'no match'
                except BadHeaderError:
                    print '33333'
                    return HttpResponse('Invalid header found.')
    for xsd in new_object1111:
        xemail_id=xsd.email_id 
        xemail_id=str(xemail_id)
    	if newsession1==xemail_id:
            return render_to_response('noticeforall.html',{'z':z,'extra_object':extra_object},
                                  RequestContext(request))               
    return render_to_response('basic_form.html',{'z':z,'extra_object':extra_object},
                                  RequestContext(request)) 


#####code for sending mail
def send_email(request):
#    subject = request.POST.get('subject', '')
#    message = request.POST.get('message', '')
#    from_email = request.POST.get('from_email', '')
    print "hello"
    subject = 'regarding leaves '
    message = 'applying for leave from abc to xyz '
    from_email = 'victory.nisha@gmail.com'
    if subject and message and from_email:
        try:
           
            send_mail(subject, message, from_email, ['sapudevidwivedi@gmail.com','sdwivedi@entigencesolutions.in'],)   
        except BadHeaderError:
            print '33333'
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
       
        return HttpResponse('Make sure all fields are entered and valid.')




#####code for captcha and signup page
def captcha(request):
    print 'test for captcha'
    if request.POST:
        print 'test2 for captcha'
        print request.POST
        print 'kkkkkkkkk'
        ob1 = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if ob1.is_valid():
            human = True
    else:
        print 'in else foe captcha'
        ob1 = CaptchaTestForm()
    print ob1
    print '********************'
    #return render_to_response('template.html',locals())
    return render_to_response('basic_form.html',{'ob1':ob1},RequestContext(request))


def SignUp(request):
    print "signup "
    
    if request.method =='POST':
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['name']
        myrequestpost['name']=myrequestpost['name'].title()
        myrequestpost['middlename']=myrequestpost['middlename'].title()
        myrequestpost['lastname']=myrequestpost['lastname'].title()
        print 'HERE I am'
        #ob2=CaptchaTestForm(request.POST)
        ob2=CaptchaTestForm(myrequestpost)
        print "ggoooooooooooooo"
        #this code is for the login button button######################
        if 'cancel1' in request.POST:
            print "inside login"
            strUrl = '/access_userbasic_detail1'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ##############################################################
        
        if ob2.is_valid():
            print 'i m inside'
            print ob2
            ob2.save()
            print "why"
            return HttpResponseRedirect('/SignUp/')
        
        return render_to_response('basic_form.html',{'ob2':ob2},
                                  RequestContext(request))
    else:
        ob3 = LMS_SIGNUP.objects.all()# for fetching all data from database
        return render_to_response('basic_form.html',{'ob3':ob3},
                                  RequestContext(request))

  ###########################################################################################
###code to display hirachy
#def manage_hirarchy(request,name=None):
def manage_hirarchy(request):  
    print 'request.signup_id*********************************'
    #if request.session['username'].DoesNotExist:
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #invalid user and password
            #if QuerySet.filter(~Q(username=request.POST['username'])) and QuerySet.filter(~Q(password=request.POST['password'])):
            #########to coreect here#####
##            if LMS_SIGNUP.objects.filter(~Q(username=request.POST['username'])) and LMS_SIGNUP.objects.filter(~Q(password=request.POST['password'])):
##            #if LMS_SIGNUP.objects.exclude(username=request.POST['username']) and LMS_SIGNUP.objects.filter(password=request.POST['password']):
##                print 'the username and password are invalid'
##                mh2=Signinform()
##                tochangeurl='mh'
##                print 'nisha'
##                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
##    #####################################################################################
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='mh'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    ############################################################
#                    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#                    for i in allsignupdata:
#                        name=i.name
#                    print 'in  try box of manage hierachy'
#                    name=str(name)
                    #print 'name:'+str(name)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    for i in extra_object:
                        name=i.name_of_employee
                        teamtocheck=i.team
                    name=str(name)    
                    a=datetime.date.today()
                    showhierchy=LMS_TEAM.objects.all()
                    return render_to_response('basic_form.html',{'showhierchy':showhierchy,'a':a,'name':name,'extra_object':extra_object},
                                      RequestContext(request))
                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='mh'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='mh'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
    print 'outside the try and except box and now session is active'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
#    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#    for i in allsignupdata:
#        name=i.name
#    print 'in manage hierachy'
#    name=str(name)
#    print 'name:'+str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    for i in extra_object:
        name=i.name_of_employee
        teamtocheck=i.team
    name=str(name)
    a=datetime.date.today()
    showhierchy=LMS_TEAM.objects.all()
    return render_to_response('basic_form.html',{'showhierchy':showhierchy,'a':a,'name':name,'extra_object':extra_object},
                                  RequestContext(request))
          
#########code for news form####
def news_detail(request):
    ob4=Newsform()
    print 'nisha'
    return render_to_response('basic_form.html',{'ob4':ob4},RequestContext(request))



def express_news(request):
    if request.method =='POST':
        print 'HERE I am'
        ob5=Newsform(request.POST)
        if ob5.is_valid():
            print 'i m inside'
            ob5.save()
            print "why"
            return HttpResponseRedirect('/express_news/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'ob5':ob5},
                                  RequestContext(request))
    else:
        ob6 = LMS_NEWS.objects.all()# for fetching all data from database
        return render_to_response('basic_form.html',{'ob6':ob6},
                                  RequestContext(request))
        

def entigence_newsedit(request,news_id):
    print "sapu"
    product = LMS_NEWS.objects.get(pk=news_id)
    if request.method == 'POST':
        ob7 = Newsform(request.POST, instance=product)

        print "PRODUCTchecking POST"

        if ob7.is_valid():
            print "Display Form"

            product1 = ob7.save( commit=False )
            product1.save()       
            print 'clicking on editttttttt'     
            return HttpResponseRedirect('/express_news/')
        return render_to_response('basic_form.html',{'ob7':ob7},
                                  RequestContext(request))
    else:
            ob8=Newsform(instance=product)
            print 'clicking on edit'
            return render_to_response('basic_form.html',{'ob8':ob8},RequestContext(request)) 
           
def nowdelete_new(request,news_id):

    print "delete"
    obj3 = LMS_NEWS.objects.get(pk=news_id)
    obj3.delete()
    return HttpResponseRedirect('/express_news/')

def complete_delete_all(request):
    print"delete all"
    obj3=LMS_NEWS.objects.all().delete()
    return HttpResponseRedirect('/express_news/')  


###for gender table##
def gender_detail(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='gender_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1) 
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)  
                    #print 'name:'+str(name)
                    a=datetime.date.today()
                    #my_object8=Holidaylistform()
                    gender=Genderform()
                    try:
                        print 'newsession1'+str(newsession1)
                        if newsession1==xemail_id:
                            print 'holiday form hrrrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'gender':gender,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='gender_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='gender_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    a=datetime.date.today()
    gender=Genderform()
    if newsession1==xemail_id:
        print 'holiday form of hrrrrrrrrrr'
        return render_to_response('basic_form.html',{'gender':gender,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

def Gendertabledisplay(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='Gendertabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    ############################################################

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)
                    gender_display1 = LMS_GENDER.objects.all()# for fetching all data from database
        
                    if len(gender_display1)==0:
                        print "length is 0"
                        tochsngeurlfunction1='gender_detail'
                        noentryintableordeletedcontent1='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
                    return render_to_response('basic_form.html',{'gender_display1':gender_display1,'extra_object':extra_object},
                                  RequestContext(request))
#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Gendertabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Gendertabledisplay'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    ################session using###############
    
    
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print request.POST    
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    
    if request.method =='POST':
        print 'HERE I am'
        myrequestpost=request.POST.copy()
        myrequestpost['emp_gender']=myrequestpost['emp_gender'].title()
        gender_display=Genderform(myrequestpost)
        #gender_display=Genderform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/Gendertabledisplay/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        if gender_display.is_valid():
            print 'i m inside'
            gender_display.save()
            print "why"
            ##############for chron tab
#           
#            z123=LMS_LEAVES_summary_TABLE.objects.all()
#            for i in z123:
#                summary_id=i.summary_id
#                summary_id=str(summary_id)
#                eligiable_avaliable_leave=i.eligiable_avaliable_leave
#                eligiable_avaliable_leave=float(eligiable_avaliable_leave)+1.5
#                print 'summary_id:'+str(summary_id)
#                print 'eligiable_avaliable_leave:'+str(eligiable_avaliable_leave)
#                LMS_LEAVES_summary_TABLE.objects.filter(summary_id=summary_id).update(eligiable_avaliable_leave=eligiable_avaliable_leave)
#                print 'kkkk'
#                print 's'
#            #qqq=LMS_LEAVES_summary_TABLE.objects.all().update(eligiable_avaliable_leave=1.5)
#            #LMS_LEAVES_summary_TABLE.objects.all().update(eligiable_avaliable_leave=1.5)
#            #LMS_LEAVES_summary_TABLE.objects.update(eligiable_avaliable_leave=1.5)
#            #LMS_LEAVES_summary_TABLE.objects.select_related().filter(summary_id=21).update(eligiable_avaliable_leave=1.5)
#            #LMS_LEAVES_summary_TABLE.objects.filter(summary_id=21).update(eligiable_avaliable_leave=5.0)
#            print 'kkkk'
#            print 's'

            ############################
            
            
            
            
            return HttpResponseRedirect('/Gendertabledisplay/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'gender_display':gender_display,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        gender_display1 = LMS_GENDER.objects.all()# for fetching all data from database
        
        if len(gender_display1)==0:
            print "length is 0"
            tochsngeurlfunction1='gender_detail'
            noentryintableordeletedcontent1='nonewnotification'
            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        return render_to_response('basic_form.html',{'gender_display1':gender_display1,'extra_object':extra_object},
                                  RequestContext(request))
        
def Gender_editfunction(request,gender_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
               
                mh2=Signinform()
                tochangeurl='Gender_editfunction/id='+str(gender_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    print 'gender_id:'+str(gender_id)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)
                    a=datetime.date.today()
                    print 'newsession1'+str(newsession1)
                    if newsession1==xemail_id:
                        getforallvalue=LMS_GENDER.objects.all()
                        if len(getforallvalue)==0:
                            noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                            tochsngeurlfunction1='gender_detail'
                            noentryintableordeletedcontent1='nonewnotification'
                            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
                        ####################when entry is deleted or not existing
                        product1 = LMS_GENDER.objects.filter(gender_id =gender_id)
                        if len(product1)==0:
                            noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                            tochsngeurlfunction1='gender_detail'
                            noentryintableordeletedcontent1='nonewnotification'
                            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        ########################    
                        product = LMS_GENDER.objects.get(pk=gender_id)    
                        my_genderedit_1=Genderform(instance=product)  
                        print 'holiday form hrrrrrrrrrrrr'
                        return render_to_response('basic_form.html',{'my_genderedit_1':my_genderedit_1,'extra_object':extra_object,'gender_id':gender_id},RequestContext(request)) 
            
                    print 'inside except=================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Gender_editfunction/id='+str(gender_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Gender_editfunction/id='+str(gender_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
      
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print 'in the change function of holiday table-----------------------------------'
    gender_id=gender_id
    print 'gender_id:'+str(gender_id)
    a=datetime.date.today()
    #name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    print 'extra_object:'+str(extra_object)
    #product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
    if request.method == 'POST':
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        myrequestpost['emp_gender']=myrequestpost['emp_gender'].title()
        product1 = LMS_GENDER.objects.filter(gender_id =gender_id)
        if len(product1)==0:
            print "length is 0"
            noentryintableordeletedcontent1='noentryintableordeletedcontent1'
            tochsngeurlfunction1='gender_detail'
            noentryintableordeletedcontent1='nonewnotification'
            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        ########################
        product = LMS_GENDER.objects.get(pk=gender_id)
        my_genderedit = Genderform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        ##########this code is for cancel of the form######
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/Gendertabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ########################################################
        if my_genderedit.is_valid():
            print "Display Form"
 
            my_genderedit.save()      
            print 'clicking on editttttttt'
            strUrl = '/Gendertabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)     
        return render_to_response('basic_form.html',{'my_genderedit':my_genderedit,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
            #my_object12=Holidaylistform(instance=product)
            #print 'my_object12:'+str(my_object12)
            if newsession1==xemail_id:
                getforallvalue=LMS_GENDER.objects.all()
                if len(getforallvalue)==0:
                    noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                    tochsngeurlfunction1='gender_detail'
                    noentryintableordeletedcontent1='nonewnotification'
                    return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
                product = LMS_GENDER.objects.get(pk=gender_id)    
                my_genderedit_1=Genderform(instance=product)    
                print ' of hrrrrrrrrrr'
                return render_to_response('basic_form.html',{'my_genderedit_1':my_genderedit_1,'extra_object':extra_object,'gender_id':gender_id},RequestContext(request)) 
            print 'inside else =================='
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

def gender_delete(request,gender_id):   
    print "delete"
    genderdelete = LMS_GENDER.objects.get(pk=gender_id)
    genderdelete.delete()
    sta_url='/Gendertabledisplay/'
    return HttpResponseRedirect(sta_url)
    
####form for position table##
def position_detail(request):    
     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='position_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1) 
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)  
                    #print 'name:'+str(name)
                    a=datetime.date.today()
                    #my_object8=Holidaylistform()
                    position=Positionform()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'position':position,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='position_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='position_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    a=datetime.date.today()
    position=Positionform()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            print 'holiday form of hrrrrrrrrrr'
            return render_to_response('basic_form.html',{'position':position,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))


def Position_tabledisplay(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='Position_tabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    ############################################################

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                    	print 'xemail_id:'+str(xemail_id)
			if newsession1==xemail_id:
                    	    position_display1 = LMS_POSITION.objects.all()# for fetching all data from database
        
                    	    if len(position_display1)==0:
                                print "length is 0"
                        	tochsngeurlfunction1='position_detail'
                        	noentryintableordeletedcontent1='nonewnotification'
                        	return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
                    	    return render_to_response('basic_form.html',{'position_display1':position_display1,'extra_object':extra_object},
                                  RequestContext(request))
		    print 'inside else'
		    invaliduser='invalid'
		    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Position_tabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Position_tabledisplay'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    ################session using###############
    
    
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print request.POST    
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    
    if request.method =='POST':
        print 'HERE I am'
        myrequestpost=request.POST.copy()
        myrequestpost['emp_position']=myrequestpost['emp_position']
        Position1_display=Positionform(myrequestpost)
        #gender_display=Genderform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/Position_tabledisplay/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        if Position1_display.is_valid():
            print 'i m inside'
            Position1_display.save()
            print "why"
            return HttpResponseRedirect('/Position_tabledisplay/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'Position1_display':Position1_display,'extra_object':extra_object},
                                  RequestContext(request))
    else:
	for x in new_object1111:
	    xemail_id=x.email_id
	    xemail_id=str(xemail_id)
	    print 'xemail_id:'+str(xemail_id)
	    if newsession1==xemail_id:
                position_display1 = LMS_POSITION.objects.all()# for fetching all data from database
        
        	if len(position_display1)==0:
                    print "length is 0"
            	    tochsngeurlfunction1='position_detail'
                    noentryintableordeletedcontent1='nonewnotification'
            	    return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        	return render_to_response('basic_form.html',{'position_display1':position_display1,'extra_object':extra_object},
                                  RequestContext(request))
	print 'inside else'
	invaliduser='invalid'
	return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
        


def Position12_editfunction(request,emp_position_id):
    print 'emp_position_id:'+str(emp_position_id)
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
               
                mh2=Signinform()
                tochangeurl='Position12_editfunction/id='+str(emp_position_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                   # print 'gender_id:'+str(gender_id)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id1=k.emp_position_id
                    print 'emp_position_id1:'+str(emp_position_id1)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        a=datetime.date.today()
                        print 'newsession1'+str(newsession1)
                        if newsession1==xemail_id:
                            getforallvalue=LMS_POSITION.objects.all()
                            if len(getforallvalue)==0:
                                noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                                tochsngeurlfunction1='position_detail'
                                noentryintableordeletedcontent1='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
                            ####################when entry is deleted or not existing
                            product1 = LMS_POSITION.objects.filter(emp_position_id =emp_position_id)
                            if len(product1)==0:
                                print "length is 0"
                                noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                                tochsngeurlfunction1='position_detail'
                                noentryintableordeletedcontent1='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
            ########################    
                            product = LMS_POSITION.objects.get(pk=emp_position_id)    
                            my_position_edit_1=Positionform(instance=product)    
                            print ' of hrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'my_position_edit_1':my_position_edit_1,'extra_object':extra_object,'emp_position_id':emp_position_id},RequestContext(request)) 
            
                    print 'inside except=================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Position12_editfunction/id='+str(emp_position_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Position12_editfunction/id='+str(emp_position_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print 'in the change function of holiday table-----------------------------------'
    emp_position_id=emp_position_id
    print 'emp_position_id:'+str(emp_position_id)
    a=datetime.date.today()
    #name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id1=k.emp_position_id
    print 'emp_position_id1:'+str(emp_position_id1)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    print 'extra_object:'+str(extra_object)
    #product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
    if request.method == 'POST':
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        myrequestpost['emp_position']=myrequestpost['emp_position']
        product1 = LMS_POSITION.objects.filter(emp_position_id =emp_position_id)
        if len(product1)==0:
            print "length is 0"
            noentryintableordeletedcontent1='noentryintableordeletedcontent1'
            tochsngeurlfunction1='position_detail'
            noentryintableordeletedcontent1='nonewnotification'
            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        ########################
        product = LMS_POSITION.objects.get(pk=emp_position_id)
        my_product_edit = Positionform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        ##########this code is for cancel of the form######
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/Position_tabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ########################################################
        if my_product_edit.is_valid():
            print "Display Form"
 
            my_product_edit.save()      
            print 'clicking on editttttttt'
            strUrl = '/Position_tabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)     
        return render_to_response('basic_form.html',{'my_product_edit':my_product_edit,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
            #my_object12=Holidaylistform(instance=product)
            #print 'my_object12:'+str(my_object12)
            for x in new_object1111:
                xemail_id=x.email_id 
                xemail_id=str(xemail_id)
                if newsession1==xemail_id:
                    getforallvalue=LMS_POSITION.objects.all()
                    if len(getforallvalue)==0:
                        noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                        tochsngeurlfunction1='position_detail'
                        noentryintableordeletedcontent1='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
                    product = LMS_POSITION.objects.get(pk=emp_position_id)    
                    my_position_edit_1=Positionform(instance=product)    
                    print ' of hrrrrrrrrrr'
                    return render_to_response('basic_form.html',{'my_position_edit_1':my_position_edit_1,'extra_object':extra_object,'emp_position_id':emp_position_id},RequestContext(request)) 
            print 'inside else =================='
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))



#############form for team table###
def team_detail(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='team_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1) 
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)  
                    #print 'name:'+str(name)
                    a=datetime.date.today()
                    #my_object8=Holidaylistform()
                    team=Teamform()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'team':team,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='team_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='team_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    a=datetime.date.today()
    team=Teamform()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            print 'holiday form of hrrrrrrrrrr'
            return render_to_response('basic_form.html',{'team':team,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))


def teamtabledisplay(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='teamtabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    ############################################################

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                    	print 'xemail_id:'+str(xemail_id)
			if newsession1==xemail_id:
                    	    Team_display1 = LMS_TEAM.objects.all()# for fetching all data from database
        
                    	    if len(Team_display1)==0:
                                print "length is 0"
                            	tochsngeurlfunction1='team_detail'
                            	noentryintableordeletedcontent1='nonewnotification'
                            	return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
                    	    return render_to_response('basic_form.html',{'Team_display1':Team_display1,'extra_object':extra_object},
                                  RequestContext(request))
		    print 'inside else'
		    invaliduser='invalid'
		    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='teamtabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='teamtabledisplay'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    ################session using###############
    
    
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print request.POST    
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    
    if request.method =='POST':
        print 'HERE I am'
        myrequestpost=request.POST.copy()
        myrequestpost['emp_team']=myrequestpost['emp_team'].title()
        team_display=Teamform(myrequestpost)
        #gender_display=Genderform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/teamtabledisplay/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        if team_display.is_valid():
            print 'i m inside'
            team_display.save()
            print "why"
            return HttpResponseRedirect('/teamtabledisplay/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'team_display':team_display,'extra_object':extra_object},
                                  RequestContext(request))
    else:
	for x in new_object1111:
	    xemail_id=x.email_id
	    xemail_id=str(xemail_id)
	    print 'xemail_id:'+str(xemail_id)
	    if newsession1==xemail_id: 
        	Team_display1 = LMS_TEAM.objects.all()# for fetching all data from database
        
       	        if len(Team_display1)==0:
            	    print "length is 0"
            	    tochsngeurlfunction1='team_detail'
            	    noentryintableordeletedcontent1='nonewnotification'
            	    return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        	return render_to_response('basic_form.html',{'Team_display1':Team_display1,'extra_object':extra_object},
                                  RequestContext(request))
	print 'inside else'
	invaliduser='invalid'
	return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
        

def Team_editfunction(request,emp_team_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
               
                mh2=Signinform()
                tochangeurl='Team_editfunction/id='+str(emp_team_id)  
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    print 'emp_team_id:'+str(emp_team_id)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        a=datetime.date.today()
                        print 'newsession1'+str(newsession1)
                        if newsession1==xemail_id:
                            getforallvalue=LMS_TEAM.objects.all()
                            if len(getforallvalue)==0:
                                noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                                tochsngeurlfunction1='team_detail'
                                noentryintableordeletedcontent1='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
                            ####################when entry is deleted or not existing
                            product1 = LMS_TEAM.objects.filter(emp_team_id =emp_team_id)
                            if len(product1)==0:
                                noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                                tochsngeurlfunction1='team_detail'
                                noentryintableordeletedcontent1='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
            ########################    
                            product = LMS_TEAM.objects.get(pk=emp_team_id)    
                            my_Teamedit_1=Teamform(instance=product)    
                            print ' of hrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'my_Teamedit_1':my_Teamedit_1,'extra_object':extra_object,'emp_team_id':emp_team_id},RequestContext(request)) 
                    
                    print 'inside except=================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Team_editfunction/id='+str(emp_team_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Team_editfunction/id='+str(emp_team_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
      
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print 'in the change function of holiday table-----------------------------------'
    emp_team_id=emp_team_id
    print 'emp_team_id:'+str(emp_team_id)
    a=datetime.date.today()
    #name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    print 'extra_object:'+str(extra_object)
    #product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
    if request.method == 'POST':
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        myrequestpost['emp_team']=myrequestpost['emp_team'].title()
        product1 = LMS_TEAM.objects.filter(emp_team_id =emp_team_id)
        if len(product1)==0:
            print "length is 0"
            noentryintableordeletedcontent1='noentryintableordeletedcontent1'
            tochsngeurlfunction1='team_detail'
            noentryintableordeletedcontent1='nonewnotification'
            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        ########################
        product = LMS_TEAM.objects.get(pk=emp_team_id)
        my_Teamedit = Teamform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        ##########this code is for cancel of the form######
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/teamtabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ########################################################
        if my_Teamedit.is_valid():
            print "Display Form"
 
            my_Teamedit.save()      
            print 'clicking on editttttttt'
            strUrl = '/teamtabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)     
        return render_to_response('basic_form.html',{'my_Teamedit':my_Teamedit,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
            #my_object12=Holidaylistform(instance=product)
            #print 'my_object12:'+str(my_object12)
            for x in new_object1111:
                xemail_id=x.email_id 
                xemail_id=str(xemail_id)
                if newsession1==xemail_id:
                    getforallvalue=LMS_TEAM.objects.all()
                    if len(getforallvalue)==0:
                        noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                        tochsngeurlfunction1='team_detail'
                        noentryintableordeletedcontent1='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
                    product = LMS_TEAM.objects.get(pk=emp_team_id)    
                    my_Teamedit_1=Teamform(instance=product)    
                    print ' of hrrrrrrrrrr'
                    return render_to_response('basic_form.html',{'my_Teamedit_1':my_Teamedit_1,'extra_object':extra_object,'emp_team_id':emp_team_id},RequestContext(request)) 
            print 'inside else =================='
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))


#####form for holiday type table##
def holidaytypetable_detail(request):
############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='holidaytypetable_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1) 
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)  
                    #print 'name:'+str(name)
                    a=datetime.date.today()
                    #my_object8=Holidaylistform()
                    holidaytypeeee=Holidaytypeform()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'holidaytypeeee':holidaytypeeee,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='holidaytypetable_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='holidaytypetable_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    a=datetime.date.today()
    holidaytypeeee=Holidaytypeform()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            print 'holiday form of hrrrrrrrrrr'
            return render_to_response('basic_form.html',{'holidaytypeeee':holidaytypeeee,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))


def holidaytype_tabledisplay(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='holidaytype_tabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    ############################################################

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                    	print 'xemail_id:'+str(xemail_id)
			if newsession1==xemail_id:
                    	    holidaytype_display1 = LMS_HOLIDAY_TYPE.objects.all()
        
                    	    if len(holidaytype_display1)==0:
                        	print "length is 0"
                        	tochsngeurlfunction1='holidaytypetable_detail'
                        	noentryintableordeletedcontent1='nonewnotification'
                        	return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
                    	    return render_to_response('basic_form.html',{'holidaytype_display1':holidaytype_display1,'extra_object':extra_object},
                                  RequestContext(request))
		    print 'inside else'
		    invaliduser='invalid'
		    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='holidaytype_tabledisplay'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='holidaytype_tabledisplay'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    ################session using###############
    
    
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print request.POST    
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    
    if request.method =='POST':
        print 'HERE I am'
        myrequestpost=request.POST.copy()
        myrequestpost['Holiday_Type']=myrequestpost['Holiday_Type'].title()
        holidaytype_display=Holidaytypeform(myrequestpost)
        #gender_display=Genderform(request.POST)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/holidaytype_tabledisplay/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        if holidaytype_display.is_valid():
            print 'i m inside'
            holidaytype_display.save()
            print "why"
            return HttpResponseRedirect('/holidaytype_tabledisplay/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'holidaytype_display':holidaytype_display,'extra_object':extra_object},
                                  RequestContext(request))
    else:
	for x in new_object1111:
	    xemail_id=x.email_id
	    xemail_id=str(xemail_id)
	    print 'xemail_id:'+str(xemail_id)
	    if newsession1==xemail_id:
        	holidaytype_display1 = LMS_HOLIDAY_TYPE.objects.all()# for fetching all data from database
        
        	if len(holidaytype_display1)==0:
            	    print "length is 0"
            	    tochsngeurlfunction1='holidaytypetable_detail'
            	    noentryintableordeletedcontent1='nonewnotification'
           	    return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
           	return render_to_response('basic_form.html',{'holidaytype_display1':holidaytype_display1,'extra_object':extra_object},
                                  RequestContext(request))
	print 'inside else'
	invaliduser='invalid'
	return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
	
        
def Holidaytype_editfunction(request,type_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
               
                mh2=Signinform()
                tochangeurl='Holidaytype_editfunction/id='+str(type_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    print 'type_id:'+str(type_id)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        a=datetime.date.today()
                        print 'newsession1'+str(newsession1)
                        if newsession1==xemail_id:
                            getforallvalue=LMS_HOLIDAY_TYPE.objects.all()
                            if len(getforallvalue)==0:
                                noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                                tochsngeurlfunction1='holidaytypetable_detail'
                                noentryintableordeletedcontent1='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
                            ####################when entry is deleted or not existing
                            product1 = LMS_HOLIDAY_TYPE.objects.filter(type_id =type_id)
                            if len(product1)==0:
                                noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                                tochsngeurlfunction1='holidaytypetable_detail'
                                noentryintableordeletedcontent1='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
            ########################    
                            product = LMS_HOLIDAY_TYPE.objects.get(pk=type_id)    
                            my_Holidaytypeedit_1=Holidaytypeform(instance=product)  
                            print 'holiday form hrrrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'my_Holidaytypeedit_1':my_Holidaytypeedit_1,'extra_object':extra_object,'type_id':type_id},RequestContext(request)) 
                
                    print 'inside except=================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Holidaytype_editfunction/id='+str(type_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Holidaytype_editfunction/id='+str(type_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
      
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print 'in the change function of holiday table-----------------------------------'
    type_id=type_id
    print 'type_id:'+str(type_id)
    a=datetime.date.today()
    #name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
    print 'extra_object:'+str(extra_object)
    #product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
    if request.method == 'POST':
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        myrequestpost['Holiday_Type']=myrequestpost['Holiday_Type'].title()
        product1 = LMS_HOLIDAY_TYPE.objects.filter(type_id=type_id)
        if len(product1)==0:
            print "length is 0"
            noentryintableordeletedcontent1='noentryintableordeletedcontent1'
            tochsngeurlfunction1='holidaytypetable_detail'
            noentryintableordeletedcontent1='nonewnotification'
            return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                  RequestContext(request))
        ########################
        product = LMS_HOLIDAY_TYPE.objects.get(pk=type_id)
        my_Holidaytype_edit = Holidaytypeform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        ##########this code is for cancel of the form######
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/holidaytype_tabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ########################################################
        if my_Holidaytype_edit.is_valid():
            print "Display Form"
 
            my_Holidaytype_edit.save()      
            print 'clicking on editttttttt'
            strUrl = '/holidaytype_tabledisplay/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)     
        return render_to_response('basic_form.html',{'my_Holidaytype_edit':my_Holidaytype_edit,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
            #my_object12=Holidaylistform(instance=product)
            #print 'my_object12:'+str(my_object12)
            for x in new_object1111:
                xemail_id=x.email_id 
                xemail_id=str(xemail_id)
                print 'xemail_id:'+str(xemail_id)
                
                if newsession1==xemail_id:
                    getforallvalue=LMS_HOLIDAY_TYPE.objects.all()
                    if len(getforallvalue)==0:
                        noentryintableordeletedcontent1='noentryintableordeletedcontent1'
                        tochsngeurlfunction1='holidaytypetable_detail'
                        noentryintableordeletedcontent1='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryintableordeletedcontent1':noentryintableordeletedcontent1,'tochsngeurlfunction1':tochsngeurlfunction1,'extra_object':extra_object},
                                      RequestContext(request))
                    product = LMS_HOLIDAY_TYPE.objects.get(pk=type_id)    
                    my_Holidaytypeedit_1=Holidaytypeform(instance=product)    
                    print ' of hrrrrrrrrrr'
                    return render_to_response('basic_form.html',{'my_Holidaytypeedit_1':my_Holidaytypeedit_1,'extra_object':extra_object,'type_id':type_id},RequestContext(request)) 
            print 'inside else =================='
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))



def Adminbasic_detail(request):
    admin=Employeeform()
    print 'nisha'
    a=datetime.date.today()
    return render_to_response('basic_form.html',{'admin':admin,'a':a,},RequestContext(request))

def admindisplay_detail(request):
    if request.method =='POST':
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['emp_name']
        myrequestpost['emp_name']=myrequestpost['emp_name'].title()
        myrequestpost['middle_name']=myrequestpost['middle_name'].title()
        myrequestpost['last_name']=myrequestpost['last_name'].title()
        myrequestpost['emp_current_address']=myrequestpost['emp_current_address'].title()
        myrequestpost['emp_permanent_address']=myrequestpost['emp_permanent_address'].title()
        myrequestpost['emp_bloodgroup']=myrequestpost['emp_bloodgroup'].title()
        print 'HERE I am'

        #adminmy_object4=Employeeform(request.POST)
        adminmy_object4=Employeeform(myrequestpost)
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/admindisplay_detail/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        print 'employeeform'
        if adminmy_object4.is_valid():
            print 'i m inside'
            
            #objmodel = my_object4.save(commit=False)
            adminmy_object4.save()
            print 'hi'
            #objmodel.save()
            #CODE FOR ASSIGNING THE VALUE TO SUMMARY TABLE
            print adminmy_object4.instance.pk
            emp_id=adminmy_object4.instance.pk
            print 'emp_id:'+str(emp_id)
            new_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
            for i in new_object:
                emp_id=i.emp_id
                emp_name=i.emp_name
                middle_name=i.middle_name  ## newentry
                last_name=i.last_name ##new entry
                emp_email_id=i.emp_email_id
                emp_position=i.emp_position
                emp_team=i.emp_team
                emp_id=i.emp_id
                emp_joining_date=i.emp_joining_date
                print 'emp_joining_date:'+str(emp_joining_date)
                print 'emp_email_id:'+str(emp_email_id)
                print 'emp_position:'+str(emp_position)
                print 'emp_team:'+str(emp_team)
                print 'emp_name:'+str(emp_name)
                print 'emp_id:'+str(emp_id)
            #emp_name=str(emp_name)
            emp_name=str(emp_name)
            middle_name=str(middle_name)
            last_name=str(last_name)
            full_name=emp_name+" "+middle_name+" "+last_name
            print 'fullname:'+str(full_name)
            current_year=datetime.date.today().year
            print current_year
           
            #emp_joining_date='03-19-2013'
            print 'emp_joning_date: '+str(emp_joining_date)
            s=emp_joining_date.split('-')
            #joining_year=s[2]
            joining_year=s[0]
            month=s[1]
            day=s[2]
            
            if current_year == (int)(joining_year):
                d1=date(int(current_year),01,01)
                d2=date(int(joining_year),int(month),int(day))
                days_left=(d2-d1).days
            else:
                days_left=0
            if ((int)(joining_year)%4)==0:
                days_in_current_year=366
            else:
                days_in_current_year=365
            casual_leave=(days_in_current_year-days_left)*(12/((float)(days_in_current_year)))
            sick_leave=(days_in_current_year-days_left)*(6/((float)(days_in_current_year)))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            sick_leave=int(round(sick_leave))
            casual_leave=int(round(casual_leave))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            print '-----------------------------------------------------------------'
            #----------------------------------------------------------------------------#
            emp_id=str(emp_id)
            createdmonth=datetime.date.today().month
            createdyear=datetime.date.today().year
            print 'createdyear:'+str(createdyear)
            print 'createdmonth:'+str(createdmonth)
            xyz=LMS_LEAVES_summary_TABLE()
            print 'xyz:'+str(xyz) 
            print emp_id
            
            #xyz.name_of_employee=emp_name
            xyz.name_of_employee=full_name
            xyz.total_casual_leaves=casual_leave
            xyz.total_sick_leaves=sick_leave 
            #xyz.emp_id_id=emp_id
            #xyz.current_casual_leaves=casual_leave
            #xyz.current_sick_leaves=sick_leave
            xyz.emp_id_of_employee=emp_id#####new addition
            xyz.eligiable_avaliable_leave=1.5####new addition
            xyz.d=createdmonth####new addition
            xyz.y=createdyear
            
            xyz.casual_leaves_used=00       
            xyz.sick_leaves_used=00
            xyz.leave_comp_off=00
            xyz.position=emp_position
            xyz.team=emp_team
            xyz.email_id=emp_email_id
            xyz.passwd='abc'
            print xyz.name_of_employee
            xyz.save() 
            print "why"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/admindisplay_detail/'
            return HttpResponseRedirect(sta_url)
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'adminmy_object4':adminmy_object4,},
                                  RequestContext(request))
    else:
        adminmy_object2 = LMS_EMPLOYEE_TABLE.objects.all()# for fetching all data from database
        
        return render_to_response('basic_form.html',{'adminmy_object2':adminmy_object2},
                                  RequestContext(request))



def adminedit(request, emp_id):
     
      
    
    a=datetime.date.today()
    
    #showname=str(name)
    #extra_object=LMS_LEAVES_summary_TABLE.objects.filter(name_of_employee=showname)
    d=datetime.date.today()
    print 'a:'+str(d)
    print "sapu"
    a=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
    for j in a:
        emp_name=j.emp_name
        middle_name=j.middle_name
        last_name=j.last_name
        emp_name=str(emp_name)
        middle_name=str(middle_name)
        last_name=str(last_name)
        full_name1=emp_name+" "+middle_name+" "+last_name
        print 'fullname1:'+str(full_name1)
        print 'emp of product:'+str(full_name1)
    product_emp_name=str(full_name1)
    print'product_emp_name:'+str(product_emp_name) 
        
    product = LMS_EMPLOYEE_TABLE.objects.get(pk=emp_id)
     
    if request.method == 'POST':
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['emp_name']
        myrequestpost['emp_name']=myrequestpost['emp_name'].title()
        myrequestpost['middle_name']=myrequestpost['middle_name'].title()
        myrequestpost['last_name']=myrequestpost['last_name'].title()
        myrequestpost['emp_current_address']=myrequestpost['emp_current_address'].title()
        myrequestpost['emp_permanent_address']=myrequestpost['emp_permanent_address'].title()
        myrequestpost['emp_bloodgroup']=myrequestpost['emp_bloodgroup'].title()
        #my_object5 = Employeeform(request.POST, instance=product)
        my_object5 = Employeeform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/admindisplay_detail/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        
        if my_object5.is_valid():
            print "Display Form"
     
            my_object5.save()
            print 'emp_id:'+str(emp_id)
            new_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
            for i in new_object:
                emp_name=i.emp_name
                middle_name=i.middle_name  ## newentry
                last_name=i.last_name ##new entry
                emp_email_id=i.emp_email_id
                emp_position=i.emp_position
                emp_team=i.emp_team
                emp_id=i.emp_id
                emp_joining_date=i.emp_joining_date
                print 'emp_joining_date:'+str(emp_joining_date)
                print 'emp_email_id:'+str(emp_email_id)
                print 'emp_position:'+str(emp_position)
                print 'emp_team:'+str(emp_team)
                print 'emp_name:'+str(emp_name)
            #emp_name=str(emp_name)
            emp_name=str(emp_name)
            middle_name=str(middle_name)
            last_name=str(last_name)
            full_name=emp_name+" "+middle_name+" "+last_name
            print 'fullname:'+str(full_name)
            current_year=datetime.date.today().year
            print current_year
           
            #emp_joining_date='03-19-2013'
            print 'emp_joning_date: '+str(emp_joining_date)
            s=emp_joining_date.split('-')
            #joining_year=s[2]
            joining_year=s[0]
            month=s[1]
            day=s[2]
            
            if current_year == (int)(joining_year):
                d1=date(int(current_year),01,01)
                d2=date(int(joining_year),int(month),int(day))
                days_left=(d2-d1).days
            else:
                days_left=0
            if ((int)(joining_year)%4)==0:
                days_in_current_year=366
            else:
                days_in_current_year=365
            casual_leave=(days_in_current_year-days_left)*(12/((float)(days_in_current_year)))
            sick_leave=(days_in_current_year-days_left)*(6/((float)(days_in_current_year)))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            sick_leave=int(round(sick_leave))
            casual_leave=int(round(casual_leave))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            print '-----------------------------------------------------------------'
            #----------------------------------------------------------------------------#
            # work for edit function
            #product_emp_name
            #xyz=LMS_LEAVES_summary_TABLE()
            print 'product_emp_name:'+str(product_emp_name)
            z1=LMS_LEAVES_summary_TABLE.objects.filter(name_of_employee=product_emp_name)
            print 'z1'
            print z1
            for i in z1:
                print 'inside for loop'
                summary_id=i.summary_id
                print 'summary_id:'+str(summary_id)

            xyz= LMS_LEAVES_summary_TABLE.objects.get(summary_id=summary_id)
            print 'xyz:'+str(xyz) 
            print emp_id
            createdmonth=datetime.date.today().month
            createdyear=datetime.date.today().year
            xyz.name_of_employee=full_name
            xyz.total_casual_leaves=casual_leave
            xyz.total_sick_leaves=sick_leave 
            #xyz.emp_id_id=emp_id
            #xyz.current_casual_leaves=casual_leave
            #xyz.current_sick_leaves=sick_leave
            xyz.emp_id_of_employee=emp_id#####new addition
            xyz.eligiable_avaliable_leave=1.5####new addition
            xyz.d=createdmonth####new addition
            xyz.y=createdyear
            xyz.casual_leaves_used=00    
            xyz.sick_leaves_used=00
            xyz.leave_comp_off=00
            xyz.position=emp_position
            xyz.team=emp_team
            xyz.email_id=emp_email_id
            xyz.passwd='abc'
            print xyz.name_of_employee
            print 'save is not working'
            xyz.save()
           
            print 'clicking on editttttttt' 
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/admindisplay_detail/'
            return HttpResponseRedirect(sta_url)    
           # return HttpResponseRedirect('/display_detail/')
        return render_to_response('basic_form.html',{'my_object5':my_object5,},
                                  RequestContext(request))
    else:
            my_object3=Employeeform(instance=product)
          
            return render_to_response('basic_form.html',{'my_object3':my_object3,},RequestContext(request))      
            
#                                    context_instance=RequestContext(request)) 

def admindelete(request,emp_id):
    a=datetime.date.today()
    print "delete"
    obj3 = LMS_EMPLOYEE_TABLE.objects.get(pk=emp_id)
    obj3.delete()
    #sta_url='/display_detail/name='+str(name)+'/'
    sta_url='/admindisplay_detail/'
    return HttpResponseRedirect(sta_url)

        
def adminHoliday_detail(request): 
   
    a=datetime.date.today()
    my_object8=Holidaylistform()
    
    return render_to_response('basic_form.html',{'my_object8':my_object8,'a':a,},RequestContext(request))
   


#@csrf_exempt
#def basic_detail(request,name=None):
def basic_detail(request):
     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='views/basic_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                    my_object=Employeeform()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            print 'xemail_id:'+str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'my_object':my_object,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='views/basic_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='views/basic_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
   
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1

    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)

    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    a=datetime.date.today()
    my_object=Employeeform()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            return render_to_response('basic_form.html',{'my_object':my_object,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))



#def display_detail(request,name=None):
def display_detail(request): 
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='display_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    print "inelse part"
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                      
                    my_object2 = LMS_EMPLOYEE_TABLE.objects.all()# for fetching all data from database
                    my_forall = LMS_EMPLOYEE_TABLE.objects.all()
                    print "display part"
                    newsession1=str(newsession1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        if newsession1==xemail_id:
                            if len(my_object2)==0: 
                                print 'len of if len(noticeforteamlead)==0: '
                                noentryinthetablefor_hrdisplaydetail='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetablefor_hrdisplaydetail':noentryinthetablefor_hrdisplaydetail,'extra_object':extra_object,},
                                      RequestContext(request))
                            return render_to_response('basic_form.html',{'my_object2':my_object2,'extra_object':extra_object},
                                      RequestContext(request))
        
                    print 'hiiii'
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

#                    if len(my_forall)==0: 
#                        print 'len of if len(noticeforteamlead)==0: '
#                        noentryinthetablefor_alldisplaydetail11='nonewnotification'
#                        return render_to_response('basic_form.html',{'noentryinthetablefor_alldisplaydetail11':noentryinthetablefor_alldisplaydetail11,'extra_object':extra_object,},
#                                  RequestContext(request))
#                    return render_to_response('basic_form.html',{'my_forall':my_forall,'extra_object':extra_object},
#                                  RequestContext(request))    

#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='display_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='display_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################

      
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
    for i in allsignupdata:
        name=i.name
    print 'in manage hierachy'
    name=str(name)
    print 'name:'+str(name)
    #extra_object=LMS_LEAVES_summary_TABLE.objects.filter(name_of_employee=name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)

    a=datetime.date.today()
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)      

    a=datetime.date.today()
    if request.method =='POST':
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['emp_name']
        myrequestpost['emp_name']=myrequestpost['emp_name'].title()
        myrequestpost['middle_name']=myrequestpost['middle_name'].title()
        myrequestpost['last_name']=myrequestpost['last_name'].title()
        myrequestpost['emp_current_address']=myrequestpost['emp_current_address'].title()
        myrequestpost['emp_permanent_address']=myrequestpost['emp_permanent_address'].title()
        myrequestpost['emp_bloodgroup']=myrequestpost['emp_bloodgroup'].title()
        print 'HERE I am'
        #my_object4=Employeeform(request.POST)myrequestpost
        my_object4=Employeeform(myrequestpost)
        print 'employeeform'
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/display_detail/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        
        if my_object4.is_valid():
            print 'i m inside'
            
            #objmodel = my_object4.save(commit=False)
            my_object4.save()
            print 'hi'
            #objmodel.save()
            #CODE FOR ASSIGNING THE VALUE TO SUMMARY TABLE
            print my_object4.instance.pk
            emp_id=my_object4.instance.pk
            print 'emp_id:'+str(emp_id)
            new_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
            for i in new_object:
                emp_id=i.emp_id
                emp_name=i.emp_name
                middle_name=i.middle_name #for middle name
                last_name=i.last_name # for last name
                emp_email_id=i.emp_email_id
                emp_position=i.emp_position
                emp_team=i.emp_team
                emp_id=i.emp_id
                emp_joining_date=i.emp_joining_date
                print 'emp_joining_date:'+str(emp_joining_date)
                print 'emp_email_id:'+str(emp_email_id)
                print 'emp_position:'+str(emp_position)
                print 'emp_team:'+str(emp_team)
                print 'emp_name:'+str(emp_name)
                print 'middle_name:'+str(middle_name)
                print 'last_name:'+str(last_name)
                print 'emp_id:'+str(emp_id)
            emp_name=str(emp_name)
            middle_name=str(middle_name)
            last_name=str(last_name)
            full_name=emp_name+" "+middle_name+" "+last_name
            print 'fullname:'+str(full_name)
            current_year=datetime.date.today().year
            print current_year
           
            #emp_joining_date='03-19-2013'
            print 'emp_joning_date: '+str(emp_joining_date)
            s=emp_joining_date.split('-')
            #joining_year=s[2]
            joining_year=s[0]
            month=s[1]
            day=s[2]
            
            if current_year == (int)(joining_year):
                d1=date(int(current_year),01,01)
                d2=date(int(joining_year),int(month),int(day))
                days_left=(d2-d1).days
            else:
                days_left=0
            if ((int)(joining_year)%4)==0:
                days_in_current_year=366
            else:
                days_in_current_year=365
            casual_leave=(days_in_current_year-days_left)*(12/((float)(days_in_current_year)))
            sick_leave=(days_in_current_year-days_left)*(6/((float)(days_in_current_year)))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            sick_leave=int(round(sick_leave))
            casual_leave=int(round(casual_leave))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            print '-----------------------------------------------------------------'
            #----------------------------------------------------------------------------#
            emp_id=str(emp_id)
            createdmonth=datetime.date.today().month
            createdyear=datetime.date.today().year
            print 'createdyear:'+str(createdyear)
            print 'createdmonth:'+str(createdmonth)
            xyz=LMS_LEAVES_summary_TABLE()
            print 'xyz:'+str(xyz) 
            print emp_id
            
            #xyz.name_of_employee=emp_name   #full_name
            xyz.name_of_employee=full_name
            xyz.total_casual_leaves=casual_leave
            xyz.total_sick_leaves=sick_leave 
            #xyz.emp_id_id=emp_id
            #xyz.current_casual_leaves=casual_leave
            #xyz.current_sick_leaves=sick_leave
            xyz.emp_id_of_employee=emp_id#####new addition
            xyz.eligiable_avaliable_leave=1.5####new addition
            xyz.d=createdmonth####new addition
            xyz.y=createdyear
            
            xyz.casual_leaves_used=0.0       
            xyz.sick_leaves_used=0.0
            xyz.leave_comp_off=0.0
            xyz.position=emp_position
            xyz.team=emp_team
            xyz.email_id=emp_email_id
            xyz.passwd='abc'
            print xyz.name_of_employee
            xyz.save() 
            print "why"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/display_detail/'
            return HttpResponseRedirect(sta_url)
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'my_object4':my_object4,'name':name,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        my_object2 = LMS_EMPLOYEE_TABLE.objects.all()# for fetching all data from database
        my_forall = LMS_EMPLOYEE_TABLE.objects.all()
        for x in new_object1111:
            xemail_id=x.email_id 
            xemail_id=str(xemail_id)
            if newsession1==xemail_id:
                if len(my_object2)==0: 
                    print 'len of if len(noticeforteamlead)==0: '
                    noentryinthetablefor_hrdisplaydetail='nonewnotification'
                    return render_to_response('basic_form.html',{'noentryinthetablefor_hrdisplaydetail':noentryinthetablefor_hrdisplaydetail,'extra_object':extra_object,},
                                      RequestContext(request))
                return render_to_response('basic_form.html',{'my_object2':my_object2,'a':a,'name':name,'extra_object':extra_object},
                                      RequestContext(request))
        invaliduser='invalid'
        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
    
#        if len(my_forall)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            noentryinthetablefor_alldisplaydetail11='nonewnotification'
#            return render_to_response('basic_form.html',{'noentryinthetablefor_alldisplaydetail11':noentryinthetablefor_alldisplaydetail11,'extra_object':extra_object,},
#                                  RequestContext(request))    
#        return render_to_response('basic_form.html',{'my_forall':my_forall,'a':a,'name':name,'extra_object':extra_object},
#                                  RequestContext(request))    



#def edit(request, emp_id,name=None):
def edit(request, emp_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                print 'employee_id:'+str(emp_id)
                mh2=Signinform()
                tochangeurl='views/edit/id='+str(emp_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    print 'employee_id:'+str(emp_id)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    d=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        print 'a:'+str(d)
                        if newsession1==xemail_id:
                            getforallvalue=LMS_EMPLOYEE_TABLE.objects.all()
                            if len(getforallvalue)==0:
                                print "length is 0"
                                noentryinthetablefor_hrdisplaydetail='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetablefor_hrdisplaydetail':noentryinthetablefor_hrdisplaydetail,'extra_object':extra_object,},
                                      RequestContext(request))
                             ####################when entry is deleted or doesnot exist
                            product1 = LMS_EMPLOYEE_TABLE.objects.filter(emp_id =emp_id)
                            if len(product1)==0:
                                print "length is 0"
                                noentryinthetableforeditbasichr='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetableforeditbasichr':noentryinthetableforeditbasichr,'extra_object':extra_object,},
                                      RequestContext(request))
                                 ########################    
                            product = LMS_EMPLOYEE_TABLE.objects.get(pk=emp_id)
                            my_object3=Employeeform(instance=product)
                            print 'holiday form hrrrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'my_object3':my_object3,'d':d,'extra_object':extra_object},RequestContext(request))      
                    print 'inside else =================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='views/edit/id='+str(emp_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='views/edit/id='+str(emp_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
##################################################################################################
   
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1

    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)

     
    if request.method == 'POST':
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['emp_name']
        myrequestpost['emp_name']=myrequestpost['emp_name'].title()
        myrequestpost['middle_name']=myrequestpost['middle_name'].title()
        myrequestpost['last_name']=myrequestpost['last_name'].title()
        myrequestpost['emp_current_address']=myrequestpost['emp_current_address'].title()
        myrequestpost['emp_permanent_address']=myrequestpost['emp_permanent_address'].title()
        myrequestpost['emp_bloodgroup']=myrequestpost['emp_bloodgroup'].title()
        print 'HERE I am'
        a=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
        for j in a:
            emp_name=j.emp_name
            middle_name=j.middle_name
            last_name=j.last_name
        print 'emp of product:'+str(emp_name)
        product_emp_name=str(emp_name)+" "+str(middle_name)+" "+str(last_name)
        product_emp_name=str(product_emp_name)
        print'product_emp_name:'+str(product_emp_name) 
        ####################when entry is deleted or doesnot exist
        product1 = LMS_EMPLOYEE_TABLE.objects.filter(emp_id =emp_id)
        if len(product1)==0:
            print "length is 0"
            noentryinthetableforeditbasichr='nonewnotification'
            return render_to_response('basic_form.html',{'noentryinthetableforeditbasichr':noentryinthetableforeditbasichr,'extra_object':extra_object,},
                    RequestContext(request))
                             ########################       
        product = LMS_EMPLOYEE_TABLE.objects.get(pk=emp_id)
        #my_object5 = Employeeform(request.POST, instance=product)
        my_object5 = Employeeform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/display_detail/'
            return HttpResponseRedirect(sta_url)
        ##############################################################
        
        if my_object5.is_valid():
            print "Display Form"
 
#            joining_date = my_object5.cleaned_data['emp_joining_date']
#            (casual_leave,sick_leave)=my_object5.Calculate_leave(joining_date)
#            objmodel = my_object5.save(commit=False)
#            (objmodel.leaves_quota_year_casual, objmodel.leaves_quota_year_sick) = (int(round(casual_leave)), int(round(sick_leave)))
##           
#            print 'hi'
#            print casual_leave
#
#            objmodel.save()      
            my_object5.save()
            print 'emp_id:'+str(emp_id)
            new_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
            for i in new_object:
                emp_name=i.emp_name
                middle_name=i.middle_name
                last_name=i.last_name
                emp_email_id=i.emp_email_id
                emp_position=i.emp_position
                emp_team=i.emp_team
                emp_id=i.emp_id
                emp_joining_date=i.emp_joining_date
                print 'emp_joining_date:'+str(emp_joining_date)
                print 'emp_email_id:'+str(emp_email_id)
                print 'emp_position:'+str(emp_position)
                print 'emp_team:'+str(emp_team)
                print 'emp_name:'+str(emp_name)
                
            emp_name=str(emp_name)
            middle_name=str(middle_name)
            last_name=str(last_name)
            full_name=emp_name+" "+middle_name+" "+last_name
            current_year=datetime.date.today().year
            print current_year
           
            #emp_joining_date='03-19-2013'
            print 'emp_joning_date: '+str(emp_joining_date)
            s=emp_joining_date.split('-')
            #joining_year=s[2]
            joining_year=s[0]
            month=s[1]
            day=s[2]
            
            if current_year == (int)(joining_year):
                d1=date(int(current_year),01,01)
                d2=date(int(joining_year),int(month),int(day))
                days_left=(d2-d1).days
            else:
                days_left=0
            if ((int)(joining_year)%4)==0:
                days_in_current_year=366
            else:
                days_in_current_year=365
            casual_leave=(days_in_current_year-days_left)*(12/((float)(days_in_current_year)))
            sick_leave=(days_in_current_year-days_left)*(6/((float)(days_in_current_year)))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            sick_leave=int(round(sick_leave))
            casual_leave=int(round(casual_leave))
            print 'casual_leave: '+str(casual_leave)
            print 'sick_leave:'+str(sick_leave)
            print '-----------------------------------------------------------------'
            #----------------------------------------------------------------------------#
            # work for edit function
            #product_emp_name
            #xyz=LMS_LEAVES_summary_TABLE()
            print 'product_emp_name:'+str(product_emp_name)
            #z1=LMS_LEAVES_summary_TABLE.objects.filter(name_of_employee=product_emp_name)
            z1=LMS_LEAVES_summary_TABLE.objects.filter(emp_id_of_employee=emp_id)####by emp_id
            print 'z1'
            print z1
            for i in z1:
                print 'inside for loop'
                summary_id=i.summary_id
                eligiable_avaliable_leave=i.eligiable_avaliable_leave
                casual_leaves_used=i.casual_leaves_used
                sick_leaves_used=i.sick_leaves_used
                leave_comp_off=i.leave_comp_off
            summary_id=str(summary_id)    
            print 'summary_id:'+str(summary_id)

            xyz= LMS_LEAVES_summary_TABLE.objects.get(summary_id=summary_id)
            print 'xyz:'+str(xyz) 
            print emp_id
            createdmonth=datetime.date.today().month
            createdyear=datetime.date.today().year
            #xyz.name_of_employee=emp_name #full_name
            xyz.name_of_employee=full_name
            xyz.total_casual_leaves=casual_leave
            xyz.total_sick_leaves=sick_leave 
            #xyz.emp_id_id=emp_id
            #xyz.current_casual_leaves=casual_leave
            #xyz.current_sick_leaves=sick_leave
            xyz.emp_id_of_employee=emp_id#####new addition
            xyz.eligiable_avaliable_leave=eligiable_avaliable_leave####new addition
            xyz.d=createdmonth####new addition
            xyz.y=createdyear
            xyz.casual_leaves_used=casual_leaves_used    
            xyz.sick_leaves_used=sick_leaves_used
            xyz.leave_comp_off=leave_comp_off
            xyz.position=emp_position
            xyz.team=emp_team
            xyz.email_id=emp_email_id
            xyz.passwd='abc'
            print xyz.name_of_employee
            print 'save is not working'
            xyz.save()
           
            print 'clicking on editttttttt' 
            #sta_url='/display_detail/name='+str(showname)+'/'
            sta_url='/display_detail/'
            return HttpResponseRedirect(sta_url)    
           # return HttpResponseRedirect('/display_detail/')
        return render_to_response('basic_form.html',{'my_object5':my_object5,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
            #my_object3=Employeeform(instance=product)
            for x in new_object1111:
                xemail_id=x.email_id 
                xemail_id=str(xemail_id)
                if newsession1==xemail_id:
                    getforallvalue=LMS_EMPLOYEE_TABLE.objects.all()
                    if len(getforallvalue)==0:
                        print "length is 0"
                        noentryinthetablefor_hrdisplaydetail='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryinthetablefor_hrdisplaydetail':noentryinthetablefor_hrdisplaydetail,'extra_object':extra_object,},
                                      RequestContext(request))
                    print 'clicking on edit'
                    ####################when entry is deleted or doesnot exist
                    product1 = LMS_EMPLOYEE_TABLE.objects.filter(emp_id =emp_id)
                    if len(product1)==0:
                        print "length is 0"
                        noentryinthetableforeditbasichr='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryinthetableforeditbasichr':noentryinthetableforeditbasichr,'extra_object':extra_object,},
                        RequestContext(request))
                                 ######################## 
                    product = LMS_EMPLOYEE_TABLE.objects.get(pk=emp_id)
                    my_object3=Employeeform(instance=product)
                    return render_to_response('basic_form.html',{'my_object3':my_object3,'extra_object':extra_object},RequestContext(request))      
            print 'inside else =================='
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))


#                                    context_instance=RequestContext(request)) 

        
#@csrf_exempt
#def delete_new(request,emp_id,name=None):

def delete_new(request,emp_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:    
        print 'username length less equal to zero which means user is logout.and session is deleted '
        my_object6=Signinform()
        print 'nisha'
        return render_to_response('new_form1.html',{'my_object6':my_object6},RequestContext(request))
##################################################################################################
       
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
#    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#    for i in allsignupdata:
#        name=i.name
#    print 'in manage hierachy'
#    name=str(name)
#    print 'name:'+str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    print "delete"
    obj3 = LMS_EMPLOYEE_TABLE.objects.get(pk=emp_id)
    obee33=LMS_EMPLOYEE_TABLE.objects.filter(emp_id=emp_id)
    for jh in obee33:
        emp_email_id=jh.emp_email_id
    emp_email_id=str(emp_email_id)
    print 'emp_email_id:LMS_EMPLOYEE_TABLE:'+str(emp_email_id)
    obj_test1=LMS_LEAVES_summary_TABLE.objects.filter(email_id=emp_email_id)
    print 'len(obj_test1):'+str(len(obj_test1))
    for jh1 in obj_test1:
        summary_id=jh1.summary_id
    summary_id=str(summary_id)
    print 'summary_id :'+str(summary_id)
    obj_test2=LMS_LEAVES_summary_TABLE.objects.get(pk=summary_id)#####to delete
    obj_test3=LMS_SIGNUP.objects.filter(username=emp_email_id)
    print 'len(obj_test3):'+str(len(obj_test3))
    #for jh2 in obj_test3:
    #    signup_id=jh2.signup_id
    #signup_id=str(signup_id)
    #print 'signup_id:'+str(signup_id)
    #obj_test4=LMS_SIGNUP.objects.get(pk=signup_id)###to delete
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for ka in testposition:
        emp_position_id=ka.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for xrt in new_object1111:
        xemail_id=xrt.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        print 'emp_email_id:'+str(emp_email_id)
        if emp_email_id==xemail_id:
            print 'match of emp_email_id==xemailid:'
            email_hrmessage='cannot delete'
            return render_to_response('basic_form.html',{'email_hrmessage':email_hrmessage,'extra_object':extra_object},RequestContext(request))
            
    obj_test2.delete()#to delete
    print 'deleted2'
    
    obj3.delete()
    print 'deleted3'
    if len(obj_test3)==0:
        print 'no entry to delte'
    else:    
        for jh2 in obj_test3:
            signup_id=jh2.signup_id
        signup_id=str(signup_id)
        print 'signup_id:'+str(signup_id)
        obj_test4=LMS_SIGNUP.objects.get(pk=signup_id)###to delete
        obj_test4.delete()#to delete
        print 'deleted1'
    sta_url='/display_detail/'
    return HttpResponseRedirect(sta_url)
    #return HttpResponseRedirect('/display_detail/')

#@csrf_exempt
def delete_all(request):
    print"delete all"
    obj3=LMS_EMPLOYEE_TABLE.objects.all().delete()
    return HttpResponseRedirect('/display_detail/')  



####code for holiday list page
#def Holiday_detail(request,name=None):
def Holiday_detail(request): 
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='views/Holiday_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1) 
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)  
                    
                    a=datetime.date.today()
                    my_object8=Holidaylistform()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            print 'xemail_id:'+str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'my_object8':my_object8,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='views/Holiday_detail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='views/Holiday_detail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1

    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    a=datetime.date.today()
    my_object8=Holidaylistform()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            print 'holiday form of hrrrrrrrrrr'
            return render_to_response('basic_form.html',{'my_object8':my_object8,'extra_object':extra_object},RequestContext(request))
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))


#def Holiday_display(request,name=None):
def Holiday_display(request):    
    print 'in holiday display page'
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='Holiday_display'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    
                    my_object10 = LMS_HOLIDAY_LIST.objects.all()# for fetching all data from database
                    allmy_object10 = LMS_HOLIDAY_LIST.objects.all()
                    print "display part"
                    newsession1=str(newsession1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        if newsession1==xemail_id:
                            if len(my_object10)==0: 
                                print 'len of if len(noticeforteamlead)==0: '
                                noentryinthetableforhrholiday='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetableforhrholiday':noentryinthetableforhrholiday,'extra_object':extra_object,},
                                      RequestContext(request))
                            return render_to_response('basic_form.html',{'my_object10':my_object10,'a':a,'extra_object':extra_object},
                                    RequestContext(request))
        
                    print my_object10
                    if len(allmy_object10)==0: 
                        print 'len of if len(noticeforteamlead)==0: '
                        noentryinthetablefor_allholiday11='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryinthetablefor_allholiday11':noentryinthetablefor_allholiday11,'extra_object':extra_object,},
                                  RequestContext(request))
                    return render_to_response('basic_form.html',{'allmy_object10':allmy_object10,'a':a,'extra_object':extra_object},
                                  RequestContext(request))
#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='Holiday_display'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='Holiday_display'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print request.POST    
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)       
    if request.method =='POST':  
        print 'HERE I am'
        #this code is for the cancel button######################
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/Holiday_display/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ##############################################################
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['holiday_called']
        myrequestpost['holiday_called']=myrequestpost['holiday_called'].title()
        print 'HERE I am'
        #my_object9=Holidaylistform(request.POST)
        my_object9=Holidaylistform(myrequestpost)
        if my_object9.is_valid():
            print 'i m inside'
            my_object9.save()
            print "why ?????????????????????????????????????????????????????????????????????????????"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/Holiday_display/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
            #return HttpResponseRedirect('/Holiday_display/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'my_object9':my_object9,'extra_object':extra_object},
                                  RequestContext(request))
    else:
        print "inelse part"
        a=datetime.date.today()
        my_object10 = LMS_HOLIDAY_LIST.objects.all()# for fetching all data from database
        allmy_object10 = LMS_HOLIDAY_LIST.objects.all()
        print "display part"
        newsession1=str(newsession1)
        for x in new_object1111:
            xemail_id=x.email_id 
            xemail_id=str(xemail_id)
            if newsession1==xemail_id:
                if len(my_object10)==0: 
                    print 'len of if len(noticeforteamlead)==0: '
                    noentryinthetableforhrholiday='nonewnotification'
                    return render_to_response('basic_form.html',{'noentryinthetableforhrholiday':noentryinthetableforhrholiday,'extra_object':extra_object,},
                                      RequestContext(request))
                return render_to_response('basic_form.html',{'my_object10':my_object10,'extra_object':extra_object},
                                      RequestContext(request))
        #check length for all user other then hr
        if len(allmy_object10)==0: 
                print 'len of if len(noticeforteamlead)==0: '
                noentryinthetablefor_allholiday11='nonewnotification'
                return render_to_response('basic_form.html',{'noentryinthetablefor_allholiday11':noentryinthetablefor_allholiday11,'extra_object':extra_object,},
                                  RequestContext(request))
        return render_to_response('basic_form.html',{'allmy_object10':allmy_object10,'extra_object':extra_object},
                                  RequestContext(request))
        
#def change(request,holiday_id,name=None):
def change(request,holiday_id): 
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                print 'holiday_id:'+str(holiday_id)
                mh2=Signinform()
                tochangeurl='views/change/id='+str(holiday_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)

                    print 'holiday_id:'+str(holiday_id)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    
                    #if there is no entry in the code
#                    getforallvalue=LMS_HOLIDAY_LIST.objects.all()
#                    if len(getforallvalue)==0:
#                        print "length is 0"
#                        noentryinthetablefor_hrholiday_edit='nonewnotification'
#                        return render_to_response('basic_form.html',{'noentryinthetablefor_hrholiday_edit':noentryinthetablefor_hrholiday_edit,'extra_object':extra_object,},
#                                  RequestContext(request))
                    #########################################    
                    #product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
                    a=datetime.date.today()
                    #my_object12=Holidaylistform(instance=product)
                    print 'newsession1'+str(newsession1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                        if newsession1==xemail_id:
                            getforallvalue=LMS_HOLIDAY_LIST.objects.all()
                            if len(getforallvalue)==0:
                                print "length is 0"
                                noentryinthetablefor_hrholiday_edit='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetablefor_hrholiday_edit':noentryinthetablefor_hrholiday_edit,'extra_object':extra_object,},
                                      RequestContext(request))
                            ####################when entry is deleted or not existing
                            product1 = LMS_HOLIDAY_LIST.objects.filter(holiday_id =holiday_id)
                            if len(product1)==0:
                                print "length is 0"
                                noentryinthetable='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                      RequestContext(request))
            ########################    
                            product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
                            my_object12=Holidaylistform(instance=product)
                            print 'holiday form hrrrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'my_object12':my_object12,'extra_object':extra_object,'holiday_id':holiday_id},RequestContext(request)) 
                    
                    print 'inside except=================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='views/change/id='+str(holiday_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='views/change/id='+str(holiday_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
      
    ################session using###############
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
#    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#    for i in allsignupdata:
#        name=i.name
#    print 'in Holiday_display'
#    name=str(name)
#    print 'name:'+str(name)
#    ##############################################
    print 'in the change function of holiday table-----------------------------------'
    holiday_id=holiday_id
    print 'holiday_id:'+str(holiday_id)
    a=datetime.date.today()
    #name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
    print 'extra_object:'+str(extra_object)
    #product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
    if request.method == 'POST':
        
        print request.POST
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        print myrequestpost['holiday_called']
        myrequestpost['holiday_called']=myrequestpost['holiday_called'].title()
        #my_object11 = Holidaylistform(request.POST, instance=product)
        ####################when entry is deleted or doesnot exist
        product1 = LMS_HOLIDAY_LIST.objects.filter(holiday_id =holiday_id)
        if len(product1)==0:
            print "length is 0"
            noentryinthetable='nonewnotification'
            return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                  RequestContext(request))
        ########################
        product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
        my_object11 = Holidaylistform(myrequestpost, instance=product)
        print "PRODUCTchecking POST"
        ##########this code is for cancel of the form######
        if 'cancel1' in request.POST:
            print "inside cancel"
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/Holiday_display/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)
        ########################################################
        if my_object11.is_valid():
            print "Display Form"

#            product2 = my_object11.save( commit=False )
#            product2.save() 
            my_object11.save()      
            print 'clicking on editttttttt'
            #strUrl = '/Holiday_display/name='+str(name)
            strUrl = '/Holiday_display/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)     
            #return HttpResponseRedirect('/Holiday_display/')
        return render_to_response('basic_form.html',{'my_object11':my_object11,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
            #my_object12=Holidaylistform(instance=product)
            #print 'my_object12:'+str(my_object12)
            for x in new_object1111:
                xemail_id=x.email_id 
                xemail_id=str(xemail_id)
                print 'xemail_id:'+str(xemail_id)
                if newsession1==xemail_id:
                    getforallvalue=LMS_HOLIDAY_LIST.objects.all()
                    if len(getforallvalue)==0:
                        print "length is 0"
                        noentryinthetablefor_hrholiday_edit='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryinthetablefor_hrholiday_edit':noentryinthetablefor_hrholiday_edit,'extra_object':extra_object,},
                                      RequestContext(request))
                    product = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)    
                    my_object12=Holidaylistform(instance=product)    
                    print ' of hrrrrrrrrrr'
                    return render_to_response('basic_form.html',{'my_object12':my_object12,'extra_object':extra_object,'holiday_id':holiday_id},RequestContext(request)) 
            print 'inside else =================='
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

            #print 'clicking on edit*********************************************************'
            #return render_to_response('basic_form.html',{'my_object12':my_object12,'a':a,'name':name,'extra_object':extra_object,'holiday_id':holiday_id},RequestContext(request)) 
        
        
#def eliminate(request,holiday_id,name=None):
def eliminate(request,holiday_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:    
        print 'username length less equal to zero which means user is logout.and session is deleted '
        my_object6=Signinform()
        print 'nisha'
        return render_to_response('new_form1.html',{'my_object6':my_object6},RequestContext(request))
##################################################################################################
       
    print 'deleting the element@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
    for i in allsignupdata:
        name=i.name
    print 'in manage hierachy'
    name=str(name)
    print 'name:'+str(name)
    name=str(name)
    print "delete"
    objx = LMS_HOLIDAY_LIST.objects.get(pk=holiday_id)
    objx.delete()
    #strUrl = '/Holiday_display/name='+str(name)
    strUrl = '/Holiday_display/'
    print 'url:'+str(strUrl)
    return HttpResponseRedirect(strUrl)
    #return HttpResponseRedirect('/Holiday_display/') 
def waste_function(request,name=None):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='views/waste_function'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    ############################################################
#                    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#                    for i in allsignupdata:
#                        name=i.name
#                    print 'in Holiday_display'
#                    name=str(name)
#                    print 'name:'+str(name)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                    newsession1=str(newsession1)
                    
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            print 'xemail_id:'+str(xemail_id)
                            if newsession1==xemail_id:
                                getforallvalue=LMS_HOLIDAY_LIST.objects.all()
                                if len(getforallvalue)==0:
                                    print "length is 0"
                                    noentryinthetablefor_hrholiday_edit='nonewnotification'
                                    return render_to_response('basic_form.html',{'noentryinthetablefor_hrholiday_edit':noentryinthetablefor_hrholiday_edit,'extra_object':extra_object,},
                                      RequestContext(request))
                                zp='abc'
                                return render_to_response('basic_form.html',{'zp':zp,'a':a,'name':name,'extra_object':extra_object},RequestContext(request)) 
    
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'a':a,'name':name,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='views/waste_function'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='views/waste_function'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
##################################################################################################
   
    print"delete all question function"
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
#    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#    for i in allsignupdata:
#        name=i.name
#    print 'in manage hierachy'
#    name=str(name)
#    print 'name:'+str(name)
    a=datetime.date.today()
#    name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    newsession1=str(newsession1)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            zp='abc'
            return render_to_response('basic_form.html',{'zp':zp,'extra_object':extra_object},RequestContext(request)) 
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

#    strUrl = '/Holiday_display/name='+str(name)


def all_delete(request):
     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='views/all_delete'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    ############################################################
#                    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#                    for i in allsignupdata:
#                        name=i.name
#                    print 'in Holiday_display'
#                    name=str(name)
#                    print 'name:'+str(name)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id)
                    
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            print 'xemail_id:'+str(xemail_id)
                            if newsession1==xemail_id:
                                getforallvalue=LMS_HOLIDAY_LIST.objects.all()
                                if len(getforallvalue)==0:
                                    print "length is 0"
                                    noentryinthetablefor_hrholiday_edit='nonewnotification'
                                    return render_to_response('basic_form.html',{'noentryinthetablefor_hrholiday_edit':noentryinthetablefor_hrholiday_edit,'extra_object':extra_object,},
                                      RequestContext(request))
                                objy=LMS_HOLIDAY_LIST.objects.all().delete()
                                zab='abc'
                                return render_to_response('basic_form.html',{'zab':zab,'extra_object':extra_object},RequestContext(request)) 
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='views/all_delete'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='views/all_delete'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
    #################################
    print"delete all"
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
#    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#    for i in allsignupdata:
#        name=i.name
#    print 'in manage hierachy'
#    name=str(name)
#    print 'name:'+str(name)
#    a=datetime.date.today()
#    name=str(name)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    print 'extra_object:'+str(extra_object)
  
    for j in extra_object:
        team=j.team
        name=j.name_of_employee
        name=str(name)
        team=str(team)
    new_object=LMS_TEAM.objects.filter(emp_team=team)
    for i in new_object:
        mh1=(i.mh1).strip()
        mh2=(i.mh2).strip()
        mh3=(i.mh3).strip()
        mh1=str(mh1)
        mh2=str(mh2)
        mh3=str(mh3)
    print 'mh1:'+str(mh1)
    print 'mh2:'+str(mh2)
    print 'mh3:'+str(mh3)   
    print 'name:'+str(name)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    newsession1=str(newsession1)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            objy=LMS_HOLIDAY_LIST.objects.all().delete()
            zab='abc'
            return render_to_response('basic_form.html',{'zab':zab,'extra_object':extra_object},RequestContext(request)) 
    print 'inside else =================='
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

#    strUrl = '/Holiday_display/name='+str(name)
#    print 'url:'+str(strUrl)
#    return HttpResponseRedirect(strUrl)
    #return HttpResponseRedirect('/Holiday_display/')         
####show case of delete 


###code for signup page
## to delete the session####
def stupidsessiondeleteit(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:    
        print 'username length less equal to zero which means user is logout.and session is deleted '
        my_object6=Signinform()
        print 'nisha'
        return render_to_response('new_form1.html',{'my_object6':my_object6},RequestContext(request))
##################################################################################################
   
   
    stupidsession=Signinform()
    print 'nisha'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    ####this is for session code#########
    try:
        print 'we are to delete the session'
        #print request.session['signup_id']
        print request.session['username']
        #del request.session['signup_id']
        del request.session['username']
        print 'we deleted the session'
    except KeyError:
        pass
#   ############################################# 
    #return render_to_response('basic_form.html',{'my_object6':my_object6},RequestContext(request))
    return render_to_response('new_form1.html',{'stupidsession':stupidsession},RequestContext(request))

############################

def access_userbasic_detail1(request):
    my_object6=Signinform()
    print 'nisha'
    ####this is for session code#########
#    try:
#        print 'we are to delete the session'
#        del request.session['signup_id']
#        print 'we deleted the session'
#    except KeyError:
#        pass
#   ############################################# 
    #return render_to_response('basic_form.html',{'my_object6':my_object6},RequestContext(request))
    return render_to_response('new_form1.html',{'my_object6':my_object6},RequestContext(request))


#def login(request,name=None):
def login(request): 
    #if session is not active##
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print 'session doesnot exist'
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='login'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    print 'session doesnot exist'
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='login'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='login'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################    
   #if the submitt button selected is login
    print request.POST
    if 'LOGIN' in request.POST:
        print "inside login"
        u_name=request.POST['username']
        u_pass=request.POST['password']
        print 'u_name:'+u_name,'u_pass:'+u_pass
        if u_name=='' and u_pass=='':
            print 'the username and password are empty'
            sblank=Signinform()
            return render_to_response('new_form1.html',{'sblank':sblank},RequestContext(request))
        try:
            print 'username:' 
            if LMS_SIGNUP.objects.get(username=u_name) and LMS_SIGNUP.objects.get(password=u_pass): 
                print "username and password matches to database"
               ##########this code is for session  #################
                request.session['username']=LMS_SIGNUP.objects.get(username=u_name).username
                print 'we are using session ie database session'
                print request.session['username']
               ############################################               
                my_object7=LMS_LEAVES_summary_TABLE.objects.filter(email_id=u_name)    
                a=datetime.date.today()
                print a
                ob10=LMS_NEWS.objects.filter(entigence_date=datetime.date.today())
# $$$$$$$$$$$$$$$this part is admin(hr)####################################################3
                testposition=LMS_POSITION.objects.filter(emp_position='HR')
                for k in testposition:
                    emp_position_id=k.emp_position_id
                print 'emp_position_id:'+str(emp_position_id)         
                new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                for x in new_object1111:
                    xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)  
                    if u_name==xemail_id:
                        HR=LMS_LEAVES_summary_TABLE.objects.filter(email_id=u_name)
                    
                        return render_to_response('basic_form.html',{'HR':HR,'ob10':ob10,'a':a,},RequestContext(request))
                        
                 ##################################################################3        
                    
                ob10=LMS_NEWS.objects.filter(entigence_date=datetime.date.today())
                print ob10
                return render_to_response('basic_form.html',{'my_object7':my_object7,'ob10':ob10,'a':a,},RequestContext(request))

                
        except:
            print "not in database" ###when password or username does not match database       
            sblank=Signinform()
            return render_to_response('new_form1.html',{'sblank':sblank},RequestContext(request))
            #return HttpResponseRedirect('/access_userbasic_detail1/')    
        
    #if the submitt button selected  is forgot password
    if 'FORGOT' in request.POST:
        print request.POST
        print 'forgot password' 
    ##this is addition to slove the login link problem which is not working due to htttp response problem
    #this code is for the login button button######################
    if 'cancel1' in request.POST:
        print "inside signup"
        strUrl = '/captcha2/'
        print 'url:'+str(strUrl)
        return HttpResponseRedirect(strUrl)
    ##############################################################
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
        print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        print 'outside try and catch and if'
        if newsession1==xemail_id:
            print 'hr'
            HR=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)   
            return render_to_response('basic_form.html',{'HR':HR,},RequestContext(request))
    print 'other user'
    my_object7=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    return render_to_response('basic_form.html',{'my_object7':my_object7,},RequestContext(request))
#################################################################

       
        
    
###notification page
#def notice(request,name=None):
def notice(request): 
    print 'notice form'
     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='notification1'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
#                    ############################################################
#                    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#                    for i in allsignupdata:
#                        name=i.name
#                    print 'in manage hierachy'
#                    name=str(name)
#                    print 'name:'+str(name)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    for j in extra_object:
                        name=j.name_of_employee
                        teamtocheck=j.team
                    name=str(name)
                    print 'name:'+str(name)
                    extra_object1=LMS_LEAVES_summary_TABLE.objects.filter(Q(position='202') | Q(position='205'))
                    print 'extra_object1:'+str(extra_object1) 
                    nameforsc_andhr=[]
                    for j in extra_object1:
                        nameforsc_andhr1=j.name_of_employee
                        nameforsc_andhr.append(str(nameforsc_andhr1))
                    print 'nameforsc_andhr:'
                    print nameforsc_andhr
                    g=nameforsc_andhr[0]
                    print 'g:'+str(g)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    for i in extra_object:
                        team=i.team
                        email_id=i.email_id
                        position=i.position
                        print 'position:'+str(position)
                        print 'team:'+str(team)
                        print 'emailid:'+str(email_id)
                    a=datetime.date.today()
                    email_id=str(email_id)
                    new_object=LMS_TEAM.objects.filter(emp_team=team)
                    e=email_id.split('@')
                    e=e[0] 
                    e=str(e)
                    for i in new_object:
                        mh1=(i.mh1).strip()
                        mh2=(i.mh2).strip()
                        mh3=(i.mh3).strip()
                        mh1=str(mh1)
                        mh2=str(mh2)
                        mh3=str(mh3)
                    print 'mh1:'+str(mh1)
                    print 'mh2:'+str(mh2)
                    print 'mh3:'+str(mh3)
                    print 'to check which emailid is of manager ,teamlead and hr'
                    if email_id==mh2:
                        print 'manager'
                        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
                        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Senior Consultant') | Q(leaves_approved_by_manager='Hr'),leaves_status='Active')
                        print len(notice1)
                        e=email_id.split('@')
                        e=e[0] 
                        e=str(e) 
        
                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='notification1'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='notification1'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
    ###################################################################################################
   
    #make changes to show notification 
    print 'request.signup_id*********************************'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    print 'session active:'
     
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    detailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_email_id=newsession1)
    for i in detailsnew_object:
        emp_number=i.emp_number
        emp_name=i.emp_name
        emp_position=i.emp_position
        emp_team=i.emp_team
        name=str(emp_name)    
        emp_team=str(emp_team)    
        emp_position=str(emp_position)    
    print 'emp_number:'+str(emp_number)
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
    xemail_id=str(xemail_id)
    print 'xemail_id of hr:'+str(xemail_id)
    
    supervisordetails= LMS_SUPERVISORHIERACHY.objects.filter(supervisor_number=emp_number) 
    for j in supervisordetails:
        emp_numberofemployeewhosesupervisoris_session=j.emp_number
        supervisor_number=j.supervisor_number
        emp_teamof_supervisor=j.emp_team
        emp_numberofemployeewhosesupervisoris_session=str(emp_numberofemployeewhosesupervisoris_session)
        emp_numberofemployeewhosesupervisoris_session=emp_numberofemployeewhosesupervisoris_session.split('-')
        emp_numberofemployeewhosesupervisoris_session=emp_numberofemployeewhosesupervisoris_session[1]
        print 'emp_team:of employee whose supervisor is session persion:::'+str(emp_teamof_supervisor)
        print 'supervisor_number:'+str(supervisor_number)
        print 'emp_numberofemployeewhosesupervisoris_session:of employee whose supervisor is session persion:'+str(emp_numberofemployeewhosesupervisoris_session)
    #######for hr##################
    for x in new_object1111:
        xemail_id=x.email_id####email id of hr 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id :
            print 'hr'
            noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not Sufficient Sick Leave') |Q(leaves_approved_by_tl='Not Sufficient Casual Leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,emp_id_ofuser=newsession1,comments='')#,leaves_approved_by=team,)
    
            notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active')
            hrisalsoansupervisor199=notice1
            hrisalsoansupervisor198=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_HR=newsession1,leaves_status='Active',)
	    if len(noticeforteamlead)==0: 
                print 'len of if len(noticeforteamlead)==0: '
                if len(notice1)==0:
                    print 'len of if len(notice1)==0: ' 
                    nonewnotification='nonewnotification'
                    print 'hi nonewnotifcation'
                    return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'name':name,'extra_object':extra_object,},
                                  RequestContext(request)) 
        ###########################################################################################
        #  'this for team group leave status display accept or reject'#############      
            if len(noticeforteamlead)==0: 
                print 'len of if len(noticeforteamlead)==0: '
                newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active')
                hrisalsoansupervisor200=newnotice1
                hrisalsoansupervisor201=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_HR=newsession1,leaves_status='Active',)
                if len(notice1)>0:
                    if len(hrisalsoansupervisor201)==0:
                        print 'len of if len(notice1)>0: ' 
                        print 'this for team group leave status display accept or reject'
                        return render_to_response('basic_form.html',{'newnotice1':newnotice1,'name':name,'extra_object':extra_object,},
                                  RequestContext(request))
                    else:
                        print 'stupid hr is also supervisor'  
                        return render_to_response('basic_form.html',{'hrisalsoansupervisor201':hrisalsoansupervisor201,'hrisalsoansupervisor200':hrisalsoansupervisor200,'name':name,'extra_object':extra_object,},
                                  RequestContext(request))                       
          
        ########################################################################### 
        #  'this for team group leave status of team lead'#############      
            if len(noticeforteamlead)>0: 
                print 'len of if len(noticeforteamlead)>0: '
                againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not Sufficient Sick Leave') |Q(leaves_approved_by_tl='Not Sufficient Casual Leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,emp_id_ofuser=newsession1,comments='')#,leaves_approved_by=team,)
    
                if len(notice1)==0:
                    print 'len of if len(notice1)==0: ' 
                    print 'this for team group leave status of team lead'
                    return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'name':name,'extra_object':extra_object,},
                                  RequestContext(request))
        ########################################################################### 
        #for both##########
            if len(noticeforteamlead)>0:
                print 'len(noticeforteamlead)>0-----'
                if len(notice1)>0:
                    if len(hrisalsoansupervisor198)==0:
                        print 'len(notice1)>0-------'       
                        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'name':name,'extra_object':extra_object,},
                                  RequestContext(request))
                    else:
                        print 'supervisor is also hr and it is for both,check ,acceptreject and show all applied for leave'    
                        return render_to_response('basic_form.html',{'hrisalsoansupervisor198':hrisalsoansupervisor198,'hrisalsoansupervisor199':hrisalsoansupervisor199,'noticeforteamlead':noticeforteamlead,'name':name,'extra_object':extra_object,},
                                  RequestContext(request))        
    ################################# 
    ######for all other  below id the code#######   
    noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not Sufficient Sick Leave') |Q(leaves_approved_by_tl='Not Sufficient Casual Leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,emp_id_ofuser=newsession1,comments='')#,leaves_approved_by=team,)
    print len(noticeforteamlead)  
    print 'team lead notification'
    print 'team lead chdck'
    notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_HR=newsession1,leaves_status='Active',)#leaves_approved_by=team)
    print len(notice1) 
    #when no notification is there neither for teamlead nor by team group#########################
    if len(noticeforteamlead)==0: 
        print 'len of if len(noticeforteamlead)==0: '
        if len(notice1)==0:
            print 'len of if len(notice1)==0: ' 
            nonewnotification='nonewnotification'
            return render_to_response('noticeforall.html',{'nonewnotification':nonewnotification,'name':name,'extra_object':extra_object,},#'e':e},
                                  RequestContext(request)) 
        ###########################################################################################
        #  'this for team group leave status display accept or reject'#############      
    if len(noticeforteamlead)==0: 
        print 'len of if len(noticeforteamlead)==0: '
        newnotice1=notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_HR=newsession1,leaves_status='Active',)#leaves_approved_by=team)
    
        if len(notice1)>0:
            print 'len of if len(notice1)>0: ' 
            print 'this for team group leave status display accept or reject'
            return render_to_response('noticeforall.html',{'newnotice1':newnotice1,'name':name,'extra_object':extra_object,},#'e':e,'a':a,},
                                  RequestContext(request))
        ########################################################################### 
        #  'this for team group leave status of team lead'#############      
    if len(noticeforteamlead)>0: 
        print 'len of if len(noticeforteamlead)>0: '
        againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not Sufficient Sick Leave') |Q(leaves_approved_by_tl='Not Sufficient Casual Leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,emp_id_ofuser=newsession1,comments='')#leaves_approved_by=team,)
        if len(notice1)==0:
            print 'len of if len(notice1)==0: ' 
            print 'this for team group leave status of team lead'
            return render_to_response('noticeforall.html',{'againnoticeforteamlead':againnoticeforteamlead,'name':name,'extra_object':extra_object,},#'e':e,'a':a,},
                                  RequestContext(request))
        ########################################################################### 
               
    print 'when both option are thereof notification'                
    return render_to_response('noticeforall.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'name':name,'extra_object':extra_object,},#'e':e,'a':a,},
                                  RequestContext(request)) 

    #fetchemailsnew_object=LMS_EMPLOYEE_TABLE.objects.filter(emp_number=supervisor_number) 
#    for k in fetchemailsnew_object:
#        emailid_of_supervisor=k.emp_email_id
#    print 'emailid_of_supervisor :'+str(emailid_of_supervisor)
#    
##    a=datetime.date.today()
##    extra_object1=LMS_LEAVES_summary_TABLE.objects.filter(Q(position='202') | Q(position='205'))
##    print 'extra_object1:'+str(extra_object1) 
##    nameforsc_andhr=[]
##    for j in extra_object1:
##        nameforsc_andhr1=j.name_of_employee
##        nameforsc_andhr.append(str(nameforsc_andhr1))
##    print 'nameforsc_andhr:'
##    print nameforsc_andhr
##    g=nameforsc_andhr[0]
##    print 'g:'+str(g)
    #for (i=1;i<nameforsc_andhr.length-1;i++){
              #str=str+nameforsc_andhr[i];
    #print 'nameforsc_andhr[0]:'+str(nameforsc_andhr[0])   
       
#    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
#    for i in extra_object:
#        team=i.team
#        email_id=i.email_id
#        position=i.position
#        print 'position:'+str(position)
#        print 'team:'+str(team)
#        print 'emailid:'+str(email_id)
#    a=datetime.date.today()
#    email_id=str(email_id)
#    new_object=LMS_TEAM.objects.filter(emp_team=team)
#    e=email_id.split('@')
#    e=e[0] 
#    e=str(e)
#  
#    for i in new_object:
#        mh1=(i.mh1).strip()
#        mh2=(i.mh2).strip()
#        mh3=(i.mh3).strip()
#        mh1=str(mh1)
#        mh2=str(mh2)
#        mh3=str(mh3)
#        print 'mh1:'+str(mh1)
#        print 'mh2:'+str(mh2)
#        print 'mh3:'+str(mh3)
#        print 'to check which emailid is of manager ,teamlead and hr'
#  
#    if email_id==mh2:
#        print 'manager'
#        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Senior Consultant') | Q(leaves_approved_by_manager='Hr'),leaves_status='Active')
#        print len(notice1)
#        e=email_id.split('@')
#        e=e[0] 
#        e=str(e) 
#        
#        
#        ##################  
#        print 'for manager'
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                nonewnotification='nonewnotification'
#                print 'hi nonewnotifcation'
#                return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#        ###########################################################################################
#        #  'this for team group leave status display accept or reject'#############      
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Senior Consultant') | Q(leaves_approved_by_manager='Hr'),leaves_status='Active')
#            if len(notice1)>0:
#                print 'len of if len(notice1)>0: ' 
#                print 'this for team group leave status display accept or reject'
#                return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #  'this for team group leave status of team lead'#############      
#        if len(noticeforteamlead)>0: 
#            print 'len of if len(noticeforteamlead)>0: '
#            againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                print 'this for team group leave status of team lead'
#                return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        
#            #notice1=LMS_LEAVES_summary_TABLE.objects.filter(Q(position='402') | Q(position='405'))
#        #for both#########
#        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#            
#    if email_id==mh3 :
#        print 'hr'
#        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active')
#        e=email_id.split('@')
#        e=e[0] 
#        e=str(e) 
#        
#        
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                nonewnotification='nonewnotification'
#                print 'hi nonewnotifcation'
#                return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#        ###########################################################################################
#        #  'this for team group leave status display accept or reject'#############      
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active')
#            if len(notice1)>0:
#                print 'len of if len(notice1)>0: ' 
#                print 'this for team group leave status display accept or reject'
#                return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #  'this for team group leave status of team lead'#############      
#        if len(noticeforteamlead)>0: 
#            print 'len of if len(noticeforteamlead)>0: '
#            againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                print 'this for team group leave status of team lead'
#                return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #for both##########
#        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        print 'to check if match'
#    email_id=str(email_id)
#    mh1=str(mh1)
#    print 'email_id:'+str(email_id)
#    print 'mh1:'+str(mh1)       
#    if email_id==mh1:
#        e=email_id.split('@')
#        e=e[0] 
#        e=str(e) 
#        
#        
#        #############code for ceo############
#        position=str(position)
#        print 'position:--------------'+str(position)
#        if position=='Ceo':
#            print 'ceo ceo'
#            #### for his leave status of ceo notification#######3
#            noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            #####333333333333333333##################
#            print len(noticeforteamlead)
#            notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_manager='Manager',leaves_status='Active')
#            print len(notice1)
#            #when no notification is there neither for teamlead nor by team group#########################
#            if len(noticeforteamlead)==0: 
#                print 'len of if len(noticeforteamlead)==0: '
#                if len(notice1)==0:
#                    print 'len of if len(notice1)==0: ' 
#                    nonewnotification='nonewnotification'
#                    print 'in ceo box'
#                    return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#            ###########################################################################################
#            #  'this for team group leave status display accept or reject'#############      
#            if len(noticeforteamlead)==0: 
#                print 'len of if len(noticeforteamlead)==0: '
#                newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_manager='Manager',leaves_status='Active')
#                if len(notice1)>0:
#                    print 'len of if len(notice1)>0: ' 
#                    print 'this for team group leave status display accept or reject'
#                    return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#            ###########################################################################
#            #  'this for team group leave status of team lead'#############      
#            if len(noticeforteamlead)>0: 
#                print 'len of if len(noticeforteamlead)>0: '
#                againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#                if len(notice1)==0:
#                    print 'len of if len(notice1)==0: ' 
#                    print 'this for team group leave status of team lead'
#                    return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#            ########################################################################### 
#            print 'when both option are thereof notification'                
#            return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#     
#        ######################################
#        print 'team lead'
#            #### for his leave status notification#######3
#        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,emp_id_ofuser=newsession1,comments='')
#            #####333333333333333333##################
#        print len(noticeforteamlead)  
#        #for team lead notification
#        print 'team lead chdck'
#        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Consultant') | Q(leaves_approved_by_manager='Application Developer'),leaves_status='Active',leaves_approved_by=team)
#        print len(notice1)
#        #when no notification is there neither for teamlead nor by team group#########################
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                nonewnotification='nonewnotification'
#                return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e},
#                                  RequestContext(request)) 
#        ###########################################################################################
#        #  'this for team group leave status display accept or reject'#############      
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Consultant') | Q(leaves_approved_by_manager='Application Developer'),leaves_status='Active',leaves_approved_by=team)
#            if len(notice1)>0:
#                print 'len of if len(notice1)>0: ' 
#                print 'this for team group leave status display accept or reject'
#                return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #  'this for team group leave status of team lead'#############      
#        if len(noticeforteamlead)>0: 
#            print 'len of if len(noticeforteamlead)>0: '
#            againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                print 'this for team group leave status of team lead'
#                return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#               
#        print 'when both option are thereof notification'                
#        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))            
##    notice1=LMS_LEAVE_INFO_TABLE.objects.all()
##    for i in notice1:
##        name_ofemployeeappliedforleave=i.name
##        print 'name_ofemployeeappliedforleave:'+str(name_ofemployeeappliedforleave)
##        checkingforteam=LMS_LEAVES_summary_TABLE.objects.filter(name_of_employee=name_ofemployeeappliedforleave)
##        for j in checkingforteam:
##            team1=j.team
##            print 'team1:'+str(team1)+"-----"+'name_ofemployeeappliedforleave:'+str(name_ofemployeeappliedforleave)
##            if team1==team:
##                print 'team1:'+str(team1)+"+++++"+'team:'+str(team)+"+++++++"+str(name_ofemployeeappliedforleave)
#    #leaves_approved_by---this is acting as carrying the team of employee from lms_leave_info_table
#    #notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active' and leaves_approved_by=team )
#    #$$$$$$$$$$$$$$$$$edit here for user otherthen team lead
#    print 'are u here'
#    
#    notice3=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')  
#    #notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by=team)
#    #notice1=notice1.filter(leaves_status='Active')
#    print 'notice3:'
#    print len(notice3)
#    if len(notice3)==0:
#        print 'no new entry'
#        nonewnotification='nonewnotification'
#        return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#    
#    for i in notice3:
#        name_ofemployeeappliedforleave=i.name
#        leave_id=i.leave_id
#        print 'leave_id:'+str(leave_id)
#        print 'name_ofemployeeappliedforleave:0000000'+str(name_ofemployeeappliedforleave)
## 
#    
#                  
#        
#    return render_to_response('basic_form.html',{'notice3':notice3,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))    
#                                  
                                  
 #############for check the notification by user################333
def checkleave(request,leave_id):
     
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='checkleave/id='+str(leave_id)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    ############################################################
                    newsession1=str(newsession1)
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id1=k.emp_position_id
                        print 'emp_position_id1:'+str(emp_position_id1)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)

                    print 'hi'
                    notice4='checked'
                    noticehr5='checked'
                    print request.POST
                    
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    ignore121we=LMS_LEAVE_INFO_TABLE.objects.filter(pk=leave_id)
                    if len(ignore121we)==0:
                         print 'no such entry-------------------------0000000'
                         for x in new_object1111:
                             xemail_id=x.email_id 
                             xemail_id=str(xemail_id)
                             if newsession1==xemail_id:
                                 invaliduserforhrr='invalid'
                                 return render_to_response('basic_form.html',{'invaliduserforhrr':invaliduserforhrr,'a':a,'extra_object':extra_object},RequestContext(request))
                         invaliduser='invalid'
                         return render_to_response('basic_form.html',{'invaliduser':invaliduser,'a':a,'extra_object':extra_object},RequestContext(request))

                    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
                    y=LMS_LEAVE_INFO_TABLE.objects.filter(pk=leave_id)
                    for i in y:
                        name=i.name
                        emp_id_ofuser=i.emp_id_ofuser
                        emp_id_ofuser=str(emp_id_ofuser)
                    print "mark the notification as unread=================="
                    x.comments='Read'
                    x.save()
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    if  newsession1==emp_id_ofuser:
                        print 'l1'
                        for xitem1qw in new_object1111:
                            xemail_id=xitem1qw.email_id 
                            xemail_id=str(xemail_id)
                            print 'l2'
                            if newsession1==xemail_id:
                                print 'l3'
                                print 'for hr'
                                return render_to_response('basic_form.html',{'noticehr5':noticehr5,'a':a,'extra_object':extra_object},
                                  RequestContext(request))
                        print 'l4'        
                        return render_to_response('basic_form.html',{'notice4':notice4,'a':a,'extra_object':extra_object},
                                  RequestContext(request))
                    
                    print 'inside else =================='
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        if newsession1==xemail_id:
                            invaliduserforhrr='invalid'
                            return render_to_response('basic_form.html',{'invaliduserforhrr':invaliduserforhrr,'a':a,'extra_object':extra_object},RequestContext(request))
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'a':a,'extra_object':extra_object},RequestContext(request))

        
                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='checkleave/id='+str(leave_id)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='checkleave/id='+str(leave_id)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id1=k.emp_position_id
    print 'emp_position_id1:'+str(emp_position_id1)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id1)
    for x in new_object1111:
        xemail_id=x.email_id 
    xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    a=datetime.date.today()
    print 'newsession1'+str(newsession1)
    #if newsession1==xemail_id:
#    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
#    for i in allsignupdata:
#        namesession=i.name
#    print 'in Holiday_display'
#    namesession=str(namesession)
    print 'hi'
    notice4='checked'
    noticehr5='checked'
    print request.POST
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    ignore121we=LMS_LEAVE_INFO_TABLE.objects.filter(pk=leave_id)
    if len(ignore121we)==0:
        print 'no such entry'
        for x in new_object1111:
            xemail_id=x.email_id 
            xemail_id=str(xemail_id)
            if newsession1==xemail_id:
                invaliduserforhrr='invalid'
                return render_to_response('basic_form.html',{'invaliduserforhrr':invaliduserforhrr,'a':a,'extra_object':extra_object},RequestContext(request))
        invaliduser='invalid'
        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'a':a,'extra_object':extra_object},RequestContext(request))

    x=LMS_LEAVE_INFO_TABLE.objects.get(pk=leave_id)
    y=LMS_LEAVE_INFO_TABLE.objects.filter(pk=leave_id)
    for i in y:
        name=i.name
        emp_id_ofuser=i.emp_id_ofuser
    print "mark the notification as unread"
    x.comments='Read'
    x.save()
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    a=datetime.date.today()
    #if namesession==name:
    if  newsession1==emp_id_ofuser:
	for x in new_object1111:
            xemail_id=x.email_id 
            xemail_id=str(xemail_id)
            if newsession1==xemail_id:
                return render_to_response('basic_form.html',{'noticehr5':noticehr5,'a':a,'extra_object':extra_object},
                                  RequestContext(request))
        return render_to_response('basic_form.html',{'notice4':notice4,'a':a,'extra_object':extra_object},
                                  RequestContext(request))
                    
    print 'inside else =================='
    #name=str(namesession)
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        if newsession1==xemail_id:
            invaliduserforhrr='invalid'
            return render_to_response('basic_form.html',{'invaliduserforhrr':invaliduserforhrr,'a':a,'extra_object':extra_object},RequestContext(request))
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'a':a,'extra_object':extra_object},RequestContext(request))

                
                     
 ###################for home page##################
def log2in(request):
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='log2in'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                    xemail_id=str(xemail_id)
                    print 'xemail_id:'+str(xemail_id)
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='log2in'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='log2in'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
    print 'request.signup_id-------------------------------'
    print request.session['username']
    newsession1=request.session['username']
    print newsession1
    my_object7=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    print 'code here for hr' 
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id:
            HR=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)           
            return render_to_response('basic_form.html',{'HR':HR,},RequestContext(request))
    return render_to_response('basic_form.html',{'my_object7':my_object7,},RequestContext(request))


def autocomplete_company(request):
    print 'hi in ajax fuction '
    if 'term' in request.GET:
        tags = LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name__istartswith=request.GET['term']) | Q(last_name__istartswith=request.GET['term']))[:10]
        print 'tags:'+str(tags)
        for tag in tags:
            a=tag.emp_name
            b=tag.middle_name
            c=tag.last_name
            d=str(a)+" "+str(b)+" "+str(c) 
        return HttpResponse( simplejson.dumps( [ tag.emp_name+" "+tag.middle_name+" "+tag.last_name for tag in tags ] ) )
    
    return HttpResponse()

############for creating supervisor form
def supervisordetail(request):
    #if session doesnot exist:
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='supervisordetail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    ############################################################
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    
                    supervisor11=Supervisorform()
                    try:
                        print 'newsession1'+str(newsession1)
                        for x in new_object1111:
                            xemail_id=x.email_id 
                            xemail_id=str(xemail_id)
                            print 'xemail_id:'+str(xemail_id)
                            if newsession1==xemail_id:
                                print 'holiday form hrrrrrrrrrrrr'
                                return render_to_response('basic_form.html',{'supervisor11':supervisor11,'a':a,'extra_object':extra_object},RequestContext(request))
                    except:
                        print 'inside except=================='
                        invaliduser='invalid'
                        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'a':a,'extra_object':extra_object},RequestContext(request))

                   # return HttpResponse("You're logged in.")
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='supervisordetail'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='supervisordetail'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################
   
##################################################################################################
    #for active session
    print request.session['username']
    newsession1=request.session['username']
    print newsession1 
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
    ####for hr#####   
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    
    #supervisor11=Supervisorform(hide_condition=True) 
    supervisor11=Supervisorform()
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
        print 'xemail_id:'+str(xemail_id)
        if newsession1==xemail_id: 
            print 'nisha'
            return render_to_response('basic_form.html',{'supervisor11':supervisor11,'extra_object':extra_object,},RequestContext(request))
    invaliduser='invalid'
    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

def xsuperdisplay22(request):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box'
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                mh2=Signinform()
                tochangeurl='xsuperdisplay22'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    a=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                    print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                     
                   
                    supervisor23 = LMS_SUPERVISORHIERACHY.objects.all()
                    supervisor24=LMS_SUPERVISORHIERACHY.objects.all()
                    print "display part"
                    newsession1=str(newsession1)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        print 'xemail_id:'+str(xemail_id) 
                        if newsession1==xemail_id:
                            if len(supervisor23)==0: 
                                print 'len of if len(noticeforteamlead)==0: '
                                noentryinthetable='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                      RequestContext(request))
                            return render_to_response('basic_form.html',{'supervisor23':supervisor23,'a':a,'extra_object':extra_object},
                                      RequestContext(request))
        
                    print 'hiiii'
#                    if len(supervisor24)==0: 
#                        print 'len of if len(noticeforteamlead)==0: '
#                        noentryinthetable11='nonewnotification'
#                        return render_to_response('basic_form.html',{'noentryinthetable11':noentryinthetable11,'extra_object':extra_object,},
#                                  RequestContext(request))
#                    return render_to_response('basic_form.html',{'supervisor24':supervisor24,'a':a,'extra_object':extra_object},
#                                  RequestContext(request))    
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))

#                    
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='xsuperdisplay22'
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################  
               ############################################ 
               
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='xsuperdisplay22'
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    
##################################################################################################

    #for active session
    print request.session['username']
    newsession1=request.session['username']
    print newsession1 
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)  
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    if request.method =='POST': 
        if 'cancel1' in request.POST:
            print "inside cancel"
            strUrl = '/xsuperdisplay22/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)       
        print 'HERE I am'
        myrequestpost=request.POST.copy()
        print 'myrequestpost:'
        print myrequestpost
        emp_number=myrequestpost['emp_number']
        emp_number=str(emp_number)
        supervisor_number=myrequestpost['supervisor_number']
        supervisor_number=str(supervisor_number)
        print 'supervisor_number:'+str(supervisor_number)
        print 'emp_number:'+str(emp_number)
        print supervisor_number
        x=emp_number.split(' ')
        a=supervisor_number.split(' ')
        print a
        y=x[0]
        z=a[0]
        print y, z
        print 'y:'+str(y)

        chkna=LMS_EMPLOYEE_TABLE.objects.filter(emp_name=y)
        #print chkna.pk
        for i in chkna:
            numberemp=i.emp_number
        #numberemp=str(numberemp)    
        chkzaaa=LMS_EMPLOYEE_TABLE.objects.filter(emp_name=z)
        for j in chkzaaa:
            numbersupervisor=j.emp_number
        #numbersupervisor=str(numbersupervisor)    
#        print 'numberemp:'+str(numberemp) 
#        print 'numbersupervisor:'+str(numbersupervisor)   
        #myrequestpost['emp_number']=chkna.emp_number
        #myrequestpost['supervisor_number']=chkzaaa.emp_number 
            
#        form = Supervisorform({'emp_number': '1'})
#        form.cleaned_data['emp_number']
        
        print myrequestpost
        supervisor22=Supervisorform(request.POST)
        ne1=Supervisorform(request.POST)
        #supervisor22=Supervisorform(myrequestpost)
        #print supervisor22
        if supervisor22.is_valid():
            print 'i m inside'
            #####
            emp_number=supervisor22.cleaned_data['emp_number']
            supervisor_number=supervisor22.cleaned_data['supervisor_number']
            supervisor22 = supervisor22.save(commit=False)
            #supervisor22 = supervisor22.save(commit=False)
            #supervisor22 = supervisor22.save()
            
            print 'supervisor_number:'+str(supervisor_number)
      	    try:
            	emp_number=str(emp_number)
            	emp_number=emp_number.split(" ")
            	first_ofemployee=emp_number[0]
            	middle_ofemployee=emp_number[1]
            	last_ofemployee=emp_number[2]
            
            	supervisor_number=str(supervisor_number)
            	supervisor_number=supervisor_number.split(" ")
            	first_ofsupervisor=supervisor_number[0]
            	middle_ofsupervisor=supervisor_number[1]
            	last_ofsupervisor=supervisor_number[2]
	    except:
		print 'no match'
		ne2='no matching entry in table'
		ne=ne2
		return render_to_response('basic_form.html',{'ne':ne,'ne1':ne1,'extra_object':extra_object,},RequestContext(request))
            print 'employee name:'+str(emp_number)
            print 'supervisor_number:'+str(supervisor_number)
            chkna=LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name=first_ofemployee) & Q(middle_name=middle_ofemployee) & Q(last_name=last_ofemployee))
            print 'chkna:'+str(chkna)
	    if len(chkna)==0:
                ne='no matching entry in table' 
                return render_to_response('basic_form.html',{'ne':ne,'ne1':ne1,'extra_object':extra_object,},
                                  RequestContext(request))
            for i in chkna:
                numberemp=i.emp_number    
            numberemp=str(numberemp)
            print 'numberemp:'+str(numberemp)    
            chkzaaa=LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name=first_ofsupervisor) & Q(middle_name=middle_ofsupervisor) & Q(last_name=last_ofsupervisor))
	    print 'chkzaaa:--'+str(chkzaaa)
            if len(chkzaaa)==0:
                ne='no matching entry in table' 
                return render_to_response('basic_form.html',{'ne':ne,'ne1':ne1,'extra_object':extra_object,},
                                  RequestContext(request))
            for j in chkzaaa:
                numbersupervisor=j.emp_number
            numbersupervisor=str(numbersupervisor) 
            supervisor22.emp_number1_id = numberemp
            supervisor22.supervisor_number1_id = numbersupervisor
            #b = LMS_SUPERVISORHIERACHY.objects.create(emp_number=numberemp)
           # supervisor22=b.save()
            #####
            supervisor22.save()
            print "why"
            return HttpResponseRedirect('/xsuperdisplay22/')
        print "ggoooooooooooooo"
        return render_to_response('basic_form.html',{'supervisor22':supervisor22,'extra_object':extra_object,},
                                  RequestContext(request))
    else:
        for x in new_object1111:
            xemail_id=x.email_id 
            xemail_id=str(xemail_id)
            if newsession1==xemail_id:
                supervisor23 = LMS_SUPERVISORHIERACHY.objects.all()
                if len(supervisor23)==0: 
                    print 'len of if len(noticeforteamlead)==0: '
                    noentryinthetable='nonewnotification'
                    return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                      RequestContext(request))
                return render_to_response('basic_form.html',{'supervisor23':supervisor23,'extra_object':extra_object,},
                                      RequestContext(request))
        invaliduser='invalid'
        return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
    
        #supervisor24=LMS_SUPERVISORHIERACHY.objects.all()# for fetching all data from database
#        if len(supervisor24)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            noentryinthetable11='nonewnotification'
#            return render_to_response('basic_form.html',{'noentryinthetable11':noentryinthetable11,'extra_object':extra_object,},
#                                  RequestContext(request))
#        return render_to_response('basic_form.html',{'supervisor24':supervisor24,'extra_object':extra_object,},
#                                  RequestContext(request))
        

def killdelete_new(request,supervisor_hierarchy_id):
   
    print "delete"
    obj3 = LMS_SUPERVISORHIERACHY.objects.get(pk=supervisor_hierarchy_id)
    obj3.delete()
    #sta_url='/display_detail/name='+str(name)+'/'
    sta_url='/xsuperdisplay22/'
    return HttpResponseRedirect(sta_url)

def doedit(request,supervisor_hierarchy_id):
    ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
    if 'username' not in request.session:
        print 'hiiiiiiiiiiii' 
        print request.POST
        try:
            print 'in the try box of edit '
            
            #print 'the username and password are empty'
            if request.POST['username']=='' and request.POST['password']=='':
                print 'the username and password are empty'
                print 'employee_id:'+str(supervisor_hierarchy_id)
                mh2=Signinform()
                tochangeurl='doedit/id='+str(supervisor_hierarchy_id)
                print 'tochangeurl:'+str(tochangeurl)
                print 'nisha'
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    ###################
            try:
                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
                    print 'username and password matched' 
                    ##########this code is for session  #################
                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
                    print 'we are using session ie database session'
                    print request.session['username']
                    newsession1=request.session['username']
                    print newsession1
                    newsession1=str(newsession1)
                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
                    d=datetime.date.today()
                    testposition=LMS_POSITION.objects.filter(emp_position='HR')
                    for k in testposition:
                        emp_position_id=k.emp_position_id
                        print 'emp_position_id:'+str(emp_position_id)         
                    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
                    for x in new_object1111:
                        xemail_id=x.email_id 
                        xemail_id=str(xemail_id)
                        if newsession1==xemail_id:
                            #if there is no entry in the code
                            getforallvalue=LMS_SUPERVISORHIERACHY.objects.all()
                            if len(getforallvalue)==0:
                                print "length is 0"
                                noentryinthetable='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                      RequestContext(request))
                        ######################################### 
                            ####################when entry is deleted
                            product1 = LMS_SUPERVISORHIERACHY.objects.filter(supervisor_hierarchy_id=supervisor_hierarchy_id)
                            if len(product1)==0:
                                print "length is 0"
                                noentryinthetable='nonewnotification'
                                return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                      RequestContext(request))
            ########################
                            product = LMS_SUPERVISORHIERACHY.objects.get(pk=supervisor_hierarchy_id)
                            doeditmy_object3=Supervisorform(instance=product)
                            print 'holiday form hrrrrrrrrrrrr'
                            return render_to_response('basic_form.html',{'doeditmy_object3':doeditmy_object3,'d':d,'extra_object':extra_object},RequestContext(request))      
                    print 'inside else =================='
                    invaliduser='invalid'
                    return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
            except: 
                print 'the username and password are invalid'
                mh2=Signinform()
                tochangeurl='doedit/id='+str(supervisor_hierarchy_id)
                print 'tochangeurl:'+str(tochangeurl)
                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
    #####################################################################################         
        except:
            print 'in the except box'
            print 'username length less equal to zero which means user is logout.and session is deleted '
            mh1=Signinform()
            tochangeurl='doedit/id='+str(supervisor_hierarchy_id)
            print 'tochangeurl:'+str(tochangeurl)
            print 'nisha'
            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
    ##########################################################################################################
    #for active session:
    print request.session['username']
    newsession1=request.session['username']
    print newsession1 
    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)   
    testposition=LMS_POSITION.objects.filter(emp_position='HR')
    for k in testposition:
        emp_position_id=k.emp_position_id
    print 'emp_position_id:'+str(emp_position_id)         
    new_object1111=LMS_LEAVES_summary_TABLE.objects.filter(position=emp_position_id)
    for x in new_object1111:
        xemail_id=x.email_id 
        xemail_id=str(xemail_id)
    print 'xemail_id:'+str(xemail_id)
    print "sapu"
    #product = LMS_SUPERVISORHIERACHY.objects.get(pk=supervisor_hierarchy_id)
    if request.method == 'POST':
        ####################
        product1 = LMS_SUPERVISORHIERACHY.objects.filter(supervisor_hierarchy_id=supervisor_hierarchy_id)
        if len(product1)==0:
            print "length is 0"
            noentryinthetable='nonewnotification'
            return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                  RequestContext(request))
        ########################
        product = LMS_SUPERVISORHIERACHY.objects.get(pk=supervisor_hierarchy_id)
        doeditmy_object5 = Supervisorform(request.POST, instance=product)
	ne1 = Supervisorform(request.POST, instance=product)
        print "PRODUCTchecking POST"
        if 'cancel1' in request.POST:
            print "inside cancel"
            strUrl = '/xsuperdisplay22/'
            print 'url:'+str(strUrl)
            return HttpResponseRedirect(strUrl)       
        
        if doeditmy_object5.is_valid():
            print "Display Form"
            #doeditmy_object5.save()  
##            ##########
            emp_number=doeditmy_object5.cleaned_data['emp_number']
            supervisor_number=doeditmy_object5.cleaned_data['supervisor_number']
            
            doeditmy_object5 = doeditmy_object5.save(commit=False)
            #print 'omg:'+str(omg)
#            omg=str(omg)
#            take=omg.split('-')
#            emp_number=take[0]
#            supervisor_number=take[1]
#            #emp_number=doeditmy_object5.cleaned_data['emp_number']
#            #supervisor_number=doeditmy_object5.cleaned_data['supervisor_number'] 
	    try:
            	emp_number=str(emp_number)
            	emp_number=emp_number.split(" ")
            	first_ofemployee=emp_number[0]
            	middle_ofemployee=emp_number[1]
            	last_ofemployee=emp_number[2]
            
            	supervisor_number=str(supervisor_number)
            	supervisor_number=supervisor_number.split(" ")
            	first_ofsupervisor=supervisor_number[0]
            	middle_ofsupervisor=supervisor_number[1]
            	last_ofsupervisor=supervisor_number[2]
	    except:
		print 'no match'
                ne2='no matching entry in table' 
                ne=ne2
                return render_to_response('basic_form.html',{'ne':ne,'ne1':ne1,'extra_object':extra_object,},
                                   RequestContext(request))
            print 'employee name:'+str(emp_number)
            print 'supervisor_number:'+str(supervisor_number)
            chkna=LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name=first_ofemployee) & Q(middle_name=middle_ofemployee) & Q(last_name=last_ofemployee))
            print 'chkna:'+str(chkna)
	    if len(chkna)==0:
                ne='no matching entry in table' 
                return render_to_response('basic_form.html',{'ne':ne,'ne1':ne1,'extra_object':extra_object,},
                                  RequestContext(request))
            for i in chkna:
                numberemp=i.emp_number    
            numberemp=str(numberemp)
            print 'numberemp:'+str(numberemp)    
            chkzaaa=LMS_EMPLOYEE_TABLE.objects.filter(Q(emp_name=first_ofsupervisor) & Q(middle_name=middle_ofsupervisor) & Q(last_name=last_ofsupervisor))
	    if len(chkzaaa)==0:
                ne='no matching entry in table' 
                return render_to_response('basic_form.html',{'ne':ne,'ne1':ne1,'extra_object':extra_object,},
                                  RequestContext(request))
            for j in chkzaaa:
                numbersupervisor=j.emp_number
            numbersupervisor=str(numbersupervisor) 
            print 'numberemp:'+str(numberemp)
            print 'numbersupervisor:'+str(numbersupervisor)      
            doeditmy_object5.emp_number1_id=numberemp
            doeditmy_object5.supervisor_number1_id=numbersupervisor
            doeditmy_object5.save()
            #############    
            print 'clicking on editttttttt'     
            return HttpResponseRedirect('/xsuperdisplay22/')
        return render_to_response('basic_form.html',{'doeditmy_object5':doeditmy_object5,'extra_object':extra_object},
                                  RequestContext(request))
    else:
            #doeditmy_object3=Supervisorform(instance=product)
            for x in new_object1111:
                xemail_id=x.email_id 
                xemail_id=str(xemail_id)
                if newsession1==xemail_id:
                    getforallvalue=LMS_SUPERVISORHIERACHY.objects.all()
                    if len(getforallvalue)==0:
                        print "length is 0"
                        noentryinthetable='nonewnotification'
                        return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},
                                      RequestContext(request))
		    product1=LMS_SUPERVISORHIERACHY.objects.filter(supervisor_hierarchy_id=supervisor_hierarchy_id)
		    if len(product1)==0:
    			print "length is 0"
    			noentryinthetable='nonewnotification'
   			return render_to_response('basic_form.html',{'noentryinthetable':noentryinthetable,'extra_object':extra_object,},RequestContext(request))

                    print 'clicking on edit'
                    product = LMS_SUPERVISORHIERACHY.objects.get(pk=supervisor_hierarchy_id)
                    doeditmy_object3=Supervisorform(instance=product)
                    return render_to_response('basic_form.html',{'doeditmy_object3':doeditmy_object3,'extra_object':extra_object},RequestContext(request)) 
            invaliduser='invalid'
            return render_to_response('basic_form.html',{'invaliduser':invaliduser,'extra_object':extra_object},RequestContext(request))
     
#                                    context_instance=RequestContext(request)) 






##############################################
#def notice(request): 
#     ############## the below code is for showing the signin form when user is loged out and to avoid error page.############
#    if 'username' not in request.session:
#        print 'hiiiiiiiiiiii' 
#        print request.POST
#        try:
#            print 'in the try box'
#            
#            #print 'the username and password are empty'
#            if request.POST['username']=='' and request.POST['password']=='':
#                print 'the username and password are empty'
#                mh2=Signinform()
#                tochangeurl='notification1'
#                print 'nisha'
#                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
#    ###################
#            try:
#                if LMS_SIGNUP.objects.get(username=request.POST['username']) and LMS_SIGNUP.objects.get(password=request.POST['password']): 
#                    print 'username and password matched' 
#                    ##########this code is for session  #################
#                    request.session['username']=LMS_SIGNUP.objects.get(username=request.POST['username']).username
#                    print 'we are using session ie database session'
#                    print request.session['username']
#                    newsession1=request.session['username']
#                    print newsession1
#                    newsession1=str(newsession1)
##                    ############################################################
##                    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
##                    for i in allsignupdata:
##                        name=i.name
##                    print 'in manage hierachy'
##                    name=str(name)
##                    print 'name:'+str(name)
#                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
#                    a=datetime.date.today()
#                    for j in extra_object:
#                        name=j.name_of_employee
#                        teamtocheck=j.team
#                    name=str(name)
#                    print 'name:'+str(name)
#                    extra_object1=LMS_LEAVES_summary_TABLE.objects.filter(Q(position='202') | Q(position='205'))
#                    print 'extra_object1:'+str(extra_object1) 
#                    nameforsc_andhr=[]
#                    for j in extra_object1:
#                        nameforsc_andhr1=j.name_of_employee
#                        nameforsc_andhr.append(str(nameforsc_andhr1))
#                    print 'nameforsc_andhr:'
#                    print nameforsc_andhr
#                    g=nameforsc_andhr[0]
#                    print 'g:'+str(g)
#                    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
#                    for i in extra_object:
#                        team=i.team
#                        email_id=i.email_id
#                        position=i.position
#                        print 'position:'+str(position)
#                        print 'team:'+str(team)
#                        print 'emailid:'+str(email_id)
#                    a=datetime.date.today()
#                    email_id=str(email_id)
#                    new_object=LMS_TEAM.objects.filter(emp_team=team)
#                    e=email_id.split('@')
#                    e=e[0] 
#                    e=str(e)
#                    for i in new_object:
#                        mh1=(i.mh1).strip()
#                        mh2=(i.mh2).strip()
#                        mh3=(i.mh3).strip()
#                        mh1=str(mh1)
#                        mh2=str(mh2)
#                        mh3=str(mh3)
#                    print 'mh1:'+str(mh1)
#                    print 'mh2:'+str(mh2)
#                    print 'mh3:'+str(mh3)
#                    print 'to check which emailid is of manager ,teamlead and hr'
#                    if email_id==mh2:
#                        print 'manager'
#                        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#                        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Senior Consultant') | Q(leaves_approved_by_manager='Hr'),leaves_status='Active')
#                        print len(notice1)
#                        e=email_id.split('@')
#                        e=e[0] 
#                        e=str(e) 
#        
#                   # return HttpResponse("You're logged in.")
#            except: 
#                print 'the username and password are invalid'
#                mh2=Signinform()
#                tochangeurl='notification1'
#                print 'nisha'
#                return render_to_response('new_form1.html',{'mh2':mh2,'tochangeurl':tochangeurl,},RequestContext(request))
#    #####################################################################################  
#               ############################################ 
#               
#        except:
#            print 'in the except box'
#            print 'username length less equal to zero which means user is logout.and session is deleted '
#            mh1=Signinform()
#            tochangeurl='notification1'
#            print 'nisha'
#            return render_to_response('new_form1.html',{'mh1':mh1,'tochangeurl':tochangeurl,},RequestContext(request))
#    ##########################################################################################################
#    
###################################################################################################
#   
#    ###################################################################################################
#   
#    #make changes to show notification 
#    print 'request.signup_id*********************************'
#    print request.session['username']
#    newsession1=request.session['username']
#    print newsession1
##    allsignupdata=LMS_SIGNUP.objects.filter(username=newsession1)
##    for i in allsignupdata:
##        name=i.name
##    print 'in manage hierachy'
##    name=str(name)
##    print 'name:'+str(name)
#    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
#    for j in extra_object:
#        name=j.name_of_employee
#    name=str(name)
#    a=datetime.date.today()
##    name=str(name)
##    print 'name:'+str(name)
#    extra_object1=LMS_LEAVES_summary_TABLE.objects.filter(Q(position='202') | Q(position='205'))
#    print 'extra_object1:'+str(extra_object1) 
#    nameforsc_andhr=[]
#    for j in extra_object1:
#        nameforsc_andhr1=j.name_of_employee
#        nameforsc_andhr.append(str(nameforsc_andhr1))
#    print 'nameforsc_andhr:'
#    print nameforsc_andhr
#    g=nameforsc_andhr[0]
#    print 'g:'+str(g)
#    #for (i=1;i<nameforsc_andhr.length-1;i++){
#              #str=str+nameforsc_andhr[i];
#    #print 'nameforsc_andhr[0]:'+str(nameforsc_andhr[0])   
#       
#    extra_object=LMS_LEAVES_summary_TABLE.objects.filter(email_id=newsession1)
#    for i in extra_object:
#        team=i.team
#        email_id=i.email_id
#        position=i.position
#        print 'position:'+str(position)
#        print 'team:'+str(team)
#        print 'emailid:'+str(email_id)
#    a=datetime.date.today()
#    email_id=str(email_id)
#    new_object=LMS_TEAM.objects.filter(emp_team=team)
#    e=email_id.split('@')
#    e=e[0] 
#    e=str(e)
#  
#    for i in new_object:
#        mh1=(i.mh1).strip()
#        mh2=(i.mh2).strip()
#        mh3=(i.mh3).strip()
#        mh1=str(mh1)
#        mh2=str(mh2)
#        mh3=str(mh3)
#        print 'mh1:'+str(mh1)
#        print 'mh2:'+str(mh2)
#        print 'mh3:'+str(mh3)
#        print 'to check which emailid is of manager ,teamlead and hr'
#  
#    if email_id==mh2:
#        print 'manager'
#        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Senior Consultant') | Q(leaves_approved_by_manager='Hr'),leaves_status='Active')
#        print len(notice1)
#        e=email_id.split('@')
#        e=e[0] 
#        e=str(e) 
#        
#        
#        ##################  
#        print 'for manager'
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                nonewnotification='nonewnotification'
#                print 'hi nonewnotifcation'
#                return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#        ###########################################################################################
#        #  'this for team group leave status display accept or reject'#############      
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Senior Consultant') | Q(leaves_approved_by_manager='Hr'),leaves_status='Active')
#            if len(notice1)>0:
#                print 'len of if len(notice1)>0: ' 
#                print 'this for team group leave status display accept or reject'
#                return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #  'this for team group leave status of team lead'#############      
#        if len(noticeforteamlead)>0: 
#            print 'len of if len(noticeforteamlead)>0: '
#            againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                print 'this for team group leave status of team lead'
#                return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        
#            #notice1=LMS_LEAVES_summary_TABLE.objects.filter(Q(position='402') | Q(position='405'))
#        #for both#########
#        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#            
#    if email_id==mh3 :
#        print 'hr'
#        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active')
#        e=email_id.split('@')
#        e=e[0] 
#        e=str(e) 
#        
#        
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                nonewnotification='nonewnotification'
#                print 'hi nonewnotifcation'
#                return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#        ###########################################################################################
#        #  'this for team group leave status display accept or reject'#############      
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active')
#            if len(notice1)>0:
#                print 'len of if len(notice1)>0: ' 
#                print 'this for team group leave status display accept or reject'
#                return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #  'this for team group leave status of team lead'#############      
#        if len(noticeforteamlead)>0: 
#            print 'len of if len(noticeforteamlead)>0: '
#            againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                print 'this for team group leave status of team lead'
#                return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #for both##########
#        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        print 'to check if match'
#    email_id=str(email_id)
#    mh1=str(mh1)
#    print 'email_id:'+str(email_id)
#    print 'mh1:'+str(mh1)       
#    if email_id==mh1:
#        e=email_id.split('@')
#        e=e[0] 
#        e=str(e) 
#        
#        
#        #############code for ceo############
#        position=str(position)
#        print 'position:--------------'+str(position)
#        if position=='Ceo':
#            print 'ceo ceo'
#            #### for his leave status of ceo notification#######3
#            noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            #####333333333333333333##################
#            print len(noticeforteamlead)
#            notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_manager='Manager',leaves_status='Active')
#            print len(notice1)
#            #when no notification is there neither for teamlead nor by team group#########################
#            if len(noticeforteamlead)==0: 
#                print 'len of if len(noticeforteamlead)==0: '
#                if len(notice1)==0:
#                    print 'len of if len(notice1)==0: ' 
#                    nonewnotification='nonewnotification'
#                    print 'in ceo box'
#                    return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#            ###########################################################################################
#            #  'this for team group leave status display accept or reject'#############      
#            if len(noticeforteamlead)==0: 
#                print 'len of if len(noticeforteamlead)==0: '
#                newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by_manager='Manager',leaves_status='Active')
#                if len(notice1)>0:
#                    print 'len of if len(notice1)>0: ' 
#                    print 'this for team group leave status display accept or reject'
#                    return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#            ###########################################################################
#            #  'this for team group leave status of team lead'#############      
#            if len(noticeforteamlead)>0: 
#                print 'len of if len(noticeforteamlead)>0: '
#                againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#                if len(notice1)==0:
#                    print 'len of if len(notice1)==0: ' 
#                    print 'this for team group leave status of team lead'
#                    return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#            ########################################################################### 
#            print 'when both option are thereof notification'                
#            return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        
#        
#        
#        
#        
#        
#        
#        ######################################
#        print 'team lead'
#            #### for his leave status notification#######3
#        noticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            #####333333333333333333##################
#        print len(noticeforteamlead)  
#        #for team lead notification
#        print 'team lead chdck'
#        notice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Consultant') | Q(leaves_approved_by_manager='Application Developer'),leaves_status='Active',leaves_approved_by=team)
#        print len(notice1)
#        #when no notification is there neither for teamlead nor by team group#########################
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                nonewnotification='nonewnotification'
#                return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e},
#                                  RequestContext(request)) 
#        ###########################################################################################
#        #  'this for team group leave status display accept or reject'#############      
#        if len(noticeforteamlead)==0: 
#            print 'len of if len(noticeforteamlead)==0: '
#            newnotice1=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_manager='Consultant') | Q(leaves_approved_by_manager='Application Developer'),leaves_status='Active',leaves_approved_by=team)
#            if len(notice1)>0:
#                print 'len of if len(notice1)>0: ' 
#                print 'this for team group leave status display accept or reject'
#                return render_to_response('basic_form.html',{'newnotice1':newnotice1,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#        #  'this for team group leave status of team lead'#############      
#        if len(noticeforteamlead)>0: 
#            print 'len of if len(noticeforteamlead)>0: '
#            againnoticeforteamlead=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave') |Q(leaves_approved_by_tl='Not sufficient casual leave')| Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')
#            if len(notice1)==0:
#                print 'len of if len(notice1)==0: ' 
#                print 'this for team group leave status of team lead'
#                return render_to_response('basic_form.html',{'againnoticeforteamlead':againnoticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))
#        ########################################################################### 
#               
#        print 'when both option are thereof notification'                
#        return render_to_response('basic_form.html',{'notice1':notice1,'noticeforteamlead':noticeforteamlead,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))            
##    notice1=LMS_LEAVE_INFO_TABLE.objects.all()
##    for i in notice1:
##        name_ofemployeeappliedforleave=i.name
##        print 'name_ofemployeeappliedforleave:'+str(name_ofemployeeappliedforleave)
##        checkingforteam=LMS_LEAVES_summary_TABLE.objects.filter(name_of_employee=name_ofemployeeappliedforleave)
##        for j in checkingforteam:
##            team1=j.team
##            print 'team1:'+str(team1)+"-----"+'name_ofemployeeappliedforleave:'+str(name_ofemployeeappliedforleave)
##            if team1==team:
##                print 'team1:'+str(team1)+"+++++"+'team:'+str(team)+"+++++++"+str(name_ofemployeeappliedforleave)
#    #leaves_approved_by---this is acting as carrying the team of employee from lms_leave_info_table
#    #notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_status='Active' and leaves_approved_by=team )
#    #$$$$$$$$$$$$$$$$$edit here for user otherthen team lead
#    print 'are u here'
#    
#    notice3=LMS_LEAVE_INFO_TABLE.objects.filter(Q(leaves_approved_by_tl='Not sufficient sick leave')|Q(leaves_approved_by_tl='Not sufficient casual leave') | Q(leaves_approved_by_tl='Leave Rejected') | Q(leaves_approved_by_tl='Leave Approved'),Q(leaves_status='Active') | Q(leaves_status='Passive'),name=name,leaves_approved_by=team,comments='')  
#    #notice1=LMS_LEAVE_INFO_TABLE.objects.filter(leaves_approved_by=team)
#    #notice1=notice1.filter(leaves_status='Active')
#    print 'notice3:'
#    print len(notice3)
#    if len(notice3)==0:
#        print 'no new entry'
#        nonewnotification='nonewnotification'
#        return render_to_response('basic_form.html',{'nonewnotification':nonewnotification,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request)) 
#    
#    for i in notice3:
#        name_ofemployeeappliedforleave=i.name
#        leave_id=i.leave_id
#        print 'leave_id:'+str(leave_id)
#        print 'name_ofemployeeappliedforleave:0000000'+str(name_ofemployeeappliedforleave)
## 
#    
#                  
#        
#    return render_to_response('basic_form.html',{'notice3':notice3,'a':a,'name':name,'extra_object':extra_object,'e':e,},
#                                  RequestContext(request))    
                                  
  
#############################################
