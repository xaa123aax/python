import urllib.request as ur
import tkinter as tk
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *


# keyword = '美好世界'
# keyword_url= (quote(keyword))


win = tk.Tk()
win.title('書籍查詢系統_ADT105112_邱奕畯')
win.geometry('1920x1080')
win.configure()

#==============================================================================================

header_label = tk.Label(win, text='書籍查詢系統', font=("微軟正黑體",48,'bold'))
header_label.pack()

key_frame = tk.Frame(win)
key_frame.pack(side='top')
keyword_label = tk.Label(key_frame, text='請輸入書籍名稱進行查詢', font=("微軟正黑體", 12,'bold'))
keyword_label.pack(side='left')

keyword_entry = tk.Entry(key_frame, width='40', font=("微軟正黑體", 16,'bold'))
keyword_entry.pack(side='left')

get_btn = tk.Button(key_frame, text='搜尋', command=lambda: [sanmin(),kingstone(),eslite()], font=("微軟正黑體", 14,'bold'), relief='raised', fg='red')
get_btn.pack(side='left' ,padx = 10)

quit_btn = tk.Button(key_frame, text='離開',command = win.destroy, font=("微軟正黑體", 14,'bold'), relief='raised', fg='red')
quit_btn.pack(side='left' ,padx = 10)


        # self.QUIT = Button(self, text = 'QUIT',

        
        #         fg = 'blue', command = wnd.destroy)
        # self.QUIT.pack(side = 'right')

list_frame = tk.Frame(win)
list_frame.pack(side='top')

#==============================================================================================

sanmin_list_frame = tk.Frame(list_frame)
sanmin_list_frame.pack(side='left', fill='y', padx = 10)

sanmin_title_label = tk.Label(sanmin_list_frame, text='三民網路書店', font=("微軟正黑體", 16,'bold'), fg='red')
sanmin_title_label.pack()

sanmin_list = Listbox(sanmin_list_frame, width=80, height=45)
sanmin_list.pack(fill='y')

#==============================================================================================

kingstone_list_frame = tk.Frame(list_frame)
kingstone_list_frame.pack(side='left', fill='y', padx = 10)

kingstone_title_label = tk.Label(kingstone_list_frame, text='金石堂', font=("微軟正黑體", 16,'bold'), fg='orange')
kingstone_title_label.pack()

kingstone_list = Listbox(kingstone_list_frame, width=80, height=45)
kingstone_list.pack(fill='y')

#==============================================================================================

eslite_list_frame = tk.Frame(list_frame)
eslite_list_frame.pack(side='right', fill='y', padx = 10)

eslite_title_label = tk.Label(eslite_list_frame, text='誠品網路書店', font=("微軟正黑體", 16,'bold'), fg='green')
eslite_title_label.pack()

eslite_list = Listbox(eslite_list_frame, width=80, height=45)
eslite_list.pack(fill='y')

# ==============================================================================================

def sanmin():

    keyword = keyword_entry.get()
    keyword_url= (quote(keyword))
    sanmin_list.delete(0, 'end')
    win.update()
    nowpage = 1
    product = []
    product_price = [] 


    html = urlopen('https://sanmin.com.tw/search/index?ct=K&K='+str(keyword_url)+'&ls=SD&vs=List&pi='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('span', {'class':'label-xs'})
    try:
        page = str(pages[0].text)
        left = int(page.rfind('/'))
        right = int(page.rfind('頁'))
        page=int(page[left+1:right])

        if page>=0:
            if page<=10:
                print('共'+str(page)+'頁')
                sanmin_list.insert(END,'共'+str(page)+'頁')
                win.update()
            if page>10:
                sanmin_list.insert(END,'共'+str(page)+'頁 顯示前200筆')
                win.update()
                page=10

            for nowpage in range(1,page+1):
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
                sanmin_list.insert(END,'掃描第'+str(nowpage)+"頁...")
                win.update()
                nowpage=nowpage+1

            number = len(product)
            print(number)
            print(len(product_price))
            win.update()
            sanmin_list.delete(0, 'end')
            for i in range(0,number):
                    print(str(product[i])+'  $'+str(product_price[i]))
                    sanmin_list.insert(END,str(product[i])+'  $'+str(product_price[i]))
        if page==0:    
            sanmin_list.insert(END,'沒書')    
        win.update()
    except:
        sanmin_list.insert(END,'搜不到東西')
# ==============================================================================================

def kingstone():
    keyword = keyword_entry.get()
    keyword_url= (quote(keyword))
    kingstone_list.delete(0, 'end')
    win.update()
    nowpage = 1
    product = []
    product_price = [] 

    html = urlopen('https://www.kingstone.com.tw/search/search?q='+str(keyword_url)+'&sort=score_asc&dis=&page='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('div', {'class':'pagetotal'})
    try:
        page = int((pages[0].find('span').next_sibling[1:]))

        if page>=0:
            if page<=10:
                print('共'+str(page)+'頁')
                kingstone_list.insert(END,'共'+str(page)+'頁')
                win.update()
            if page>10:
                kingstone_list.insert(END,'共'+str(page)+'頁 顯示前200筆')
                win.update()
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
                kingstone_list.insert(END,'掃描第'+str(nowpage)+"頁...")
                win.update()
                nowpage=nowpage+1

            number = len(product)
    
            kingstone_list.delete(0, 'end')
            for i in range(0,number):
                    print(str(product[i])+'  $'+str(product_price[i]))
                    kingstone_list.insert(END,str(product[i])+'  $'+str(product_price[i]))
    
            win.update()
    except:
        kingstone_list.insert(END,'搜不到東西')   
# ==============================================================================================

def eslite():
    keyword = keyword_entry.get()
    keyword_url= (quote(keyword))
    eslite_list.delete(0, 'end')
    win.update()
    nowpage = 1
    product = []
    product_price = [] 

    html = urlopen('http://www.eslite.com/Search_BW.aspx?query='+str(keyword_url)+'&searchType=&page='+str(nowpage))
    bsObj = BeautifulSoup(html, "lxml")
    pages = bsObj.findAll('div', {'class':'box_summary'})
    try:
        page = int(pages[0].find('div').next_sibling.next_sibling.find('span').next_sibling.next_sibling.next_sibling.next_sibling.text)
        print('總共頁數'+str(page))
        if page==0:
            eslite_list.insert(END,'搜不到東西')
            win.update()
        
        if page>0:        
            if page<=20:
                print('共'+str(page)+'頁')
                eslite_list.insert(END,'共'+str(page)+'頁')
                win.update()
            if page>20:
                eslite_list.insert(END,'共'+str(page)+'頁 顯示前200筆')
                win.update()
                page=20

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
                eslite_list.insert(END,'掃描第'+str(nowpage)+"頁...")
                win.update()
                nowpage=nowpage+1

            number = len(product)

            eslite_list.delete(0, 'end')
            for i in range(0,number):
                    print(str(product[i])+'  $'+str(product_price[i]))
                    eslite_list.insert(END,str(product[i])+'  $'+str(product_price[i]))
            win.update()
    except:
        eslite_list.insert(END,'搜不到東西')   
# ==============================================================================================


win.mainloop()


#  pyinstaller ADT105112.py -F -w