import urllib.request as ur
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup

keyword = input('請輸入要查詢的關鍵字')
keyword_url= (quote(keyword))

def sanmin():
    nowpage = 1
    product = []
    product_price = [] 
    html = urlopen('https://sanmin.com.tw/search/index?ct=K&K='+str(keyword_url)+'&ls=SD&vs=List&pi='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('span', {'class':'label-xs'})
    page = str(pages[0].text)
    left = int(page.rfind('/'))
    right = int(page.rfind('頁'))
    page=int(page[left+1:right])


    if page>0:
        print('共'+str(page)+'頁')
        if page>10:
            page=10
        for nowpage in range(1,3+1):
            url = 'https://sanmin.com.tw/search/index?ct=K&K='+str(keyword_url)+'&ls=SD&vs=List&pi='+str(nowpage)           
            html = urlopen(url)
            bsObj2 = BeautifulSoup(html, "lxml")
            nameList = bsObj2.findAll("h3", {"style":"margin-bottom:10px;"})
            priceList = bsObj2.findAll('span', {'class':'price'})

            for name in nameList:
                product.append(name.get_text())
            for price in priceList:
                product_price.append(price.text)


            print ('掃描第'+str(nowpage)+"頁...")
            nowpage=nowpage+1

        number = len(product)
        
        for i in range(0,number):
                print(str(product[i])+'  $'+str(product_price[i]))

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

        for nowpage in range(1,3+1):
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


def eslite():

    nowpage = 1
    product = []
    product_price = [] 

    html = urlopen('http://www.eslite.com/Search_BW.aspx?query='+str(keyword_url)+'&searchType=&page='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('div', {'class':'box_summary'})
    page = int(pages[0].find('div').next_sibling.next_sibling.find('span').next_sibling.next_sibling.next_sibling.next_sibling.text)
    print('總共頁數'+str(page))

    if page>0:
        print('共'+str(page)+'頁')
        if page>10:
            page=10
        for nowpage in range(1,3+1):
            url = 'http://www.eslite.com/Search_BW.aspx?query='+str(keyword_url)+'&searchType=&page='+str(nowpage)
            html = urlopen(url)
            bsObj2 = BeautifulSoup(html, "lxml")
            nameList = bsObj2.findAll("td", {"class":'name'})
            priceList = bsObj2.findAll('td', {'class':'summary'})


            for name in nameList:
                product.append(name.find('span').get_text())
            for price in priceList:
                product_price.append(price.find('font').text)
    

            print ('掃描第'+str(nowpage)+"頁...")
            nowpage=nowpage+1

        number = len(product)

        for i in range(0,number):
                print(str(product[i])+'  $'+str(product_price[i]))


sanmin()
kingstone()
eslite()
