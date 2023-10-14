from typing import Tuple

from nicegui import ui
import time
import asyncio
import datetime
import random

loca_dict = {}
loca_dict["San Francisco"] = {
  "City": "旧金山",
  "State": "加利福尼亚州",
  "Country": "美国",
  "Location": {
    "Latitude": 37.7749, 
    "Longitude": -122.4194
  },
  "PopularTouristSpots": [
    "1. 金门大桥: 连接旧金山和马林县的标志性吊桥,拥有绝佳的照相景点和视野。",
    "2. 渔人码头: 热闹的滨水区域,有海鲜餐厅、商店、街头艺人和 Alca 岛的景观。",  
    "3. 阿尔卡特拉斯岛: 以其过去的臭名昭著的监狱而闻名,如今成为博物馆,可游览其历史并欣赏城市美景。",
    "4. 39号码头: 流行的码头,有商店、餐厅、海狮群落和各种娱乐活动。",
    "5. 缆车: 标志性的有轨电车,爬上旧金山陡峭的山坡,乘车可欣赏城市美景。"
  ],
  "PopularRestaurants": [
    "1. Benu: 3星米其林餐厅,以创新品鉴菜单而著称,主厨为Corey Lee。",
    "2. State Bird Provisions: 获奖餐厅,提供独特的点心式用餐体验。",
    "3. Swan Oyster Depot: 长期经营的海鲜店和咖啡馆,提供新鲜牡蛎、蟹肉、蛤蜊浓汤等。",
    "4. Tartine Manufactory: 以烘焙食品如乡村面包而著称,也提供早餐、午餐和晚餐。", 
    "5. Liholiho Yacht Club: 热闹欢乐的夏威夷风格小吃和鸡尾酒餐厅。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "旧金山国际机场(SFO)位于旧金山市中心以南13英里处。",
    "PublicTransit": "BART、有轨电车、公交和标志性的缆车组成了旧金山的公共交通网络。",
    "Highways": "主要高速公路包括101号美国国道和280号州际公路,连接半岛和南湾区域,以及连接东湾的80号州际公路。"
  }
}


loca_dict["Fresno"] = {
  "City": "弗雷斯诺",
  "State": "加利福尼亚州",
  "Country": "美国",
  "Location": {
    "Latitude": 36.7468,
    "Longitude": -119.7726
  },
  "PopularTouristSpots": [
    "1. 弗雷斯诺查菲动物园: 一个大型动物园,拥有各种珍稀和濒危物种。",
    "2. 旧金山和圣华金谷铁路: 一条保存完好的老式火车和车站,进行历史火车游。",
    "3. 福雷斯特艾尔国家森林: 自然风景区,适合徒步游览、露营和骑马。",
    "4. 威尔逊剧院: 一座历史悠久的剧院,定期上演各类表演。",
    "5. 米歇尔堡: 一座历史悠久的墨西哥式建筑,现为博物馆。"
  ],
  "PopularRestaurants": [
    "1. La Elegante: 一家知名的墨西哥餐厅,以牛肉玉米卷闻名。", 
    "2. Irene's Cafe: 供应美味的家常菜式和甜点的小餐馆。",
    "3. Pismo's Coastal Grill: 一家海鲜餐厅,提供新鲜的当地海鲜。",
    "4. Chicken Pie Shop: 供应传统鸡肉派的老餐馆。",
    "5. Pho Nouveau: 一家越南餐厅,以河粉和春卷著称。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "弗雷斯诺机场(FAT)位于市中心以北约6英里处。",
    "PublicTransit": "弗雷斯诺地区运输局运营公交系统覆盖弗雷斯诺都市区。",
    "Highways": "加州99号州际公路穿过弗雷斯诺,连接北部和南部城市。"
  }  
}

