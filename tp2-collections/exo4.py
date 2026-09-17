p = [10, 2, 'C', 'D', '+']

def calculScore(list):
    score = []
    for i in list:
        if type(i) == int:
            score.append(i)
        elif i == '+':
            s = score[-1] + score[-2]
            score.append(s)
        elif i == 'D':
            score.append(score[-1] * 2)
        elif i == 'C':
            del score[-1]
        #print(score)
                
    sc = sum(score)
    print(f'la somme des scores est : {sc}')

calculScore(p)