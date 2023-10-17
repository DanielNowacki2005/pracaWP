import Request,Sorting,Showing
import tkinter as tk
class Main:
    def __init__(self):
        self.url = self.getUrl()
        self.request = self.searchFull()#self.request.queryFull
        self.result = self.sort()
        self.amount = 25
        self.showing = Showing(self.result.name,self.result.price,self.result.productScore,window)
    def searchFull(self):
        return  Request.Request(self.url)
    def sort(self):
        return  Sorting.Sorting(self.request.queryFull)

    def getUrl(self):
        self.question = input("Write what kind of product do you want to search. From Ceneo exapmple komputery for computer or Bizuteria_i_zegarki")
        url = "https://www.ceneo.pl/"+self.question
        return url
window = tk.Tk()
window.geometry("1800x900")
aplikacja = Main()
window.mainloop()
