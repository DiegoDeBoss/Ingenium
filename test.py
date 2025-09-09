nome = input("Inserisci il tuo nome ")
eta = int(input("Inserisci la tua età "))


if eta<18:
    print("Benvenuto ",nome+"!")
    print("purtroppo non puoi accedere, sei minorenne.")
else:
    print("Benvenuto ",nome+"!")
    print("Hai", eta,"anni e di conseguenza puoi accedere.")
