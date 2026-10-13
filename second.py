def cislo_text(cislo):
    hodnota = int(cislo)
    
    do_19 = [
        "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", 
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", 
        "sedmnáct", "osmnáct", "devatenáct"
    ]
    
    desitky = [
        "", "", "dvacet", "třicet", "čtyřicet", "padesát", 
        "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]

    if hodnota == 100:
        return "sto"
    if 0 <= hodnota < 20:
        return do_19[hodnota]
        
    desitka = hodnota // 10
    jednotka = hodnota % 10
    
    if jednotka == 0:
        return desitky[desitka]
        
    return f"{desitky[desitka]} {do_19[jednotka]}"


if __name__ == "__main__":
    vstup = input("Zadej číslo: ")
    if vstup.strip():
        print(cislo_text(vstup))
    else:
        print("Nezadal jsi žádné číslo.")