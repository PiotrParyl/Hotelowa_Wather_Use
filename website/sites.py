from optparse import Values
from flask import Blueprint, render_template
from . import *
import pygal
views = Blueprint('views', __name__)






@views.route('/')
def home():



    '''Prepare data for line graph'''
    values = [1,2,3,4]
    labels = [1,2,3,4]



    '''Renders bar graph to web page based on Fibonacci sequence.'''
    bar_chart = pygal.Bar(height=300)  # instance of Bar class
    bar_chart.title = 'Zużycie wody przez 7h'  # title of bar chart
    bar_chart.add('litry', [water_use_per_hour(24), water_use_per_hour(20), water_use_per_hour(10), water_use_per_hour(6), water_use_per_hour(4), water_use_per_hour(2), water_use_per_hour(1)])  # add fibo data to chart
    chart = bar_chart.render_data_uri()  # render bar chart


    return render_template('home.html',chart=chart,values=values, labels=labels)


@views.route('/login')
def login():
    return render_template('login.html')


