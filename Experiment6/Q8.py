d={'a':2,'b':2,'c':2}
unique=lambda d:len(set(d.values()))==1
print(unique(d))