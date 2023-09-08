def poziom_ryzyka(wiek, plec, wyksztalcenie):
    if wiek > 17 and wiek < 30:
        return 5
    elif plec.lower() == 'm':
        return 4
    else:
        return 3