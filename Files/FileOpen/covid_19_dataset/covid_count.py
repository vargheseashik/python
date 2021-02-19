f=open("covid_19_india(1).csv","r")
dict={}
for data in f:
    #1,30/01/20,6:00 PM,Kerala,1,0,0,0,1
        words=data.rstrip("\n").split(",")
        states=words[3]
        cofirmed_case=words[-1]
        if states not in dict :
            dict[states]=cofirmed_case
        else:
            dict[states]=cofirmed_case


for k,v in dict.items():
    print(k,v)
    print(max(dict,key=dict.get))