def decode(encoded):
    c = ""
    lines = encoded.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("begin") or line.startswith("end") or not line:
            continue
        g = (ord(line[0]) - 32) & 63
        for h in range(1, len(line), 4):
            if h + 3 >= len(line):
                break
            i = (ord(line[h]) - 32) & 63
            j = (ord(line[h + 1]) - 32) & 63
            k = (ord(line[h + 2]) - 32) & 63
            l = (ord(line[h + 3]) - 32) & 63
            c += chr((i << 2) | (j >> 4))
            if h + 2 < len(line) - 1:
                c += chr(((j & 15) << 4) | (k >> 2))
            if h + 3 < len(line) - 1:
                c += chr(((k & 3) << 6) | l)
    return c[:g]

# decode password
encoded_password = "G9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*"
decoded_password = decode(encoded_password)
print(decoded_password)
