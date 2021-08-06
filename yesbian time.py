Timechoice=int(input("What is your choice of time?"))
Hours=(Timechoice//3600)
Minutes=Timechoice-(Hours*3600)//60
Seconds=Timechoice-(Minutes*60)//60
if Seconds<10:
    print(f"{Hours}:{Minutes}:0{Seconds}")
else:
    print(f"{Hours}:{Minutes}:{Seconds}")
 