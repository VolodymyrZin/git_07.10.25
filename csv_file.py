import csv


with open('random-michaels.csv', 'r') as f:
    reader1 = list(csv.reader(f))
header1 = reader1[0]
body1 = reader1[1:]
rows_updated1 = [dict(zip(header1, row)) for row in body1]

with open('random.csv', 'r') as f:
    reader2 = list(csv.reader(f))
header2 = reader2[0]
body2 = reader2[1:]
rows_updated2 = [dict(zip(header2, row)) for row in body2]

def common_list(rows_updated1, rows_updated2):
    unique_rows = []
    unique_check = set()

    for row in rows_updated1 + rows_updated2:
        row_tuple = tuple(row.items())
        if row_tuple not in unique_check:
            unique_check.add(row_tuple)
            unique_rows.append(row)
    return unique_rows


with open('merged.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=header1)
    writer.writeheader()
    writer.writerows(common_list(rows_updated1, rows_updated2))


result = common_list(rows_updated1, rows_updated2)
print(result)





