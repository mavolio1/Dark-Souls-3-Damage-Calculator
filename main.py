import requests
import json
from bs4 import BeautifulSoup
from utils import Weapon
from tqdm import tqdm
from config import cfg

def main():
    print('+------------------------------------------------------+')
    print('|                DARK SOUL 3 CALCULATOR                |')
    print('+------------------------------------------------------+')

    # main utilities
    weapons_list = load_weapon_data()
    json_to_persistent(weapons_list)

    # test
    weapons_list = load_from_json()
    highest_damage_wep(weapons_list)


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
        wep = {'name'           : url.replace(cfg.root_url, '').replace('/', '').replace('+', ' '),
               'weapon_type'    : 'tmp',
               'attack_type'    : 'tmp',
               'phys_atk'       : 0,
               'magic_atk'      : 0,
               'fire_atk'       : 0,
               'lightning_atk'  : 0,
               'dark_atk'       : 0,
               'str_scale'      : '-',
               'dex_scale'      : '-',
               'int_scale'      : '-',
               'faith_scale'    : '-'
               }
        
        trs = infobox.find_all('tr')
        for tr in trs:
            if tr.find('img'):
                imgs = tr.find_all('img')
                for img in imgs:
                    if img.get('title'):
                        # parse damage stats and weapon type
                        title = img.get('title')
                        if title == 'Physical Attack':
                            if img.find_next().text != '-':
                                wep['phys_atk'] = int(img.find_next().text)
                        elif title == 'Magical Attack':
                            if img.find_next().text != '-':
                                wep['magic_atk'] = int(img.find_next().text)
                        elif title == 'Fire Attack':
                            if img.find_next().text != '-':
                                wep['fire_atk'] = int(img.find_next().text)
                        elif title == 'Lightning Attack':
                            if img.find_next().text != '-':
                                wep['lightning_atk'] = int(img.find_next().text)
                        elif title == 'Dark Attack':
                            if img.find_next().text != '-':
                                wep['dark_atk'] = int(img.find_next().text)
                        elif title == 'Weapon Type':
                            wep['weapon_type'] = img.find_next().text
                        elif title == 'Attack Type':
                            wep['attack_type'] = img.find_next().text.replace(' ', '')

            if tr.find('td') and tr.find('td').text in cfg.scalings:
                # parse scalings
                tds = tr.find_all('td')
                wep['str_scale'] = tds[0].text
                wep['dex_scale'] = tds[1].text
                wep['int_scale'] = tds[2].text
                wep['faith_scale'] = tds[3].text

        weapons_list.append(Weapon(wep))

    return weapons_list

def json_to_persistent(weapons_list):
    json_list = []

    for wep in weapons_list:
        json_list.append(json.dumps(wep.__dict__))
    
    with open(cfg.persistent_folder + 'weapons.json', 'w') as f:
        json.dump(json_list, f)

def load_from_json():
    json_list = []
    with open(cfg.persistent_folder + 'weapons.json', 'r') as f:
        json_list = json.load(f)

    weapons_list = []
    for wep in json_list:
        weapons_list.append(Weapon(json.loads(wep)))
    
    return weapons_list

def highest_damage_wep(weapons_list):
    top_dmg_wep = {'name'       : 'best_wep',
                   'tot_damage' : 0,
                   'wep'        : None}
    
    for wep in weapons_list:
        tot_damage = wep.phys_atk + wep.magic_atk + wep.fire_atk + wep.lightning_atk + wep.dark_atk

        if tot_damage > top_dmg_wep['tot_damage']:
            top_dmg_wep['name'] = wep.name
            top_dmg_wep['tot_damage'] = tot_damage
            top_dmg_wep['wep'] = wep

    print(top_dmg_wep['wep'])




if __name__ == "__main__":
    main()
        