import math
from collections import defaultdict
from operator import itemgetter


def conditional_probability(diseaseSymptomDict, WDiseaseSymptomDict, diseaseList):
    rlsymptomDict = defaultdict(dict)

    for keyCp, valueCp in diseaseSymptomDict.items():
        diseaseCp = keyCp.split(';')[0]
        symptomCp = keyCp.split(';')[1]

        rlsymptomDict[diseaseCp][symptomCp] = WDiseaseSymptomDict[keyCp]
    print("rlsymptomdict")
    print(rlsymptomDict)

    index = 0
    rlDrl_dict = defaultdict(dict)

    CondDiseaseSymptomDict = {}
    countslot = 0
    SlotDict = {}
    i = 0
    for diseaseElement in diseaseList:
        condProb = 0

        for keyCD, valueCD in diseaseSymptomDict.items():
            disease1 = keyCD.split(';')[0]
            symptom1 = keyCD.split(';')[1]
            # print(type(rlsymptomDict[disease1][symptom1]))

            if disease1 == diseaseElement:

                if symptom1 in rlsymptomDict[disease1] and rlsymptomDict[disease1][symptom1] > 0.01:
                    # Add the symptom and its index to the rlDrl_dict dictionary
                    rlDrl_dict[disease1]['index'] = index
                    rlDrl_dict[disease1]['symptom'] = rlsymptomDict[disease1]


                    # Add the symptom to SlotDict if it's not already there
                    if symptom1 not in SlotDict:
                        SlotDict[symptom1] = i
                        i += 1

                    # Check if the current symptom has a larger probability than the 12th largest value
                    symptom_prob = rlsymptomDict[disease1][symptom1]

                    #if symptom_prob > 0.01:
                            # sorted(rlDrl_dict[disease1]['symptom'].values(), reverse=True)[0]
                            # If the symptom has a larger probability than the 12th largest value, add it to the dictionary

                        # If the dictionary has more than 12 symptoms, remove the smallest one
                        #length =len(rlDrl_dict[disease1]['symptom'])
                        #print(length)
                        #if len(rlDrl_dict[disease1]['symptom']) > 12:
                        #smallest_symptom = min(rlDrl_dict[disease1]['symptom'],
                         #                              key=rlDrl_dict[disease1]['symptom'].get)
                        #del rlDrl_dict[disease1]['symptom'][smallest_symptom]

        index += 1
        condProb = condProb + math.log10(0.25)
        CondDiseaseSymptomDict[diseaseElement] = condProb

    for key2, value2 in rlDrl_dict.items():
        print(key2)

        symptoms = rlDrl_dict[key2]['symptom']
        sorted_symptoms = dict(sorted(symptoms.items(), key=lambda x: x[1], reverse=True))

        top_12_symptoms = dict(list(sorted_symptoms.items())[:12])

        sum_values = sum(top_12_symptoms.values())

        normalized_symptoms = {k: v / sum_values for k, v in top_12_symptoms.items()}

        rlDrl_dict[key2]['symptom'] = normalized_symptoms

    return SlotDict, rlDrl_dict, CondDiseaseSymptomDict
