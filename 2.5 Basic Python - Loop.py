d = 9
while (d < 100):
    g = 2
    print(d/g)
    while (g < (d/g)):
         print('loop in loop')
         g = g + 1
         d = d + 1
print("Done")

for reb in "Strong":
     if reb == "n":
          continue
     print(reb)