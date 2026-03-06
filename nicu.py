from seleniumbase import SB
import random
import base64
import requests
geo_data = requests.get("http://ip-api.com/json/").json()
proxy_str = False
urlt = f"https://www.twitch.tv/brutalles"
while True:
    with SB(uc=True, locale="en",ad_block=True,chromium_arg='--disable-webgl',proxy = proxy_str) as attww:
        rnd = random.randint(450,800)
        
        attww.activate_cdp_mode(urlt,tzone=f"{geo_data["timezone"]}",geoloc=(geo_data["lat"], geo_data["lon"]))
        attww.sleep(2)
        if attww.is_element_present('button:contains("Accept")'):
            attww.cdp.click('button:contains("Accept")', timeout=4)
        attww.sleep(2)    
        attww.sleep(12)
        if attww.is_element_present('button:contains("Start Watching")'):
            attww.cdp.click('button:contains("Start Watching")', timeout=4)
            attww.sleep(10)
        if attww.is_element_present('button:contains("Accept")'):
            attww.cdp.click('button:contains("Accept")', timeout=4)
        if attww.is_element_present("#live-channel-stream-information"):
        
            if attww.is_element_present('button:contains("Accept")'):
                attww.cdp.click('button:contains("Accept")', timeout=4)
            if True:
                attww2 = attww.get_new_driver(undetectable=True)
                attww2.activate_cdp_mode(urlt,tzone=f"{geo_data["timezone"]}",geoloc=(geo_data["lat"], geo_data["lon"]))
                attww2.sleep(10)
                if attww2.is_element_present('button:contains("Start Watching")'):
                    attww2.cdp.click('button:contains("Start Watching")', timeout=4)
                    attww2.sleep(10)
                if attww2.is_element_present('button:contains("Accept")'):
                    attww2.cdp.click('button:contains("Accept")', timeout=4)
                attww.sleep(10)
                attww.sleep(rnd)

        else:
            break

