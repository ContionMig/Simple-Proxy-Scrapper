import requests, os

sources = ['https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all', 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all', 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all', 'https://www.proxy-list.download/api/v1/get?type=http', 'https://www.proxy-list.download/api/v1/get?type=https', 'https://www.proxy-list.download/api/v1/get?type=socks4', 'https://www.proxy-list.download/api/v1/get?type=socks5']

try:
    os.remove("Proxies.txt")
except:
    pass

for x in range(len(sources)):
    r = requests.get(sources[x])
    file = open("Proxies.txt", "a")

    lines = r.text.split('\n')
    lines = [line for line in lines if line.strip()]
    for x in range(len(lines)):
        file.write(lines[x])
    file.close()