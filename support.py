from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
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
    "color": "red",                   # 글자색을 설정
    'font-weight':'bold',
    "overflow-y": "auto",  # 스크롤 기능 추가
}

print(SIDEBAR_STYLE['position'])
SIDEBAR_STYLE['top'] = '10px'

fs1 = 24;  fs2 = 20;  fs3 = 16
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

header = html.P("[Information : 입력값]", style={**style, **style_center, **{'color':'blue', 'font-size':f'{fs1}px'}})
Slab = html.Div([
    html.P('1. 슬래브', style={**style, **{'font-size':f'{fs2}px'}}),
    html.P('층고 [mm]', style={**style, **{'font-size':f'{fs3}px'}}),
    ])

form = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Email", html_for="example-email-grid"),
                dbc.Input(
                    type="number", value = 100,
                    id="example-email-grid",
                    placeholder="Enter email",
                    style={"width": "50%"},
                ),
            ],
            # width=6,
        ),
        dbc.Col(
            [
                dbc.Label("Password", html_for="example-password-grid"),
                dbc.Input(
                    type="number",
                    id="example-password-grid",
                    placeholder="Enter password",
                ),
            ],
            # width=6,
        ),
    ],
    className="g-3",
)

sidebar = dbc.Container(
    [
        header,
        Slab,
        form,
        dbc.InputGroup(
        [
            html.Div(
                [
                    html.Span("문자 입력 2", className="input-group-text")
                ], className="input-group-prepend"
            ),
            dbc.Input(id="text-input-1", type="text"),
        ], className="mb-3"
        ),
        dbc.InputGroup(
            [
                html.Span("문자 입력 2", className="input-group-text d-flex align-items-center"),
                dbc.Input(id="text-input-2", type="text"),
            ], className="mb-3"
        ),

        dbc.InputGroup(
            [
                html.Span("숫자 입력 1", className="input-group-text d-flex align-items-center"),
                dbc.Input(id="number-input-1", type="number"),
            ], className="mb-3"
        ),

        dcc.RadioItems(
            id='radio-items-2',
            options=[
                {'label': 'Option 3', 'value': 3},
                {'label': 'Option 4', 'value': 4}
            ],
            value=3,
            className="mb-3"
        ),
    ],
    # className="my-text",
    style=SIDEBAR_STYLE,
)

main_content = dbc.Container(id="main-content")

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar),
                dbc.Col(main_content),
            ], align="top"
        ),
    ], fluid=True
)

# @app.callback(
#     Output("main-content", "children"),
#     [
#         Input("text-input-1", "value"),
#         # Input("text-input-2", "value"),
#         # Input("number-input-1", "value"),
#         # Input("number-input-2", "value"),
#         # Input("radio-items-1", "value"),
#         # Input("radio-items-2", "value"),
#     ],
# )
# def update_main_content(ti1, ti2, ni1, ni2, ri1, ri2):
#     return html.Div([
#         html.H4("사용자 입력:"),
#     #     html.P(f"문자 입력 1: {ti1}"),
#     #     html.P(f"문자 입력 2: {ti2}"),
#     #     html.P(f"숫자 입력 1: {ni1}"),
#     #     html.P(f"숫자 입력 2: {ni2}"),
#     #     html.P(f"라디오 버튼 1: {ri1}"),
#     #     html.P(f"라디오 버튼 2: {ri2}"),
#     ])

if __name__ == '__main__':
    app.run_server(debug=True)
