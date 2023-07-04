import pickle

def out_wrt(diseaseSymptomDict,SlotDict,rlDict,CondDiseaseSymptomDict):

    with open('co-occurance_group1.txt', 'w') as fileo:
        for key, value in diseaseSymptomDict.items():
            fileo.write(key + '\t' + str(value) + '\n')
    fileo.close()

    filename = 'slot_set_group1.p'
    outfile = open(filename, 'wb')
    pickle.dump(SlotDict, outfile)
    outfile.close()

    with open('disease_symptom_file_group1.txt', 'w') as fileo:
        for key, value in rlDict.items():
            fileo.write(key + '\t' + str(value) + '\n')
    fileo.close()
    with open('disease_symptom_file_group1.p', 'wb') as fl:
        pickle.dump(rlDict, fl)
    # outfile.close()

    print("--------------------------------------------------")
    for keyd, valued in CondDiseaseSymptomDict.items():
        print("Conditional probability of", keyd, ":", valued)
