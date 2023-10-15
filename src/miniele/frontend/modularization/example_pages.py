import theme
import asyncio
from PIL import Image
from io import BytesIO
import base64
from threading import Thread
import random, requests, json, time
from nicegui import ui, events, Client
from leaflet import leaflet

locations = [{ "City": "San Francisco", "State": "California", "Country": "United States", "Location": { "Latitude": 37.7749, "Longitude": -122.4194 } }, 
{ "City": "Fresno", "State": "California", "Country": "United States", "Location": { "Latitude": 36.7481, "Longitude": -119.7631 } }, 
{ "City": "Las Vegas", "State": "Nevada", "Country": "United States", "Location": { "Latitude": 36.1749, "Longitude": -115.1451 } }, 
{ "City": "San Diego", "State": "California", "Country": "United States", "Location": { "Latitude": 32.7139, "Longitude": -117.1611 } }, 
{ "City": "Los Angeles", "State": "California", "Country": "United States", "Location": { "Latitude": 34.0522, "Longitude": -118.2437 } }, 
{ "City": "San Jose", "State": "California", "Country": "United States", "Location": { "Latitude": 37.3681, "Longitude": -121.8951 } }, 
{ "City": "Sacramento", "State": "California", "Country": "United States", "Location": { "Latitude": 38.5751, "Longitude": -121.4501 } }]

import os
os.environ["http_proxy"] = "http://172.22.3.247:33210"
os.environ["https_proxy"] = "http://172.22.3.247:33210"

locations = {(37.7749, -122.4194): 'San Francisco',
             (36.7481, -119.7631): 'Fresno',
             (36.1749, -115.1451): 'Las Vegas',
             (32.7139, -117.1611): 'San Diego', 
             (34.0522, -118.2437): 'Los Angeles',
             (37.3681, -121.8951): 'San Jose',
             (38.5751, -121.4501): 'Sacramento'}

def handle_img(last_img):
    url = "http://35.90.213.203:8899/worker_generate_stream"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": "请描述该图片",
        "image": last_img,
        "session": time.time()
    }
    try:
        response = requests.post(url = url, json = data, stream = True, timeout = 10, headers = headers)
        dic = json.loads(response.content)
        return dic
    except Exception as e:
        time.sleep(5)
        return {}


@ui.page("/travel")
async def travel_page(client: Client):
    map = leaflet().classes('w-full h-96')
    selection = ui.select(locations, on_change=lambda e: map.set_location(e.value)).classes('w-40')
    await client.connected()  # wait for websocket connection
    selection.set_value(next(iter(locations)))  # trigger map.set_location with first location in selection


from nicegui import ui,app
import pandas as pd
global choosed_file
import random



from datetime import datetime
from typing import List, Tuple
from uuid import uuid4

from nicegui import Client, ui

messages: List[Tuple[str, str, str, str]] = []


@ui.refreshable
async def chat_messages(own_id: str) -> None:
    for user_id, avatar, text, stamp in messages:
        ui.chat_message(text=text, stamp=stamp, avatar=avatar, sent=own_id == user_id)
    await ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)', respond=False)



async def chat(client: Client):
    def send() -> None:
        stamp = datetime.utcnow().strftime('%X')
        messages.append((user_id, avatar, text.value, stamp))
        text.value = ''
        chat_messages.refresh()

    user_id = str(uuid4())
    avatar = f'https://robohash.org/{user_id}?bgset=bg2'

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    ui.add_head_html(f'<style>{anchor_style}</style>')
    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            with ui.avatar().on('click', lambda: ui.open(chat)):
                ui.image(avatar)
            text = ui.input(placeholder='message').on('keydown.enter', send) \
                .props('rounded outlined input-class=mx-3').classes('flex-grow')
        ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io)') \
            .classes('text-xs self-end mr-8 m-[-1em] text-primary')

    await client.connected()  # chat_messages(...) uses run_javascript which is only possible after connecting
    with ui.column().classes('w-full max-w-2xl mx-auto items-stretch'):
        await chat_messages(user_id)



async def generate():
    time=random.randint(2,8)
    progress=ui.spinner(size='lg')
    await asyncio.sleep(time)
    progress.delete()
    ui.button('Continue',icon='stock')

    # ui.notify(f'finish generate')

async def async_task():
    label1=ui.label('Finical Analysis0').classes('text-h4 text-grey-8') 
    await generate()
    label1.delete()
    label2=ui.label('Finical').classes('text-h4 text-grey-8') 
from local_file_picker import local_file_picker

async def pick_file() -> None:
    result = await local_file_picker('~', multiple=True)
    ui.notify(f'You chose {result}')
    choosed_file = result

def update(*, df: pd.DataFrame, r: int, c: int, value):
    df.iat[r, c] = value

