lst=[3,4,6,7,8]
elist=list()
olist=list()
for i in  lst:
    if (i % 2 == 0):
        elist.append(i)
    else:
        olist.append(i)
print("even list is ",elist)
print("odd list is ",olist)


