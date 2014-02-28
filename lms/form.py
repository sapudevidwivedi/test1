from django import forms
from django.forms import ModelForm
from models import LMS_EMPLOYEE_TABLE,LMS_HOLIDAY_LIST,LMS_HOLIDAY_TYPE,LMS_SIGNUP,LMS_NEWS,LMS_LEAVE_INFO_TABLE,LMS_LEAVES_summary_TABLE,LMS_DEPARTMENT_EMP_DETAILS,LMS_LEAVE_TYPES,LMS_SUPERVISORHIERACHY,CV_UNIVERSITY,CV_CV,CV_VEIFYWITHDENOGFILE,CV_POSITION, CV_GENDER, CV_SIGNUP, CV_College,CV_Department,CV_HELPTEXT,CV_CLIENTFOFPARSINGCV
from django.forms.widgets import TextInput, DateInput, Textarea
from lms.models import LMS_GENDER, LMS_SIGNIN
from lms.models import LMS_POSITION
from lms.models import LMS_TEAM

import datetime
from datetime import date

#from lms import settings
#from django.conf import Settings

import lms.settings
from captcha.fields import CaptchaField
from django.forms import extras
from django.forms.extras import widgets
from lms.widgets import MySelectDateWidget
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import HiddenInput
from django.core.exceptions import ValidationError
import re
from django.core.validators import RegexValidator, MinLengthValidator,\
    MaxLengthValidator

class Genderform(ModelForm):
    emp_gender=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Gender',required=False)
    
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['emp_gender']
        
        if self.cleaned_data['emp_gender']== '' or msg.strip()== '' :
            self._errors['emp_gender']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    class Meta:
        model=LMS_GENDER
        fields=('emp_gender',)

class Positionform(ModelForm):
    emp_position=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Position',required=False)
    
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['emp_position']
        
        if self.cleaned_data['emp_position']== '' or msg.strip()== '' :
            self._errors['emp_position']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    
    class Meta:
        model=LMS_POSITION
        fields=('emp_position',)

class Teamform(ModelForm):
    emp_team=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Department',required=False)
    
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['emp_team']
        
        if self.cleaned_data['emp_team']== '' or msg.strip()== '' :
            self._errors['emp_team']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    
    class Meta:
        model=LMS_TEAM
        fields=('emp_team',)  

class Holidaytypeform(ModelForm):
    Holiday_Type=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Holiday Type',required=False)
    
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['Holiday_Type']
        
        if self.cleaned_data['Holiday_Type']== '' or msg.strip()== '' :
            self._errors['Holiday_Type']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    
    class Meta:
        model=LMS_HOLIDAY_TYPE
        fields=('Holiday_Type',)                      
        

class Supervisorform(ModelForm):
    #emp_number=forms.CharField(widget=TextInput(attrs={'onclick':'employeelist_Calculate();'}),label='Employee Name',required=True)
    #supervisor_number=forms.CharField(widget=TextInput(attrs={'onclick':'employeelist_Calculate();'}),label='Supervisor Name',required=True)
    emp_number=forms.CharField(label='Employee Name',required=True)
    #emp_number=forms.CharField(widget=forms.HiddenInput(), initial=123)
    
    supervisor_number=forms.CharField(label='Supervisor Name',required=True) 
    emp_team=forms.ModelChoiceField(queryset=LMS_TEAM.objects.all(),label='Department')
#    emp_number=forms.ModelChoiceField(queryset=LMS_EMPLOYEE_TABLE.objects.all(),label='Employee Name')
#    supervisor_number=forms.ModelChoiceField(queryset=LMS_EMPLOYEE_TABLE.objects.all(),label='Supervisor Name') 
#    emp_team=forms.ModelChoiceField(queryset=LMS_TEAM.objects.all(),label='Team')
#    form = Supervisorform({'emp_number': '1'})
#    form.cleaned_data['emp_number']
    def __init__(self,*args, **kwargs):
        #hide_condition = kwargs.pop('hide_condition',None)
        super(Supervisorform, self).__init__(*args, **kwargs)
        self.fields['emp_number'].widget.attrs['id']='tags1'
        self.fields['supervisor_number'].widget.attrs['id']='tags2' 
        #if hide_condition:
            #self.fields['emp_team'].widget = HiddenInput()
        
    class Meta:
        model=LMS_SUPERVISORHIERACHY
        #exclude = ("emp_number","supervisor_number")
        #fields=('emp_team',)
        fields=('emp_number','supervisor_number','emp_team',)#'emp_team',)


