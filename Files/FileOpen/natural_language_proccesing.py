f=open("demo1","r")
names=set()

dict={}
stopwords=["the","where","is","have","with","that","had","of","you","to","a"]
print(stopwords)
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word in stopwords:
            pass
        else:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
print(dict)
print(max(dict,key=dict.get))