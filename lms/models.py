from django.db import models
from django.core.exceptions import ValidationError


class LMS_NEWS(models.Model):
    news_id=models.AutoField(primary_key=True)
    entigence_date=models.CharField(max_length=200,blank=False)
    entigence_news=models.CharField(max_length=200,blank=False)
    entigence_deliveredby=models.CharField(max_length=200,blank=False)
    
    def __unicode__(self):
        namexy=''+str(self.entigence_date)+""+str(self.entigence_news)+""+str(self.entigence_deliveredby)
        return namexy
        
    
class LMS_HOLIDAY_TYPE(models.Model):
    type_id                      =models.AutoField(primary_key=True) 
    Holiday_Type                =models.CharField(max_length=200,blank=False)
    holiday_informed_client         =models.CharField(max_length=200,blank=False)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
        
    def __unicode__(self):
        name2=''+str(self.Holiday_Type)
        return name2


#def validate_not_spaces(value):
#    if value.strip() == '':
#        raise ValidationError(u"You must provide more than just whitespace.")
class LMS_GENDER(models.Model):
    gender_id                      =models.AutoField(primary_key=True)
    emp_gender                       =models.CharField(max_length=200,blank=False,)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
    def __unicode__(self):
        return self.emp_gender
    
     
class LMS_POSITION(models.Model):
    emp_position_id                      =models.AutoField(primary_key=True)
    emp_position                       =models.CharField(max_length=200,blank=False)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
    def __unicode__(self):
        return self.emp_position  
    
class LMS_TEAM(models.Model):
    emp_team_id                      =models.AutoField(primary_key=True)
    emp_team                       =models.CharField(max_length=200,blank=False)
    mh1                  =models.CharField(max_length=200,blank=False)
    mh2                =models.CharField(max_length=200,blank=False)
    mh3                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
    def __unicode__(self):
        return self.emp_team        
                  



            
class LMS_EMPLOYEE_TABLE(models.Model):
    emp_id = models.AutoField(primary_key=True)
    #emp_number=models.CharField(max_length=200,blank=False)
    #emp_number=models.CharField(max_length=200,unique=True)
    emp_number=models.CharField(max_length=200,unique=True,null=True)
    
    emp_name = models.CharField(max_length=200,blank=False)# first name
    middle_name = models.CharField(max_length=200,blank=False)#newentry for middle name
    last_name = models.CharField(max_length=200,blank=False)#new entry for last name
    emp_email_id =models.CharField(max_length=200,unique=True,null=True)
    emp_position                =models.ForeignKey(LMS_POSITION,related_name='emp_position1')
    emp_team             =models.ForeignKey(LMS_TEAM,related_name='emp_team1')
    
    emp_gender                      =models.ForeignKey(LMS_GENDER,related_name='emp_gender1')
    
    emp_current_address             =models.CharField(max_length=200,blank=False)
    emp_permanent_address           =models.CharField(max_length=200,blank=False)
    Emp_contact_info                =models.CharField(max_length=200,blank=False)
    emp_joining_date                =models.CharField(max_length=200,blank=False)
    emp_dob=models.CharField(max_length=200,blank=False)
    emp_bloodgroup=models.CharField(max_length=200,blank=False)

    leaves_quota_year_casual           =models.CharField(max_length=200,blank=False)
    leaves_quota_year_sick              =models.CharField(max_length=200,blank=False)
    comp_off_Gained                     =models.CharField(max_length=200,blank=False)
    leaves_to_be_approved_by            =models.CharField(max_length=200,blank=False)
    created_by                          =models.CharField(max_length=200,blank=False)
    created_date                            =models.CharField(max_length=200,blank=False)
    updated_by                              =models.CharField(max_length=200,blank=False)
    updated_date                            =models.CharField(max_length=200,blank=False)


    def __unicode__(self):
        name=''+str(self.emp_name)+"-"+str(self.middle_name)+"-"+str(self.last_name)#+"-"+str(self.emp_number)
        return name


