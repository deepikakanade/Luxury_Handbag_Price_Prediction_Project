import urllib.request as urllib2 
#making url requests
import csv
from bs4 import BeautifulSoup
#extracts data from a webpage
import pandas as pd
import requests #to download the html page
import re

main_link = "https://www.gucci.com/us/en/ca/women/womens-handbags-c-women-handbags" 

for i in range(9): ##loop over all the handbags links
    second_link = main_link + '/' + str(i)
    page = requests.get(second_link)
    soup = BeautifulSoup(page.content,'html.parser')
    product_tags = soup.find_all(class_ = 'product-tiles-grid-item-link') #get the class for the tiles
    for x in product_tags:
        l.append(x['href']) #extract all the links to the product pages


mystring="https://www.gucci.com/" ##append to get the proper link
l1 = [mystring + s for s in l] #get all the urls for the bags

column = ['Brand','Title', 'Price','Style','Size','Make','Lining', 'Bullets', 'Description','URL']
gucci = pd.DataFrame(columns=column)

for x in l1:
    page = requests.get(x)
    if(page.ok == False):
        continue;
    #use beautiful soup to parse this
    soup = BeautifulSoup(page.content,'html.parser')
    #get the product details from the tag on the website
    product_details = soup.find(id="accordion-product-details")
    all_details = product_details.find(class_ = "product-detail")
    bullets = list(all_details.children)[3] #get some of the bullet information
    make = list(bullets)[-2].get_text()
    lining = list(bullets)[-4].get_text()
    size = list(bullets)[-6].get_text()
    all_details = product_details.find(class_ = "product-detail")
    para_details = all_details.p.get_text()
    para_details  = para_details.replace("\n"," ").replace("  ","")#gets all the para, type:tag
    bullet_points = all_details.ul.get_text()
    bullet_points = bullet_points.replace("\n"," ")##get all bullet points as string
    price = soup.find(class_="product-detail-purchase")
    ##get the name of the bag
    name = soup.find(class_="product-name product-detail-product-name").get_text()
    p = soup.find(id="markedDown_full_Price").get_text()
    p = re.sub("[^0-9]", "", p) #actual price retained only in numbers 
    type_bag = soup.find('input', {'class': 'gucciProductCategory'}).get('value')
    type_bag = type_bag[type_bag.rfind('/')+1 :]
    record = ['Gucci', name, p, type_bag, size, make, lining, bullet_points, para_details, x]
    gucci.loc[len(gucci)] = record

    #COMMENT: Turn on the images, takes forever and downloads the images. Way to compress them? do we want to compress them?

    
    ##get images:
    # For finding the images
    """
    img_tags = soup.find_all('img')
    l = [i for i in img_tags] #get all the elements which have img_tags
    a = [k for k in l] 
    c = []
    for x in range(len(a)):
        try:
            c.append(a[x]['srcset']) #get the tags which have srcset, these contain the urls
        except KeyError:
            continue
    
    c1 = list(set(c)) #removes duplicates
    sub="style"
    mystring="http:"
    c2 = [mystring +s for s in c1 if sub in s] #search for keyword style for bag image, add http at the start
    for x1 in range(len(c2)): ##saves all the images with names as the title of bag and price
        img = urllib2.urlopen(c2[x1])
        filename = 'images/'+name+p+str(x1)
        localFile = open(filename+'.jpg', 'wb')
        localFile.write(img.read())
        localFile.close()
    """
    gucci.to_csv('gucci_info.csv')

    



