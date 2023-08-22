#caesar cipher
#just looking to try out some ideas here and there
letters = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def text():
    text = input("message : ")
    text = text.lower()

    encode = int(input("number of sHuFFle : "))
    if encode == 0:     #for a  number bigger than 26, i'll just use the modulo for the shifts
        while encode == 0:
            encode = int(input("that is not secure or close...how much scramble"))
    data1 = (text, encode)



