with open('normalized-data.csv', 'r') as r, open('normalized-data.csv', 'w') as w:
    data = r.readlines()
    header, rows = data[0], data[1:]
    random.shuffle(rows)
    rows = '\n'.join([row.strip() for row in rows])
    w.write(header + rows)
