FROM python:3.11.6
ADD Main.py .
ADD Request.py .
ADD Sorting.py .
RUN pip install tk
RUN pip install BeautifulSoup4
RUN pip install requests
CMD ["python","./Main.py"]
#docker run -p 4000:80 -it main_dockerization
#fix 
#_tkinter.TclError: no display name and no $DISPLAY environment variable