#############
class Summaryleavefillform(ModelForm):
    #leaves_type=forms.ModelChoiceField(queryset=LMS_EMPLOYEE_TABLE.objects.all(),label='Emp Id')
    leaves_type=forms.CharField(widget=TextInput(),label='Emp Id',required=False)
    #emp_team=forms.ModelChoiceField(queryset=LMS_TEAM.objects.all(),label='Team')
    #total_casual_leaves=forms.CharField(widget=TextInput(),label='Total Casual leave',required=False)
    #total_sick_leaves=forms.CharField(widget=TextInput(),label='Total Sick leave',required=False)

    updated_date=forms.CharField(widget=TextInput(),label='Eligiable Avaliable Leave',required=False)####new addition
    
    created_by =forms.CharField(widget=TextInput(),label='Casual Leaves Used',required=False)
    created_date=forms.CharField(widget=TextInput(),label='Sick Leave Used',required=False)
    updated_by= forms.CharField(widget=TextInput(),label='Comp Off',required=False)
    #position=forms.ModelChoiceField(queryset=LMS_POSITION.objects.all(),label='Position')
    #emp_team=forms.ModelChoiceField(queryset=LMS_TEAM.objects.all(),label='Team')
    
    class Meta:
        model=LMS_LEAVE_TYPES
        fields=('leaves_type','updated_date','created_by','created_date','updated_by',)#'emp_team',)

        #fields=('emp_id_of_employee','total_casual_leaves','total_sick_leaves','eligiable_avaliable_leave','casual_leaves_used','sick_leaves_used','leave_comp_off','position','team',)

#def validate_actualleave(value):
##        if LMS_SIGNUP.objects.filter(username=value).exists():
##            raise ValidationError('Sorry, This Username Is Alloted ')
#        if value=='' or value.strip()== '' :
#            raise ValidationError('Sorry, Space Not Allowered ')
#        else:
#            
#                RegexValidator(
#                               r'^[0-9]*$',
#                               'Only 0-9 are allowed.',
#                               'Invalid Number'
#                               ),
#                MinLengthValidator(1),
#                MaxLengthValidator(2),

class Leaveapplyform(ModelForm):
    LEAVETYPE=(
            ('SL','SICK LEAVE'),
            ('CL','CASUAL LEAVE')#,('CO','COMP OFF')
            )
   
    #name=forms.CharField(widget=TextInput(),label='NAME',required=False)
    #leaves_from=forms.DateField(widget=SelectDateWidget(years=range(2013,2030)),label='LEAVE FROM*',required=False)
    leaves_from   =forms.DateField(label='Leave From*',required=True)
    #leaves_till=forms.DateField(widget=SelectDateWidget(years=range(2013,2030)),label='LEAVE TO*',required=False)
    leaves_till=forms.DateField(label='Leave Till*',required=True)
    actual_totalleavesdifference=forms.CharField(widget=TextInput(attrs={'onclick':'days_Calculate();'}),label='Total Days',required=False)
    #leave_type_id           =forms.CharField(max_length=200,blank=False)
    leave_type_id =forms.ChoiceField(choices=LEAVETYPE,label='Leave Type')
    leaves_applied_reason =forms.CharField(widget=Textarea(attrs={'cols':40,'rows':5}),label='Reason',required=False)
    
    # to initialise the calendar filed of jquery .imp setting the id of jquery to field
    def __init__(self,*args, **kwargs):
        super(Leaveapplyform, self).__init__(*args, **kwargs)
        self.fields['leaves_from'].widget.attrs['id']='datepicker1'
        self.fields['leaves_till'].widget.attrs['id']='datepicker2'
        ###self.fields['actual_totalleavesdifference'].widget=self.days_Calculate(self.leaves_from,self.leaves_till)
    
    
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['actual_totalleavesdifference']
#        if not re.match(r'[A-z0-9]+', msg):
#            raise ValidationError('AlphaNumeric characters only.')
        if not re.match(r'^[0-9]*$',msg):
           self._errors['actual_totalleavesdifference']='Only Integer Values Are Alloweddd' 
           
        if self.cleaned_data['actual_totalleavesdifference']== '' or msg.strip()== '' :
            self._errors['actual_totalleavesdifference']='space not allowered'
        return self.cleaned_data
#    def days_Calculate(self,leaves_from,leaves_till):
#                current_year=datetime.date.today().year
#                print current_year
#                print leaves_from.__doc__
#                print 'leaves_from: '+str(leaves_from)
#                print 'leaves_till:'+str(leaves_till)
#                
#                s_leaves_from_year=leaves_from.year
#                s_leaves_from_month=leaves_from.month
#                s_leaves_from_day=leaves_from.day
#                
#                p_leaves_till_year=leaves_till.year
#                p_leaves_till_month=leaves_till.month
#                p_leaves_till_day=leaves_till.day
#                
#                print 's_leaves_from_year:'+str(s_leaves_from_year)
#                print 's_leaves_from_month:'+str(s_leaves_from_month)
#                print 's_leaves_from_day:'+str(s_leaves_from_day)
#                
#                print 'p_leaves_till_year:'+str(p_leaves_till_year)
#                print 'p_leaves_till_month:'+str(p_leaves_till_month)
#                print 'p_leaves_till_day:'+str(p_leaves_till_day)
#               
#                if s_leaves_from_year == (int)(p_leaves_till_year):
#                    d1=date(int(s_leaves_from_year),int(s_leaves_from_month),int(s_leaves_from_day))
#                    d2=date(int(p_leaves_till_year),int(p_leaves_till_month),int(p_leaves_till_day))
#                    if d2>=d1:
#                        print 'hi'
#                        days_left=(d2-d1).days
#                        print 'days_left:'+str(days_left)
#                    else:
#                        print 'invalid date selection'
#            
#                return days_left
#            
 
    class Meta:
        model=LMS_LEAVE_INFO_TABLE
        fields=('leaves_from','leaves_till','actual_totalleavesdifference','leave_type_id','leaves_applied_reason',)#'name',)



