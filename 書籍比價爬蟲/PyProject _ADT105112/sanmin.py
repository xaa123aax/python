import urllib.request as ur
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup

keyword = '心理學'
keyword_url= (quote(keyword))

def sanmin():
    nowpage = 1
    product = []
    product_price = [] 
    html = urlopen('https://sanmin.com.tw/search/index?ct=K&K='+str(keyword_url)+'&ls=SD&vs=List&pi='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('span', {'class':'label-xs'})
    page = str(pages[0].text)
    page_left = int(page.rfind('/'))
    page_right = int(page.rfind('頁'))
    page=int(page[page_left+1:page_right])


    if page>0:
        print('共'+str(page)+'頁')
        if page>10:
            page=10
        for nowpage in range(1,3+1):
            url = 'https://sanmin.com.tw/search/index?ct=K&K='+str(keyword_url)+'&ls=SD&vs=List&pi='+str(nowpage)           
            html = urlopen(url)
            bsObj2 = BeautifulSoup(html, "lxml")
            nameList = bsObj2.findAll("h3", {"style":"margin-bottom:10px;"})
            priceList = bsObj2.findAll('div', {'class':'resultBooksLayout'})

            for name in nameList:
                product.append(name.get_text())

            for price in priceList:
                if '折' in str(price.find('span')):                 
                    product_price.append(price.find('p').find('span').find('span').next_sibling.next_sibling.text)
                else:
                    product_prices=price.find('p').text
                    product_price_left = int(product_prices.find('：'))                
                    product_price_right = int(product_prices.rfind('元'))
                    price=(product_prices[product_price_left+1:product_price_right])
                    product_price.append(price)


            print ('掃描第'+str(nowpage)+"頁...")
            nowpage=nowpage+1

        number = len(product)
        
        for i in range(0,number):
                print(str(product[i])+'  $'+str(product_price[i]))
sanmin()