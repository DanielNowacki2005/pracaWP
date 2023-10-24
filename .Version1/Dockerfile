FROM python:3.11.6
ADD Main.py .
ADD Request.py .
ADD Sorting.py .
RUN pip install tk
RUN pip install BeautifulSoup4
RUN pip install requests
ENV USERNAME myNewUserName
CMD ["python","./Main.py"]
ENTRYPOINT  ["python","./Main.py"]