rqcode="""
import pandas as pd
import talib

# 读取数据
data = pd.read_csv('tmp_data.csv', index_col=0, parse_dates=True)
data.columns = ['Year', 'Automotive Revenues', 'Total Revenues', 'Automotive Gross Profit', 'Total Gross Profit', 'Automotive Gross Margin']

# 计算RSI
data['Automotive Revenues RSI'] = talib.RSI(data['Automotive Revenues'], timeperiod=14)[-1]
data['Total Revenues RSI'] = talib.RSI(data['Total Revenues'], timeperiod=14)[-1]
data['Automotive Gross Profit RSI'] = talib.RSI(data['Automotive Gross Profit'], timeperiod=14)[-1]
data['Total Gross Profit RSI'] = talib.RSI(data['Total Gross Profit'], timeperiod=14)[-1]
data['Automotive Gross Margin RSI'] = talib.RSI(data['Automotive Gross Margin'], timeperiod=14)[-1]

# 设置RSI阈值
HIGH_RSI = 85
LOW_RSI = 30

# 定义投资策略
def handle_bar(context, bar_dict):
    # 获取当前股票数据
    stock_data = data.loc[context.current_dt]

    # 计算RSI值
    automotive_revenues_rsi = stock_data['Automotive Revenues RSI']
    total_revenues_rsi = stock_data['Total Revenues RSI']
    automotive_gross_profit_rsi = stock_data['Automotive Gross Profit RSI']
    total_gross_profit_rsi = stock_data['Total Gross Profit RSI']
    automotive_gross_margin_rsi = stock_data['Automotive Gross Margin RSI']

    # 判断是否应该买入或卖出
    if automotive_revenues_rsi > HIGH_RSI:
        order_target_percent('TSLA', 0)
    elif automotive_revenues_rsi < LOW_RSI:
        order_target_percent('TSLA', context.portfolio.cash * 0.3)
"""


async def finical_runcode():
    await generate()
    
    
async def finical_process():
    await generate()
    ui.code(rqcode).classes('w-99')
    autobutton=ui.button('generate auto quantitative', on_click=finical_runcode, icon='stock')
    await generate()
    autobutton.delete()
   
    runcode=ui.button('run', on_click=finical_runcode, icon='stock')
    ui.button('Chat', on_click=chat, icon='stock')



async def finical() -> None:
    # ui.notify('finical process report with {choosed_file}'.format(choosed_file=choosed_file))
    ui.html("""
    <iframe src="https://tesla-cdn.thron.com/static/SVCPTV_2022_Q4_Quarterly_Update_6UDS97.pdf?xseo=&response-content-disposition=inline%3Bfilename%3D%22b7871185-dd6a-4d79-9c3b-19b497227f2a.pdf%22" width="1080px" height="1000px"></iframe>
    """
    )
    await generate()

    
    
#     ui.markdown(
#     """
# Here is a summary of the key information from the Tesla Q4 2022 and FY 2022 Update:

# **Highlights:**

# - Profitability: 16.8% operating margin in 2022; 16.0% in Q4
# - Financial Summary: $13.7B GAAP operating income in 2022; $3.9B in Q4; $12.6B GAAP net income in 2022; $3.7B in Q4
# - Cash: Operating cash flow of $14.7B; free cash flow of $7.6B in 2022
# - Operations: 6.5 GWh of energy storage deployed in 2022, up 64% YoY; record vehicle deliveries of 1.31 million in 2022
# - Key Metrics: ASPs have generally been on a downward trajectory for many years, but operating margin consistently improved from approximately negative 14% to positive 17% in the same period

# **Financial Summary:**

# - Automotive revenues: $71.5B in 2022, up 51% YoY
# - Total revenues: $81.5B in 2022, up 51% YoY
# - Total gross profit: $20.9B in 2022, up 53% YoY
# - Operating expenses: $7.2B in 2022, up 2% YoY
# - Income from operations: $13.7B in 2022, up 109% YoY
# - Operating margin: 16.8% in 2022, up 464 bp YoY
# - Adjusted EBITDA: $19.2B in 2022, up 65% YoY
# - Adjusted EBITDA margin: 23.6% in 2022, up 196 bp YoY
# - Net income attributable to common stockholders (GAAP): $12.6B in 2022, up 128% YoY
# - Net income attributable to common stockholders (non-GAAP): $14.1B in 2022, up 85% YoY
# - EPS attributable to common stockholders, diluted (GAAP): $3.62 in 2022, up 122% YoY
# - EPS attributable to common stockholders, diluted (non-GAAP): $4.07 in 2022, up 80% YoY
# - Net cash provided by operating activities: $14.7B in 2022, up 28% YoY
# - Capital expenditures: $7.2B in 2022, up 10% YoY
# - Free cash flow: $7.6B in 2022, up 51% YoY
# - Cash, cash equivalents, and investments: $22.2B at the end of 2022, up 25% YoY

