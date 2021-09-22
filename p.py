# note: every time you press "enter" , start inputting the command 
# do not press "enter again"!!
lotarr=[]
def command():
    n=list(map(str ,input().split(" ")))
    if(n[0]=="create_parking_lot"):
        print("Created a parking lot with ",n[1]," Slots")
        global lot
        lot=int(n[1])
        for i in range(0,lot):
            i=list(map(str,input().split(" ")))
            lotarr.append(i)
        for j in range(0,len(lotarr)):
            lotarr[j][0]=j+1
        command()
        # recalling the function for different command
    elif(n[0]=="leave"):
        # leaving the required slot by poping it
        global rem
        rem=int(n[1])-1
        lotarr.pop(rem)
        print("Slot number ",n[1]," is free")
        command()
    elif(n[0]=="status"):
        print("Slot No. Registration No  Color")
        for i in range(0,len(lotarr)):
            for j in range(0,3):
                print(lotarr[i][j],end="    ")
            print("\n")
        command()
    elif(n[0]=="registration_numbers_for_cars_with_colour"):
        for i in lotarr:
            if(n[1] in i):
                print(i[1],end=" ")
        print("")
        command()
    elif(n[0]=="slot_numbers_for_cars_with_colour"):
        for i in lotarr:
            if(n[1] in i):
                print(i[0],end=" ")
        print("")
        command()
    elif(n[0]=="slot_number_for_registration_number"):
        h=False
        re=""
        for i in lotarr:
            if(n[1] in i):
                h=True
                re=i[0]
                break;
        if(h==True):
            print(re)
        else:
            print("not found")
        print("")
        command()
    elif(n[0]=="park"):
        if(len(lotarr)==lot):
            print("Sorry,Parking lot is full")
        else:
            lotarr.insert(rem,n)
            lotarr[rem][0]=rem+1
    command()

command()
