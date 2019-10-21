import re

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Host': 'www.zhihu.com',
    'Cookie': r'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1570955503;'
              'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1570933515,1570933669,1570949463,1570949640;'
              '__cfduid=df9c379813133d352a8dfbc5b353c82e61561813389;'
              '_xsrf=964acd5b-3b76-44f3-a20d-1acbf3cf5a44;'
              '_zap=6f247a7b-6e1c-4d0b-89af-88d81531ac93;'
              'capsion_ticket="2|1:0|10:1570955194|14:capsion_ticket|44:YzQyMDllZDFhNDEwNGJmOGIwMzM4OGFhNjZmMDI0YTQ=|4ce1ed6057562042379f90654d27426bcdcccd3ed25900bfd5f0a20046db5230";'
              'd_c0="APCtP-roqA-PTkVlI2zo77Ecjgeg0tFl8pY=|1561813384";'
              'tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7;'
              'tgw_l7_route=73af20938a97f63d9b695ad561c4c10c;'
              'tst=r;'
              'unlock_ticket="AACAa-EcAAAmAAAAYAJVTUTnol3F5ohON6CP_hfGfhw0rFNs-j9l3w==";'
              'z_c0="2|1:0|10:1570955211|4:z_c0|92:Mi4xN25rU0FBQUFBQUFBOEswXzZ1aW9EeVlBQUFCZ0FsVk55eTJRWGdEcmtldmNEZkJxcWV3RERXM2Ezc1NOS1haellR|216de0c327792e87c70ec228887f18f22e04d38de08117aa4acbd8a3f8c7b292"'
}

r = requests.get('https://www.zhihu.com/', headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')
title_regex = re.compile(
    '<a target="_blank" data-za-detail-view-element_name="Title" data-za-detail-view-id="2812" href="/question/41476832/answer/746042923">有哪些高质量的自学网站？</a>')
titles = re.findall(title_regex,r.text)
for t in titles:
    print(t.string)