# **Operational Summary:**

# - Model S/X production: 71,177 units in 2022, up 192% YoY
# - Model 3/Y production: 1,298,434 units in 2022, up 43% YoY
# - Total production: 1,369,611 units in 2022, up 47% YoY
# - Model S/X deliveries: 66,705 units in 2022, up 167% YoY
# - Model 3/Y deliveries: 1,247,146 units in 2022, up 37% YoY
# - Total deliveries: 1,313,851 units in 2022, up 40% YoY
# - Solar deployed: 348 MW in 2022, up 1% YoY
# - Storage deployed: 6,541 MWh in 2022, up 64% YoY
# - Store and service locations: 764 in 2022, up 19% YoY
# - Mobile service fleet: 1,584 in 2022, up 24% YoY
# - Supercharger stations: 4,678 in 2022, up 35% YoY
# - Supercharger connectors: 42,419 in 2022, up 35% YoY

# **Outlook:**

# - Tesla plans to grow production as quickly as possible in alignment with the 50% CAGR target they began guiding to in early 2021.
# - For 2023, they expect to remain ahead of the long-term 50% CAGR with around 1.8M cars for the year.
# - They have sufficient liquidity to fund their product roadmap, long-term capacity expansion plans, and other expenses.
# - They will manage the business such that they maintain a strong balance sheet during this uncertain period.
# - While they continue to execute on innovations to reduce the cost of manufacturing and operations, over time, they expect their hardware-related profits to be accompanied with an acceleration of software-related profits. They continue to believe that their operating margin will remain the highest among volume OEMs.
# - Cybertruck remains on track to begin production later this year at Gigafactory Texas.
# - Their next-generation vehicle platform is under development, with additional details to be shared at Investor Day (March 1st, 2023).
#     """
#     )
 

    data = {
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Automotive Revenues": [18515, 20821, 27236, 47231, 71462],
        "Automotive Gross Profit": [4341, 4423, 6977, 13839, 20354],
        "Automotive Gross Margin": [23.4, 21.2, 25.6, 29.3, 28.5],
        "Total Revenues": [21461, 24578, 31536, 53823, 81462],
        "Total Gross Profit": [4420, 4690, 6630, 13590, 20853],
        "Total GAAP Gross Margin": [18.8, 16.6, 21.0, 25.3, 25.6],
        "Operating Expenses": [4430, 4138, 4636, 7833, 7197],
        "(Loss) Income from Operations": [-388, -69, 1994, 6523, 13566],
        "Operating Margin": [-1.8, -0.3, 6.3, 12.1, 16.8],
        "Adjusted EBITDA": [2395, 2985, 5817, 11621, 19186],
        "Adjusted EBITDA Margin": [11.2, 12.1, 18.4, 21.6, 23.6],
        "Net (Loss) Income attributable to common stockholders (GAAP)": [-976, -862, 721, 5519, 12556],
        "Net (Loss) Income attributable to common stockholders (non-GAAP)": [-227, 36, 2455, 7640, 14116],
        "EPS attributable to common stockholders, diluted (GAAP)": [-0.38, -0.33, 0.21, 1.63, 3.62],
        "EPS attributable to common stockholders, diluted (non-GAAP)": [-0.09, 0.01, 0.75, 2.26, 4.07],
        "Net cash provided by operating activities": [2098, 2405, 5943, 11497, 14724],
        "Capital Expenditures": [-2101, -1327, -3157, -6482, -7158],
        "Free cash flow": [-3, 178, 2786, 5151, 7566],
        "Cash, cash equivalents and investments": [3686, 6268, 19384, 17707, 22185]
    }

    df = pd.DataFrame(data)
    await generate()



    with ui.grid(rows=len(df.index)+1).classes('grid-flow-col'):
        from pandas.api.types import is_bool_dtype, is_numeric_dtype
        for c, col in enumerate(df.columns):
            ui.label(col).classes('font-bold')
            for r, row in enumerate(df.loc[:, col]):
                if is_bool_dtype(df[col].dtype):
                    cls = ui.checkbox
                elif is_numeric_dtype(df[col].dtype):
                    cls = ui.number
                else:
                    cls = ui.input
                cls(value=row, on_change=lambda event, r=r, c=c: update(df=df, r=r, c=c, value=event.value))
    generate()

    
