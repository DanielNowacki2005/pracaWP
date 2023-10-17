import requests
from bs4 import BeautifulSoup
class Sorting: 
          #Sorts data
        #deletets everything outside important data
    def __init__(self,queryFull):
        self.queryFull = queryFull
        self.price = self.queryFull.find_all('span',class_="value",string=True)
        self.name = self.queryFull.find_all('strong',class_="cat-prod-row__name")
        self.productScore = self.queryFull.find_all('span', class_="product-score")
        self.sort()
        #Removes <span> and other from data
    def sort(self):    
        j=0 
        for i in self.price:
            self.price[j] = i.text + "zł"
            j+=1
        j=0
        for l  in self.productScore:
            self.productScore[j] = l.text
            j+=1
        j=0
        for n  in self.name:
            self.name[j] = n.text
            j+=1
        
