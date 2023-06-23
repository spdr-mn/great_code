def funkcia(h):
    f=h//30.48
    d=(h-(f*30.48))//2.54
    return(round(f),round(d))

##print(type(funkcia(170)))
