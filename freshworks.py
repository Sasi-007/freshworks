import threading 
from threading import*
import time

d={}

def create(key,value,timeout=0):
    if key in d:
        print("Already exists.Try with another key-pair") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Please enter small data(Memory exceeded)")
        else:
            print("Key doesn't allow rather than alphabets")
            
def read(key):
    if key not in d:
        print("Enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("Expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

def delete(key):
    if key not in d:
        print("Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del d[key]
                print("Deleted")
            else:
                print("Expired") 
        else:
            del d[key]
            print("Deleted")
