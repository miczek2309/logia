
def liczba_3_cyfrowa(cyfra):
   a = cyfra // 100
   cyfra = cyfra - 100 * a
   b = cyfra // 10
   cyfra = cyfra - 10 * b
   c = cyfra // 1
   if a > b:
      if a > c:
         return a
      else:
         return c
   else:
      if b > c:
         return b
      else:
         return c
      
print(liczba_3_cyfrowa(886))

