from jkpy.modul import jkfunk as jk

jk.saghallo()

x,y=jk.addmule(3,4)
xt,yt=jk.addmult(5,6)
xl,yl=jk.addmull(2,8)
l=jk.addmull(22,5)
t=jk.addmull(21,3)

print(f"einz. sum: {x}  prod: {y}")
print(f"tupel sum: {xl}  prod: {yl}")
print(f"liste sum: {xt}  prod: {yt}")
print(f"tupel sum: {t[0]}  prod: {t[1]}")
print(f"liste sum: {l[0]}  prod: {l[1]}")

print(f"Version: {jk.version}  ")
