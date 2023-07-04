import csv

def read_tsvfile(filename):
    with open(filename, encoding='cp850') as file:
        tsvfile = csv.reader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
        data = []
        for row in tsvfile:
            entry = {
                'documentId': row[0],
                'termIri': row[1],
                'conceptLabel': row[2],
                'matchedText': row[3],
                'group': row[4].strip(),
                'tags': row[5],
                'sentenceId': row[6],
                'text': row[7],
            }
            data.append(entry)
        return data
