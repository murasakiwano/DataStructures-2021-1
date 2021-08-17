# Implementação da simulação de Batata Quente.
# Também pode ser considerada uma versão do problema clássico Flavius Josephus.

from DataStructuresChapter3.Queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Jojo", "Lulu", "Diego", "Mixirica", "Ismael", "Vinius"], 9))