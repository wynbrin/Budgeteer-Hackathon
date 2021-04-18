
from main import budgetGrouping
import plotly.express as px


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


budge = budgetGrouping()
grouped = budge.reformat()




print(grouped)
#plotf = px.data.stocks()
# Plot Expenses

all_dims = ['Date', 'Income', 'Expenses($)']
app = dash.Dash(__name__)

app.layout =  html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} 
                 for x in all_dims],
        value=all_dims,
        multi=True
    ),
    dcc.Graph(id="splom"),
])

@app.callback(Output("splom", "figure"), [Input("dropdown", "value")])

def update_chart(dims):
    fig = px.line(grouped, x = dims[0], y = dims[1:])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    return fig

app.run_server(debug=True)
# Using input expense sheet(above) and input income sheet, use same method 
# to plot a new df in which each day is a continous sum