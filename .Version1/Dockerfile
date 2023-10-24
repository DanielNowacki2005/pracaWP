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

#done to fix error that might be not real
#1  Attempt to search sollution to error
#2  Attempt to fix by setting Display as 0:0 - dosen't work
#3  Searching why according what i found i need to connect linux display to docker
#4. Attempting to fix display error from ubuntu cmd inside windows -dosesn't work
#5. attempting to install ubuntu-desktop -also dosen't fix the problem
#6. attempting to launch already installed ubuntu-destop  -also dosen't work
#7. install unbuntu on another computer because i was running low in memory in c do for my bad disk fragmentation
#8. realise after installing the ubuntu-desktop and then losing it to mysterious reasons that virtual box might work
#9. install newest version of ubuntu desktop
#10.attempt to install docker on newsest version of ubuntu desktop multiple times and even making multiple versions of virtual machines.
#11.Realise that it won't work because that version of ubuntu-desktop dosen't support docker
#12.Install correct version of ubuntu-desktop
#13.Sucesfully install docker
#14.Attempt to activate docker can't virutlization isn't on
#15.Check in bios virtualization it is on
#16.Check in virtual box if it is on -it isn't
#17.Attempt to enable it can't
#18.Try by cmd - VBoxManage is not recognized as internal command
#to do
#somehow activate virtulization in vm by using cmd because virtual box dosen't agree that this is possible by not allowing graying out the check for virtualization
#but before that i need to add virtual box to dependencies on windows so windows acknowlodges that it exist
#get this VBoxManage.exe: error: The machine is not mutable (state is Saved)
