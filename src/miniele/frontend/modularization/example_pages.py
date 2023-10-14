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


async def async_task():
    ui.label('Finical Analysis0').classes('text-h4 text-grey-8') 
    await asyncio.sleep(1)
    ui.label('Finical').classes('text-h4 text-grey-8') 

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
        with theme.frame('Finical Analysis'):
            ui.label('Finical Analysis').classes('text-h4 text-grey-8') 

    @ui.page('/d')
    def example_page_b():
        with theme.frame('Auto'):
            ui.label('Auto').classes('text-h4 text-grey-8')
