phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist= plist[1:8:1]
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
temp=plist[2]
plist[2]=plist[3]
plist[3]=temp
new_phrase= ''.join(plist)
print(plist)
print(new_phrase)