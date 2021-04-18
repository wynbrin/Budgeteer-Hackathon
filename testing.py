
from main import budgetGrouping
import plotly.express as px
budge = budgetGrouping()
grouped = budge.reformat()

print(grouped)
#plotf = px.data.stocks()
# Plot Expenses
fig = px.line(grouped, x='Date', y='Expenses($)')
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
fig.show()
# Using input expense sheet(above) and input income sheet, use same method 
# to plot a new df in which each day is a continous sum