class Newsform(ModelForm):
    entigence_date=forms.CharField(widget=TextInput(),label='DATE(YYYY-MM-DD)',required=False)
    entigence_news=forms.CharField(widget=TextInput(),label='NEWS',required=False)
    entigence_deliveredby=forms.CharField(widget=TextInput(),label='UPDATED BY',required=False)
    class Meta:
        model=LMS_NEWS
        fields=('entigence_date','entigence_news','entigence_deliveredby',)

def validate_username_unique(value):
        if LMS_SIGNUP.objects.filter(username=value).exists():
            raise ValidationError('Sorry, This Username Is Alloted ')

class CaptchaTestForm(ModelForm):
    name=forms.CharField(widget=TextInput(),label='First Name*',required=False)
    middlename=forms.CharField(widget=TextInput(),label='Middle Name',required=False)
    lastname=forms.CharField(widget=TextInput(),label='Last Name*',required=False)
    username=forms.EmailField(validators=[validate_username_unique])
    
    #username=forms.EmailField(widget=TextInput(),label='Username*',required=False)
    password=forms.CharField(widget=forms.PasswordInput(render_value=False), label='Password*',required=False)
    confirm_password=forms.CharField(widget=forms.PasswordInput(render_value=False), label='Confirm Password*',required=False)
    date_of_birth=forms.CharField(widget=TextInput(),label='Date Of Birth(yyyy-mm-dd)',required=False)
    emp_gender =forms.ModelChoiceField(queryset=LMS_GENDER.objects.all(),label='Gender')
    captcha = CaptchaField()
   
    
    def clean(self):
        super(ModelForm,self).clean()
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                self._errors['password'] = 'Passwords Must Match'
                self._errors['confirm_password'] = 'Passwords Must Match'
        return self.cleaned_data
       
    class Meta:
        model=LMS_SIGNUP
        fields=('name','middlename','lastname','username','password','confirm_password','date_of_birth','emp_gender','captcha')

class Holidaylistform(ModelForm):
   # holiday_date=forms.CharField(widget=TextInput(),label='Date',required=False)
    holiday_date=forms.DateField(widget=SelectDateWidget(years=range(2013,2030), attrs={'class':'input-small'}),label='Date',required=False)
    Holiday_Type=forms.ModelChoiceField(queryset=LMS_HOLIDAY_TYPE.objects.all(),label='Holiday Type')
    holiday_called=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Holiday Name',required=False)
    
    class Meta:
        model=LMS_HOLIDAY_LIST
        fields=('holiday_date','Holiday_Type','holiday_called',)

#def validate_unique1(value):
#        if not LMS_SIGNUP.objects.filter(username=value).exists():
#            raise ValidationError('Sorry, This Username Does Not Exists')
class Passwordrecoveryform(forms.Form):
    username=forms.EmailField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Email address'}),label='Username*',required=False)
    
    def clean(self):
        msg = self.cleaned_data['username']
        if not LMS_SIGNUP.objects.filter(username=msg).exists():
            self._errors['username']='Sorry,Username Does Not Exists'
#        if not re.match(r'^[0-9]*$',msg):
#           self._errors['actual_totalleavesdifference']='Only Integer Values Are Alloweddd' 
#           
        if self.cleaned_data['username']== '' or msg.strip()== '' :
            self._errors['username']='space not allowered'
        return self.cleaned_data

class ChangePasswordform(forms.Form):
    username=forms.EmailField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Email address'}),label='Username*',required=False)
    oldpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'Old Password'},render_value=False), label='Old Password*',required=False)
    newpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'New Password'},render_value=False), label='New Password*',required=False)
    confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'Confirm Password'},render_value=False), label='Confirm Password*',required=False)
    
    def clean(self):
        username = self.cleaned_data['username']
        oldpassword = self.cleaned_data['oldpassword']
        newpassword = self.cleaned_data['newpassword']
        confirmpassword = self.cleaned_data['confirmpassword']
        
        #if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
        if self.cleaned_data['newpassword'] != self.cleaned_data['confirmpassword']:
            self._errors['newpassword'] = 'Passwords Must Match'
            self._errors['confirmpassword'] = 'Passwords Must Match'
        
        if not LMS_SIGNUP.objects.filter(username=username).exists():
            self._errors['username']='Sorry,Username Does Not Exists'
        if not LMS_SIGNUP.objects.filter(username=username,password=oldpassword).exists():
            self._errors['oldpassword']='Password Does Not match'    
