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
RUN -it --rm \
    --user=$(id -u $USER):$(id -g $USER) \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    osrf/ros:indigo-desktop-full
#to run in interactive mode
#docker run -p 4000:80 -it main_dockerization 
