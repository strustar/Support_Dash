from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import json
import pandas as pd
from side import Sidebar, fs, In

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# s_h = ['s_h', 2000];  s_t = ['s_t', 350]


main_content = dbc.Container(id="main-content")
app.layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col(Sidebar()),
            dbc.Col(main_content),
        ], align="top", ), 
    ],),
], fluid=True, )


@app.callback(
    Output("main-content", "children"),
    [Input(In.s_h[0], "value"), Input(In.s_t[0], "value")],
)
def update_output(h, t):
    In.s_h[1] = h
    In.s_t[1] = t
    print(In.s_h, In.s_t)
    # data = {In.s_h[0]:h, In.s_t[0]:t}    
    # with open("In.json", "w") as f:
    #     json.dump(data, f)
    # return html.Div([]) #, print(height, thickness)


# # JSON 파일 읽기
# with open("data.json", "r") as f:
#     s = json.load(f)

# def flexible_function(a, b, *args, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("args:", args[0])
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# flexible_function(111, 2, s_h, 4, 5, s_t, y=20)

# print(fs)

if __name__ == '__main__':
    app.run_server(debug=True)