#        if not re.match(r'^[0-9]*$',msg):
#           self._errors['actual_totalleavesdifference']='Only Integer Values Are Alloweddd' 
#           
        if self.cleaned_data['username']== '' or username.strip()== '' :
            self._errors['username']='space not allowered'
        if self.cleaned_data['oldpassword']== '' or oldpassword.strip()== '' :
            self._errors['oldpassword']='space not allowered'
        if self.cleaned_data['newpassword']== '' or newpassword.strip()== '' :
            self._errors['newpassword']='space not allowered'
        if self.cleaned_data['confirmpassword']== '' or confirmpassword.strip()== '' :
            self._errors['confirmpassword']='space not allowered'        
            
        return self.cleaned_data
    

class Signinform(forms.Form):
    username=forms.EmailField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Email address'}),label='Username*',required=False)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'Password'},render_value=False), label='Password*',required=False)
    #username=forms.EmailField(widget=TextInput(attrs={'class':'input-xlarge','placeholder':'Email address'}),label='USERNAME*',required=False)
    #password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-xlarge','placeholder':'Password'},render_value=False), label='PASSWORD*',required=False)

    #class Meta:
        #model=LMS_SIGNIN
        #model=LMS_SIGNUP
        #fields=('username','password',)
        

#####defalult employee page####
#class Employeeform(ModelForm):
#    emp_name=forms.CharField(widget=TextInput(),label= 'Name',required=False)
#    emp_number=forms.CharField(widget=TextInput(),label='Employee Number',required=False)
#    emp_email_id=forms.EmailField(widget=TextInput(),label= 'Email Id ',required=False)
#    emp_position=forms.ModelChoiceField(queryset=LMS_POSITION.objects.all(),label='Position')
#    emp_team=forms.ModelChoiceField(queryset=LMS_TEAM.objects.all(),label='Team')
#    
#    emp_gender=forms.ModelChoiceField(queryset=LMS_GENDER.objects.all(),label='Gender')
#    
#    emp_current_address=forms.CharField(widget=TextInput(),label='Current Address',required=False)
#    emp_permanent_address=forms.CharField(widget=TextInput(),label='Permanent Address',required=False)
#    Emp_contact_info=forms.CharField(widget=TextInput(),label='Contact Info',required=False)
#    emp_joining_date   =forms.CharField(widget=TextInput(),label='Joining Date(yyyy-mm-dd)',required=False)
#    leaves_quota_year_casual         =forms.CharField(widget=forms.HiddenInput,label='Casual Leaves',required=False)
#    leaves_quota_year_sick=forms.CharField(widget=forms.HiddenInput,label='Sick Leaves',required=False)
#    comp_off_Gained=forms.CharField(widget=TextInput(),label='Comp Off',required=False)
#    leaves_to_be_approved_by=forms.CharField(widget=TextInput(),label='Leaves Approved',required=False)

#def validate_username_unique12(value):
#        if LMS_EMPLOYEE_TABLE.objects.filter(emp_number=value).exists():
#            raise ValidationError('Sorry, This Employee Number Is Alloted ')    
#def validate_username_unique11(value):
#        if LMS_EMPLOYEE_TABLE.objects.filter(emp_email_id=value).exists():
#            raise ValidationError('Sorry, This Email Id Is Alloted ')   
 #employee form with calendar####   
class Employeeform(ModelForm):
    
    emp_name=forms.CharField(widget=TextInput(),label= 'First Name',required=False)
    middle_name=forms.CharField(widget=TextInput(),label= 'Middle Name',required=False)##new entry for middle name
    last_name=forms.CharField(widget=TextInput(),label= 'Last Name',required=False)# new entry for last name
    emp_number=forms.CharField(widget=TextInput(),label='Employee Number',required=False)
    emp_email_id=forms.EmailField(widget=TextInput(),label= 'Email Id ',required=False,)
    
    #emp_number=forms.CharField(widget=TextInput(),validators=[validate_username_unique12],label='Employee Number',required=False)
    #emp_email_id=forms.EmailField(widget=TextInput(),validators=[validate_username_unique11],label= 'Email Id ',required=False,)
    emp_position=forms.ModelChoiceField(queryset=LMS_POSITION.objects.all(),label='Position')
    emp_team=forms.ModelChoiceField(queryset=LMS_TEAM.objects.all(),label='Department')
    
    emp_gender=forms.ModelChoiceField(queryset=LMS_GENDER.objects.all(),label='Gender')
    
    emp_current_address=forms.CharField(widget=TextInput(),label='Current Address',required=False)
    emp_permanent_address=forms.CharField(widget=TextInput(),label='Permanent Address',required=False)
    Emp_contact_info=forms.CharField(widget=TextInput(),label='Contact Info',required=False)
    # to initialise the calendar filed of jquery .imp setting the id of jquery to field.called here.
    #emp_joining_date   =forms.DateField(label='Joining Date',required=False)
    emp_joining_date   =forms.DateField(widget=SelectDateWidget(years=range(2002,2030),attrs={'class':'input-small'}),label='Joining Date',required=False)
    #emp_dob=forms.DateField(label='Date Of Birth',required=False)
    #emp_dob = forms.DateField(required=False,widget=SelectDateWidget(years=range(1980, 2013)), label='Date Of Birth')
    emp_dob = forms.DateField(required=False,widget=MySelectDateWidget(years=range(1970, 2013),attrs={'class':'input-small'}),label='Date Of Birth')
    emp_bloodgroup=forms.CharField(widget=TextInput(),label='Blood Group',required=False)
    
    # to initialise the calendar filed of jquery .imp setting the id of jquery to field
