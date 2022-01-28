def f(p1, p2):
    print(p1, p2)
    
d = dict(p2=2, column=None)

f(p1=1, **d)