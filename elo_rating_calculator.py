from math import pow

#risultatoPartita: 0(sconfitta), 0.5(pareggio), 1(vittoria)
def calcoloPunteggioElo(punteggioA, punteggioB_avversario,risultatoPartita):
  k = 32
  punteggioAtteso = 1 / (1 + pow(10, (punteggioB_avversario - punteggioA) / 400))
  nuovo_punteggio = punteggioA + k * (punteggioAtteso - risultatoPartita)
  return nuovo_punteggio

def testPartite(punteggioA):  #ELO iniziale del giocatore A
    #Test 5 partite
    risultatoPartite = [0, 1, 0.5, 1, 0]
    ELO_avversari = [1700, 1577, 1388, 1620, 1710]

    for i in range(5):   #Si aggiorna l'ELO
     punteggioA= calcoloPunteggioElo(punteggioA,ELO_avversari[i],risultatoPartite[i])
     print("ELO dopo la partita",i+1,":",punteggioA)

punteggioA=1580
print("ELO giocatore A:",punteggioA)
testPartite(punteggioA)