#    def __init__(self,*args, **kwargs):
#        super(Employeeform, self).__init__(*args, **kwargs)
#        self.fields['emp_joining_date'].widget.attrs['id']='datepicker'
#####        self.fields['emp_dob'].widget = MySelectDateWidget(years=('Select year','1990','2012'),months=(), day=())



#    def Calculate_leave(self, emp_joining_date):
#            current_year=datetime.date.today().year
##            print current_year
#            print emp_joining_date.__doc__
#            print 'emp_joning_date: '+str(emp_joining_date)
#            s=emp_joining_date.split('-')
#            joining_year=s[0]
#            month=s[1]
#            day=s[2]
#            if current_year == (int)(joining_year):
#                d1=date(int(current_year),01,01)
#                d2=date(int(joining_year),int(month),int(day))
#                days_left=(d2-d1).days
#            else:
#                days_left=0
#            if ((int)(joining_year)%4)==0:
#                days_in_current_year=366
#            else:
#                days_in_current_year=365
#            casual_leave=(days_in_current_year-days_left)*(12/((float)(days_in_current_year)))
#            sick_leave=(days_in_current_year-days_left)*(6/((float)(days_in_current_year)))
##            print 'casual_leave: '+str(casual_leave)
##            print 'sick_leave:'+str(sick_leave)
#            return (casual_leave,sick_leave)
            
   

#        
    
    
#    def __init__(self,request=None,*args,**kwargs):
#        
#        super(Employeeform, self).__init__(*args, **kwargs)
#        if request:
#            super(Employeeform, self).__init__(request, *args, **kwargs)
#            if request['emp_joining_date']:
#                print"employee joining date"
#                emp_joining_date=request['emp_joining_date']
#                self.fields['leaves_quota_year_casual']=self.Calculate_leave()
#                
#                print "working people"
    
    
    
#    class Meta:
#        model=LMS_EMPLOYEE_TABLE
#        fields=('emp_name','emp_number',                
#    'emp_email_id',                   
#    'emp_position',                
#    'emp_team',            
#    'emp_gender',                   
#    'emp_current_address',             
#    'emp_permanent_address',           
#    'Emp_contact_info',               
#    'emp_joining_date',                
#    'leaves_quota_year_casual',           
#    'leaves_quota_year_sick',              
#    'comp_off_Gained',                     
#    'leaves_to_be_approved_by',  )

    class Meta:
            model=LMS_EMPLOYEE_TABLE
            fields=('emp_name','middle_name','last_name','emp_number',                
        'emp_email_id',                   
        'emp_position',                
        'emp_team',            
        'emp_gender',                   
        'emp_current_address',             
        'emp_permanent_address',           
        'Emp_contact_info',               
        'emp_joining_date',
        'emp_dob',
        'emp_bloodgroup'               
          )
    




    
#############################################################form for cvtracking#######################################
##########for help text ######################################################################################
class CV_Helptext(ModelForm):

    helpCustomer_Name=forms.CharField(widget=TextInput(),label= 'Customer Name',required=False)
    Faculty_Name=forms.CharField(widget=TextInput(),label= 'Faculty Name',required=False)
    Faculty_id=forms.CharField(widget=TextInput(),label= 'Faculty Id',required=False)
    Date_Requested=forms.CharField(widget=TextInput(),label= 'Date Requested',required=False)
    Nature_of_the_Request=forms.CharField(widget=TextInput(),label= 'Nature Of Request',required=False)
    Resolution_of_problem=forms.CharField(widget=Textarea(attrs={'cols': 80, 'rows': 10}),label= 'Resolution',required=False)
    Date_Responded=forms.CharField(widget=TextInput(),label= 'Date Responded',required=False)
    Responders_Name=forms.CharField(widget=TextInput(),label= 'Responders Name',required=False)
    Closed_Y_N=forms.CharField(widget=TextInput(),label= 'Closed Y/N',required=False)
    class Meta:
            model=CV_HELPTEXT
            fields=('helpCustomer_Name',
                    'Faculty_Name',
                    'Faculty_id',
                    'Date_Requested',
                    'Nature_of_the_Request',
                    'Resolution_of_problem',
                    'Date_Responded',
                    'Responders_Name',
                    'Closed_Y_N'                           
                     )
        

