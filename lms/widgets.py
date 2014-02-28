from django import forms
from django.db import models
from django.template.loader import render_to_string
from django.forms.widgets import Select, MultiWidget, DateInput, TextInput
from time import strftime
from django.forms import extras
from django.forms.extras import widgets
from django.forms.extras.widgets import SelectDateWidget


class MySelectDateWidget(SelectDateWidget):
    def render(self, name, value, attrs=None):
        from collections import namedtuple
        date_tweak = namedtuple('Date', 'year month day')
        date_value = date_tweak(1970, 1, 1) #tweak to cheat SelectDateWidget's 
                                   #render method which expects a datetime object
        return super(MySelectDateWidget, self).render(name, date_value, attrs)



class JqSplitDateTimeWidget(MultiWidget):

    def __init__(self, attrs=None, date_format=None, time_format=None):
        date_class = attrs['date_class']
        time_class = attrs['time_class']
        del attrs['date_class']
        del attrs['time_class']

        time_attrs = attrs.copy()
        time_attrs['class'] = time_class
        date_attrs = attrs.copy()
        date_attrs['class'] = date_class
        
        widgets = (DateInput(attrs=date_attrs, format=date_format), 
                   TextInput(attrs=time_attrs), TextInput(attrs=time_attrs), 
                   Select(attrs=attrs, choices=[('AM','AM'),('PM','PM')]))
        
        super(JqSplitDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            d = strftime("%Y-%m-%d", value.timetuple())
            hour = strftime("%I", value.timetuple())
            minute = strftime("%M", value.timetuple())
            meridian = strftime("%p", value.timetuple())
            return (d, hour, minute, meridian)
        else:
            return (None, None, None, None)

    def format_output(self, rendered_widgets):
        """
        Given a list of rendered widgets (as strings), it inserts an HTML
        linebreak between them.
        
        Returns a Unicode string representing the HTML for the whole lot.
        """
        return "Date: %s<br/>Time: %s:%s %s" % (rendered_widgets[0], rendered_widgets[1],
                                                rendered_widgets[2], rendered_widgets[3])

    class Media:
        css = {
            }
        js = (
            "js/jqsplitdatetime.js",
            )