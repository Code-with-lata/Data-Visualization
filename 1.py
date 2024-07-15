# time = int (input("Enter the time :"))
# if(time >=0 ):
#     t1 = time/3600
#     min = (time %3600)/60
#     sec = time/60
#     print (t1,"Hours ",min,"minute ",sec, "second")
    

# else:
#     print("Enter invalid")


time = int(input("Enter time in sec :"))

if(time >=0):
    hour = 0
    min = 0
    #conver to hours
    if(time >=3600):
        hour = time //3600
        time = time % 3600
    #convert to min
    if(time >=60):
        min = time //60
        time = time %60

        print (hour,"hours",min,"min",time,"sec")
else:
    print("invalid")
