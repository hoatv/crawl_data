import requests

url = 'https://tiki.vn/deal-hot?src=header_label&tab=now&page=1'

response = requests.get(url)
with open('a.html', 'wt', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))


