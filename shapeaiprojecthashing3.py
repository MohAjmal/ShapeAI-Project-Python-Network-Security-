#Program to hash given input using three different algorithms

#importing required module
import hashlib

#defining function
def hashing3() :
    
    #acceping string to be hashed and encoding
    string = input(str("Enter the string to be hashed: ")).encode("utf-8")
    
    #assigning fuctions to variable
    m = hashlib.md5()
    b = hashlib.blake2b()
    s = hashlib.sha256()

    #updating or hashing the strings
    m.update(string)
    b.update(string)
    s.update(string)

    #printing the output
    print("MD5 converted string for the given input: ",m.hexdigest())
    print()
    print("BLAKE2B converted string for the given input: ",b.hexdigest())
    print()
    print("SHA256 converted string for the given input: ",s.hexdigest())

#function call
hashing3()

