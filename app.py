from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.figure_factory as ff

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#Review start date of obj through yearly reports
@app.route("/1")
def index_obj1():
   df_obj1_1 = pd.DataFrame([
    dict(Task = "1", Start = "2023-03-01", Finish = "2023-05-31", Completion_pct = 76, Description = ""),
    dict(Task = "2", Start = "2023-03-31", Finish = "2023-04-30", Completion_pct = 100, Description = ""),
    dict(Task = "3", Start = "2023-03-31", Finish = "2023-04-30", Completion_pct = 76, Description = ""),
    dict(Task = "4", Start = "2023-04-30", Finish = "2023-06-30", Completion_pct = 75, Description = ""),
    dict(Task = "5", Start = "2023-03-31", Finish = "2023-04-30", Completion_pct = 76, Description = ""),
    dict(Task = "6", Start = "2020-01-05", Finish = "2023-03-31", Completion_pct = 100, Description = ""),
    dict(Task = "7", Start = "2021-01-20", Finish = "2023-06-30", Completion_pct = 100, Description = ""),
    dict(Task = "8", Start = "2019-01-20", Finish = "2023-06-30", Completion_pct = 100, Description = ""),
    dict(Task = "9", Start = "2022-01-20", Finish = "2023-06-30", Completion_pct = 25, Description = ""),
    dict(Task = "10", Start = "2022-01-20", Finish = "2023-06-30", Completion_pct = 76, Description = ""),
    dict(Task = "11", Start = "2020-01-20", Finish = "2023-06-30", Completion_pct = 100, Description = ""),
    dict(Task = "12", Start = "2020-01-20", Finish = "2023-06-30", Completion_pct = 100, Description = "")  
])

   fig1 = ff.create_gantt(df_obj1_1, title=None,index_col='Completion_pct', show_colorbar= True, 
                          colors= ['rgb(210, 43, 43)', 'rgb(64, 224, 208)'],
                      showgrid_x=True, showgrid_y=True,height=800)
   graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
   header1 = "Title"
   description1 = """ 
   Description
   """

   df_obj1_2 = pd.DataFrame([
    dict(Task = "1", Start = "2023-05-31", Finish = "2023-06-30", Completion_pct = 0, Description = ""),
    dict(Task = "2", Start = "2022-09-30", Finish = "2023-05-31", Completion_pct = 50, Description = ""),
    dict(Task = "3", Start = "2022-09-30", Finish = "2023-06-30", Completion_pct = 60, Description = "")
])
   
   fig2 = ff.create_gantt(df_obj1_2, title=None,index_col='Completion_pct', show_colorbar = True,
                          colors= ['rgb(210, 43, 43)', 'rgb(64, 224, 208)'],
                      showgrid_x=True, showgrid_y=True,height=800)
   graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
   header2 = "Title"
   description2 = """
   Description
   """
   
   df_obj1_3 = pd.DataFrame([
      dict(Task = "1", Start = "2023-05-30", Finish = "2023-06-30", Completion_pct = 0, Description = ""),
      dict(Task = "2", Start = "2021-09-01", Finish = "2023-04-30", Completion_pct = 0, Description = ""),
      dict(Task = "3", Start = "2021-09-01", Finish = "2023-05-30", Completion_pct = 0, Description = ""),
      dict(Task = "4", Start = "2021-06-01", Finish = "2023-04-30", Completion_pct = 75, Description = ""),
      dict(Task = "5", Start = "2021-06-01", Finish = "2023-04-30", Completion_pct = 100, Description = ""), 
      dict(Task = "6", Start = "2021-01-01", Finish = "2023-05-30", Completion_pct = 76, Description = "")
   ])
   
   fig3 = ff.create_gantt(df_obj1_3, title=None,index_col='Completion_pct', show_colorbar = True,
                          colors= ['rgb(210, 43, 43)', 'rgb(64, 224, 208)'],
                      showgrid_x=True, showgrid_y=True,height=800)
   graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
   header3 = "Title"
   description3 = """
   Description
   """
   
   df_obj1_4 = pd.DataFrame([
      dict(Task = "1", Start = "2023-04-30", Finish = "2023-05-31", Completion_pct = 0, Description = ""),
      dict(Task = "2", Start = "2021-06-01", Finish = "2023-04-30", Completion_pct = 100, Description = ""),
      dict(Task = "3", Start = "2021-06-01", Finish = "2023-04-30", Completion_pct = 100, Description = ""),
      dict(Task = "4", Start = "2021-01-01", Finish = "2023-06-30", Completion_pct = 100, Description = "")
   ])
   
   fig4 = ff.create_gantt(df_obj1_4, title=None,index_col='Completion_pct', show_colorbar = True,
                          colors= ['rgb(210, 43, 43)', 'rgb(64, 224, 208)'],
                      showgrid_x=True, showgrid_y=True,height=800)
   graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
   header4 = "Title"
   description4 = """
   Description
   """   
   
   df_obj1_5 = pd.DataFrame([
      dict(Task = "1", Start = "2023-06-01", Finish = "2023-06-30", Completion_pct = 0, Description = ""),
      dict(Task = "2", Start = "2023-06-01", Finish = "2023-06-30", Completion_pct = 0, Description = ""),
      dict(Task = "3", Start = "2021-01-01", Finish = "2023-06-30", Completion_pct = 50, Description = "")
   ])
   
   fig5 = ff.create_gantt(df_obj1_5, title=None,index_col='Completion_pct', show_colorbar = True,
                          colors= ['rgb(210, 43, 43)', 'rgb(64, 224, 208)'],
                      showgrid_x=True, showgrid_y=True,height=800)
   graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
   header5 = "Title"
   description5 = """
   Description
   """   
   
   return render_template('Ganttcharts.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON, graph4JSON=graph4JSON, graph5JSON=graph5JSON,
                          header1 = header1, description1 = description1, header2 = header2, description2 = description2, 
                          header3 = header3, description3 = description3, header4= header4, description4 = description4, header5 = header5, description5 = description5)
   
@app.route("/2")
def index_obj2():
    df_obj2_1 = pd.DataFrame([
    dict(Task = "1", Start = "2023-01-01", Finish = "2023-06-30", Completion_pct = 25, Description = ""),
    dict(Task = "2", Start = "2023-01-01", Finish = "2023-05-31", Completion_pct = 100, Description = ""),
    dict(Task = "3", Start = "2023-01-01", Finish = "2023-05-10", Completion_pct = 100, Description = ""),
    dict(Task = "4", Start = "2022-01-20", Finish = "2023-03-31", Completion_pct = 100, Description = "")    
])

    fig1 = ff.create_gantt(df_obj2_1, title=None,index_col='Completion_pct', show_colorbar= True, 
                          colors= ['rgb(210, 43, 43)', 'rgb(64, 224, 208)'],
                      showgrid_x=True, showgrid_y=True,height=800)
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    header1 = "Title"
    description1 = """
    Description
    """
    
    return render_template('Ganttcharts2.html', graph1JSON=graph1JSON, header1=header1, description1=description1)
    