# try to summrary all person & company & entity relation to output mermaid from file
# here is mermaid format example: 
# ```mermaid
# graph LR
#     A[Square Rect] -- Link text --> B((Circle))
#     A --> C(Round Rect)
#     B --> D{Rhombus}
#     C --> D
# ```

    mermaid="""
    
    graph LR
        A(Tesla, Inc.) --> B(Elon Musk)
        A --> C(Gigafactory)
        A --> D(Vehicle Models)
        A --> E(Autopilot & FSD)
        A --> F(Energy Storage Deployments)
        A --> G(Solar Deployments)
        C --> H(California)
        C --> I(Shanghai)
        C --> J(Berlin-Brandenburg)
        C --> K(Texas)
        D --> L(Model S, Model X)
        D --> M(Model 3, Model Y)
        D --> N(Cybertruck, Tesla Semi, Roadster)
        E --> O(Advanced Driver-Assistance System)
        F --> P(Megapack Factory)
        G --> Q(Solar Energy Systems)
    
    """
    ui.mermaid(mermaid)
    await generate()


    # 数据
    x = data["Year"]
    y1 = data["Automotive Revenues"]
    y2 = data["Total Revenues"]
    y3 = data["Automotive Gross Profit"]
    y4 = data["Total Gross Profit"]
    y5 = data["Automotive Gross Margin"]

    # 归一化
    max_value = max(max(y1), max(y2), max(y3), max(y4), max(y5))
    y1_normalized = [y / max_value for y in y1]
    y2_normalized = [y / max_value for y in y2]
    y3_normalized = [y / max_value for y in y3]
    y4_normalized = [y / max_value for y in y4]
    y5_normalized = [y / max_value for y in y5]

    # 创建图表
    import plotly.graph_objects as go

    fig = go.Figure()

    # 添加折线
    fig.add_trace(go.Scatter(x=x, y=y1_normalized, name="Automotive Revenues"))
    fig.add_trace(go.Scatter(x=x, y=y2_normalized, name="Total Revenues"))
    fig.add_trace(go.Scatter(x=x, y=y3_normalized, name="Automotive Gross Profit"))
    fig.add_trace(go.Scatter(x=x, y=y4_normalized, name="Total Gross Profit"))
    fig.add_trace(go.Scatter(x=x, y=y5_normalized, name="Automotive Gross Margin"))

    # 更新布局
    fig.update_layout(
        title="Normalized Tesla's Automotive and Total Revenues and Gross Profits",
        xaxis_title="Year",
        yaxis_title="Normalized Amount",
        legend=dict(orientation="h", x=0, y=1.02, xanchor="left", yanchor="top"),
    )
    await generate()
    # 显示图表
    ui.plotly(fig).classes('w-99 h-99')
    autobutton=ui.button('generate auto quantitative', on_click=finical_process, icon='stock')
    await generate()
   


async def auto() -> None:
    ui.notify(f'automatic front-end generate')
    await generate()
    ui.html("""<iframe src="//player.bilibili.com/player.html?aid=962074250&bvid=BV1uH4y1R7Ec&cid=1298183764&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>""")
    # app.add_static_files('/stl',"static")

    # with ui.scene(width=1024, height=800) as scene:
    #     scene.spot_light(distance=100, intensity=0.1).move(-10, 0, 10)
    #     scene.stl('/Users/tanwenxuan/workspace/minielements/miniele/src/miniele/frontend/modularization/static/pikachu.stl').move(x=-0.5).scale(0.06)






async def async_upload(e: events.UploadEventArguments):
    img_content = e.content.read()
    image = Image.open(BytesIO(img_content)).convert('RGB')
    last_img = str(time.time()) + ".jpg"
    image.save(last_img)
    t = Thread(target = handle_img,  args = (last_img, ))
    t.setDaemon(True)
    t.start()

    sleep_time = random.choice([10, 15, 20, 30])
    time.sleep(sleep_time)
    await asyncio.sleep(sleep_time)
    ui.link('travel', travel_page, new_tab = True).classes(replace='text-pink').set_text('travel')

def create() -> None:

    @ui.page('/a')
    async def example_page_a(client:Client):
        with theme.frame('MultiModal Parse'):
            upload = ui.upload(on_upload = async_upload).props('accept=.jpg').classes('max-w-full')

    @ui.page('/b')
    def example_page_b():
        with theme.frame('Finical'):
            ui.label('Finical Analysis').classes('text-h4 md:p-8 text-grey-8') 
            ui.button('Choose file', on_click=pick_file, icon='folder')
            ui.button('Parse file', on_click=finical, icon='stock')


    @ui.page('/d')
    def example_page_b():
        with theme.frame('Front-end'):
            ui.label('Front-end Automatic Generator').classes('text-h4 md:p-8 text-grey-8')
            ui.button('Choose file', on_click=pick_file, icon='folder')
            ui.button('Chat', on_click=chat, icon='stock')
            ui.button('automatic generate', on_click=auto, icon='history')
