import urllib.request as ur
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup


keyword = '美好世界'
# input('請輸入要查詢的關鍵字')
keyword_url= (quote(keyword))

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
        for nowpage in range(1,page+1):
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

