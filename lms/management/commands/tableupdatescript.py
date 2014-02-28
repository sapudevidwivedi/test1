
from django.core.management import setup_environ
import lms.settings
setup_environ(lms.settings)

from django.core.management.base import BaseCommand, CommandError
from lms.models import LMS_LEAVES_summary_TABLE
from django.utils.datetime_safe import datetime

class Command(BaseCommand):
    args = '21'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        #for poll_id in args:
#        try:
        z123=LMS_LEAVES_summary_TABLE.objects.all()
        for i in z123:
            summary_id=i.summary_id
            summary_id=str(summary_id)
            eligiable_avaliable_leave=i.eligiable_avaliable_leave
            eligiable_avaliable_leave=float(eligiable_avaliable_leave)+1.5
            LMS_LEAVES_summary_TABLE.objects.filter(summary_id=summary_id).update(eligiable_avaliable_leave=eligiable_avaliable_leave)
#                
            #poll = Poll.objects.get(pk=int(poll_id))
#        except Poll.DoesNotExist:
#            raise CommandError('Poll "%s" does not exist' % poll_id)

        LMS_LEAVES_summary_TABLE.opened = False
        #LMS_LEAVES_summary_TABLE.save()

        self.stdout.write('Successfully closed poll "%s"')

#def updatetable_lmsleavesummary():
#    z123=LMS_LEAVES_summary_TABLE.objects.all()
#    for i in z123:
#        summary_id=i.summary_id
#        summary_id=str(summary_id)
#        eligiable_avaliable_leave=i.eligiable_avaliable_leave
#        eligiable_avaliable_leave=float(eligiable_avaliable_leave)+1.5
#        print 'summary_id:'+str(summary_id)
#        print 'eligiable_avaliable_leave:'+str(eligiable_avaliable_leave)
#        LMS_LEAVES_summary_TABLE.objects.filter(summary_id=summary_id).update(eligiable_avaliable_leave=eligiable_avaliable_leave)
#                
#    #qq=LMS_LEAVES_summary_TABLE.objects.all().update(eligiable_avaliable_leave=1.5,d=datetime.date.today().month,y=datetime.date.today().year
##)
#      
   
