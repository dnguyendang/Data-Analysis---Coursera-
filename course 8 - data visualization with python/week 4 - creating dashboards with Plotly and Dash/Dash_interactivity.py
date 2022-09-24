### TASK 1 - READ THE DATA 

# importing necessary libraries
# reading the data
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', encoding = "ISO-8859-1", dtype={'Div1Airport': str, 'Div1TailNum': str,'Div2Airport': str, 'Div2TailNum': str})
### TASK 2 - CREATE DASH APPLICATION AND GET THE LAYOUT SKELETON 

# title of the application - title added using html.H1() tag
# component to enter input year inside a layout division - layout division added using html.Div() and input component added using dcc.Input() tag inside the layout division
# chart conveying the average monthly arrival delay inside a layout division - layout division added using html.Div() and chart added using dcc.Graph() tag inside the layout division

#create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Performance Dashboard', style={'textAlign':'center', 'color':'#503D36', 'font-size':40}), html.Div(["Input Year", dcc.Input(id='input-yr', value='2010', type='number', style={'height':'50px', 'font-size':35}),],style={'font-size':40}),html.Br(),html.Br(),html.Div(dcc.Graph(id='line-plot')), ])


### TASK 3 - UPDATE LAYOUT COMPONENTS

# heading reference: Plotly H1 HTML Component
# Title as Airline Performance Dashboard
# use style parameter and make the title center aligned, with color code #503D36, and font-size as 40

# update dcc.Input component id as input-year, default value as 2010, and type as number. use style parameter and assign height of the input box to be 50px and font-size to be 35
# use style parameter and assign font-size as 40 for the whole division

# add dcc.Graph() component to the second division
# update dcc.Graph component id as line-plot


### TASK 4 - ADD THE APPLICATION CALLBACK FUNCTION

# define the callback decorator
# define the callback function that uses the input provided to perform the computation
# create graph and return it as an output 
# run the application

#add callback decorator
@app.callback(Output(component_id='line-plot', component_property='figure'),Input(component_id='input-yr', component_property='value'))

# add computation to callback function and return graph
def get_graph(entered_year):
    # select data based on the entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # group the data by Month and compute average over arrival delay time
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    #
    fig = go.Figure(data = go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode = 'lines', marker = dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    return fig
# Run the app
if __name__ == '__main__':
    app.run_server()


### TASK 5 - UPDATE THE CALLBACK FUNCTION

# Update output component id parameter with the id provided in the dcc.Graph() component and component property as figure.
# Update input component id parameter with the id provided in the dcc.Input() component and component property as value.


### TASK 6 - RUN THE APPLICATION

