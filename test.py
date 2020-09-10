import netflixtitles as nt
totlenght = 0


nt.setup()

for row in nt.data:
    name = row.get('director')
    totlenght += len(name)

print(totlenght/ len(nt.data))