loca_dict["Las Vegas"] = {
  "City": "拉斯维加斯", 
  "State": "内华达州",
  "Country": "美国",
  "Location": {
    "Latitude": 36.1699,
    "Longitude": -115.1398
  },
  "PopularTouristSpots": [
    "1. 永利拉斯维加斯: 一座著名的酒店和赌场,以其精美喷泉而闻名。",
    "2. 百乐宫: 一个大型娱乐场所,提供各种表演、餐厅和夜总会。",
    "3. 弗里蒙特街: 一个著名的赌城大道,两旁布满主题酒店和赌场。",
    "4. 红石峡谷: 一个壮丽的自然景观,适合徒步和攀岩活动。",
    "5. 胡佛水坝: 一个巨大的水坝,可在此进行观光游览。"
  ],
  "PopularRestaurants": [
    "1. 奥古斯都牧场餐厅: 米其林三星法式餐厅,由知名大厨古斯塔夫·马约服务。",
    "2. 乔尔斯: 知名的高档海鲜和牛排餐厅。",
    "3. 火锅城: 供应正宗中餐火锅的著名餐厅。", 
    "4. 好世界村自助餐: 一个大型的国际自助餐厅,提供各国美食。",
    "5. 赌城小馆: 供应地道粤菜的餐厅,深受华人游客欢迎。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "麦卡伦国际机场(LAS)位于拉斯维加斯市中心以南2英里处。",
    "PublicTransit": "RTC公交系统和摩纳铁路提供拉斯维加斯市区公共交通服务。",
    "Highways": "15号州际公路是通往拉斯维加斯的主要高速公路。"
  }
}

loca_dict["San Diego"] = {
  "City": "圣迭戈",
  "State": "加利福尼亚州",
  "Country": "美国",  
  "Location": {
    "Latitude": 32.7157, 
    "Longitude": -117.1611
  },
  "PopularTouristSpots": [
    "1. 圣迭戈动物园:世界知名的动物园,园内有大熊猫等许多珍稀动物。", 
    "2. 巴尔博亚公园:市区中心的大型城市公园,有博物馆、花园和迷你小火车。",
    "3. 加斯灯区:著名的历史街区,维多利亚式和殖民复兴式建筑林立。",
    "4. 科罗纳多海滩:金色沙滩和蔚蓝海水的海滨度假胜地。",
    "5. 旧城:墨西哥风情的历史街区,以西班牙式建筑见长。"
  ],
  "PopularRestaurants": [
    "1. Addison:米其林三星餐厅,由知名大厨William Bradley掌舵。",
    "2. Ironside Fish & Oyster:供应新鲜海鲜和牡蛎的餐厅。",
    "3. City Tacos:墨西哥风味的餐厅,以牛肉卷饼和鳄梨酱闻名。",
    "4. Buona Forchetta:供应手工意大利面食和比萨的餐厅。",
    "5. The Prado:位于巴尔博亚公园内的高档餐厅,环境优雅。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "圣迭戈国际机场(SAN)位于市中心以西3英里处。",
    "PublicTransit": "圣迭戈有轨电车和MTS公交系统组成公共交通网络。",  
    "Highways": "5号州际公路沿海岸线贯穿圣迭戈。"
  }
}

loca_dict["Los Angeles"] = {
  "City": "洛杉矶",
  "State": "加利福尼亚州",
  "Country": "美国",
  "Location": {
    "Latitude": 34.0522,
    "Longitude": -118.2437
  },
  "PopularTouristSpots": [
    "1. 好莱坞环球影城:世界知名的电影主题乐园。",
    "2. 洛杉矶县美术馆:收藏众多艺术精品的世界级艺术博物馆。", 
    "3. 格里菲斯天文台:可以眺望洛杉矶全景的著名观景点。",
    "4. 世纪城:充满未来主义建筑风格的高档购物中心。",
    "5. 马尔比海滩:阳光明媚的海滨度假胜地。"
  ],
  "PopularRestaurants": [
    "1. 朱苏:米其林三星餐厅,由大厨乔瑟·安达鲁斯掌舵。",
    "2. 瑞士小馆:洛杉矶最负盛名的汉堡包餐厅。",
    "3. 菲利普堡:供应法式早午餐的知名餐厅。",
    "4. 阳光沙龙:热门的墨西哥菜餐厅。",
    "5. 大隆面家:在洛杉矶很有人气的台湾小吃店。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "洛杉矶国际机场(LAX)位于洛杉矶西南部。",
    "PublicTransit": "洛杉矶都会运输局运营轻轨、公交和地铁组成公共交通网络。",
    "Highways": "5号、10号和405号州际公路都是该市的主要高速公路。"
  }
}

