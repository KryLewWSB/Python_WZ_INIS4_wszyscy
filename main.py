print("Podaj roczny przychod (brutto): ")
wprowadzonaWartosc = int(input())

if(wprowadzonaWartosc < 120_000):
    print(f"Wprowadziłeś przychod: {wprowadzonaWartosc} zł.\n"
          f"Musisz zapłacić: {wprowadzonaWartosc * 0.12} zł.\n")
else:
    pierwszyProg = 120_000 * 0.12
    drugiProg = (wprowadzonaWartosc - 120_000) * 0.32
    print(f"Wprowadziłeś przychod: {wprowadzonaWartosc} zł.\n"
          f"Musisz zapłacić w I progu podatkowym: {pierwszyProg} zł.\n"
          f"Musisz zapłacić w II progu podatkowym: {drugiProg} zł.\n"
          f"Ogół podatku: {pierwszyProg + drugiProg}\n")