#### to_field='site_id',db_column='emp_numberxxx'
class LMS_SUPERVISORHIERACHY(models.Model):
    supervisor_hierarchy_id = models.AutoField(primary_key=True)
    emp_number=models.CharField(max_length=200,blank=False)
    supervisor_number=models.CharField(max_length=200,blank=False)
    
    emp_number1=models.ForeignKey(LMS_EMPLOYEE_TABLE,to_field='emp_number',related_name='Employee Number0000')
    supervisor_number1=models.ForeignKey(LMS_EMPLOYEE_TABLE,to_field='emp_number',related_name='Supervisor Number00000000')
   
    #emp_number=models.ForeignKey(LMS_EMPLOYEE_TABLE,to_field='emp_number',related_name='Employee Number0000')
    #supervisor_number=models.ForeignKey(LMS_EMPLOYEE_TABLE,to_field='emp_number',related_name='Supervisor Number00000000')
   
    emp_team    =models.ForeignKey(LMS_TEAM,related_name='emp_team14555')
    
    created_by                          =models.CharField(max_length=200,blank=False)
    created_date                            =models.CharField(max_length=200,blank=False)
    updated_by                              =models.CharField(max_length=200,blank=False)
    updated_date                            =models.CharField(max_length=200,blank=False)


    def __unicode__(self):
        name=''+str(self.emp_number)+"-"+str(self.supervisor_number)
        return name
#############

    
##########signup page table
###########
class LMS_SIGNUP(models.Model):
    signup_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,blank=False)
    middlename=models.CharField(max_length=200,blank=False)
    lastname=models.CharField(max_length=200,blank=False)
    
    username=models.CharField(max_length=200,blank=False)
    password=models.CharField(max_length=200,blank=False)
    confirm_password=models.CharField(max_length=200,blank=False)
    date_of_birth=models.CharField(max_length=200,blank=False)
    emp_gender =models.ForeignKey(LMS_GENDER,related_name='emp_gender2')
    captcha=models.CharField(max_length=200,blank=False)
    
    def __unicode__(self):
        name=''+str(self.name)+""+str(self.middlename)+""+str(self.lastname)
        #+""+str(self.username)
        #+""+str(self.password)
        #+""+str(self.confirm_password)+""+str(self.date_of_birth)
#        +""+str(self.emp_gender)
        return name
    
class LMS_SIGNIN(models.Model):
    username=models.CharField(max_length=200,blank=False)
    password=models.CharField(max_length=200,blank=False)  
      
    def __unicode__(self):
        name=''+str(self.username)+""+str(self.password)
        return name    

class LMS_LEAVE_INFO_TABLE(models.Model):
    leave_id                      =models.AutoField(primary_key=True)
    emp_id                       =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_id1',null=True)#,related_name='emp_id1'
    emp_name                =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_name1',null=True)
    emp_team                 =models.ForeignKey(LMS_TEAM,related_name='emp_team2',null=True)
    leaves_applied_date         =models.CharField(max_length=200,blank=False)
    
    leaves_from         =models.CharField(max_length=200,blank=False)
    leaves_till       =models.CharField(max_length=200,blank=False)
    actual_totalleavesdifference=models.CharField(max_length=200,blank=False)
    leaves_applied_reason            =models.CharField(max_length=200,blank=False)
    leaves_status            =models.CharField(max_length=200,blank=False)
    leaves_approved_by    =models.CharField(max_length=200,blank=False)
    leaves_approved_by_tl      =models.CharField(max_length=200,blank=False)
    leaves_approved_by_manager             =models.CharField(max_length=200,blank=False)
    leaves_approved_by_HR    =models.CharField(max_length=200,blank=False)##supervisor email_id
    leave_type_id           =models.CharField(max_length=200,blank=False)
    comments                =models.CharField(max_length=200,blank=False)
    name=models.CharField(max_length=200,blank=False)
    emp_id_ofuser=models.CharField(max_length=200,blank=False)
        
    def __unicode__(self):
        name1=''+str(self.emp_name)+""+str(self.emp_team)+""+str(self.leaves_applied_date)
        +""+str(self.leaves_from)+""+str(self.leaves_till)+""+str(self.leaves_applied_reason)
        +""+str(self.leaves_status)+""+str(self.actual_totalleavesdifference)
        return name1
    
