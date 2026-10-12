t1= (1,2,5,7,9,2,4,6,8,10)

#a. Print contents of t1 in two separate lines
half=len(t1) // 2
print("First half of tl:", t1[:half])
print("Second half of tl:", t1[half:])

#b.Print all even values of tl as another tuple t2
t2=tuple(x for x in t1 if x % 2 == 0)
print("Tuple of even values (t2):", t2)

#c.Concatenate a new tuple with t1
t3=(11, 13, 15)
concatenated=t1+t3
print("Concatenated tuple (t1 + t3):", concatenated)

#d. Return max and min from t1
print("Maximum value in tl:", max(t1))
print("Minimum value in tl:", min(t1))
