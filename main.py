import pandas as pd
import plotly.graph_objects as go

DATASET_PATH = 'ObesityDataset.csv'
VISUALIZATION_PATH = 'visualization.html'
COLORS = {'Male': 'blue', 'Female': 'red'}

def ReadDataset(dataset_path:str):
    df = pd.read_csv(dataset_path)
    return df

def BarChart(df):
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(
        x=df['NObeyesdad'].value_counts().index,
        y=df['NObeyesdad'].value_counts().values,
        text=df['NObeyesdad'].value_counts().values,
        textposition='auto'
    ))
    bar_fig.update_layout(
        title_text='Count of individuals by weight status',
        xaxis_title='Weight Status',
        yaxis_title='Count'
    )
    return bar_fig

def ScatterPlot(df):
    scatter_fig = go.Figure()
    for gender in df['Gender'].unique():
        scatter_fig.add_trace(go.Scatter(
            x=df[df['Gender'] == gender]['Height'],
            y=df[df['Gender'] == gender]['Weight'],
            mode='markers',
            marker=dict(color=COLORS[gender]),
            name=gender,
            legendgroup=gender
        ))
    scatter_fig.update_layout(
        title_text='Height vs. Weight',
        xaxis_title='Height',
        yaxis_title='Weight',
        showlegend=True
    )
    return scatter_fig

def Histogram(df):
    hist_fig = go.Figure()
    hist_fig.add_trace(go.Histogram(
        x=df['Age'], nbinsx=20,
        text=df['Age'],
        marker_color='blue',
        opacity=0.7
    ))
    hist_fig.update_layout(
        title_text='Age Distribution',
        xaxis_title='Age',
        yaxis_title='Frequency'
    )
    hist_fig.update_traces(textposition='outside', textfont_size=10)
    return hist_fig

def PieChart(df):
    pie_fig = go.Figure()
    pie_fig.add_trace(go.Pie(
        labels=df['Gender'].unique(),
        values=df['Gender'].value_counts()
    ))
    pie_fig.update_layout(title_text='Gender Distribution')
    return pie_fig

def CreateHTML(html_path:str, graph_list):
    with open(html_path, 'w') as f:
        for graph in graph_list:
            f.write(graph.to_html(full_html=False, include_plotlyjs='cdn'))

if __name__ == '__main__':
    df = ReadDataset(DATASET_PATH)
    bar_chart = BarChart(df)
    scatter_plot = ScatterPlot(df)
    historgram = Histogram(df)
    pie_chart = PieChart(df)
    CreateHTML(VISUALIZATION_PATH, [bar_chart, scatter_plot, historgram, pie_chart])

