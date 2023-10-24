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
#RUN -it --rm \
#    --user=$(id -u $USER):$(id -g $USER) \
#    --env="DISPLAY" \
#    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
#    osrf/ros:indigo-desktop-full
#to run in interactive mode
#docker run -p 4000:80 -it main_dockerization 
#I don't think error is beacause of this file but linux display configuration.
#Now i believe that this dosen;t work not because lack of something but it needs to activated inside linux with graphical interface
#I hope that this works it probably needs to be activated inside linux with graphical interface.
#I really want to check if it i did this right but i with how long does me to even launch docker on linux and how many attemps i did i don't see it 
#I hope that i will check it today on linux