loca_dict["San Jose"] = {
  "City": "圣何塞", 
  "State": "加利福尼亚州",
  "Country": "美国",
  "Location": {
    "Latitude": 37.3382,
    "Longitude": -121.8863
  },
  "PopularTouristSpots": [
    "1. 西蒙技术博物馆: 一个互动科技博物馆,展示硅谷的创新历史。",
    "2. 圣何塞历史公园: 历史悠久的城市公园,展示早期加州历史。",
    "3. 玫瑰园: 一个巨大的玫瑰园,拥有超过 4000 种不同品种的玫瑰。",
    "4. 圣何塞市政厅: 一座新古典主义风格的历史建筑,其圆顶很有特色。",
    "5. 日本友好花园: 一个日式园林,具有代表日本文化的景点。"
  ],
  "PopularRestaurants": [
    "1. 田园: 米其林星级餐厅,供应创新加州料理。",
    "2. 厨神气韵: 知名的越南菜餐厅。",
    "3. 原汁原味: 供应地道墨西哥菜肴的餐厅。",
    "4. 胡椒之家: 一个家庭经营的越南菜馆。",
    "5. 圣佩德罗广场: 市中心的西班牙式广场,周围环绕各种餐厅。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "圣何塞国际机场(SJC)位于市中心以西4英里处。",
    "PublicTransit": "VTA轻轨和公交系统覆盖圣何塞都市区。",
    "Highways": "280号、680号、101号和880号州际公路经过圣何塞。"
  }
}

loca_dict["Sacramento"] = {
  "City": "萨克拉门托",
  "State": "加利福尼亚州",
  "Country": "美国",
  "Location": {
    "Latitude": 38.5816,
    "Longitude": -121.4944 
  },
  "PopularTouristSpots": [
    "1. 加州州议会大厦: 加州州政府所在地,进行免费导游游览。",
    "2. 老城: 历史悠久的街区,有各种博物馆、画廊和餐馆。",
    "3. 萨克拉门托历史火车博物馆: 展示19世纪火车和铁路设备。",  
    "4. 斯特拉塔塔中心: 一个多功能的表演艺术场馆。",
    "5. 萨克拉门托河河畔公园: 河边的绿地公园,适合野餐散步。"
  ],
  "PopularRestaurants": [
    "1. The Kitchen: 提供创新美式菜肴,深受食客喜爱。",
    "2. Mulvaney's B&L: 米其林星级餐厅,主打现代创意料理。",
    "3. Centro Cocina Mexicana: 供应正宗墨西哥菜的餐厅。",
    "4. Mikuni Sushi: 日本料理,以刺身和卷饼见长。", 
    "5. Tower Cafe: 一个早午餐餐厅,提供美味的家常菜式。"
  ],
  "MajorTransportationRoutes": {
    "Airport": "萨克拉门托国际机场(SMF)位于市中心以西10英里处。",
    "PublicTransit": "轻轨和SacRT公交系统覆盖市区。",
    "Highways": "5号、50号和80号州际公路通过萨克拉门托。"
  }
}

