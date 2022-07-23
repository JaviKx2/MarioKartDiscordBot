import requests
import json

mapping = dict(
    lc=49,
    mg=50,
    mmm=51,
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
    rbc64=80
)


def get_course(track_name):
    track_json = requests.get(
        f"https://www.mkleaderboards.com/api/charts/mkw_nonsc_spain/{mapping.get(track_name)}").content
    track = json.loads(track_json)
    return track
