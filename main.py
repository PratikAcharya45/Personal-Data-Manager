import os

import time
passkey=list(time.strftime("%H %M").strip())
passkey.remove(" ")
pcode="".join(passkey)
print(pcode)

from getpass import getpass


def authorize(pcode):
    loginp=getpass("")
    if loginp=="helloworld"+pcode:
        purpose=input("You wanna view the data or add?\n")
        if(purpose.lower()=="view"):
            view()
        elif(purpose.lower()=="add"):
            add()
        else:
            print("Not a valid option.")
def add():
    with open("D:\\Python\\Projects\\Personal Data Manager\\info.txt","a") as f:
        domain_name=input("Website Name : ")
        f.write(f"\n{domain_name}:")
        info={}
        req_info=list(map(str,input("Enter required info : ").split(" ")))
        for i in req_info:
            info[i]=input(f"Enter {i} :")
        for keys in info:
            k=f"{keys} = {info[keys]}_"
            f.write((k))
def view():
    rdomain_name=input("Website Name : ").upper()
    with open("D:\\Python\\Projects\\Personal Data Manager\\info.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            domain_name,req_info=line.split(":")
            domain_name=domain_name.upper()
            if(domain_name==rdomain_name):
                infos=req_info.split("_")
                os.system("cls")
                print(domain_name.center(60))
                for info in infos:
                    print(info)
                break
os.system("cls")
authorize(pcode)
