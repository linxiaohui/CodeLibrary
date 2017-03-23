def flat_list(a):
  r=[]
  for i in a:
    if isinstance(i,int):
      r.append(i)
    else:
      r.extend(flat_list(i))
  return r