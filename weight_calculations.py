def weight_calculation(diseaseSymptomDict, symptomDictionary, diseaseDictionary):
    # A large weight of the ‘symptom_of’ relationship indicate the disease is an important source of the symptom
    # For example, acute myocardial infarction is an important cause of chest pain

    WSymptomDiseaseDict = {}
    for keyDS, valueDS in diseaseSymptomDict.items():
        symptom = keyDS.split(';')[1]
        WSymptomDiseaseDict[keyDS] = int(valueDS) / symptomDictionary[symptom]
    print('𝑤𝑠𝑦𝑚𝑝𝑡𝑜𝑚_𝑜𝑓')
    for wkey, wvalue in WSymptomDiseaseDict.items():
        print(wkey, wvalue)

    # A large weight of the ‘disease_of’ relationship indicate the symptom is an important manifestation of the disease.
    # For example, fever is an important symptom of influenza.

    WDiseaseSymptomDict = {}
    diseaseList = []

    for keyDS, valueDS in diseaseSymptomDict.items():
        disease = keyDS.split(';')[0]

        if disease not in diseaseList:
            diseaseList.append(disease)
        WDiseaseSymptomDict[keyDS] = int(valueDS) / diseaseDictionary[disease]
    print('𝑤𝑑𝑖𝑠𝑒𝑎𝑠𝑒_𝑜𝑓')
    for wkey, wvalue in WDiseaseSymptomDict.items():
        print(wkey, wvalue)

    return WDiseaseSymptomDict, WSymptomDiseaseDict,diseaseList
