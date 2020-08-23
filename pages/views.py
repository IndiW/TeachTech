from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar, Data, Figure, Layout
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
    x_data = [2.4,3.6,7.2,13.2,25,28.3,35.3,36.7,37.5,44.6]
    y_data = [0,-1,-1,0,1,1,1,0,0,-1]
    layout = Layout(
        title='Student Comprehension',
        xaxis=dict(
            title='Timestamp',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Comprehension',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    data = Data([Scatter(x=x_data, y=y_data,
                        mode='lines+markers', name='Comprehension Data',
                        opacity=0.8, marker_color='blue')])
    fig = Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div')

    x_bar_data = ["3:34","15:55","24:48","44:30"]
    y_bar_data = [2,4,3,6]
    layout2 = Layout(
        title='Topics that needed repeating',
        xaxis=dict(
            title='Timestamp',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Number of votes',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    data2 = Data([Bar(x=["3:34","15:55","24:48","44:30"],y=[2,4,3,6],name="Repeat Requests")])
    fig2 = Figure(data=data2,layout=layout2)
    plot_div2 = plot(fig2,output_type='div')
    
    return render(request,"teacher.html",{'plot_div': plot_div,'plot_div2': plot_div2})

