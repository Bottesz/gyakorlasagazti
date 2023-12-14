import pogyasz1

print("III/A,B:")
csomag_list=pogyasz1.fajlbeolvasas()
print(f"\t A pogyászok száma {len(csomag_list)}")
atlag=pogyasz1.pogyasz_atlagsuly(csomag_list)
print(f"Az első csomag szélessége : {csomag_list[0].a} ?")

print("III/C:")
print(f"\t Az 51cm-es pogyászok átlag súlyértéke: {round(atlag,2)} :g")


print("III/D:")
magas=pogyasz1.pogyasz_atlagsuly(csomag_list)
max_index=pogyasz1.legmagasabb(csomag_list)
print(f"\t A legmagasabb pogyász méretei: {csomag_list[max_index]}")
print(f"legmagasabb pogysz méretei: {magas[0],magas[1]magas[2],magas[3]")
