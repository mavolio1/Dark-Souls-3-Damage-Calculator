import requests
import json
from bs4 import BeautifulSoup
from utils import Weapon
from tqdm import tqdm
from config import cfg

def main():
    weapons_list = []

    print('+------------------------------------------------------+')
    print('|                DARK SOUL 3 CALCULATOR                |')
    print('+------------------------------------------------------+')

    # main utilities
    weapons_list = load_weapon_data()
    json_to_persistent(weapons_list)

    # test
    #weapons_list = load_from_json()
    #print(weapons_list[0])


def load_weapon_data():
    # parse html and extract weapon hrefs
    request = requests.get(cfg.root_url + '/Weapons')
    html = request.content
    soup = BeautifulSoup(html, 'html.parser')
    weapons_divs = soup.find_all('div', class_='col-xs-6 col-sm-2')

    # populate the list with all weapons urls
    weapons_url_list = []
    for div in weapons_divs:
        weapons_url_list.append(cfg.root_url + div.find('a')['href'])

    # loop through all weapon urls and retrieve infos
    weapons_list = []
    for url in tqdm(weapons_url_list):
        request = requests.get(url)
        html = request.content
        soup = BeautifulSoup(html, 'html.parser')
        infobox = soup.find('div', class_='infobox')
        wep = Weapon(url.replace(cfg.root_url, '').replace('/', '').replace('+', ' '),
                      'tmp', 'tmp', 0, 0, 0, 0, 0, '-', '-', '-', '-')
        
        trs = infobox.find_all('tr')
        for tr in trs:
            if tr.find('img'):
                img = tr.find('img')
                if img.get('title'):
                    title = img.get('title')
                    if title == 'Physical Attack':
                        if img.find_next().text != '-':
                            wep.phys_atk = int(img.find_next().text)
                    elif title == 'Magical Attack':
                        if img.find_next().text != '-':
                            wep.magic_atk = int(img.find_next().text)
                    elif title == 'Fire Attack':
                        if img.find_next().text != '-':
                            wep.fire_atk = int(img.find_next().text)
                    elif title == 'Lightning Attack':
                        if img.find_next().text != '-':
                            wep.lightning_atk = int(img.find_next().text)
                    elif title == 'Dark Attack':
                        if img.find_next().text != '-':
                            wep.dark_atk = int(img.find_next().text)
                    elif title == 'Weapon Type':
                        wep.weapon_type = img.find_next().text

        weapons_list.append(wep)

    return weapons_list

def json_to_persistent(weapons_list):
    json_list = []

    for wep in weapons_list:
        json_list.append(json.dumps(wep.__dict__))
    
    with open(cfg.persistent_folder + 'weapons.json', 'w') as f:
        json.dump(json_list, f)

def load_from_json():
    weapons_list = []
    with open(cfg.persistent_folder + 'weapons.json', 'r') as f:
        weapons_list = json.load(f)
    
    return weapons_list



if __name__ == "__main__":
    main()
        