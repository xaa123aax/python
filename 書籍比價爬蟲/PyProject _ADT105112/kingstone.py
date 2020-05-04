import urllib.request as ur
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup


keyword = input('請輸入要查詢的關鍵字')
keyword_url= (quote(keyword))

def kingstone():

    nowpage = 1
    product = []
    product_price = [] 

    html = urlopen('https://www.kingstone.com.tw/search/search?q='+str(keyword_url)+'&sort=score_asc&dis=&page='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('div', {'class':'pagetotal'})
    page = int((pages[0].find('span').next_sibling[1:]))

    if page>0:
        print('共'+str(page)+'頁')
        if page>10:
            page=10

        for nowpage in range(1,page+1):
            url = 'https://www.kingstone.com.tw/search/search?q='+str(keyword_url)+'&sort=score_asc&dis=&page='+str(nowpage)               
            html = urlopen(url)
            bsObj2 = BeautifulSoup(html, "lxml")
            nameList = bsObj2.findAll("h3", {"class":"pdnamebox"})
            priceList = bsObj2.findAll('div', {'class':'buymixbox'})

            for name in nameList:
                product.append(name.get_text())
            for price in priceList:
                if '折' in str(price.find('span').text):
                    product_price.append(price.find('span').next_sibling.find('b').text)
                else:
                    product_price.append(price.find('span').find('b').text)

            print ('掃描第'+str(nowpage)+"頁...")
            nowpage=nowpage+1

        number = len(product)

        for i in range(0,number):
                print(str(product[i])+'  $'+str(product_price[i]))