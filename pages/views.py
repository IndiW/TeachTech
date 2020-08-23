from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
# Create your views here.

def home_view(request, *args,**kwargs):
    #return HttpResponse("<h1>Hello</h1>")
    return render(request,"home.html",{})

def student_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "test",
        "number" : 123,
        "my_list" : ["Makes sense","idgi"]
    }
    return render(request,"student.html",my_context)


def teacher_view(request, *args, **kwargs):
    x_data = [i for i in range(10)]
    y_data = [0,0,-1,0,1,0,1,1,0,-1]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines+markers', name='Comprehension Data',
                        opacity=0.8, marker_color='blue')],
            output_type='div')
    
    return render(request,"teacher.html",{'plot_div': plot_div})

