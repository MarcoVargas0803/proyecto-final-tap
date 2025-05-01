def desvielado(km):
    if km <= 15000:
        return 20000
    elif km == 30000:
        return 30000
    elif km == 45000:
        return 40000
    elif km == 60000:
        return 45000
    elif km == 75000:
        return 50000
    elif km == 90000:
        return 50000
    else:
        return 60000

def caja_automatica(km):
    if km <= 15000:
        return 1500
    elif 15000 < km < 45000:
        return 4000
    elif km == 60000:
        return 5000
    elif 75000 <= km < 90000:
        return 8000
    else:
        return 9000

def caja_manual(km):
    if km <= 15000:
        return 1000
    elif 15000 < km < 45000:
        return 2000
    elif 60000 <= km < 90000:
        return 3000
    else:
        return 4000

def motor(km):
    if km <= 15000:
        return 2000
    elif 15000 < km < 30000:
        return 3500
    elif km == 45000:
        return 4000
    elif km == 60000:
        return 5000
    elif 75000 <= km < 90000:
        return 5500
    else:
        return 6000

def llanta_ponchada(km):
    if km <= 15000:
        return 200
    elif 15000 < km < 90000:
        return 300
    else:
        return 350

def fallas_filtros(km):
    if km <= 15000:
        return 699
    elif km == 30000:
        return 789
    elif km == 45000:
        return 900
    elif km == 60000:
        return 1550
    elif 75000 <= km < 90000:
        return 2500
    else:
        return 3900

def fallas_bateria(km):
    if km <= 15000:
        return 2000
    elif 15000 < km < 30000:
        return 3500
    elif km == 45000:
        return 5000
    elif km == 60000:
        return 6000
    elif 75000 <= km < 90000:
        return 6800
    else:
        return 9000