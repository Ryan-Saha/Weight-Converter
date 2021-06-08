#when it asks for kg or lbs but lowercase l or k
weight = input("Weight: ")
kg_or_lbs = input("(K)g or (L)bs: ")
l = 'l'
k = 'k'
if kg_or_lbs == l:
    print("Weight in Kg: " + str(float(weight) * 0.45))
elif kg_or_lbs == k:
    print("Weight in Lbs: " + str(float(weight) / 0.45))
