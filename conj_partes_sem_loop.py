def termo_01(n, comeco, fim):
  if comeco < len(n):
    if fim < len(n):
      print(n[comeco:fim + 1]) #printa o comeco + o fim + 1 recursivando
      termo_01(n, comeco, fim + 1)
    else:
      termo_01(n, comeco + 1, comeco + 1) #rechama a funcao com o index inicio 1 e fim 1

n = "PNEUMOULTRA"
termo_01(n, 0, 0) # tenho que comecar com o inicio do index 0 e o fim com o index 0