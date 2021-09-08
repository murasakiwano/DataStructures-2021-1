table_of_results = {}

def descartar(cards):
    desc_first = pontuar(cards[1:])
    desc_last = pontuar(cards[:-1])
    return max(desc_first, desc_last)

def pontuar(cards):
    if str(cards) in table_of_results:
        return table_of_results[str(cards)]
    if len(cards) <= 2:
        return max(cards)
    pontua_first = cards[0] + descartar(cards[1:])
    pontua_last = cards[-1] + descartar(cards[:-1])
    table_of_results[str(cards)] = max(pontua_first, pontua_last)
    return table_of_results[str(cards)]

N = int(input())
cards = [int(x) for x in input().split()]

print(pontuar(cards))