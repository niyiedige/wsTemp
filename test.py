from urllib.parse import urlparse

link="http://egfbank.zhiye.com/zpdetail/310028588?p=3%5E17"

print(urlparse(link).query)
print(urlparse(link).netloc)
print(urlparse(link).path)