class LMS_HOLIDAY_LIST(models.Model):
    holiday_id                      =models.AutoField(primary_key=True)
    holiday_called                      =models.CharField(max_length=200,blank=False)
    Holiday_Type                =models.ForeignKey(LMS_HOLIDAY_TYPE)
    holiday_date                =models.CharField(max_length=200,blank=False)
    holiday_informed_client        =models.CharField(max_length=200,blank=True)
    created_by                  =models.CharField(max_length=200)
    created_date                =models.CharField(max_length=200)
    updated_by                  =models.CharField(max_length=200)
    updated_date                =models.CharField(max_length=200)
        
    def __unicode__(self):
        name2=''+str(self.holiday_called)+""+str(self.Holiday_Type)+""+str(self.holiday_date)
        return name2    
class LMS_DEPARTMENT_EMP_DETAILS(models.Model):
    Dept_ID                      =models.AutoField(primary_key=True)
    emp_id                       =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_id2')
    emp_team                 =models.ForeignKey(LMS_TEAM,related_name='emp_team3')
    Department_name              =models.CharField(max_length=200,blank=False)
    comments                    =models.CharField(max_length=200,blank=False)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
    
    def __unicode__(self):
        name3=''+str(self.emp_team)+""+str(self.Department_name)+""+str(self.comments)
       
        return name3       

class LMS_EMPLOYEE_ADDRESS_INFO(models.Model):
    
    emp_id                       =models.ForeignKey(LMS_EMPLOYEE_TABLE)
    emp_current_address                =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_current_address1')
    emp_permanent_Address                =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_permanent_address1')
    active_Address                  =models.CharField(max_length=200,blank=False)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
        
    def __unicode__(self):
        name4=''+str(self.emp_current_address)+""+str(self.emp_permanent_Address)+""+str(self.active_Address)
       
        return name4       
    
        
class LMS_EMPLOYEE_CONTACT_INFO(models.Model):
    
    emp_id                       =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_id3')
    emp_contact_info               =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_contact_info1')
    emp_contact_info_2                 =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_contact_info_2_1')
    emp_contact_info_3         =models.CharField(max_length=200,blank=False)
    active_number        =models.CharField(max_length=200,blank=False)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)

    def __unicode__(self):
        name5=''+str(self.emp_contact_info)+""+str(self.emp_contact_info_2)+""+str(self.emp_contact_info_3)
        +""+str(self.active_number)
       
        return name5
     
class LMS_EMPLOYEE_JOINING_TABLE(models.Model):
    #leave_id                      =models.AutoField(primary_key=True)
    emp_id                       =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_id4')
    emp_joining_date               =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_joining_date1')
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
    
    def __unicode__(self):
        name6=''+str(self.emp_joining_date)
        return name6


###########LEAVE SUMMARY TABLE#########

class LMS_LEAVES_summary_TABLE(models.Model):
    summary_id =models.AutoField(primary_key=True)
   # emp_id   =models.ForeignKey(LMS_EMPLOYEE_TABLE,related_name='emp_id5')
    name_of_employee=models.CharField(max_length=200,blank=False)
    total_casual_leaves=models.CharField(max_length=200,blank=False)
    total_sick_leaves=models.CharField(max_length=200,blank=False)
    #current_casual_leaves=models.CharField(max_length=200,blank=False)
    #current_sick_leaves=models.CharField(max_length=200,blank=False)
    
    emp_id_of_employee=models.CharField(max_length=200,blank=False)#####new addition
    eligiable_avaliable_leave=models.CharField(max_length=200,blank=False)####new addition
    d=models.CharField(max_length=200,blank=False)####new addition
    y=models.CharField(max_length=200,blank=False)####new addition
    
    casual_leaves_used=models.CharField(max_length=200,blank=False)
    sick_leaves_used=models.CharField(max_length=200,blank=False)
    leave_comp_off= models.CharField(max_length=200,blank=False)
    position   =models.ForeignKey(LMS_POSITION,related_name='position_6')
    team   =models.ForeignKey(LMS_TEAM,related_name='emp_team7')
    email_id=models.CharField(max_length=200,blank=False)
    passwd=models.CharField(max_length=200,blank=False)
 
         
    def __unicode__(self):
