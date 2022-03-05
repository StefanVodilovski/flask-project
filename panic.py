phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
second_phrase=['o','n','t','a','p']
for i in phrase:
    if i not in second_phrase:
        plist.remove(i)
plist.pop(5)
plist.insert(2,' ')
plist.extend([plist.pop(),plist.pop()])
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)