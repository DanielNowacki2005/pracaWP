import Request,Sorting
import tkinter as tk
class Main:
    def __init__(self):
        self.url = ""
        while self.url != "https://www.ceneo.pl/exit" :
            self.url = self.getUrl()#gets user item
            if self.url == "https://www.ceneo.pl/exit":
                break
            else:
                self.request = self.searchFull()#gets data
                if self.request.getData() != 1: #if request not failed
                    self.result = self.sort() #sorts data
                    self.show = self.showAsTable() # shows table
                else:#if request failed

                    print("there is typo or that product dosen't exist")
                
    def searchFull(self):
        return  Request.Request(self.url)
    def sort(self):
        return  Sorting.Sorting(self.request.queryFull)
    def showAsTable(self):
        totalRows = len(self.result.name)
        if len(self.result.name) == 0 or len(self.result.price) == 0 or len(self.result.productScore) == 0: # checks if query is empty 
             print("there is typo or that product dosen't exist")
        else:
        #shows data as table
            window = tk.Tk()
            window.title("WP Daniel Nowacki 2023")
            DISPLAY=0.0
            window.geometry("1800x900")
            self.amount = 20
            #headers of the table
            name = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text= self.question+" name.")
            name.grid(row=0, column=1)

            price = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text=self.question+" price.")
            price.grid(row=0, column=2)
            productScore = tk.Label(window, width=20, fg='black',font=('Arial',16,'bold'),text=self.question+" Score.")
            productScore.grid(row=0, column=4)
        #table body             
            for i in range(totalRows-3):
                    if i == self.amount: break
                    self.e = tk.Entry(window, width=50, fg='black',font=('Arial',12,'bold'))
                    self.e.grid(row=i+1, column=1)
                    self.e.insert("end",self.result.name[i+3])
                    print(self.result.name)
            totalRows = len(self.result.price)
            for i in range(totalRows):
                    if i == self.amount: break
                    self.e = tk.Entry(window, width=10, fg='black',font=('Arial',12,'bold'))
                    self.e.grid(row=i+1, column=2)
                    self.e.insert("end",self.result.price[i])
            
            totalRows = len(self.result.productScore)
            for i in range(totalRows):
                    if i == self.amount: break
                    self.e = tk.Entry(window, width=10, fg='black',font=('Arial',12,'bold'))
                    self.e.grid(row=i+1, column=4)
                    self.e.insert("end",self.result.productScore[i])
                    #writes data
            window.mainloop()
    def getUrl(self):
        self.question = input("Write what kind of product do you want to search. From Ceneo exapmple komputery for computer or Bizuteria_i_zegarki or exit to exit: ")
        url = "https://www.ceneo.pl/"+self.question
        return url
aplikacja = Main()