images_dic = {
    "San Francisco" : "https://upload.wikimedia.org/wikipedia/commons/6/61/San_Francisco_from_the_Marin_Headlands_in_August_2022.jpg",
    "Fresno": "http://res.cloudinary.com/simpleview/image/upload/v1557431686/clients/fresnoca/PF_Downtown_Fresno_Skyline_04_dfd24056-3371-41ca-a250-1d330e191223.jpg",
    "Las Vegas": "https://vegasexperience.com/wp-content/uploads/2023/01/Photo-of-Las-Vegas-Downtown-1920x1280.jpg",
    "San Diego": "https://www.tripsavvy.com/thmb/XIx0gfr_i-ay7XLKJRXakT6FS2M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/sunset-at-la-jolla-cove-1278353139-583584d99afb438a9889e8d381b836ed.jpg",
    "Los Angeles":"https://upload.wikimedia.org/wikipedia/commons/3/32/20190616154621%21Echo_Park_Lake_with_Downtown_Los_Angeles_Skyline.jpg",
    "San Jose": "https://upload.wikimedia.org/wikipedia/commons/3/32/20190616154621%21Echo_Park_Lake_with_Downtown_Los_Angeles_Skyline.jpg",
    "Sacramento": "https://cdn.britannica.com/32/145032-050-C0C04D18/Sacramento-River-California.jpg"
}

locations = {(37.7749, -122.4194): 'San Francisco', 
             (36.7481, -119.7631): 'Fresno', 
             (36.1749, -115.1451): 'Las Vegas', 
             (32.7139, -117.1611): 'San Diego', 
             (34.0522, -118.2437): 'Los Angeles', 
             (37.3681, -121.8951): 'San Jose', 
             (38.5751, -121.4501): 'Sacramento'}
    
class leaflet(ui.element, component='leaflet.js'):

    def __init__(self) -> None:
        super().__init__()
        ui.add_head_html('<link href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" rel="stylesheet"/>')
        ui.add_head_html('<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"></script>')
        self.last_img = None
        self.last_json = None
        self.last_card = None
        self.timeline = None

    async def set_location(self, location: Tuple[float, float]) -> None:
        city = locations.get(location)
        self.run_method('set_location', location[0], location[1])        
        detail = loca_dict.get(city)
        await asyncio.sleep(20)

        if self.last_img is not None:
            self.last_img.delete()
        if self.last_json is not None:
            self.last_json.delete()
        if self.last_card is not None:
            self.last_card.delete()
        if self.timeline is not None:
            self.timeline.delete()

        with ui.timeline(side='right') as timeline:
          self.timeline = timeline
          sights = detail.get("PopularTouristSpots")
          add_hours = random.choice([0, 24, 48, 72])
          cur = datetime.datetime.now() 
          ix = 0
          for sight in sights:
            addr_half = sight.split(":")[0]
            describe = sight.split(":")[1]
            addr = addr_half.split(" ")[-1]
            add_hours = random.choice([0, 24, 48, 72])
            if ix != 0:
              cur = cur + datetime.timedelta(hours = add_hours)
            ymd = cur.strftime('%Y-%m-%d')
            if ix == 0:
              ui.timeline_entry(describe,
                                title = addr,
                                subtitle = ymd,
                                icon = "rocket")
            else:
              ui.timeline_entry(describe,
                                title = addr,
                                subtitle = ymd)
              ix += 1
        with ui.card().tight().classes("md:flex bg-slate-100 rounded-xl p-8 md:p-0 dark:bg-slate-800") as card:
          self.last_card = card
          self.last_img = ui.image(images_dic.get(city)).classes("w-384 h-512 md:w-128 md:h-auto md:rounded-none rounded-full mx-auto")    
          with ui.card_section().classes("pt-4 md:p-6 text-center md:text-left space-y-4"):
            label_str = ""
            label_str += detail.get("City") + "\n"
            label_str += "景点:" + "\n" +"\n".join(detail.get("PopularTouristSpots"))
            label_str += "饮食：" + "\n" + "\n".join(detail.get("PopularRestaurants"))
            traffic = detail.get("MajorTransportationRoutes")
            label_str += "交通:" + "\n"
            label_str += "机场:" + traffic.get("Airport") + "\n"
            label_str += "公共交通:" + traffic.get("PublicTransit") + "\n"
            label_str += "高速" + traffic.get("Airport")
            # print(label_str)
            self.last_json =  ui.label(label_str).classes("text-lg font-light")