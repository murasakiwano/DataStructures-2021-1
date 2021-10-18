def getElementById(raiz, id, lista=None):
    if lista is None:
        lista = []
    if type(raiz) == dict:
        l = searchId(raiz, id)
        if l not in lista:
            lista += l
        for key in raiz.values():
            getElementById(key, id, lista)
    
    return lista
    
    
def searchId(no, id): 
    k = []
    if '*' in id:
        i = len(id)
        for x in no.keys():
            if x[:i-1].lower() == id[:i-1].lower():
                k = [x]
    else:
        for x in no.keys():
            if x.lower() == id.lower():
                k = [x]
    return k

# raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'Cabeçalho', 'p': 'Parágrafo'}}}
# print(sorted(getElementById(raiz, 'H*')))

# raiz = {'HTML': {'HEAD': {'TITLE': 'Título'},'BODY': {'H1': 'header', 'P': 'Lorem', 'p': 'ipsum', 'div': {'P': 'wat?'}}}}
# print(sorted(getElementById(raiz, 'div')))
