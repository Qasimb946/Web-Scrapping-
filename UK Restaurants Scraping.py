import requests
import bs4
import csv 
import time
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}
f = open('My Run.csv', 'w', newline = '')

writer = csv.writer(f)
writer.writerow(['Name', 'Cuisine Type', 'Total Reviews', 'Address', 'Postal Code'])
frs = open('Output.csv' , 'r')
csv_reader_s = csv.reader(frs)
count = 1
for j in csv_reader_s:
    link_s = str(*j)
    URL = link_s
    print(URL)

    Name = ''
    cuisine = ''
    reviews = ''
    address = ''
    Postal_code = ''
    print(count)
    time.sleep(10)
    res = requests.get(URL, headers = headers)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    try:
        
        Name = soup.find('h1' , attrs = {'class' , 'c-mediaElement-heading u-text-center'})
        Name = Name.text.strip()
        print(Name)
        
    except: pass
    
    
    try:
        
        cuisine = soup.find('span', attrs= {'class', 'c-badge c-badge--light c-badge--large'})
        temp = cuisine.find_all('span')
        
        type = len(temp)
        
        if type == 1:
            cuisine = temp[0].text.strip()
            print(cuisine)
            
        if type == 3:
            a = temp[0].text.strip()
            b = temp[1].text.strip()
            cuisine = a + ' ' + b
            print(cuisine)
            
        if type == 5:
            a = temp[0].text.strip()
            b = temp[1].text.strip()
            c = temp[3].text.strip()
            cuisine = a + ' ' + b + ' ' + c
            print(cuisine)
    except:pass
    
    
    
    try: 
        
         reviews = soup.find('strong' , attrs = {'class' , 'u-spacingLeft'})
         reviews = reviews.text.strip()
         reviews = reviews.replace('View','')
         reviews = reviews.strip()
         print(reviews)
        
    except: pass
    
    try: 

        address = soup.find('p', attrs = {'class' , 'l-centered c-restaurant-header-address'})
        address = address.text.strip()
        h =address.rsplit(',' , 1)
        Postal_code = h[1].strip()
        address = h[0]
        print(address)
        print(Postal_code)
    
    except: pass
    count = count + 1
    
    writer.writerow([Name, cuisine, reviews, address,Postal_code])

f.close()