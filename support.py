from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
fs1 = 24;  fs2 = 20;  fs3 = 16

SIDEBAR_STYLE = {
    "position": "fixed",                  # 요소의 위치를 상대적이 아닌 고정된 위치로 설정
    "top": "10px",                       # 상단에서의 위치를 100 픽셀로 설정
    "left": "10px",                       # 좌측에서의 위치를 10 픽셀로 설정
    "bottom": "10px",                      # 하단에서의 위치를 0 픽셀로 설정
    "width": "500px",                     # 너비를 32rem으로 설정
    "padding": "10px",               #  padding, margin 속성은 top, right, bottom, left 값을 순서
    # "margin": "10px",                    # 바깥쪽 여백을 모든 방향에 100 픽셀로 설정
    "background-color": "#f8f9fa",        # 배경색을 설정
    "border": "2px solid #dee2e6",        # 2픽셀 두께의 실선 테두리 설정
    "border-radius": "0.25rem",           # 테두리 반경 (둥근 모서리)을 0.25rem으로 설정
    # "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # 박스 그림자 추가
    "font-family": "'Roboto', sans-serif",         # 글꼴 변경
    # "color": "red",                   # 글자색을 설정
    'font-weight':'bold',
    'font-size':f'{fs3}px',
    "overflow-y": "auto",  # 스크롤 기능 추가
}

print(SIDEBAR_STYLE['position'])
SIDEBAR_STYLE['top'] = '10px'

style = {
    "color": 'black',
    'font-size':f'{fs3}px',
    "font-weight": "bold",
    'margin-top':'0px',
    'padding-left':'0px',
}
style_center = {
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "width": "100%",
}
style_number = {
    "width": "50%",
    'font-weight': 'bold',
    'background-color': 'linen',
    'color': 'black',
    "border": "1px solid gray",
    'padding': '5px'
}

header = html.P("[Information : 입력값]", style={**style, **style_center, **{'color':'blue', 'font-size':f'{fs1}px'}})
s_h = ['s_h', 2000]
s_t = ['s_t', 350]
Slab = html.Div([
    html.P('1. 슬래브', style={**style, **{'font-size':f'{fs2}px'}}),
    dbc.Row([
        dbc.Col([
            dbc.Label("층고 [mm]", html_for=s_h[0], style={'margin-left':'0px'}),
            dbc.Input(
                type="number", value=s_h[1], step=10,
                id=s_h[0],
                # placeholder="Enter number",
                style=style_number,
            ),
        ],),
        dbc.Col([
            dbc.Label("두께 [mm]", html_for=s_t[0]),
            dbc.Input(
                type="number", value=s_t[1], step=10,
                id=s_t[0],
                style=style_number,
            ),
        ],),
    ], style={'margin-left': '10px', 'margin-right': '10px'}),
], style={"border": "2px solid gray",'padding': '5px'},    
)

stored_values = html.Div(
    [
        html.Div(id="hidden_s_h", children=""),
        html.Div(id="hidden_s_t", children="")
    ],
    style={"display": "none"}
)

sidebar = dbc.Container( [header, Slab, ], style=SIDEBAR_STYLE,)


main_content = dbc.Container(id="main-content")


app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(sidebar),
                        dbc.Col(main_content),
                    ], align="top"
                ),
                dbc.Row(  # 새로운 행을 추가하여 변경 값 출력
                    [
                        html.Label("s_h 값: "),
                        html.Span(id="output-s_h-value"),
                        html.Label(" s_t 값: "),
                        html.Span(id="output-s_t-value")
                    ],
                    style={'margin-left': '700px', 'font-size': '20px'}
                )
            ], fluid=True
        ),
        stored_values
    ]
)

@app.callback(
    [Output("hidden_s_h", "children"),
    Output("hidden_s_t", "children")],
    [Input(s_h[0], "value"),
    Input(s_t[0], "value")]
)
def update_input_values(s_h_value, s_t_value):
    # print(f's_h_value: {s_h_value}')  # 콘솔에 입력 값 출력
    # print(f's_t_value: {s_t_value}')  # 콘솔에 입력 값 출력
    return s_h_value, s_t_value

s = update_input_values
print(s)

if __name__ == '__main__':
    app.run_server(debug=True)