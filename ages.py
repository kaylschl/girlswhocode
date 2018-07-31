names = {
"Cindy" : 49,
"Kent" : 60,
"Aaron" : 20,
"Rosie" : 9,
"Jordan" : 17,
"Delaney" : 16,
"Rachel" : 17,
"Kayla" : 17,
"Gma G" : 70,
"Gma R" : 95,
"Josh" : 37,
"Tom" : 22,
}
y = 0
for k,v in names.items():
    y += v
avg = y/len(names)
print(avg)

print(sum(names.values())/len(names))
