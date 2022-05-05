
import googlesearch
import requests

print ("Inserisci la ricerca di cui scaricare i PDF")
query = input()

request = googlesearch.search (query + ":PDF", num_results=5, lang="it")
i = 0

for r in request:
    
    print (r)
    response = requests.get(r)
    
    i = i + 1
    print (query + str(i) + ".pdf")
    
    open (query + str(i) + ".pdf", "wb").write(response.content)