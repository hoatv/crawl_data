import json

import requests
from bs4 import BeautifulSoup

# 1. Lấy html
url = 'https://dantri.com.vn/su-kien.htm'

response = requests.get(url)

# 2. Trích rút thông tin các bài viết gồm tiêu đề, ảnh và mô tả
soup = BeautifulSoup(response.content, 'html.parser')

post_elements = soup.find_all("div", {"data-boxtype": 'timelineposition'})

result = []
for v in post_elements:
    result.append({
        'title': v.a.attrs['title'],
        'img_src': v.a.img.attrs['src'],
        'description': list(v.div.div.children)[2].strip()
    })

print(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False))

# 3. Lưu ra file json
with open('result.json', 'wt', encoding='utf-8') as f:
    f.write(json.dumps(result, ensure_ascii=False))



# result = []
# for v in post_elments:
#     result.append({'title': v.a.attrs['title'], 'src': v.a.img.attrs['src'], 'description': v.div.div.text.strip()})
