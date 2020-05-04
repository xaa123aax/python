import urllib.request
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36

'}
keyword = '迷霧之子'
#input('請輸入要查詢的關鍵字')
keyword_url= (quote(keyword))
nowpage = 1
product = []
product_price = [] 
url = 'https://search.books.com.tw/search/query/cat/all/key/'+str(keyword_url)+'/sort/1/ms2/ms2_1/page/'+str(nowpage)+'/v/0/'
req = urllib.request.Request(url, headers=headers)
html = urlopen(req)
bsObj = BeautifulSoup(html, "lxml")
pages = bsObj.findAll('div', {'class':'page'})
page = int((pages[0].find('span')).text)
print('總共頁數'+str(page))

if page>1:
    for nowpage in range(1,2):
        url = 'https://search.books.com.tw/search/query/cat/all/key/'+str(keyword_url)+'/sort/1/ms2/ms2_1/page/'+str(nowpage)+'/v/0/'       
        req = urllib.request.Request(url, headers=headers)
        html = urlopen(req)
        bsObj2 = BeautifulSoup(html, "html.parser")
        nameList = bsObj2.findAll('li', {'class':'item'})
        # priceList = bsObj2.findAll('div', {'class':'price'})

        for name in nameList:
            product.append(name.text)
        # for price in priceList:
        #     if '折' in str(price.find('strong').text):
        #         product_price.append(price.find('strong').next_sibling.find('b').text)
        #     else:
        #         product_price.append(price.find('strong').find('b').text)

        print (str(nowpage)+'/' +str(page))
        nowpage=nowpage+1

    number = len(product)

    for i in range(0,number):
            print(str(product[i]))
