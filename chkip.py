import requests
import re
import json
import os

#http://httpbin.org/get?show_env=1
#http://www.ip181.com/

def online():
    downloads = []
    test_url = 'https://www.rmccurdy.com/scripts/proxy/good.txt'
    headers = {
"cookie": "__cfduid=d0a5b92249a4ff07d29b74f7d3fe175a61514081133",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38",
"accept-language": "zh-cn"
}
    down = requests.get(test_url,headers= headers).text
    k = down.split('\n')
    for j in k:
        if j not in downloads and j != ':':
            downloads.append(j)
    urls = ['http://www.proxylists.net/http_highanon.txt','http://www.proxylists.net/http.txt','http://ab57.ru/downloads/proxylist.txt']
    for url in urls:
        download = requests.get(url).text
        key = download.split('\r\n')
        for i in key:
            if i not in downloads and i != '':
                downloads.append(i)
    return downloads

def check(host):
    proxies = {
        'http':host,
        'https':host
    }
    try:
        r = requests.get("http://2017.ip138.com/ic.asp", proxies=proxies,timeout=3)
        data = r.content.decode('gb2312')
        print(r)
        ip = re.findall(r'\[(.*?)\]',data)[0]
        if ip.count('.') == 3:
            return ip
    except:pass

def save(filename, contents):
  fh = open(filename, 'a+')
  fh.write(contents)
  fh.close()

if __name__ == '__main__':
    url = 'http://2017.ip138.com/ic.asp'
    rep = requests.get(url=url)
    print(rep.content.decode('gb2312'))
    verify_ip = re.findall(r'\[(.*?)\]',rep.content.decode('gb2312'))[0]
    print(verify_ip)
    onlines = online()
    #fh = open("./proxy.txt", 'a+')
    filePath ="./proxy.txt"
    if os.path.exists(filePath):
        os.remove(filePath)
    for pro in onlines:
        resp = check(pro)
        if verify_ip != resp and resp:
            print(pro)
            #fh.write(pro)
            #fh.close()
            save(filePath,pro + "\n")