#################################################################end of help text#############################  
#####################################
class CV_CLIENTFOFPARSINGCVform(ModelForm):
    Parsingclient_name=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='CV Parsing Client Name*',required=False)
    
    def clean(self):
        msg1 = self.cleaned_data['Parsingclient_name']
        
        if self.cleaned_data['Parsingclient_name']== '' or msg1.strip()== '' :
            self._errors['Parsingclient_name']='space not allowered'
        return self.cleaned_data
    
    class Meta:
        model=CV_CLIENTFOFPARSINGCV
        fields=('Parsingclient_name',)


class CV_searchmorespecificForm(forms.Form):
    cv_uid=forms.ModelChoiceField(queryset=CV_UNIVERSITY.objects.all(),label='University')
    cv_cid=forms.ModelChoiceField(queryset=CV_College.objects.all(),label='College')
    cv_did=forms.ModelChoiceField(queryset=CV_Department.objects.all(),label='Department')
   

class CV_searchform(forms.Form):
    search=forms.CharField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Search'}),required=False)


class CV_insertupdatefile(forms.Form):
    Path=forms.CharField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'eg:C:/abc.py'}),label='Enter Path Of File*',required=False)
    

class CV_Passwordrecoveryform(forms.Form):
    username=forms.EmailField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Email address'}),label='Username*',required=False)
    
    def clean(self):
        msg = self.cleaned_data['username']
        if not CV_SIGNUP.objects.filter(username=msg).exists():
            self._errors['username']='Sorry,Username Does Not Exists'
#        if not re.match(r'^[0-9]*$',msg):
#           self._errors['actual_totalleavesdifference']='Only Integer Values Are Alloweddd' 
#           
        if self.cleaned_data['username']== '' or msg.strip()== '' :
            self._errors['username']='space not allowered'
        return self.cleaned_data

class CV_ChangePasswordform(forms.Form):
    username=forms.EmailField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Email address'}),label='Username*',required=False)
    oldpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'Old Password'},render_value=False), label='Old Password*',required=False)
    newpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'New Password'},render_value=False), label='New Password*',required=False)
    confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'Confirm Password'},render_value=False), label='Confirm Password*',required=False)
    
    def clean(self):
        username = self.cleaned_data['username']
        oldpassword = self.cleaned_data['oldpassword']
        newpassword = self.cleaned_data['newpassword']
        confirmpassword = self.cleaned_data['confirmpassword']
        
        #if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
        if self.cleaned_data['newpassword'] != self.cleaned_data['confirmpassword']:
            self._errors['newpassword'] = 'Passwords Must Match'
            self._errors['confirmpassword'] = 'Passwords Must Match'
        
        if not CV_SIGNUP.objects.filter(username=username).exists():
            self._errors['username']='Sorry,Username Does Not Exists'
        if not CV_SIGNUP.objects.filter(username=username,password=oldpassword).exists():
            self._errors['oldpassword']='Password Does Not match'    
#        if not re.match(r'^[0-9]*$',msg):
#           self._errors['actual_totalleavesdifference']='Only Integer Values Are Alloweddd' 
#           
        if self.cleaned_data['username']== '' or username.strip()== '' :
            self._errors['username']='space not allowered'
        if self.cleaned_data['oldpassword']== '' or oldpassword.strip()== '' :
            self._errors['oldpassword']='space not allowered'
        if self.cleaned_data['newpassword']== '' or newpassword.strip()== '' :
            self._errors['newpassword']='space not allowered'
        if self.cleaned_data['confirmpassword']== '' or confirmpassword.strip()== '' :
            self._errors['confirmpassword']='space not allowered'        
            
        return self.cleaned_data
    

class CV_Signinform(forms.Form):
    username=forms.EmailField(widget=TextInput(attrs={'class':'input-block-level','placeholder':'Email address'}),label='Username*',required=False)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-block-level','placeholder':'Password'},render_value=False), label='Password*',required=False)
    #username=forms.EmailField(widget=TextInput(attrs={'class':'input-xlarge','placeholder':'Email address'}),label='USERNAME*',required=False)

def CV_validate_username_unique(value):
        if CV_SIGNUP.objects.filter(username=value).exists():
            raise ValidationError('Sorry, This Username Is Alloted ')

