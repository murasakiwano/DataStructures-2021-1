# Programação dinâmica
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
    
def main():
    amnt = 10
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Fazendo troco para", amnt, "requer")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "moedas")
    print("Elas são:")
    printCoins(coinsUsed, amnt)
    print("Lista de moedas usadas:")
    print(coinsUsed)

main()
