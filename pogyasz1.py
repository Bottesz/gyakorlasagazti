from Csomag import Csomag
"""fáljbeolvasás"""

def fajlbeolvasas():
    fajl=open("csomag.txt","r",encoding="UTF-8")
    fajl.readline()
    fajlbol_sorok_lista=fajl.readlines()
    fajl.close()
    """
    1. megnyitom a fájlt olvasásra
    2.beolvasom a fejlécsort, ha van
    3.beolvasom az összes sort egy listába - string lista
    4.bezárom a fájlt
    5.Sorokat átalakítom objektumokká, szétszedem a benne levő adatokat
        1. létrehozom az osztályt amiben majd beolvasom az adatokat
        2.Végigmegyek a listán, és minden sorát feldolgozom
            1. eltüntetm a végéről az entert
            2. szétvágom a separatorok mentén
    """
    csomag_lista = []
    for i in range(0,len(fajlbol_sorok_lista),1):
        akt_elem=fajlbol_sorok_lista[i]
        sor_lista=akt_elem.strip().split("#") # ez az elválasztojel mentén szétválasztja az 
        a=int(sor_lista[0])
        b=int(sor_lista[1])
        c=int(sor_lista[2])
        m=int(sor_lista[3])
        csomag=Csomag(a,b,c,m)
        csomag_lista.append(csomag)
    return csomag_lista 

def pogyasz_atlagsuly(lista):
    ossz:int = 0
    szamlalo:int = 0
    for i in range(0,len(lista),1):
        if (lista [i].a==51):
            ossz += lista[i].m
            szamlalo += 1
    return 1000*ossz/szamlalo


def legmagasabb():
    magas = 0 
    adat= 0
    for i in range(0(len(lista),1):
                   magas = lista[i].b 
                    adat = lista[i].a, lista[i].b, lista[i].c, lista[i].m