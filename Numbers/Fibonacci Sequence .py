'''
name =fibonacci sequnce
accept the last numper place and generate fibonacci sequnce up to the the last number
'''
ans= [0,1]
start=2
theLastPlacce=int(input("the last fibonacci sequnce place: "))


while start < theLastPlacce:
    seq= ans[start-2] + ans[start-1]
    ans.append(seq)
    start +=1
print(ans)
 