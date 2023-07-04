#symptomDictionary includes the symptoms as keys and the number of each symptoms as values.
#symDictionary includes the symptoms that are pair with diseases. It's format is suitable with the format that used
#in RL.

def count_symptomsanddiseases(data):
    cnt = 0
    symptoms = []
    symDictionary = {}

    diseaseSymptomDict = {}
    documentKeyDict = {}

    symptomDictionary = {}
    symptomDocumentDictionary = {}

    diseaseDictionary = {}
    diseaseDocumentDictionary = {}

    for idx, tup in enumerate(data):
        documentId = tup['documentId']
        keySymptom = ''
        keyDisease = ''

        if tup['group'] == "<http://purl.obolibrary.org/obo/SYMP_0000462>":
            keySymptom = tup['conceptLabel']
            keySymptomDocument = keySymptom + ';' + documentId
            if keySymptomDocument not in symptomDocumentDictionary:
                if keySymptom not in symptomDictionary:
                    symptomDictionary[keySymptom] = 1
                else:
                    countSym = symptomDictionary.get(keySymptom) + 1
                    symptomDictionary[keySymptom] = countSym
                symptomDocumentDictionary[keySymptomDocument] = ""
        elif tup['group'] != "<http://purl.obolibrary.org/obo/SYMP_0000462>":
            keyDisease = tup['conceptLabel']
            keyDiseaseDocument = keyDisease + ';' + documentId
            if keyDiseaseDocument not in diseaseDocumentDictionary:
                if keyDisease not in diseaseDictionary:
                    diseaseDictionary[keyDisease] = 1
                else:
                    countDis = diseaseDictionary.get(keyDisease) + 1
                    diseaseDictionary[keyDisease] = countDis
                diseaseDocumentDictionary[keyDiseaseDocument] = ""
        if idx <= len(data) - 2:

            documentId = tup['documentId']
            # print(documentId)
            innerIdx = idx
            key = ''
            # print(tup['group'], data[innerIdx+1]['group'])
            if tup['group'] == "<http://purl.obolibrary.org/obo/SYMP_0000462>" and data[idx + 1][
                'group'] != "<http://purl.obolibrary.org/obo/SYMP_0000462>":
                key = data[innerIdx + 1]['conceptLabel'] + ';' + tup['conceptLabel']
                if tup['conceptLabel'] not in symptoms:
                    cnt = cnt + 1
                    # print(cnt)
                    symptoms.append(tup['conceptLabel'])
                    symDictionary[tup['conceptLabel']] = cnt

                else:
                    cnt = cnt
            elif tup['group'] != "<http://purl.obolibrary.org/obo/SYMP_0000462>" and data[innerIdx + 1][
                'group'] == "<http://purl.obolibrary.org/obo/SYMP_0000462>":
                key = tup['conceptLabel'] + ';' + data[innerIdx + 1]['conceptLabel']
                if data[innerIdx + 1]['group'] not in symptoms:
                    cnt = cnt + 1
                    # print(cnt)
                    symptoms.append(data[innerIdx + 1]['group'])
                    symDictionary[data[innerIdx + 1]['group']] = cnt

                else:
                    cnt = cnt
            else:
                innerIdx += 1
                continue

            innerIdx += 1
            keyDocument = documentId + ';' + key
            if keyDocument in documentKeyDict:
                continue
            else:
                documentKeyDict[keyDocument] = keyDocument
                if key in diseaseSymptomDict:
                    count = diseaseSymptomDict.get(key) + 1
                    diseaseSymptomDict[key] = count
                else:
                    diseaseSymptomDict[key] = 1
    # print("symptomdictionary--------------")
    # print(symptomDictionary)
    # print("symdictionary-----------------------------------------")
    # print(symDictionary)
    # slot set (saving as p file) tüm semptomları yazdırma
    # filename = 'slot_set_group19.p'
    # outfile = open(filename, 'wb')
    # pickle.dump(symDictionary, outfile)
    # outfile.close()
    return symptomDictionary, diseaseDictionary, diseaseSymptomDict
