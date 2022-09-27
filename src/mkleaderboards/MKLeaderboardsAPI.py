import json

import requests
from bs4 import BeautifulSoup

MKLEADERBOARDS_API_URL = "https://www.mkleaderboards.com/api"
MKLEADERBOARDS_URL = "https://www.mkleaderboards.com"

mapping = dict(
    lc=49,
    mmm=50,
    mg=51,
    tf=52,
    mc=53,
    cm=54,
    dks=55,
    dksc=55,
    wgm=56,
    dc=57,
    kc=58,
    mt=59,
    gv=60,
    ddr=61,
    mh=62,
    bc=63,
    rr=64,
    rpb=65,
    ryf=66,
    rgv2=67,
    rmr=68,
    rsl=69,
    rsgb=70,
    rds=71,
    rws=72,
    rdh=73,
    rbc3=74,
    rdkjp=75,
    rmc=76,
    rmc3=77,
    rpg=78,
    rdkm=79,
    rbc64=80,
    rbc=80
)


def get_course(track_abbrev: str, location: str = 'mkw_nonsc_spain'):
    url = f"{MKLEADERBOARDS_API_URL}/charts/{location}/{mapping.get(track_abbrev)}"
    return __request_json(url)


def get_ranking(location: str = 'spain'):
    url = f"{MKLEADERBOARDS_URL}/mkw/charts/{location}/nonsc/stats"
    content = requests.get(url).content
    parsed_html = BeautifulSoup(content, 'html.parser')
    first_table = parsed_html.find_all("table")[0]
    counter = 0
    current_row = dict()
    rows = list()
    for cell in first_table.find_all('td')[4:]:
        counter = counter + 1
        if counter == 1:
            current_row.update(position=cell.text)
        if counter == 3:
            current_row.update(player=cell.text)
        if counter == 4:
            current_row.update(points=cell.text)
        if counter % 4 != 0:
            continue
        rows.append(current_row)
        current_row = dict()
        counter = 0
    return rows


def __request_json(url):
    response_content = requests.get(url).content
    content_json = json.loads(response_content)
    return content_json