#        return (str(self.name_of_employee)+" "+str(self.total_casual_leaves)+" "+str(self.total_sick_leaves)
#        +" "+str(self.current_casual_leaves)+" "+str(self.current_sick_leaves)+" "+str(self.casual_leaves_used)
#        +" "+str(self.sick_leaves_used)+" "+str(self.leave_comp_off)+" "+str(self.position))
        name7=''+str(self.name_of_employee)
        return name7
    
class LMS_LEAVE_TYPES(models.Model):
    leave_type_id                      =models.AutoField(primary_key=True)
    leaves_type         =models.CharField(max_length=200,blank=False)
    created_by                  =models.CharField(max_length=200,blank=False)
    created_date                =models.CharField(max_length=200,blank=False)
    updated_by                  =models.CharField(max_length=200,blank=False)
    updated_date                =models.CharField(max_length=200,blank=False)
    
    def __unicode__(self):
        name8=''+str(self.leaves_type)
        return name8  
              
            
    
            
#####################################################models for cvtracking #############################################################################

####################new entry for help text#############
class CV_HELPTEXT(models.Model):
    helptext_id                      =models.AutoField(primary_key=True)
    helpCustomer_Name                       =models.CharField(max_length=200,blank=False,)
    Faculty_Name=models.CharField(max_length=200,blank=False,)
    Faculty_id=models.CharField(max_length=200,blank=False,)
    Date_Requested=models.CharField(max_length=200,blank=False,)
    Nature_of_the_Request=models.CharField(max_length=200,blank=False,)
    Resolution_of_problem=models.CharField(max_length=200,blank=False,)
    Date_Responded=models.CharField(max_length=200,blank=False,)
    Responders_Name=models.CharField(max_length=200,blank=False,)
    Closed_Y_N=models.CharField(max_length=200,blank=False,)
    def __unicode__(self):
        name=''+str(self.helpCustomer_Name)+"-"+str(self.Faculty_Name)
        return name


########################################################
class CV_CLIENTFOFPARSINGCV(models.Model):
    Parsingclient_id=models.AutoField(primary_key=True)
    Parsingclient_name=models.CharField(max_length=200,blank=False)
    
    def __Unicode__(self):
        return self.Parsingclient_name

class CV_GENDER(models.Model):
    gender_id                      =models.AutoField(primary_key=True)
    emp_gender                       =models.CharField(max_length=200,blank=False,)

    def __unicode__(self):
        return self.emp_gender

class CV_POSITION(models.Model):
    emp_position_id                      =models.AutoField(primary_key=True)
    emp_position                       =models.CharField(max_length=200,blank=False)

    def __unicode__(self):
        return self.emp_position  
        
class CV_SIGNUP(models.Model):
    signup_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,blank=False)
    middlename=models.CharField(max_length=200,blank=False)
    lastname=models.CharField(max_length=200,blank=False)
    
    username=models.CharField(max_length=200,blank=False)
    password=models.CharField(max_length=200,blank=False)
    confirm_password=models.CharField(max_length=200,blank=False)
    date_of_birth=models.CharField(max_length=200,blank=False)
    emp_position=models.ForeignKey(CV_POSITION,related_name='emp_position2')
    emp_gender =models.ForeignKey(CV_GENDER,related_name='emp_gender2')
    captcha=models.CharField(max_length=200,blank=False)
    
    def __unicode__(self):
        name=''+str(self.name)+""+str(self.middlename)+""+str(self.lastname)
        return name

