import os
import re
import requests
from bs4 import BeautifulSoup

ROOT = "https://mojim.com"
INVALID_FLAGS = ['<', '[', '作词', '作曲', '编曲', '演唱', '监制', '制作人', '监唱', '录音师', '混音', '人声编辑', '主题曲' 'Mojim']
DIRTY_CHARS = ['＊', '＃', '△', '.', '&amp;', '*']

def write_file(text, singer):
    with open('lyrics/'+ singer +'.txt', 'a+', encoding="utf-8") as f:
        f.write(text)

def is_invalid_line(line):
    contains_invalid_flag = list(filter(None, [flag in line for flag in INVALID_FLAGS]))
    if line and not contains_invalid_flag:
        return True
    return False

def clean_raw(text):
    for c in DIRTY_CHARS:
        text = text.replace(c, '')
    return text

def get_lyrics_for_song(song_link):
    lyric_page_url = song_link.get('href')
    response = requests.get(ROOT + lyric_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    lyric_container = soup.find('dl','fsZx1')
    lines = re.split('<br/>|\n', clean_raw(str(lyric_container)))
    lines = list(filter(is_invalid_line, lines))[2:]
    return '\n'.join(lines) + ";\n"

def search_lyrics_for_singer(url, singer_name):
    response = requests.get(ROOT + url)
    soup = BeautifulSoup(response.text, 'html.parser')
    blocks = soup.find_all('dd', 'hb2') + soup.find_all('dd','hb3')

    for block in blocks:
        song_lists = block.find_all('span','hc3') + block.find_all('span','hc4')
        for song_list in song_lists:
            song_links = song_list.find_all('a')
            for link in song_links:
                lyric = get_lyrics_for_song(link)
                write_file(lyric, singer_name)

def get_singers(singer_list_url, count):
    response = requests.get(ROOT + singer_list_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    singer_container = soup.find('ul', 's_listA')
    singers = singer_container.find_all('a')
    for singer in singers:
        if os.path.isfile('.\lyrics\\' + singer.text + '.txt'):
            print(singer.text + '.txt already exists. Skipping...')
            continue
        count += 1
        print('Crawling for singer No. %s: %s' % (count, singer.text))
        search_lyrics_for_singer(singer.get('href'), singer.text)
    return count

if __name__ == "__main__":
    count = 0
    for url in ['/cnza2.htm', '/cnzb2.htm', '/cnzc2.htm']:
        count = get_singers(url, count)
