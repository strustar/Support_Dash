from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

fs = [28, 24, 20, 16];  width_side = 500

style_sidebar = {
    "position": "fixed",                  # 요소의 위치를 상대적이 아닌 고정된 위치로 설정
    "top": "20px",                       # 상단에서의 위치를 100 픽셀로 설정
    "left": "10px",                       # 좌측에서의 위치를 10 픽셀로 설정
    "bottom": "10px",                      # 하단에서의 위치를 0 픽셀로 설정
    "width": f"{width_side}px",                     # 너비를 32rem으로 설정
    "padding": "10px",               #  padding, margin 속성은 top, right, bottom, left 값을 순서
    # "margin": "10px",                    # 바깥쪽 여백을 모든 방향에 100 픽셀로 설정
    "background-color": "#f8f9fa",        # 배경색을 설정
    "border": "2px solid #dee2e6",        # 2픽셀 두께의 실선 테두리 설정
    "border-radius": "0.25rem",           # 테두리 반경 (둥근 모서리)을 0.25rem으로 설정
    # "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",  # 박스 그림자 추가
    "font-family": "'Roboto', sans-serif",         # 글꼴 변경
    # "color": "red",                   # 글자색을 설정
    'font-weight':'bold',
    'font-size':f'{fs[3]}px',
    "overflow-y": "auto",  # 스크롤 기능 추가
}
style = {
    "color": 'black',
    'font-size':f'{fs[3]}px',
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
    "width": "100%",
    'font-weight': 'bold',
    'background-color': 'linen',
    'color': 'black',
    "border": "1px solid gray",
    'padding': '5px'
}

class In:
    pass
In.s_h = {'id':'s_h', 'v':2000}
In.s_t = {'id':'s_t', 'v':350}

def Sidebar():
    header = html.P("[Information : 입력값]", style={**style, **style_center, **{'color':'blue', 'font-size':f'{fs[1]}px'}})    
    Slab = html.Div([html.Span('< 슬래브 >', style={**style, **{'font-size':f'{fs[2]}px'}}),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label("층고 [mm]", html_for=In.s_h['id'], style={'margin-left':'0px'}),
                dbc.Input(type="number", value=In.s_h['v'], step=10, id=In.s_h['id'], style=style_number,), ],),
            dbc.Col([
                dbc.Label("두께 [mm]", html_for=In.s_t['id']),
                dbc.Input(type="number", value=In.s_t['v'], step=10, id=In.s_t['id'], style=style_number,), ],), # width=3),
        ], style={'margin-left': '10px', 'margin-right': '10px'}),
    ], style={"border": "2px solid gray",'padding': '5px'}, )

    sidebar = dbc.Container( [header, Slab, ], style=style_sidebar,)    
    return sidebar

# def Callback():
#     Sidebar()