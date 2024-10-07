import csv

def get_lookup_table(lookup_file):
    lookup = {}
    with open(lookup_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dstport = int(row['dstport'])
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup[(dstport, protocol)] = tag
    return lookup
