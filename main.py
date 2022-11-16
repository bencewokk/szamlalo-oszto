osztosz = ("igen")
megoldas=[]
megoldas2=[]
clear=[]

while True:
    elsoszam = int(input("elso szam? "))
    masodiksz = int(input("masodik szam?"))


    if elsoszam < masodiksz:
        x=1
        masodiksz+=1
    else:
        x=-1
        masodiksz-=1

    for i in range(elsoszam, masodiksz, x):
        megoldas.append(i)


    while osztosz==("igen"):
        print(megoldas)
        osztosz=input("kell oszto? (igen/nem)")
        if osztosz!="igen":
            print(megoldas)
            break
        else:
            oszto=int(input("mivel osszuk? "))
            for i in megoldas:
                if i%oszto==0:
                    megoldas2.append(i)


        megoldas.clear()
        megoldas=megoldas2
        megoldas2=clear


