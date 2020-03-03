N = int(input())
hh,hhmod = divmod(N,3600) 
mm,ss = divmod(hhmod,60)
print(str(hh).zfill(2),":",str(mm).zfill(2),":",str(ss).zfill(2),sep='')