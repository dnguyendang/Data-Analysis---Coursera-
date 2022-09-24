
### TASK 1: DATA PREPARATION 

# Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')


### TASK 2: CREATE DASH APPLICATION AND GET THE LAYOUT SKELETON

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),
                                               
                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()


### TASK 3: ADD THE APPLICATION TITLE 

#Application title is Airline Dashboard
#Use style parameter provided below to make the title center aligned, with color code #503D36, and font-size as 40


### TASK 4: ADD THE APPLICATION DESCRIPTION

#Description is Proportion of distance group (250 mile distance interval group) by flights.
#Use style parameter to make the description center aligned and with color #F57241.

### TASK 5: UPDATE THE GRAPH