class CV_CaptchaTestForm(ModelForm):
    name=forms.CharField(widget=TextInput(),label='First Name*',required=False)
    middlename=forms.CharField(widget=TextInput(),label='Middle Name',required=False)
    lastname=forms.CharField(widget=TextInput(),label='Last Name*',required=False)
    username=forms.EmailField(validators=[CV_validate_username_unique])
    
    #username=forms.EmailField(widget=TextInput(),label='Username*',required=False)
    password=forms.CharField(widget=forms.PasswordInput(render_value=False), label='Password*',required=False)
    confirm_password=forms.CharField(widget=forms.PasswordInput(render_value=False), label='Confirm Password*',required=False)
    date_of_birth=forms.CharField(widget=TextInput(),label='Date Of Birth(yyyy-mm-dd)',required=False)
    emp_position=forms.ModelChoiceField(queryset=CV_POSITION.objects.all(),label='Position')
    emp_gender =forms.ModelChoiceField(queryset=CV_GENDER.objects.all(),label='Gender')
    #captcha = CaptchaField()
   
    
    def clean(self):
        super(ModelForm,self).clean()
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                self._errors['password'] = 'Passwords Must Match'
                self._errors['confirm_password'] = 'Passwords Must Match'
        return self.cleaned_data
       
    class Meta:
        model=CV_SIGNUP
        fields=('name','middlename','lastname','username','password','confirm_password','date_of_birth','emp_position','emp_gender')#,'captcha')
 
class CV_UploadFileForm(forms.Form):
    
    file  = forms.FileField()

class CV_UNIVERSITYform(ModelForm):
    uid=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='University Id*',required=False)
    uname=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='University Name*',required=False)
    
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['uid']
        msg1 = self.cleaned_data['uname']
        
        if self.cleaned_data['uid']== '' or msg.strip()== '' :
            self._errors['uid']='space not allowered'
        if self.cleaned_data['uname']== '' or msg1.strip()== '' :
            self._errors['uname']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    class Meta:
        model=CV_UNIVERSITY
        fields=('uid','uname')

class CV_COLLEGEform(ModelForm):
    cid=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='College Id*',required=False)
    cname=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='College Name*',required=False)
   
    uid=forms.ModelChoiceField(queryset=CV_UNIVERSITY.objects.all(),label='University')
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['cid']
        msg1 = self.cleaned_data['cname']
        
        if self.cleaned_data['cid']== '' or msg.strip()== '' :
            self._errors['cid']='space not allowered'
        if self.cleaned_data['cname']== '' or msg1.strip()== '' :
            self._errors['cname']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    class Meta:
        model=CV_College
        fields=('cid','cname','uid')

class CV_Departmentform(ModelForm):
    did=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Department Id*',required=False)
    dname=forms.CharField(widget=TextInput(attrs={'class':'input-large'}),label='Department Name*',required=False)
    uid=forms.ModelChoiceField(queryset=CV_UNIVERSITY.objects.all(),label='University')
    cid=forms.ModelChoiceField(queryset=CV_College.objects.all(),label='College')
    
       
    def clean(self):
        #if re.match('/[\s]+$',msg):
        msg = self.cleaned_data['did']
        msg1 = self.cleaned_data['dname']
        
        if self.cleaned_data['did']== '' or msg.strip()== '' :
            self._errors['did']='space not allowered'
        if self.cleaned_data['dname']== '' or msg1.strip()== '' :
            self._errors['dname']='space not allowered'
            ##raise ValidationError("Spaces not allowed")
        #return msg
        return self.cleaned_data
    class Meta:
        model=CV_Department
        fields=('did','dname','uid','cid')#,'cid','uid')
        


