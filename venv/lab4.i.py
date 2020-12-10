n=input()
language = set()
dict = dict()
i = 0
while i < int(n):
    language = input().split()
    dict[i] = set(language)
    i+=1
inters = {'eng', 'ua', 'deu', 'jap'}
i = 0
while i < int(n):
    inters = inters.intersection(dict[i])
    i+=1
print(inters)
language2=set()
i=0
while i<int(n):
    language2=language2.union(dict[i])
    i+=1

print(language2.difference(inters))
