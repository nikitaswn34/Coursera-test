x = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#print (x)
#x = x.replace("k", "m")
#x = x.replace("o", "q")
#x = x.replace("e", "g")
if "k" in x:
    i1 = x.index("k", 1)
    print (i1)
    x1 = x[i1:]
    if "m" in x1:
        i2 = x1.index("m", 1)
        print (i2)
        x2 = x1[i2:]
for i in range(52,len(x),12):
    print (x[i])
print (x1)
print (x2)

