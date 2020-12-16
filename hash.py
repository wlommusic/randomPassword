import hashlib
def do_md5(string=None):

    if string == None:
        return "please enter a string"
    else:
        return hashlib.md5(str(string).encode()).hexdigest()[0:16]


