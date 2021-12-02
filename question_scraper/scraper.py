import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

current_day = datetime.now().day
current_folder = f'Day {current_day}'
os.makedirs(current_folder, exist_ok=True)
readme_path = os.path.join(current_folder, 'README.md')

url = f'https://adventofcode.com/{datetime.now().year}/day/{current_day}'
COOKIE = os.environ.get('COOKIE', '')
headers = {
    'cookie': f'session={COOKIE}'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content)

content = ''
for block in soup.find_all('article', class_='day-desc'):
    content += str(block)

content = content.replace(str(soup.h2),f'<h2><a href="{url}">{soup.h2.text}</a></h2>') 

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
