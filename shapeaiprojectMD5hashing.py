import hashlib
def md5converting() :
    string = input(str("Enter the string to convert to MD5: ")).encode("utf-8")
    m = hashlib.md5()
    m.update(string)
    print("MD5 converted string for the given input: ",m.hexdigest())
md5converting()
