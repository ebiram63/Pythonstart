patrons = ""
waitEstimate  = ""
Hungry = ""
Alternate = ""
Runing = ""
Reservation = ""
Bari = ""
Frai = ""

if patrons == "Full":
    if waitEstimate is not None:
        if  0 < waitEstimate < 10:
            print("yes")
        elif 10 <= waitEstimate < 30:
            if Hungry is not None:
                if Hungry == "Yes":
                    if Alternate is not None:
                        if Alternate == "Yes":
                            if Runing is not None:
                                if Runing == "Yes":
                                    print("yes")
                                else:
                                    print("no")
                elif Hungry == "No":
                    print("yes") 
        elif 30 <= waitEstimate < 60:
            if Alternate is not None:
                if Alternate == "Yes":
                    if Frai is not None:
                        if Frai == "Yes":
                            print("yes")
                        else:
                            print("no")    
                else:
                    if Reservation is not None:
                        if Reservation == "Yes":
                            print("yes")
                        elif Reservation == "No":
                            if Bari is not None:
                                if Bari == "Yes":
                                    print("yes")
                                elif Bari == "No":
                                    print("no")    
elif patrons == "some":
    print("yes")
elif patrons == "none":
    print("no")    
    
     






    
    

