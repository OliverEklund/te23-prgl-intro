svar = input("Skriv ett tal: ")
x = float(svar)
y = x * x
print(f"Talet i kvadrat är: {y:.2f}")

print(f"Visst var det där inte coolt?")
åsikt = input("Ja eller Nej: ")
if åsikt == "Nej":
    print(f"Se till att sova med ett öga öppet asså")
if åsikt == "nej":
    print(f"Jag kommer att komma till dit hus inatt")
if åsikt == "Ja":
    print(f"Tack så mycket :D")
if åsikt == "ja":
    print (f"VAR MER TACKSAM ELLER SÅ ÄR DET ÖVER lil skit!")
    sanningen = input("VISST VAR DET KANSKA COOLT ELLER HUR!?")
    if sanningen == "JA":
        print (f"EXAKT!")
    else:
        print(f"DET ÄR ÖVER MED DIG DIN LÖGNANDE ORM!")
else:
    print (f"......")