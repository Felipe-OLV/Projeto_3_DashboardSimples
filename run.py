from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('evolucao_do_salario_minimo.xls')
fig = px.line(df, x="Inicio_vigente", y="valor_salario")

app.layout = html.Div(children=[
    html.H1(children='Gráfico da evolução do salário mínimo brasileiro.'),

    html.Div(children='''
        Gráfico simples representando a evolução do salário mínimo.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)