import netflixtitles as nt

nt.setup()
for row in nt.data:
    totlenght = 0
    name = row.get('director')
    totlenght += len(name)
    print(totlenght)

print(totlenght/ len(nt.data))