class CV_form(ModelForm):
    cvid=forms.CharField(widget=TextInput(),label= 'Faculty Id',required=False)
    cvlast_name=forms.CharField(widget=TextInput(),label= 'Last Name',required=False)##new entry for middle name
    cvemp_name=forms.CharField(widget=TextInput(),label= 'First Name',required=False)# new entry for last name
    cv_uid=forms.ModelChoiceField(queryset=CV_UNIVERSITY.objects.all(),label='University')
    cv_cid=forms.ModelChoiceField(queryset=CV_College.objects.all(), label='College')
    
    cv_did=forms.ModelChoiceField(queryset=CV_Department.objects.all(),label='Department')
    cv_email_id=forms.CharField(widget=TextInput(),label= 'Email Id',required=False)##new entry for middle name
   
    #cv_datereceived=forms.DateField(widget=SelectDateWidget(years=range(2013,2030),attrs={'class':'input-small'}),label='CV Received Date',required=False)
    cv_datereceived   =forms.CharField(widget=TextInput(),label='CV Received Date',required=False)
    
    verify_demog=forms.ModelChoiceField(queryset=CV_VEIFYWITHDENOGFILE.objects.all(),label='Verify With HR File')     
    Parsingclientoption=forms.ModelChoiceField(queryset=CV_CLIENTFOFPARSINGCV.objects.all(),label='Client Name for CV Parsing')
    cv_date_sendtoaspiration   =forms.CharField(widget=TextInput(),label='Date Sent For Parsing(YYYY-MM-DD)',required=False)
    cv_date_expectedfromaspiration=forms.CharField(widget=TextInput(),label='Date Expected From Aspiration(YYYY-MM-DD)',required=False)
    cv_date_recivedfromaspiration=forms.CharField(widget=TextInput(),label='Date Received From Aspiration(YYYY-MM-DD)',required=False)
    cv_date_sendtouniversity =forms.CharField(widget=TextInput(),label='Date CV Send Back To university(YYYY-MM-DD)',required=False)                    ##new entry wait for confirmation
    cv_date_receivedfromuniversity =forms.CharField(widget=TextInput(),label='Date CV Received From University(YYYY-MM-DD)',required=False)               ##new entry wait for confirmation
    no_oftimesendtouniversity  =forms.CharField(widget=TextInput(),label='Total Times CV Send To University',required=False)           
    cv_date_sendforrework  =forms.CharField(widget=TextInput(),label='Date CV Send For Rework(YYYY-MM-DD)',required=False)           
    cv_date_receivedfromrework=forms.CharField(widget=TextInput(),label='Date CV Received After Rework(YYYY-MM-DD)',required=False) 
    nooftime_sendforrework=forms.CharField(widget=TextInput(),label='Count Of Rework',required=False) 
     
    cv_date_validationcompleted=forms.CharField(widget=TextInput(),label='Date Validation Completed(YYYY-MM-DD)',required=False)
    cv_date_cvloadedintest=forms.CharField(widget=TextInput(),label='Date CV Loaded In Test(YYYY-MM-DD)',required=False)
    cv_date_cvloadedinproduction=forms.CharField(widget=TextInput(),label='Date CV Loaded In Production(YYYY-MM-DD)',required=False)
    CV_UserId=forms.CharField(widget=TextInput(),label='User Id',required=False)
    CV_additionaldetails=forms.CharField(widget=TextInput(),label='Additional Details',required=False)
#    def __init__(self,*args, **kwargs):
#        #hide_condition = kwargs.pop('hide_condition',None)
#        super(CVform, self).__init__(*args, **kwargs)
#        self.fields['cv_uid'].widget.attrs['id']='tags1'
#        self.fields['cv_cid'].widget.attrs['id']='tags2' 

#    def __init__(self,request=None,*args,**kwargs):
#        
#        super(CVform, self).__init__(*args, **kwargs)
#        if request:
#            super(CVform, self).__init__(request, *args, **kwargs)
#            if request['cv_uid']:
#                print"cv_uid---"
#                cv_uid=request['cv_uid']
#                self.fields['cv_cid']=forms.ModelChoiceField(required=True,queryset=CV_College.objects.exclude(uid=cv_uid))
#                #manager_name=forms.ModelChoiceField(queryset=Employee1.objects.exclude(first_name='first_name'))
#                print "checked"
#    def __init__(self, *args, **kwargs):
#        forms.Form.__init__(self, *args, **kwargs)
#        parents=CV_UNIVERSITY.objects.all()
#        if len(parents)==1:
#            self.fields['cv_uid'].initial=parents[0].pk

#        parent_id=self.fields['cv_uid'].initial or self.initial.get('cv_uid') \
#                  or self._raw_value('cv_uid')
#        if parent_id:
#            # parent is known. Now I can display the matching children.
#            cv_cid=CV_College.objects.filter(uid__id=parent_id)
#            self.fields['cv_cid'].queryset=cv_cid
#            if len(cv_cid)==1:
#                self.fields['children'].initial=cv_cid[0].pk  

    class Meta:
            model=CV_CV
            fields=('cvid','cvlast_name','cvemp_name','cv_uid','cv_cid','cv_did','cv_email_id',                
        'cv_datereceived',                   
        'verify_demog','Parsingclientoption',                
        'cv_date_sendtoaspiration',            
        'cv_date_expectedfromaspiration',                   
        'cv_date_recivedfromaspiration','cv_date_sendtouniversity','cv_date_receivedfromuniversity', 'no_oftimesendtouniversity', 'cv_date_sendforrework', 'cv_date_receivedfromrework' , 'nooftime_sendforrework',             
        'cv_date_validationcompleted',           
        'cv_date_cvloadedintest',               
        'cv_date_cvloadedinproduction',
        'CV_UserId',
        'CV_additionaldetails'                
          )
        
class CV_CalculateCvcountform(forms.Form):
    fromdate=forms.DateField(widget=SelectDateWidget(years=range(2013,2030),attrs={'class':'input-small'}),label='From Date*',required=False)
    todate=forms.DateField(widget=SelectDateWidget(years=range(2013,2030),attrs={'class':'input-small'}),label='To Date*',required=False)
    cv_uid=forms.ModelChoiceField(queryset=CV_UNIVERSITY.objects.all(),label='University')
    
#     class Meta:
#             model=CV_CV
#             fields=('cv_uid'               
#           )
    


  
