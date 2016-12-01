from urllib.parse import urlparse

link="http://career.cmbchina.com/Campus/Position.aspx?id=10297"

print(urlparse(link).query)
print(urlparse(link).netloc)
