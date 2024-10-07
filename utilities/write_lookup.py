import csv

data = [
    ['dstport', 'protocol', 'tag'],
    ['25', 'tcp', 'sv_P1'],
    ['68', 'udp', 'sv_P2'],
    ['23', 'tcp', 'sv_P1'],
    ['31', 'udp', 'SV_P3'],
    ['443', 'tcp', 'sv_P2'],
    ['22', 'tcp', 'sv_P4'],
    ['3389', 'tcp', 'sv_P5'],
    ['0', 'icmp', 'sv_P5'],
    ['110', 'tcp', 'email'],
    ['993', 'tcp', 'email'],
    ['143', 'tcp', 'email'],
]

with open('lookup_table.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print("lookup data saved to lookup_table.csv")
