import requests,socket,sys



target = input("Please enter url: ")


def check_url(path):
    try:
        u = "http://" + target + "/" + path
        print(f"\n test for {u}")
        r = requests.get(u).status_code

    except Exception:
        print("\n can not reach url {u}")
        sys.exit(1)

    if r == 200:
        print("\n [+] valid url {u}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("\n check Host ...")
    status = s.connect_ex((target,80))
    s.close()

    if status == 0:
        print("done")
        pass
    else:
        print("target Fail")
        sys.exit(1)

    print("\n check list ....")
    with open("dlist.txt" , "r") as myfile :
        check_list = myfile.read().strip().split('\n')
        print("Done")
        print("\n Total path:  %s" %str(len(check_list)))

    print("Strat test")

    for i in range(len(check_list)):
        check_url(check_list[i])
    print("End test")

except socket.error:
    print("\n socket error")

except IOError:
    print("\n Io error")

except KeyboardInterrupt:
    print("\n key error")

