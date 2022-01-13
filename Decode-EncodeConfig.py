key = 121

def toHex(d):
    return ("0" + (str(int(d)))[-2:]).upper()
    
def decode(text):
    done = ""
    text = text.split('\n')
    for a in range(len(text)):
        if text[a].find("=") != -1:
            done += text[a][:text[a].index("=")] + "="
            enc = text[a][text[a].index("=") + 1:].split(" ")
            for b in range(len(enc)):
                done += chr(key ^ int(enc[b], 16))
            done += "\n"
        else:
            done += text[a] + "\n"
    return done
    
def encode(text):
    done = ""
    text = text.split('\n')
    for a in range(len(text)):
        if "=" in text[a]:
            done += text[a][:text[a].index("=")] + "="
            dec = text[a][text[a].index("=") + 1:]
            for b in range(len(dec)): done += toHex(ord(dec[b]) ^ key)
            done += "\n"
        else: done += text[a] + "\n"
    return done
    
if __name__ == "__main__":
    file = open("UserCostume.ini", "rb").read()
    decoded = decode(file)
    print("Decoded File : " + decoded)
    encoded = encode(decoded)
    file1 = open("encode.ini", "wb").write(encoded)