def tri_recu(k):
  if(k>0):
    result = k+tri_recu(k-1)
    print(result)
  else:
    result = 0
  return result



tri_recu(5)


reduce 