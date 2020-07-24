def Tool ():
    import random

    from time import sleep

    import requests
    Red = "\033[1;31;31m"

    GREEN = "\033"

    Color = "\033[1;30;32m"
    print('''
    8888888b.                                          .d8888b.  888                        888                       
    888   Y88b                                        d88P  Y88b 888                        888                       
    888    888                                        888    888 888                        888                       
    888   d88P 888d888 .d88b.  888  888 888  888      888        88888b.   .d88b.   .d8888b 888  888  .d88b.  888d888 
    8888888P"  888P"  d88""88b `Y8bd8P' 888  888      888        888 "88b d8P  Y8b d88P"    888 .88P d8P  Y8b 888P"   
    888        888    888  888   X88K   888  888      888    888 888  888 88888888 888      888888K  88888888 888     
    888        888    Y88..88P .d8""8b. Y88b 888      Y88b  d88P 888  888 Y8b.     Y88b.    888 "88b Y8b.     888     
    888        888     "Y88P"  888  888  "Y88888       "Y8888P"  888  888  "Y8888   "Y8888P 888  888  "Y8888  888     
                                             888                                                                      
                                        Y8b d88P                                                                      
                                         "Y88P"
                                          .    
             .              .   .'.     \   /  
           \   /      .'. .' '.'   '  -=  o  =-
         -=  o  =-  .'   '              / | \  
           / | \                          |    
             |                            |    
             |                            |    
             |                            |''')
    Password015 = "ASDFGHJKL1234567890"
    passwordlen15 = 4
    password543 = "".join(random.sample(Password015, passwordlen15))
    Sy_File = ".txt"
    all1 = password543 + Sy_File
    print(Color + '''[+] insta : t8qu_ & 00017z''')
    print(Color+"Coded By OpHacker")

    IP_TARGET = input("[+] Enter Your Proxy file : ")

    file = IP_TARGET

    Prox = open(file, "r")

    for Proxy in Prox:
        try:
            Req = requests.get("https://ipinfo.io/" + Proxy)
            if ('    "message": "Please provide a valid IP address"') in Req.text:
                print(Red + "[-] IS OFLINE ---> ", Proxy)
            else:
                f = open(all1, "a")
                f.write(Proxy)
                f.close()
                print(Color + "[+] IS ONLINE ---> ", Proxy)
        except:
            print(" You Have Error ")
    print(Red+"------/------")
    print(Color+"ONLINE IP SAVED HERE ---> ", all1)
    Ag = input(Color+"[+] again y/n : ")
    if Ag == "y":
        Tool()
    if Ag == "n":
        print(Color+"GoodBay...")
        sleep(3)
        exit()
    else:
        print(Red+" You Have Error ")
Tool()