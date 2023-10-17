import requests
from bs4 import BeautifulSoup
class Request: 
    def __init__(self,url):
            self.url = url
            print(self.url)
            self.getData()
                #Connect to targeted website and downoald from api
    def getData(self):
        request = requests.get(self.url,allow_redirects= True)
        self.queryFull = BeautifulSoup(request.text,"html.parser")
        if self.queryFull != []:
            return self.queryFull
        else:
             return 1
