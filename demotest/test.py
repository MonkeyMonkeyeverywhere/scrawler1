import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Host': 'www.behance.net',
    'X-Requested-With': 'XMLHttpRequest',
    'X-BCP': '141fe6a8-d820-4f83-b4e7-b163d9c4bcea',
    'Cookie': 'gk_suid=28673185; gki=%7B%22db_semaphore%22%3Afalse%2C%22live_featured_hero%22%3Afalse%7D; bcp=141fe6a8-d820-4f83-b4e7-b163d9c4bcea; bcp_generated=1571629359737; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=-227196251%7CMCMID%7C72889074359490452383631747725102698294%7CMCAAMLH-1572234171%7C11%7CMCAAMB-1572234171%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1571636571s%7CNONE%7CMCAID%7CNONE; s_sess=%20s_dmdbase%3D1%3B%20s_dmdbase_custom%3D1%3B%20s_cpc%3D0%3B%20s_sq%3D%3B%20s_ppv%3D%255B%2522www.behance.net%252Fgalleries%252Fphotography%2522%252C100%252C0%252C5139%252C1707%252C569%252C1707%252C960%252C1.5%252C%2522P%2522%255D%3B%20s_cc%3Dtrue%3B; s_pers=%20s_nr%3D1571629834624-New%7C1603165834624%3B%20cpn%3Dbehance.net%253Agalleries%7C1729482634745%3B%20ppn%3Dbehance.net%253Agallery%7C1729482634746%3B%20s_vs%3D1%7C1571633339745%3B'
}

res = requests.get('https://www.behance.net/v2/discover/photography?ordinal=96>', headers=headers)
print(res.status_code)
print(res.text)
