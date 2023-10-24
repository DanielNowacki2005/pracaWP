#RUN -it --rm \
#    --user=$(id -u $USER):$(id -g $USER) \
#    --env="DISPLAY" \
#    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
#    osrf/ros:indigo-desktop-full
#to run in interactive mode<br>
#docker run -p 4000:80 -it main_dockerization <br>
#I don't think error is beacause of this file but linux display configuration.<br>
#Now i believe that this dosen;t work not because lack of something but it needs to activated inside linux with graphical interface<br>
#I hope that this works it probably needs to be activated inside linux with graphical interface.<br>
#I really want to check if it i did this right but i with how long does me to even launch docker on linux and how many attemps i did i don't see it <br>
#I hope that i will check it today on linux<br>

#done to fix error that might be not real<br>
#1  Attempt to search sollution to error<br>
#2  Attempt to fix by setting Display as 0:0 - dosen't work<br>
#3  Searching why according what i found i need to connect linux display to docker<br>
#4. Attempting to fix display error from ubuntu cmd inside windows -dosesn't work<br>
#5. attempting to install ubuntu-desktop -also dosen't fix the problem<br>
#6. attempting to launch already installed ubuntu-destop  -also dosen't work<br>
#7. install unbuntu on another computer because i was running low in memory in c do for my bad disk fragmentation<br>
#8. realise after installing the ubuntu-desktop and then losing it to mysterious reasons that virtual box might work<br>
#9. install newest version of ubuntu desktop<br>
#10.attempt to install docker on newsest version of ubuntu desktop multiple times and even making multiple versions of virtual machines.<br>
#11.Realise that it won't work because that version of ubuntu-desktop dosen't support docker<br>
#12.Install correct version of ubuntu-desktop<br>
#13.Sucesfully install docker<br>
#14.Attempt to activate docker can't virutlization isn't on<br>
#15.Check in bios virtualization it is on<br>
#16.Check in virtual box if it is on -it isn't<br>
#17.Attempt to enable it can't<br>
#18.Try by cmd - VBoxManage is not recognized as internal command<br>
#to do
#somehow activate virtulization in vm by using cmd because virtual box dosen't agree that this is possible by not allowing graying out the check for virtualization
#but before that i need to add virtual box to dependencies on windows so windows acknowlodges that it exist
#get this VBoxManage.exe: error: The machine is not mutable (state is Saved)
#now this VBoxManage.exe: error: Context: "SetCPUProperty(CPUPropertyType_HWVirt, ValueUnion.f)" at line 941 of file VBoxManageModifyVM.cpp
