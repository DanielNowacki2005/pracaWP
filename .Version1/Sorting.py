class Sorting: 
    def  findAll(self):
          #Sorts data
        #deletets everything outside important data
        self.price = self.queryFull.find_all('span',class_="value",string=True)
        self.name = self.queryFull.find_all('strong',class_="cat-prod-row__name")
        self.resolution = self.queryFull.find_all('strong',class_="",string=True)
        self.productScore = self.queryFull.find_all('span', class_="product-score")
        print(self.productScore)
        #Removes <span> and other from data
        j=0 
        for i in self.price:
            self.price[j] = i.text + "zł"
            j+=1
        j=0
        for k  in self.resolution:
            self.resolution[j] = k.text
            j+=1
        j=0
        for l  in self.productScore:
            self.productScore[j] = l.text
            j+=1
        j=0
        for n  in self.name:
            self.name[j] = n.text
            j+=1
    