class CV_VEIFYWITHDENOGFILE(models.Model):
    demogfile_id                      =models.AutoField(primary_key=True)
    demogfileoption                       =models.CharField(max_length=200,blank=False,)

    def __unicode__(self):
        return self.demogfileoption
 

class CV_UNIVERSITY(models.Model):
    normal_id=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=200,unique=True,null=True)
    uname=models.CharField(max_length=200,blank=False)
    
    
    def __unicode__(self):
        namexy=''+str(self.uname)
        return namexy

class CV_College(models.Model):
    normalCollege_id=models.AutoField(primary_key=True)
    cid=models.CharField(max_length=200,unique=True,null=True)
    cname=models.CharField(max_length=200,blank=False)
    uid  = models.ForeignKey(CV_UNIVERSITY,related_name='universityid2')###test
    
    def __unicode__(self):
        namexyc=''+str(self.cname)
        return namexyc

class CV_Department(models.Model):
    normalDepartment_id=models.AutoField(primary_key=True)
    did=models.CharField(max_length=200,unique=True,null=True)
    dname=models.CharField(max_length=200,blank=False)
    cid  = models.ForeignKey(CV_College,related_name='collegeid2')
    uid  = models.ForeignKey(CV_UNIVERSITY,related_name='universityid3')###test
    
    def __unicode__(self):
        #namexy=''+str(self.uid)+"-"+str(self.uname)
        namexyd=''+str(self.dname)
        return namexyd    

class CV_CV(models.Model):
    cv_id = models.AutoField(primary_key=True)
    #emp_number=models.CharField(max_length=200,blank=False)
    #emp_number=models.CharField(max_length=200,unique=True
    
    cvid=models.CharField(max_length=200,unique=True,null=True)###actual cv id
    cvlast_name = models.CharField(max_length=200,blank=False)
    cvemp_name = models.CharField(max_length=200,blank=False)
    cv_uid                      =models.ForeignKey(CV_UNIVERSITY,related_name='universityid1')
    cv_cid                      =models.ForeignKey(CV_College,related_name='collegeid1')
    cv_did                      =models.ForeignKey(CV_Department,related_name='departmentid1')
    cv_email_id  = models.CharField(max_length=200,blank=False) # new entry
    cv_datereceived      =models.CharField(max_length=200,blank=False)
    verify_demog                      =models.ForeignKey(CV_VEIFYWITHDENOGFILE,related_name='deogfileoption1')
    Parsingclientoption  =models.ForeignKey(CV_CLIENTFOFPARSINGCV,related_name='Parsingclient_name1')    

    cv_date_sendtoaspiration      =models.CharField(max_length=200,blank=False)
    cv_date_expectedfromaspiration      =models.CharField(max_length=200,blank=False)
    cv_date_recivedfromaspiration      =models.CharField(max_length=200,blank=False)
    cv_date_sendtouniversity        =models.CharField(max_length=200,blank=False)##new entry wait for confirmation
    cv_date_receivedfromuniversity   =models.CharField(max_length=200,blank=False)##new entry wait for confirmation
    no_oftimesendtouniversity =models.CharField(max_length=200,blank=False)##new entry wait for confirmation
    cv_date_sendforrework              =models.CharField(max_length=200,blank=False)##new entry wait for confirmation
    cv_date_receivedfromrework        =models.CharField(max_length=200,blank=False)##new entry wait for confirmation
    nooftime_sendforrework           =models.CharField(max_length=200,blank=False)##new entry wait for confirmation
    
    cv_date_validationcompleted      =models.CharField(max_length=200,blank=False)
    cv_date_cvloadedintest      =models.CharField(max_length=200,blank=False)
    cv_date_cvloadedinproduction      =models.CharField(max_length=200,blank=False)
    CV_UserId =models.CharField(max_length=200,blank=False)
    CV_additionaldetails=models.CharField(max_length=200,blank=False)    

    def __unicode__(self):
        name=''+str(self.cvid)+"-"+str(self.cvlast_name)+"-"+str(self.cvemp_name)+"-"+str(self.cv_uid)
        return name
    
            
        

    

