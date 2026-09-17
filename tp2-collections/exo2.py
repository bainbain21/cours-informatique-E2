classDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

#1 afficher le nom des eleves :
print(classDict["class"]["student"]["name"])

#2 changer la note de mike
classDict["class"]["student"]["marks"]["physics"]=89

#3 ajout de la moyenne
classDict["class"]["student"]["average"]=(classDict["class"]["student"]["marks"]["physics"]+classDict["class"]["student"]["marks"]["history"])/2
# ou 
# classDict["class"]["student"]["average"]=sum(marks.values())/len(marks) 
# avec marks = classDict["class"]["student"]["marks"]

#4 on transforme student en liste
classDict['class']['student']=[{'name':'Mike','marks': {'physics':89, 'history':80}}]

#5 on ajoute Ted
classDict['class']['student'].append({'name':'Ted','marks':{'physics':34,'history':99}})

#6 on calcul la moyenne de Mike et Ted (en rajoutant de nouveau la class average)
marksM = classDict['class']['student'][0]["marks"]
marksT= classDict['class']['student'][1]["marks"]
classDict['class']['student'][0]['average']=sum(marksM.values())/len(marksM)
classDict['class']['student'][1]['average']=sum(marksT.values())/len(marksT)

#7 ajout d'une moyenne de classe
classDict['class']['average_grade']=sum(s['average'] for s in classDict['class']['student'])/len(classDict['class']['student'])

#8 on affiche le tableau complet
print(classDict)