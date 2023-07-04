import pickle
from func.conditional_prob import conditional_probability
from func.count_symptoms_and_diseases import count_symptomsanddiseases
from func.read_tsv_file import read_tsvfile
from func.weight_calculations import weight_calculation
import math
from collections import defaultdict

filename = 'group19_changed.tsv'
data = read_tsvfile(filename)
symptomDictionary, diseaseDictionary, diseaseSymptomDict = count_symptomsanddiseases(data)
WDiseaseSymptomDict, WSymptomDiseaseDict,diseaseList = weight_calculation(diseaseSymptomDict, symptomDictionary, diseaseDictionary)
SlotDict,rlDict, CondDiseaseSymptomDict = conditional_probability(diseaseSymptomDict, WDiseaseSymptomDict, diseaseList)


"""
rlsymptomDict = defaultdict(dict)

for keyCp, valueCp in diseaseSymptomDict.items():
    diseaseCp = keyCp.split(';')[0]
    symptomCp = keyCp.split(';')[1]
    rlsymptomDict[diseaseCp][symptomCp] = WDiseaseSymptomDict[keyCp]
#print("rlsymptomdict")
#print(rlsymptomDict)

index = 0
rlDict = defaultdict(dict)

CondDiseaseSymptomDict = {}
SlotDict = {}
i = 0
for diseaseElement in diseaseList:
    condProb = 0

    for keyCD, valueCD in diseaseSymptomDict.items():
        disease1 = keyCD.split(';')[0]
        symptom1 = keyCD.split(';')[1]

        if disease1 == diseaseElement:

            #if statement probabiltyleri 0.01den küçük olan semptomları çıkarmak için eklendi
            if rlsymptomDict[disease1][symptom1] >= 0.01:
                print("değer o.01den küçük")
                print(rlsymptomDict[disease1][symptom1])
                condProb += (WDiseaseSymptomDict[keyCD])
                rlDict[disease1]['index'] = index
                rlDict[disease1]['symptom'] = rlsymptomDict[disease1]
                rlDict[disease1]['symptom'][symptom1] = rlsymptomDict[disease1][symptom1]
                print(rlDict[disease1]['symptom'])
                while(i <121):
                    if symptom1 not in SlotDict:
                        #print("Adding symptom to SlotDict")
                        SlotDict[symptom1] = i
                        i += 1
                    else:
                        #print("Symptom already in SlotDict")
                        i = i
                        break

    index += 1

    condProb = condProb + math.log10(0.25)
    CondDiseaseSymptomDict[diseaseElement] = condProb
"""
with open('co-occurance_group19_limited-----.txt', 'w') as fileo:
    for key, value in diseaseSymptomDict.items():
        fileo.write(key + '\t' + str(value) + '\n')
fileo.close()

print("SlotDict*---------------------")
print(SlotDict)

print("-------------------------------------------------")
for kd, vl in rlDict.items():
    print(kd, rlDict[kd])
print(len(SlotDict))
#filename = 'slot_set_group19_limited.p'
#outfile = open(filename, 'wb')
#pickle.dump(SlotDict, outfile)
#outfile.close()
with open('slot_set_group19_limited-----.txt', 'w') as fil:
    for key, value in SlotDict.items():
        fil.write(key + '\t' + str(value) + '\n')
fil.close()

with open('disease_symptom_file_group19_limited-----.txt', 'w') as fileo:
    for key, value in rlDict.items():
        fileo.write(key + '\t' + str(value) + '\n')
fileo.close()
# filename = 'disease_symptom_file'
# outfile = open(filename, 'wb')
with open('disease_symptom_file_group19_limited----.p', 'wb') as fl:
    pickle.dump(rlDict, fl)
# outfile.close()
"""
print("--------------------------------------------------")
for keyd, valued in CondDiseaseSymptomDict.items():
    print("Conditional probability of", keyd, ":", valued)
"""