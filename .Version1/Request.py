import requests
from bs4 import BeautifulSoup
class Request: 
    def __init__(self,url,window):
            self.url = url
            self.queryFull = ""
            self.amount = 25
            self.requestWebsite = ""
            self.request = ""
                #Connect to targeted website and downoald from api
    def getData(self):
        request = requests.get(self.url,allow_redirects= True)
        self.queryFull = BeautifulSoup(request.text,"html.parser")